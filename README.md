[README.md](https://github.com/user-attachments/files/32923095/README.md)[Uploading README.md# FitBuddy AI

FitBuddy is a FastAPI web application that creates personalized seven-day workout plans, supplies goal-based nutrition and recovery guidance, and revises an existing plan from user feedback. The project uses the current Google Gen AI Python SDK when a Gemini API key is configured and includes a safe offline demonstration mode so every required screen can still be shown during evaluation.

## Core features

- Personalized Day 1 to Day 7 workout plan
- Goal-based nutrition and hydration tip
- Feedback-based plan revision
- SQLite storage for users, original plans, and updated plans
- Coach/admin page to review all registered users
- HTML user interface plus JSON API endpoints
- Gemini integration with configurable model name
- Offline fallback for classroom demonstrations and automated testing
- Input validation, secret-safe configuration, and responsive UI

## Technology stack

| Layer | Technology |
|---|---|
| Frontend | HTML, CSS, JavaScript, Jinja2 |
| Backend | Python, FastAPI, Uvicorn |
| AI | Google Gen AI SDK and Gemini |
| Database | SQLite and SQLAlchemy |
| Validation | Pydantic |
| Testing | Pytest and FastAPI TestClient |

## Project structure

```text
FitBuddy-AI/
├── app/
│   ├── ai_service.py
│   ├── config.py
│   ├── database.py
│   ├── main.py
│   ├── routes.py
│   ├── schemas.py
│   ├── services.py
│   ├── static/
│   │   ├── css/style.css
│   │   └── js/app.js
│   └── templates/
│       ├── all_users.html
│       ├── base.html
│       ├── error.html
│       ├── index.html
│       └── result.html
├── docs/
│   ├── 01_Brainstorming_and_Ideation.md
│   ├── 02_Requirement_Analysis.md
│   ├── 03_Project_Design.md
│   ├── 04_Project_Planning.md
│   ├── 05_Project_Development.md
│   ├── 06_Project_Testing.md
│   ├── 07_Project_Documentation.md
│   ├── 08_Project_Demonstration.md
│   ├── Demo_Video_Script.md
│   └── GitHub_Upload_Guide.md
├── reports/
├── tests/
├── .env.example
├── Dockerfile
├── requirements.txt
├── run.bat
└── run.sh
```

## Quick start on Windows

1. Install Python 3.11 or newer and VS Code.
2. Extract the project ZIP and open the `FitBuddy-AI` folder in VS Code.
3. Open **Terminal > New Terminal**.
4. Run these commands:

```powershell
py -m venv .venv
.venv\Scripts\activate
python -m pip install -r requirements.txt
copy .env.example .env
python -m uvicorn app.main:app --reload
```

5. Open <http://127.0.0.1:8000>.

You can also double-click `run.bat`; it creates the virtual environment, installs the requirements, and starts the server.

## Quick start on macOS or Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
cp .env.example .env
python -m uvicorn app.main:app --reload
```

Then open <http://127.0.0.1:8000>.

## Configure Gemini

1. Create an API key in Google AI Studio.
2. Copy `.env.example` to `.env`.
3. Add the key without quotes:

```env
GEMINI_API_KEY=your_private_key_here
GEMINI_MODEL=gemini-3.8-flash
DEMO_MODE=false
ALLOW_AI_FALLBACK=true
```

Never upload `.env` or an API key to GitHub. The included `.gitignore` prevents accidental commits of `.env`.

If the key is blank, `DEMO_MODE=true`, or the API is temporarily unavailable while fallback is allowed, FitBuddy produces a deterministic offline plan. This keeps the full workflow available for demonstration; the result page clearly shows the generation mode.

## Main pages

| URL | Purpose |
|---|---|
| `/` | User details and plan generator |
| `/generate-workout` | Form action that creates a plan |
| `/submit-feedback` | Form action that revises a plan |
| `/view-all-users` | Coach/admin overview |
| `/docs` | Interactive FastAPI API documentation |
| `/api/health` | Health and configured mode |

## Verified interface

### Plan generator

![FitBuddy plan generator](docs/screenshots/01_homepage.png)

### Generated plan and nutrition tip

![FitBuddy generated workout plan](docs/screenshots/02_generated_plan.png)

### Feedback-based update

![FitBuddy updated workout plan](docs/screenshots/03_feedback_update.png)

### Admin dashboard

![FitBuddy admin dashboard](docs/screenshots/04_admin_dashboard.png)

## JSON API examples

Create a plan:

```bash
curl -X POST http://127.0.0.1:8000/api/workouts \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Demo User",
    "user_code": "FIT1001",
    "age": 20,
    "weight": 65,
    "goal": "general_wellness",
    "intensity": "medium"
  }'
```

Update it with feedback:

```bash
curl -X POST http://127.0.0.1:8000/api/feedback \
  -H "Content-Type: application/json" \
  -d '{
    "user_code": "FIT1001",
    "feedback": "Add more cardio and one additional mobility session"
  }'
```

## Run tests

```bash
python -m pip install -r requirements-dev.txt
python -m pytest
```

The suite verifies the home page, plan creation, database storage, feedback updates, admin view, API validation, and deterministic fallback generation.

## Submission checklist

- [ ] Keep the GitHub repository public.
- [ ] Upload the complete project, `docs` folder, and report.
- [ ] Do not upload `.env`, API keys, `.venv`, or the SQLite database.
- [ ] Add output screenshots to the documentation if the UI is changed.
- [ ] Record a five-minute demo with screen sharing and voice-over.
- [ ] Show the project name, purpose, benefits, working process, and final output.
- [ ] Upload the demo to Google Drive and enable **Anyone with the link can view**.
- [ ] Submit GitHub, documentation, and demo links in SkillWallet.
- [ ] Move completed SkillWallet tasks to **To Be Reviewed**.

## Important safety note

FitBuddy provides general fitness and wellness information for demonstration and educational use. It does not diagnose conditions or replace advice from a qualified doctor, physiotherapist, dietitian, or fitness professional.
…]()
