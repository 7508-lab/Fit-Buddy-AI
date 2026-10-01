def sample_form(user_code="FIT1001"):
    return {
        "name": "Demo User",
        "user_code": user_code,
        "age": "20",
        "weight": "65",
        "goal": "general_wellness",
        "intensity": "medium",
    }


def test_home_page(client):
    response = client.get("/")
    assert response.status_code == 200
    assert "Build your personalized week" in response.text
    assert "Demo mode ready" in response.text


def test_generate_plan_and_view_admin(client):
    response = client.post("/generate-workout", data=sample_form())
    assert response.status_code == 200
    assert "your week is ready" in response.text
    assert "Day 7" in response.text
    assert "offline-fallback" in response.text

    admin = client.get("/view-all-users")
    assert admin.status_code == 200
    assert "Demo User" in admin.text
    assert "FIT1001" in admin.text


def test_feedback_updates_latest_plan(client):
    client.post("/generate-workout", data=sample_form("FIT2001"))
    response = client.post(
        "/submit-feedback",
        data={"user_code": "FIT2001", "feedback": "Add more cardio and mobility"},
    )
    assert response.status_code == 200
    assert "Plan updated" in response.text
    assert "Feedback applied" in response.text
    assert "Add more cardio and mobility" in response.text


def test_feedback_for_unknown_user_returns_404(client):
    response = client.post(
        "/submit-feedback",
        data={"user_code": "UNKNOWN", "feedback": "Add one rest day"},
    )
    assert response.status_code == 404
    assert "Plan not found" in response.text


def test_invalid_form_is_rejected(client):
    data = sample_form()
    data["age"] = "5"
    response = client.post("/generate-workout", data=data)
    assert response.status_code == 422
    assert "Please check your details" in response.text


def test_json_api_flow(client):
    payload = {
        "name": "API User",
        "user_code": "API1001",
        "age": 24,
        "weight": 72,
        "goal": "endurance",
        "intensity": "high",
    }
    created = client.post("/api/workouts", json=payload)
    assert created.status_code == 200
    data = created.json()
    assert data["generation_mode"] == "demo"
    assert "Day 7" in data["workout_plan"]

    updated = client.post(
        "/api/feedback",
        json={"user_code": "API1001", "feedback": "Add one longer easy cardio day"},
    )
    assert updated.status_code == 200
    assert "Feedback applied" in updated.json()["workout_plan"]


def test_health_endpoint(client):
    response = client.get("/api/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"
    assert response.json()["ai_mode"] == "demo"
