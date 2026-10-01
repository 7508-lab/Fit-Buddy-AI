"""Validated request and response schemas."""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, ConfigDict, Field, field_validator


FitnessGoal = Literal[
    "weight_loss", "muscle_gain", "general_wellness", "endurance", "flexibility"
]
WorkoutIntensity = Literal["low", "medium", "high"]


class WorkoutRequest(BaseModel):
    name: str = Field(min_length=2, max_length=80)
    user_code: str = Field(min_length=2, max_length=40)
    age: int = Field(ge=13, le=90)
    weight: float = Field(ge=25, le=300)
    goal: FitnessGoal
    intensity: WorkoutIntensity

    @field_validator("name", "user_code")
    @classmethod
    def strip_and_reject_markup(cls, value: str) -> str:
        cleaned = " ".join(value.strip().split())
        if any(char in cleaned for char in "<>\x00"):
            raise ValueError("HTML markup is not allowed")
        return cleaned


class FeedbackRequest(BaseModel):
    user_code: str = Field(min_length=2, max_length=40)
    feedback: str = Field(min_length=5, max_length=500)

    @field_validator("user_code", "feedback")
    @classmethod
    def normalize_text(cls, value: str) -> str:
        cleaned = " ".join(value.strip().split())
        if any(char in cleaned for char in "<>\x00"):
            raise ValueError("HTML markup is not allowed")
        return cleaned


class WorkoutPlanResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    user_code: str
    name: str
    goal: str
    intensity: str
    workout_plan: str
    nutrition_tip: str
    generation_mode: str
    model_name: str
