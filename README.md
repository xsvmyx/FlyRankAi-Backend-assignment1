# Task API

A simple Task Management API built with FastAPI. 

## Features
- Create, read, update, and delete tasks.
- Health check endpoints.

## Screenshot

![Swagger Documentation](screenshot/swagger.png)



## The mortality experiment: 

If the server is restarted, everything starts from scratch because the data is not persistent.
We need to create a file or a database to save the tasks.



## AI version

Prompt used:

> You'll help me to create a basic FastAPI crud api.
> in only one file :
> 
> * define a task list : it got title string , done bool and a auto generated id .
> * create the api with / endpoint to say hello and a healthcheck.
> * get endpoint to get all tasks and one to get a task by id
> * post add task endpoint that receives only the title and set done=false
> * delete task endpoint with id
> * put endpoint to update either the title or done or both
> * get endpoint to search by a string (if it's in the title)
> * stat endpoint to count the tasks , the done ones and the undone
> * get endpoint to filter the done/undone tasks


difference between my version and AI version:

1. **Validation & Schemas**: The AI version uses Pydantic models (`BaseModel`) for request payloads and returns (`response_model`). This provides automatic data validation and better Swagger documentation. The manual version uses plain dictionaries and manual key validation.
2. **Status Codes**: The AI version uses FastAPI's built-in status definitions (e.g., `status.HTTP_201_CREATED`) which makes the code more robust, instead of hardcoding integers like `201` or `204`.
3. **Route Ordering**: The AI version carefully places specific endpoints (like `/tasks/search` and `/tasks/stats`) *before* parameterized endpoints (like `/tasks/{task_id}`) to avoid any routing conflicts.
4. **Data handling & Type Hinting**: The AI implementation uses strong Python type hints (`List`, `Optional`) and creates dedicated schema models (`TaskCreate`, `TaskUpdate`) for cleaner request body handling.
