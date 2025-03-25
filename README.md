# Django + React Task Tracker
This repository contains a task tracker web application built with Django and React. It allows users to register, log in, manage their tasks, and perform CRUD (Create, Read, Update, Delete) operations on them. The application includes both a backend API built with Django REST framework and a frontend built with React.

## Frontend (React)
The React frontend enables users to:

Register & Log in: Users can create an account and log in with credentials.

Manage Tasks: Users can create, view, and delete their tasks.


## Backend (Django REST API)
The Django backend provides the following API endpoints:

POST /api/user/register - Registers a new user.

POST /api/user/login - Authenticates user and returns access & refresh tokens.

POST /api/user/refresh - Refreshes the access token.

GET /api/tasks/ - Retrieves all tasks for the authenticated user.

POST /api/tasks/ - Creates a new task.

DELETE /api/tasks/{id} - Deletes a task by ID.

## Backend Setup  
1. clone the repo: git clone https://github.com/Ajeripotula1/django-task-api.git
2. install dependencies : pip install -r requirements.txt
3. apply migrations and run the server:
python manage.py migrate
python manage.py runserver

## Frontend Setup 
1. Install dependencies:
cd frontend/task-tracker-ui 
npm install
2. start the react server:
npm start
   
