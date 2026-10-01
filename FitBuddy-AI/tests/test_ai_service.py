from app.ai_service import AIService
from app.schemas import WorkoutRequest


def test_offline_plan_contains_all_seven_days():
    payload = WorkoutRequest(
        name="Demo User",
        user_code="FIT1001",
        age=20,
        weight=65,
        goal="general_wellness",
        intensity="medium",
    )
    result = AIService().generate_workout(payload)
    assert result.mode == "demo"
    assert result.model == "offline-fallback"
    assert result.text.count("Day ") == 7
    assert "Safety note" in result.text


def test_offline_tip_matches_goal():
    payload = WorkoutRequest(
        name="Demo User",
        user_code="FIT1002",
        age=21,
        weight=70,
        goal="muscle_gain",
        intensity="high",
    )
    result = AIService().generate_nutrition_tip(payload)
    assert "protein" in result.text.lower()
    assert "water" in result.text.lower()
