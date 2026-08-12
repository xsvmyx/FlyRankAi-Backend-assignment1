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