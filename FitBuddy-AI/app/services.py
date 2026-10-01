"""Database service functions used by HTML and JSON routes."""

from __future__ import annotations

from sqlalchemy import select
from sqlalchemy.orm import Session, selectinload

from .ai_service import AIResult
from .database import User, WorkoutPlan
from .schemas import WorkoutRequest


def upsert_user(db: Session, data: WorkoutRequest) -> User:
    user = db.scalar(select(User).where(User.user_code == data.user_code))
    if user is None:
        user = User(user_code=data.user_code)
        db.add(user)

    user.name = data.name
    user.age = data.age
    user.weight = data.weight
    user.goal = data.goal
    user.intensity = data.intensity
    db.flush()
    return user


def create_plan(
    db: Session,
    user: User,
    workout: AIResult,
    nutrition: AIResult,
) -> WorkoutPlan:
    mode = "gemini" if workout.mode == "gemini" and nutrition.mode == "gemini" else workout.mode
    plan = WorkoutPlan(
        user_id=user.id,
        original_plan=workout.text,
        nutrition_tip=nutrition.text,
        generation_mode=mode,
        model_name=workout.model,
    )
    db.add(plan)
    db.commit()
    db.refresh(plan)
    db.refresh(user)
    return plan


def latest_plan_for_user_code(db: Session, user_code: str) -> WorkoutPlan | None:
    statement = (
        select(WorkoutPlan)
        .join(WorkoutPlan.user)
        .options(selectinload(WorkoutPlan.user))
        .where(User.user_code == user_code)
        .order_by(WorkoutPlan.created_at.desc(), WorkoutPlan.id.desc())
    )
    return db.scalars(statement).first()


def update_saved_plan(
    db: Session, plan: WorkoutPlan, feedback: str, result: AIResult
) -> WorkoutPlan:
    plan.feedback = feedback
    plan.updated_plan = result.text
    plan.generation_mode = result.mode
    plan.model_name = result.model
    db.commit()
    db.refresh(plan)
    return plan


def users_with_plans(db: Session) -> list[User]:
    statement = select(User).options(selectinload(User.plans)).order_by(User.created_at.desc())
    return list(db.scalars(statement).all())
