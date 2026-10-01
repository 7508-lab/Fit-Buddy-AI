# FitBuddy Five Minute Demo Video Script

This script uses simple English and can be read directly during screen recording.

## Opening

Hello everyone. My project name is FitBuddy, an AI Fitness Plan Generator using Gemini models. The purpose of this project is to create a personalized seven-day workout plan based on a user's age, weight, fitness goal, and preferred workout intensity.

The project also generates a nutrition or recovery tip. If the user is not satisfied with the first plan, they can enter feedback, and FitBuddy will create an updated plan. User details and both plan versions are stored in an SQLite database.

## Code explanation

This is the complete project structure in Visual Studio Code. The backend is developed with Python and FastAPI. The frontend uses HTML, CSS, JavaScript, and Jinja2 templates. SQLite and SQLAlchemy are used for data storage. The Google Gen AI Python SDK connects the application to Gemini.

The `main.py` file starts the FastAPI application. The `routes.py` file handles the home page, plan generation, feedback, admin page, and JSON API. The `ai_service.py` file contains the Gemini prompts and the offline fallback. The `database.py` file defines the user and workout-plan tables.

The API key is not stored in the code. It is read from a private `.env` file, and that file is excluded from GitHub.

## Start the application

Now I am opening the terminal and running the Uvicorn command.

`python -m uvicorn app.main:app --reload`

The server has started successfully at `http://127.0.0.1:8000`. I will open this link in the browser.

## Generate a plan

This is the FitBuddy home page. The form collects the user's name, user ID, age, weight, fitness goal, and intensity.

For this demonstration, I am entering Demo User, user ID FIT1001, age 20, weight 65 kilograms, general wellness, and medium intensity.

Now I am clicking Generate my plan.

FitBuddy has created a complete seven-day schedule. Each day includes a warm-up, main workout, and cooldown. The plan also includes recovery and a safety note. On the right side, FitBuddy displays a goal-based nutrition and hydration tip.

## Feedback update

Next, I will test the feedback feature. I am entering: Add more cardio and one extra mobility session.

Now I am clicking Update my plan. The page shows Plan updated, and a revised schedule is displayed. The original plan is still stored for comparison.

## Admin dashboard

I am opening the Admin view. It displays the registered user, age, weight, fitness goal, intensity, number of saved plans, generation mode, and whether feedback has been applied.

## Testing and conclusion

The project also includes automated tests for the home page, plan generation, database storage, feedback, admin view, validation, JSON API, and health endpoint. All nine tests pass, and application code coverage is 91 percent.

The main benefits of FitBuddy are personalized planning, feedback-based improvement, local data storage, API support, and a fallback mode for reliable demonstrations.

This is the final output of my FitBuddy AI Fitness Plan Generator project. Thank you.
