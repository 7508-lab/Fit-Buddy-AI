# Phase 4 Project Planning

## Delivery goal

Produce a complete, testable, GitHub-ready FitBuddy project with source code, phase-wise documentation, final report, output screenshots, and a demonstration script.

## Seven-day execution plan

| Day | Work item | Expected output |
|---|---|---|
| Day 1 | Confirm idea, scope, users, and success criteria | Brainstorming document |
| Day 2 | Define requirements, fields, entities, risks, and routes | Requirement analysis |
| Day 3 | Design architecture, database, interface, and AI flow | Design document |
| Day 4 | Build FastAPI modules, database, templates, and styling | Working application |
| Day 5 | Complete Gemini integration, feedback, admin, and API | Feature-complete build |
| Day 6 | Run automated/manual tests and capture output | Test report and screenshots |
| Day 7 | Finalize documentation, demo script, repository, and ZIP | Submission package |

## Work breakdown structure

1. Project foundation
   - Create folders and dependency files
   - Configure FastAPI and static assets
   - Configure SQLite and SQLAlchemy
2. User workflow
   - Build form and validation
   - Generate plan and tip
   - Render result page
3. Feedback workflow
   - Retrieve latest plan
   - Apply feedback
   - Store and compare revisions
4. Admin and API
   - Build all-users page
   - Add JSON endpoints and health check
5. Quality
   - Automated tests
   - Responsive design review
   - Secret and safety review
6. Submission
   - Phase files
   - Final report and screenshots
   - Demo script and GitHub guide

## Roles for a student team

| Role | Responsibility |
|---|---|
| Project coordinator | Track scope, phases, and final submission |
| Backend developer | FastAPI routes, schemas, services, and Gemini integration |
| Database developer | SQLAlchemy models, persistence, and queries |
| Frontend developer | Templates, CSS, browser behavior, and responsiveness |
| Tester/documenter | Test cases, screenshots, report, demo, and repository checks |

One student may hold more than one role. The repository remains the single source of truth.

## Technical dependencies

- Python 3.11 or newer
- VS Code or another editor
- FastAPI and Uvicorn
- Jinja2 and python-multipart
- SQLAlchemy and SQLite
- Pydantic
- Google Gen AI Python SDK
- Pytest and FastAPI TestClient
- Optional Gemini API key

## Quality gates

| Gate | Pass condition |
|---|---|
| Structure | All documented folders and files exist |
| Startup | Uvicorn starts without an application error |
| Generation | Valid details produce Day 1 through Day 7 |
| Feedback | Feedback produces and stores a revised plan |
| Admin | Saved user appears on dashboard |
| Validation | Invalid data receives an appropriate error |
| Automated tests | Complete test suite passes |
| Secrets | No `.env` or real API key in repository |
| Documentation | Eight phases and final report are included |
| Demonstration | Five-minute script covers required points |

## Risk management plan

| Risk | Probability | Impact | Response |
|---|---|---|---|
| API unavailable during demo | Medium | High | Use verified offline fallback |
| Dependency setup issue | Medium | Medium | Include run scripts and explicit commands |
| Model endpoint changes | Medium | Medium | Keep model configurable in `.env` |
| Time shortage | Medium | High | Prioritize required flow before optional polish |
| Invalid data | Medium | Medium | Pydantic validation and negative tests |
| Secret exposure | Low | High | `.gitignore`, `.env.example`, checklist |
| UI layout issue | Low | Medium | Responsive CSS and rendered screenshots |

## Version control plan

Recommended commit sequence:

1. `chore: create FitBuddy project structure`
2. `feat: add database models and validation`
3. `feat: add workout and nutrition generation`
4. `feat: add feedback and admin dashboard`
5. `style: complete responsive FitBuddy interface`
6. `test: add application and API tests`
7. `docs: add phases report and demo guide`

## Definition of done

The project is complete when the code runs locally, tests pass, screenshots reflect the working flow, all required documents are present, a secret-safe GitHub-ready ZIP is produced, and the student can follow the demo script without additional development.
