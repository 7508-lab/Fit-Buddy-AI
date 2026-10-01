# Phase 2 Requirement Analysis

## Purpose

This phase converts the FitBuddy concept into measurable requirements. The requirements define what the application must do, how it should behave, and the limits that protect users and project data.

## Stakeholders

| Stakeholder | Need |
|---|---|
| Fitness user | A clear plan matched to their goal and intensity |
| Returning user | A way to revise the latest plan using feedback |
| Coach or evaluator | A dashboard showing users and plan status |
| Project team | Maintainable code, documented setup, and test evidence |
| Faculty evaluator | A complete working demonstration and public repository |

## Functional requirements

| ID | Requirement | Acceptance condition |
|---|---|---|
| FR-01 | Display the plan generation form | Home page shows all required fields |
| FR-02 | Validate user input | Invalid age, weight, goal, intensity, or text is rejected |
| FR-03 | Generate a seven-day workout plan | Output includes headings Day 1 through Day 7 |
| FR-04 | Generate a nutrition/recovery tip | Result page shows a goal-based tip |
| FR-05 | Save user details | User is stored with a unique user ID |
| FR-06 | Save the original plan | Generated plan is persisted in SQLite |
| FR-07 | Accept feedback | User can submit 5-500 characters of feedback |
| FR-08 | Generate and save a revised plan | Updated plan is shown and stored separately |
| FR-09 | Display all users | Admin page lists profile, goal, plan count, and status |
| FR-10 | Provide JSON endpoints | API supports plan generation and feedback |
| FR-11 | Show system status | Health endpoint reports app version and AI mode |
| FR-12 | Support offline demonstration | Missing API key does not block required project flow |

## Non-functional requirements

| ID | Requirement | Implementation approach |
|---|---|---|
| NFR-01 | Usability | Responsive UI, clear labels, readable status messages |
| NFR-02 | Performance | Local form requests should complete quickly in demo mode |
| NFR-03 | Reliability | API failures fall back safely when fallback is enabled |
| NFR-04 | Security | API key stored only in `.env`; `.env` excluded from Git |
| NFR-05 | Privacy | Only necessary project data is stored locally |
| NFR-06 | Maintainability | Separate routes, schemas, services, AI, and database modules |
| NFR-07 | Testability | Deterministic fallback and isolated test database |
| NFR-08 | Accessibility | Semantic labels, keyboard-accessible fields, sufficient contrast |
| NFR-09 | Portability | Setup documented for Windows, macOS, Linux, and Docker |
| NFR-10 | Safety | No diagnosis; plans include an exercise safety note |

## User stories

1. As a new user, I want to enter my fitness details so that I can receive a weekly plan.
2. As a user, I want a nutrition and recovery tip so that the plan includes supporting guidance.
3. As a returning user, I want to request more cardio or recovery so that the plan better fits my preference.
4. As a coach, I want to view all registered users so that I can review activity and plan status.
5. As a student, I want demo mode so that an API outage does not prevent my project presentation.
6. As a developer, I want JSON endpoints and interactive docs so that the backend can be tested independently.

## Input specification

| Field | Type | Rule |
|---|---|---|
| Name | Text | 2-80 characters; markup rejected |
| User ID | Text | 2-40 characters; unique user identity |
| Age | Integer | 13-90 |
| Weight | Decimal | 25-300 kg |
| Goal | Selection | Weight loss, muscle gain, general wellness, endurance, or flexibility |
| Intensity | Selection | Low, medium, or high |
| Feedback | Text | 5-500 characters; markup rejected |

## Output specification

The workout response must contain:

- Day 1 through Day 7 headings
- A warm-up for each day
- Main exercise details using sets, repetitions, duration, or a clear activity
- Cooldown or recovery guidance
- At least one appropriate recovery day
- A short safety note

The nutrition response must be concise, goal-related, mention hydration, avoid diagnosis, and clearly remain general guidance.

## Data requirements

### User entity

- Internal numeric ID
- User code
- Name
- Age
- Weight
- Goal
- Intensity
- Created and updated timestamps

### Workout plan entity

- Internal numeric ID
- User reference
- Original plan
- Optional revised plan
- Nutrition tip
- Optional feedback
- Generation mode
- Model name
- Created and updated timestamps

## Assumptions

- The user can run Python 3.11 or newer.
- An internet connection is needed only for live Gemini generation and dependency installation.
- A Gemini API key is provided by the user and is never committed.
- SQLite is sufficient for the academic project scale.
- The coach/admin page is a demonstration feature and is not exposed as a public production system.

## Constraints and risks

| Risk | Impact | Mitigation |
|---|---|---|
| Gemini API key missing | Live AI generation unavailable | Demonstration fallback mode |
| Model name changes | API request may fail | Configurable `GEMINI_MODEL` environment variable |
| AI response varies | Formatting may differ | Strong Day 1-7 prompt and fallback output |
| Unsafe user expectation | Fitness output treated as medical advice | Safety notice and limited project scope |
| Secret committed to GitHub | Credential exposure | `.env`, `.gitignore`, and documentation warnings |
| Invalid or malicious input | Broken page or prompt manipulation | Pydantic validation and bounded fields |

## Requirement traceability

Every functional requirement is covered by a route, service, or test. The testing phase maps test cases to these requirement IDs and records the verified result.
