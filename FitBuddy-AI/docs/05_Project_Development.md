# Phase 5 Project Development

## Development summary

FitBuddy was implemented as a modular FastAPI project. The application serves a responsive Jinja2 interface, validates inputs with Pydantic, generates content through Gemini when configured, saves data through SQLAlchemy, and supports a deterministic offline demonstration mode.

## Environment setup

```bash
python -m venv .venv
```

Windows activation:

```powershell
.venv\Scripts\activate
```

macOS or Linux activation:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

Create local configuration:

```bash
copy .env.example .env
```

Start the application:

```bash
python -m uvicorn app.main:app --reload
```

Open `http://127.0.0.1:8000`.

## Source modules

### Application entry point

`app/main.py` creates the FastAPI application, initializes database tables in the lifespan hook, mounts `/static`, and includes the shared router.

### Configuration

`app/config.py` loads:

- `GEMINI_API_KEY`
- `GEMINI_MODEL`
- `DEMO_MODE`
- `ALLOW_AI_FALLBACK`
- `DATABASE_URL`

The API key is never hard-coded or returned to a page.

### Database implementation

`app/database.py` defines two SQLAlchemy entities:

- `User` for profile fields
- `WorkoutPlan` for original/revised plan, tip, feedback, model, and generation mode

The relationship is one user to many workout plans. A user code is unique, while repeated plan generation creates additional plan records for that user.

### Validation

`app/schemas.py` uses Pydantic models:

- `WorkoutRequest`
- `FeedbackRequest`
- `WorkoutPlanResponse`

The schema layer enforces ranges, valid goal/intensity options, field lengths, and simple markup rejection.

### AI generation

`app/ai_service.py` contains three primary methods:

1. `generate_workout()` builds a structured seven-day plan prompt.
2. `generate_nutrition_tip()` requests a concise goal-based tip.
3. `update_plan()` sends the original plan and validated feedback for revision.

When Gemini is enabled, the code uses the Google Gen AI SDK:

```python
from google import genai

with genai.Client(api_key=settings.gemini_api_key) as client:
    response = client.models.generate_content(
        model=settings.gemini_model,
        contents=prompt,
    )
```

The model defaults to `gemini-3.8-flash` but remains configurable. If the key is missing or a call fails while fallback is permitted, the service returns a structured offline plan. The result records its mode as `gemini`, `demo`, or `fallback`.

### Database services

`app/services.py` separates data operations from routes:

- Upsert user by user code
- Create a plan
- Retrieve the latest plan
- Save feedback and updated plan
- List all users with plans

### Web and API routes

`app/routes.py` provides HTML pages and JSON endpoints. HTML form data and JSON data share the same Pydantic schemas and AI/database services, reducing duplicate logic.

## Frontend implementation

### Templates

- `base.html`: navigation and shared footer
- `index.html`: hero, form, and feature summary
- `result.html`: weekly plan, tip, feedback, original/revised comparison
- `all_users.html`: coach/admin table
- `error.html`: readable validation or service errors

### Styling

`app/static/css/style.css` implements:

- Responsive grid layouts
- Accessible inputs and focus states
- Plan/result cards
- Mobile breakpoints
- Print-friendly plan view
- Consistent navy, blue, cyan, and violet visual system

### Browser behavior

`app/static/js/app.js` adds:

- Loading state for form submissions
- Copy-plan action
- Graceful clipboard fallback

## Main execution flow

1. User opens the home page.
2. User enters name, ID, age, weight, goal, and intensity.
3. Pydantic validates and normalizes the fields.
4. AI service generates a workout plan and nutrition tip.
5. Database service saves the user and plan.
6. Jinja2 renders the result page.
7. User submits feedback with the user ID.
8. Latest plan is retrieved and revised.
9. Revised plan and feedback are stored.
10. Admin dashboard reflects the update.

## Development safeguards

- All database access uses SQLAlchemy.
- Jinja2 auto-escapes inserted values.
- `.env` and database files are ignored by Git.
- API failures return a controlled 503 response when fallback is disabled.
- Unknown user feedback returns 404.
- Invalid forms return 422 with readable details.
- Generated outputs carry a safety notice.

## Development completion evidence

- Working HTML workflow implemented
- Working JSON workflow implemented
- SQLite persistence verified
- Feedback revision verified
- Admin view verified
- Responsive screenshots captured in `docs/screenshots`
- Automated tests added in `tests`
