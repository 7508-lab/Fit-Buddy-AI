# Phase 8 Project Demonstration

## Demonstration objective

Show that FitBuddy is a complete working project by explaining the project name, purpose, benefits, execution process, and final output while recording the screen and voice.

## Recommended video length

Approximately five minutes.

## Five-minute flow

| Time | Screen | Explanation |
|---|---|---|
| 0:00-0:30 | Title or README | Project name, purpose, and technology stack |
| 0:30-1:15 | VS Code project tree | Main modules, templates, static files, tests, and docs |
| 1:15-1:45 | `.env.example` and `ai_service.py` | Secure key setup, Gemini model, and fallback |
| 1:45-2:15 | Terminal | Start Uvicorn and show local URL |
| 2:15-3:05 | Home page | Enter user details and generate a plan |
| 3:05-3:40 | Result page | Show seven days and nutrition tip |
| 3:40-4:15 | Feedback | Request a change and show revised plan |
| 4:15-4:35 | Admin page | Show saved user and update status |
| 4:35-4:50 | Test terminal | Show 9 passed tests |
| 4:50-5:00 | Closing | State benefits and submission items |

## Required screen recording sequence

1. Open the root project folder in VS Code.
2. Expand `app`, `templates`, `static`, `tests`, `docs`, and `reports`.
3. Briefly show `app/main.py`, `app/routes.py`, `app/ai_service.py`, and `app/database.py`.
4. Open a terminal and activate the virtual environment.
5. Run `python -m uvicorn app.main:app --reload`.
6. Open the local URL in a browser.
7. Complete the form with demonstration data.
8. Generate the plan and show Day 1 through Day 7.
9. Point to the nutrition/recovery tip.
10. Submit feedback and show **Plan updated**.
11. Open the admin page and show the user record.
12. Optionally open `/docs` to show the API.
13. Show the Pytest result.

## Suggested demonstration data

| Field | Value |
|---|---|
| Name | Demo User |
| User ID | FIT1001 |
| Age | 20 |
| Weight | 65 kg |
| Goal | General wellness |
| Intensity | Medium |
| Feedback | Add more cardio and one extra mobility session |

## Demonstration checks

- The browser must show the project, not only code.
- The voice-over should be clear and continuous.
- Do not display a real API key.
- Keep the `.env` file closed.
- Show the generation mode badge honestly.
- Include final output and feedback update.
- Keep personal notifications and unrelated browser tabs closed.

## Recording tools

- Windows Game Bar: `Win + Alt + R`
- OBS Studio
- Built-in phone screen recorder when using a remote desktop
- Any recorder that captures screen and microphone clearly

## Upload procedure

1. Export the video as MP4.
2. Upload it to Google Drive.
3. Open **Share**.
4. Change General access to **Anyone with the link**.
5. Keep permission as **Viewer**.
6. Copy the link and test it in an incognito window.
7. Submit the Drive link in SkillWallet.

## SkillWallet completion flow

1. Upload or link the public GitHub repository.
2. Submit the required documentation.
3. Submit the public-view demo video link.
4. Move completed tasks from **In Progress** to **To Be Reviewed**.
5. The organizer or evaluator handles the final **Completed** status.

## Final demonstration outcome

The evaluator should see a responsive FitBuddy interface, a valid seven-day plan, a nutrition tip, a feedback-based revision, a stored user in the admin dashboard, and passing automated tests.
