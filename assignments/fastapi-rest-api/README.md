# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Create a small RESTful API in Python using FastAPI to manage tasks or records. This assignment introduces students to endpoint design, request validation, JSON responses, and basic CRUD operations in a modern web framework.

## 📝 Tasks

### 🛠️ Set up the FastAPI app

#### Description
Build a basic FastAPI application and define a simple data model for tasks.

#### Requirements
Completed program should:

- Create a FastAPI app instance with a meaningful title and description
- Define a task model using Python data classes or Pydantic models
- Store data in an in-memory list or dictionary for the assignment
- Expose a `GET /tasks` endpoint that returns all task records as JSON

### 🛠️ Add CRUD endpoints

#### Description
Add the endpoints required to create, read, update, and delete tasks through the API.

#### Requirements
Completed program should:

- Implement `POST /tasks` to create a new task
- Implement `GET /tasks/{task_id}` to fetch a single task by ID
- Implement `PUT /tasks/{task_id}` to update an existing task
- Implement `DELETE /tasks/{task_id}` to remove a task
- Return clear status codes for successful and failed requests
- Handle invalid IDs or missing tasks gracefully

### 🛠️ Improve validation and API behavior

#### Description
Make the API more robust by validating input and improving the user experience for API consumers.

#### Requirements
Completed program should:

- Validate required fields such as title and description
- Prevent empty or invalid values from being stored
- Return helpful error responses for invalid requests
- Include descriptive names and clean responses for each endpoint
- Use FastAPI’s automatic documentation by opening the generated docs in a browser
