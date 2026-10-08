# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a simple REST API in Python using FastAPI. Students will create endpoints, work with JSON data, and practice designing a basic API for managing information.

## 📝 Tasks

### 🛠️ Create the FastAPI app

#### Description
Set up a basic FastAPI application and define the data model your API will use.

#### Requirements
Completed program should:

- Create a FastAPI app instance
- Define a model for a resource such as a task, book, or student
- Use Pydantic models to validate incoming data
- Start the app locally and confirm it runs

### 🛠️ Add API endpoints

#### Description
Implement the core routes for creating, reading, updating, and deleting records.

#### Requirements
Completed program should:

- Add a `GET` route to list all records
- Add a `GET` route to retrieve one record by ID
- Add a `POST` route to create a new record
- Add a `PUT` route to update an existing record
- Add a `DELETE` route to remove a record
- Return JSON responses in a clear format

### 🛠️ Handle errors and testing

#### Description
Make the API more reliable by handling invalid requests and testing the endpoints.

#### Requirements
Completed program should:

- Return a `404` response for missing records
- Validate required fields before saving data
- Show meaningful error messages for bad input
- Use the FastAPI docs or a client to test the API
- Explain how each endpoint supports the application workflow
