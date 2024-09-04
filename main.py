from fastapi import FastAPI
from typing import Union

description = """

This FastAPI-based project implements a comprehensive School Management System API. The API offers a range of endpoints for efficiently managing various aspects of a school's operations. Key features include:

1. Student Management: Perform CRUD operations on student records.
2. Teacher Management: Handle teacher information and assignments.
3. Course Management: Manage course offerings, schedules, and enrollments.
4. Related Entities: Additional functionalities for managing other school-related data.

The API utilizes JSON for data exchange, ensuring easy integration with various client applications. It provides a robust set of tools for school administrators, teachers, and other stakeholders to streamline school management processes.

This API serves as a powerful backend solution for school management software, offering flexibility and scalability to meet diverse educational institution needs.
"""


app = FastAPI(
    title="School Management System API",
    summary="A School management system  with robust functionalities.",
    description=description,
    version="0.0.1"
)

@app.get('/')
def read_root():
    return {'Hello': "world"}
