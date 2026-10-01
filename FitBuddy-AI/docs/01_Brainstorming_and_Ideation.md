# Phase 1 Brainstorming and Ideation

## Project title

FitBuddy - AI Fitness Plan Generator using Gemini Models

## Problem statement

Many students and beginner fitness users do not know how to convert a broad goal such as weight loss, muscle gain, endurance, flexibility, or general wellness into a balanced weekly routine. Generic online plans often ignore the user's age, weight, preferred intensity, and feedback. They may also separate exercise and recovery guidance across different tools.

FitBuddy addresses this problem through one web application that accepts basic fitness details and produces a structured seven-day workout plan. A user can then provide feedback such as "add more cardio" or "include an extra recovery session" and receive a revised plan. A short nutrition and recovery tip complements the schedule.

## Brainstormed solution ideas

| Idea | Strength | Limitation | Decision |
|---|---|---|---|
| Static plan library | Simple and fast | Cannot adapt to each user | Rejected as the main solution |
| Rule-based plan generator | Works offline and is predictable | Limited variety and feedback understanding | Retained as a fallback mode |
| Gemini-powered planner | Natural-language plan generation and revision | Requires an API key and internet access | Selected as the primary solution |
| Mobile-only application | Familiar interface for students | More build complexity and platform tooling | Deferred |
| Responsive web application | Works on laptops and phones, easy to demonstrate | Requires a local web server | Selected delivery format |

## Selected concept

The selected concept is a responsive FastAPI web application with four connected capabilities:

1. Collect validated user details.
2. Generate a day-by-day workout plan using Gemini.
3. Generate a short goal-based nutrition or recovery tip.
4. Accept feedback and revise the most recent saved plan.

SQLite stores users and plans. An admin or coach page displays registered users, their goals, and whether a plan has been updated.

## Intended users

- Students demonstrating an AI web application project
- Beginners who need a simple weekly fitness structure
- Coaches or project evaluators who need to view stored plans
- Developers learning FastAPI, Gemini integration, and SQLite persistence

## Core value proposition

FitBuddy combines personalization, iteration, and persistence. The plan is not a one-time static output: it can be revised from feedback, saved, and reviewed through a clean interface.

## In-scope features

- Name, user ID, age, weight, fitness goal, and intensity input
- Personalized seven-day plan
- Warm-up, main workout, cooldown, and recovery content
- Goal-based nutrition and hydration tip
- Feedback-driven revised plan
- User and plan storage in SQLite
- Admin view of all users
- HTML interface and JSON API
- Gemini mode plus offline demonstration fallback
- Automated tests and documentation

## Out-of-scope features

- Medical diagnosis or treatment recommendations
- Wearable-device integration
- Calorie tracking or prescription diets
- Payments, subscriptions, or public user accounts
- Real-time coach chat
- Cloud production deployment

## Success criteria

- The application starts locally with one documented command.
- A valid form submission produces Day 1 through Day 7 content.
- A nutrition/recovery tip appears with the plan.
- Feedback creates and displays a revised plan.
- User data and both plan versions are stored in SQLite.
- The admin page lists saved users.
- Invalid inputs are rejected with a readable message.
- The project works in demo mode even without an API key.
- Automated tests pass before submission.

## Ethical and safety position

The system provides general fitness information only. It does not diagnose medical conditions or replace a doctor, physiotherapist, dietitian, or qualified trainer. Generated plans include a safety note, and the application advises users to stop if they experience sharp pain.

## Phase output

The final idea is approved for development as a FastAPI, Gemini, Jinja2, SQLAlchemy, and SQLite web project with a responsive interface and phase-wise submission package.
