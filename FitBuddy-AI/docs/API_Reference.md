# FitBuddy API Reference

## Base URL

`http://127.0.0.1:8000`

## Health check

`GET /api/health`

Example response:

```json
{
  "status": "ok",
  "application": "FitBuddy AI",
  "version": "1.0.0",
  "ai_mode": "demo",
  "model": "offline-fallback"
}
```

## Generate workout

`POST /api/workouts`

Request:

```json
{
  "name": "Demo User",
  "user_code": "FIT1001",
  "age": 20,
  "weight": 65,
  "goal": "general_wellness",
  "intensity": "medium"
}
```

Allowed goals:

- `weight_loss`
- `muscle_gain`
- `general_wellness`
- `endurance`
- `flexibility`

Allowed intensities:

- `low`
- `medium`
- `high`

Successful response fields:

- `user_code`
- `name`
- `goal`
- `intensity`
- `workout_plan`
- `nutrition_tip`
- `generation_mode`
- `model_name`

## Submit feedback

`POST /api/feedback`

Request:

```json
{
  "user_code": "FIT1001",
  "feedback": "Add more cardio and one extra mobility session"
}
```

The endpoint retrieves the latest plan for the user, revises it, saves the revision, and returns the same response fields as the workout endpoint.

## Response codes

| Code | Meaning |
|---|---|
| 200 | Request completed |
| 404 | No plan exists for the supplied user ID |
| 422 | Input validation failed |
| 503 | Gemini unavailable and fallback disabled |

## Interactive documentation

- Swagger UI: `http://127.0.0.1:8000/docs`
- OpenAPI JSON: `http://127.0.0.1:8000/openapi.json`
