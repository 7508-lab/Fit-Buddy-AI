"""HTML pages and JSON API routes."""

from __future__ import annotations

from pathlib import Path

from fastapi import APIRouter, Depends, Form, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import ValidationError
from sqlalchemy.orm import Session

from .ai_service import GOAL_LABELS, get_ai_service
from .config import get_settings
from .database import get_db
from .schemas import FeedbackRequest, WorkoutPlanResponse, WorkoutRequest
from .services import (
    create_plan,
    latest_plan_for_user_code,
    update_saved_plan,
    upsert_user,
    users_with_plans,
)


router = APIRouter()
templates = Jinja2Templates(directory=str(Path(__file__).parent / "templates"))


def _validation_message(error: ValidationError) -> str:
    details = []
    for item in error.errors():
        field = str(item.get("loc", ["field"])[-1]).replace("_", " ").title()
        details.append(f"{field}: {item.get('msg', 'invalid value')}")
    return " | ".join(details)


def _workout_payload(
    name: str,
    user_code: str,
    age: int,
    weight: float,
    goal: str,
    intensity: str,
) -> WorkoutRequest:
    return WorkoutRequest(
        name=name,
        user_code=user_code,
        age=age,
        weight=weight,
        goal=goal,
        intensity=intensity,
    )


@router.get("/", response_class=HTMLResponse)
def home(request: Request):
    settings = get_settings()
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "ai_status": "Gemini ready" if settings.ai_enabled else "Demo mode ready",
            "model_name": settings.gemini_model if settings.ai_enabled else "offline-fallback",
        },
    )


@router.post("/generate-workout", response_class=HTMLResponse)
def generate_workout(
    request: Request,
    name: str = Form(...),
    user_code: str = Form(...),
    age: int = Form(...),
    weight: float = Form(...),
    goal: str = Form(...),
    intensity: str = Form(...),
    db: Session = Depends(get_db),
):
    try:
        data = _workout_payload(name, user_code, age, weight, goal, intensity)
    except ValidationError as exc:
        return templates.TemplateResponse(
            request=request,
            name="error.html",
            context={"title": "Please check your details", "message": _validation_message(exc)},
            status_code=422,
        )

    ai = get_ai_service()
    try:
        workout = ai.generate_workout(data)
        nutrition = ai.generate_nutrition_tip(data)
    except RuntimeError as exc:
        return templates.TemplateResponse(
            request=request,
            name="error.html",
            context={"title": "AI service unavailable", "message": str(exc)},
            status_code=503,
        )

    user = upsert_user(db, data)
    plan = create_plan(db, user, workout, nutrition)
    return templates.TemplateResponse(
        request=request,
        name="result.html",
        context={"user": user, "plan": plan, "goal_label": GOAL_LABELS[user.goal]},
    )


@router.post("/submit-feedback", response_class=HTMLResponse)
def submit_feedback(
    request: Request,
    user_code: str = Form(...),
    feedback: str = Form(...),
    db: Session = Depends(get_db),
):
    try:
        payload = FeedbackRequest(user_code=user_code, feedback=feedback)
    except ValidationError as exc:
        return templates.TemplateResponse(
            request=request,
            name="error.html",
            context={"title": "Feedback could not be submitted", "message": _validation_message(exc)},
            status_code=422,
        )

    plan = latest_plan_for_user_code(db, payload.user_code)
    if plan is None:
        return templates.TemplateResponse(
            request=request,
            name="error.html",
            context={"title": "Plan not found", "message": "Generate a workout plan before submitting feedback."},
            status_code=404,
        )

    user = plan.user
    data = WorkoutRequest(
        name=user.name,
        user_code=user.user_code,
        age=user.age,
        weight=user.weight,
        goal=user.goal,
        intensity=user.intensity,
    )
    try:
        result = get_ai_service().update_plan(plan.original_plan, payload.feedback, data)
    except RuntimeError as exc:
        return templates.TemplateResponse(
            request=request,
            name="error.html",
            context={"title": "AI service unavailable", "message": str(exc)},
            status_code=503,
        )

    plan = update_saved_plan(db, plan, payload.feedback, result)
    return templates.TemplateResponse(
        request=request,
        name="result.html",
        context={"user": user, "plan": plan, "goal_label": GOAL_LABELS[user.goal], "updated": True},
    )


@router.get("/view-all-users", response_class=HTMLResponse)
def view_all_users(request: Request, db: Session = Depends(get_db)):
    return templates.TemplateResponse(
        request=request,
        name="all_users.html",
        context={"users": users_with_plans(db), "goal_labels": GOAL_LABELS},
    )


@router.get("/api/health")
def api_health():
    settings = get_settings()
    return {
        "status": "ok",
        "application": settings.app_name,
        "version": settings.app_version,
        "ai_mode": "gemini" if settings.ai_enabled else "demo",
        "model": settings.gemini_model if settings.ai_enabled else "offline-fallback",
    }


@router.post("/api/workouts", response_model=WorkoutPlanResponse)
def api_generate_workout(data: WorkoutRequest, db: Session = Depends(get_db)):
    try:
        ai = get_ai_service()
        workout = ai.generate_workout(data)
        nutrition = ai.generate_nutrition_tip(data)
    except RuntimeError as exc:
        raise HTTPException(status_code=503, detail=str(exc)) from exc

    user = upsert_user(db, data)
    plan = create_plan(db, user, workout, nutrition)
    return WorkoutPlanResponse(
        user_code=user.user_code,
        name=user.name,
        goal=user.goal,
        intensity=user.intensity,
        workout_plan=plan.original_plan,
        nutrition_tip=plan.nutrition_tip,
        generation_mode=plan.generation_mode,
        model_name=plan.model_name,
    )


@router.post("/api/feedback", response_model=WorkoutPlanResponse)
def api_submit_feedback(data: FeedbackRequest, db: Session = Depends(get_db)):
    plan = latest_plan_for_user_code(db, data.user_code)
    if plan is None:
        raise HTTPException(status_code=404, detail="Plan not found")

    user = plan.user
    workout_data = WorkoutRequest(
        name=user.name,
        user_code=user.user_code,
        age=user.age,
        weight=user.weight,
        goal=user.goal,
        intensity=user.intensity,
    )
    try:
        result = get_ai_service().update_plan(plan.original_plan, data.feedback, workout_data)
    except RuntimeError as exc:
        raise HTTPException(status_code=503, detail=str(exc)) from exc
    plan = update_saved_plan(db, plan, data.feedback, result)
    return WorkoutPlanResponse(
        user_code=user.user_code,
        name=user.name,
        goal=user.goal,
        intensity=user.intensity,
        workout_plan=plan.updated_plan or plan.original_plan,
        nutrition_tip=plan.nutrition_tip,
        generation_mode=plan.generation_mode,
        model_name=plan.model_name,
    )
