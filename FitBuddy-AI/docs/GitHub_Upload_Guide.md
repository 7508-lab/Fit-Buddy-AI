# GitHub Upload Guide

## Before uploading

Confirm these items:

- `.env` is not present in the upload.
- No real API key appears in any file.
- `.venv`, `fitbuddy.db`, `fitbuddy_test.db`, and cache folders are excluded.
- Source code, tests, docs, screenshots, and reports are present.
- Tests pass.

## Method 1 GitHub website

1. Sign in to GitHub.
2. Click **New repository**.
3. Repository name: `FitBuddy-AI`.
4. Add the description: `AI fitness plan generator using FastAPI, Gemini, and SQLite`.
5. Select **Public**.
6. Do not initialize with another README because one is already included.
7. Click **Create repository**.
8. Choose **uploading an existing file**.
9. Extract the supplied ZIP on your computer.
10. Open the `FitBuddy-AI` folder and upload its contents, not the outer ZIP alone.
11. Add commit message: `Add complete FitBuddy AI project`.
12. Click **Commit changes**.
13. Open the repository in a private/incognito window to verify public access.

## Method 2 Git command line

Open a terminal inside the project folder:

```bash
git init
git add .
git status
git commit -m "Add complete FitBuddy AI project"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/FitBuddy-AI.git
git push -u origin main
```

Replace `YOUR_USERNAME` with the correct GitHub username.

## Secret check before push

Run:

```bash
git status
git ls-files
```

The list must not contain:

- `.env`
- `.venv`
- Any `.db` file
- API keys

If `.env` was accidentally staged but not committed:

```bash
git rm --cached .env
```

If a real key was committed, remove it from the repository and revoke/regenerate the key in Google AI Studio. Deleting only the visible file does not make an exposed key safe.

## Final repository checks

- Repository visibility is Public.
- README displays correctly.
- `app`, `tests`, `docs`, and `reports` folders open correctly.
- Images in `docs/screenshots` load.
- DOCX and PDF report files download.
- No secret or local database is present.
- Copy the exact repository URL for SkillWallet.
