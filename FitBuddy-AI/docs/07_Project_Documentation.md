# Phase 7 Project Documentation

## Project overview

FitBuddy is an AI-assisted fitness planning web application. It converts a user profile and fitness preference into a seven-day workout plan, creates a supporting nutrition/recovery tip, saves the result, and revises the plan from feedback.

## Documentation inventory

| File | Purpose |
|---|---|
| `README.md` | Main installation, usage, API, and submission guide |
| `01_Brainstorming_and_Ideation.md` | Problem, ideas, selected concept, and scope |
| `02_Requirement_Analysis.md` | Functional/non-functional requirements and data rules |
| `03_Project_Design.md` | Architecture, routes, entities, UI, security, and safety |
| `04_Project_Planning.md` | Schedule, work breakdown, roles, risks, and gates |
| `05_Project_Development.md` | Implementation and source module explanation |
| `06_Project_Testing.md` | Test cases, results, coverage, and evidence |
| `07_Project_Documentation.md` | Operating and maintenance reference |
| `08_Project_Demonstration.md` | Presentation flow and submission procedure |
| `API_Reference.md` | HTML and JSON endpoint reference |
| `Demo_Video_Script.md` | Ready-to-read five-minute voice-over |
| `GitHub_Upload_Guide.md` | Web and command-line repository upload steps |
| `SUBMISSION_CHECKLIST.md` | Final pre-submission checks |
| `reports/FitBuddy_Project_Report.docx` | Editable formal project report |
| `reports/FitBuddy_Project_Report.pdf` | Final-view project report |

## Installation reference

```bash
python -m venv .venv
```

Activate the environment, then run:

```bash
python -m pip install -r requirements.txt
python -m uvicorn app.main:app --reload
```

The application opens at `http://127.0.0.1:8000`.

## Configuration reference

| Variable | Default | Purpose |
|---|---|---|
| `GEMINI_API_KEY` | Empty | Private Gemini credential |
| `GEMINI_MODEL` | `gemini-3.8-flash` | Model endpoint used for generation |
| `DEMO_MODE` | `false` | Force deterministic offline output |
| `ALLOW_AI_FALLBACK` | `true` | Allow fallback if Gemini fails |
| `DATABASE_URL` | `sqlite:///./fitbuddy.db` | Database connection string |

## Operating guide

### Create a plan

1. Open the home page.
2. Enter all profile fields.
3. Select a goal and intensity.
4. Click **Generate my plan**.
5. Review the weekly plan and tip.

### Update a plan

1. On the result page, enter a specific change in the feedback box.
2. Click **Update my plan**.
3. Confirm the page status shows **Plan updated**.
4. Expand the original plan section if a comparison is needed.

### Review users

1. Open **Admin view** from the navigation.
2. Review user, profile, goal, plan count, mode, and update status.

### Use the API

Open `/docs` for interactive OpenAPI documentation, or use the examples in `API_Reference.md`.

## Maintenance guide

- Change the default model in `.env`, not in source code.
- Back up `fitbuddy.db` before schema changes.
- Run tests after changing routes, schemas, services, or templates.
- Keep the fallback output synchronized with supported goals and intensity levels.
- Never commit a real API key.
- Review Gemini model availability before a future live demonstration.

## Troubleshooting

| Problem | Resolution |
|---|---|
| `python` not found | Install Python and enable Add Python to PATH |
| Import error | Activate `.venv` and install `requirements.txt` |
| Port 8000 busy | Run Uvicorn with `--port 8001` |
| Gemini authentication error | Confirm `GEMINI_API_KEY` in local `.env` |
| Gemini model unavailable | Set `GEMINI_MODEL` to an available text model |
| Live AI slow/unavailable | Set `DEMO_MODE=true` for the presentation |
| Feedback says plan not found | Generate a plan using the same user ID first |
| Database needs reset | Stop app, remove local DB, restart (data is lost) |

## Backup and recovery

The academic app uses one local SQLite file. To back it up, stop the server and copy `fitbuddy.db`. To start clean, stop the server and remove the file; tables are recreated on the next startup. Never remove the database if saved demonstration data must be preserved.

## Safety and responsible use

- Results are general educational fitness information.
- Users should stop if they feel sharp pain.
- Health conditions and injuries require qualified guidance.
- The app should not be presented as medical diagnosis or treatment software.
- A production version would require professional content review and stronger privacy controls.

## References

- FastAPI documentation: https://fastapi.tiangolo.com/
- SQLAlchemy documentation: https://docs.sqlalchemy.org/
- Pydantic documentation: https://docs.pydantic.dev/
- Google Gemini API documentation: https://ai.google.dev/gemini-api/docs
- Google Gen AI Python SDK: https://googleapis.github.io/python-genai/
- Python documentation: https://docs.python.org/3/
