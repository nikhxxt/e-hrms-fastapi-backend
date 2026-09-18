# 🧑‍💼 E-HRMS Backend API

A modular **FastAPI backend for Human Resource Management System (HRMS) workflows**, providing REST APIs for employee and HR-related operations.

The project focuses on practical backend development including **API design, CRUD operations, authentication, data validation, database integration, and API documentation**.

---

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-API-green)
![Render](https://img.shields.io/badge/Deployed%20on-Render-purple)

---

## ✨ Features

### 👥 Employee Management
- Create employee records
- Retrieve employee information
- Update employee details
- Delete employee records

### 🕒 Attendance Management
- Manage employee attendance records
- Associate attendance data with employees

### 🔐 Authentication & Authorization
- Protected API endpoints
- Token-based authentication
- JWT-based access control
- Password hashing

### 🗄️ Database Operations
- Database-backed application data
- Structured data models
- Request validation
- ORM-based database interaction

### 📚 API Documentation
- OpenAPI specification
- Interactive Swagger UI
- ReDoc API documentation

---

## 📡 API Modules

### Employees

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/employees/` | Create an employee |
| `GET` | `/employees/` | Get all employees |
| `GET` | `/employees/{employee_id}` | Get employee by ID |
| `PUT` | `/employees/{employee_id}` | Update employee |
| `DELETE` | `/employees/{employee_id}` | Delete employee |

### Attendance

Provides endpoints for managing employee attendance records.

### HR Operations

Provides APIs for HR-related employee management workflows.

> The complete list of available endpoints and schemas is available through the live Swagger documentation.

---

## 🛠️ Tech Stack

- **Python** – Backend development
- **FastAPI** – REST API framework
- **Pydantic** – Data validation and serialization
- **SQLAlchemy** – ORM and database interaction
- **PostgreSQL / Neon** – Database
- **JWT** – Authentication and access control
- **bcrypt** – Password hashing
- **Uvicorn** – ASGI server
- **OpenAPI / Swagger UI** – API documentation
- **ReDoc** – API reference
- **Render** – Deployment

---

## 🏗️ Architecture

```text
Client
   │
   ▼
FastAPI Application
   │
   ├── Authentication
   ├── API Routers
   │     ├── Employees
   │     ├── Attendance
   │     └── HR Operations
   │
   ├── Schemas / Validation
   ├── Services
   │
   ▼
Database Layer
   │
   ▼
PostgreSQL / Neon
````

---

## 📁 Project Structure

```text
e-hrms-fastapi-backend/
├── app/
│   ├── routers/
│   ├── models/
│   ├── schemas/
│   ├── services/
│   ├── dependencies/
│   └── main.py
│
├── tests/
├── requirements.txt
├── render.yaml
├── LICENSE
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites

* Python 3.10+
* pip
* Git
* PostgreSQL or the configured database service

### Clone the Repository

```bash
git clone https://github.com/nikhxxt/e-hrms-fastapi-backend.git
cd e-hrms-fastapi-backend
```

### Create a Virtual Environment

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**macOS / Linux**

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file with the variables required by the application.

Example:

```env
DATABASE_URL=your_database_url
SECRET_KEY=your_secret_key
```

> Keep credentials and secret keys out of the repository.

### Run Locally

```bash
uvicorn main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

---

## 🧪 API Documentation

Once the application is running, use the following endpoints:

### Swagger UI

```text
http://127.0.0.1:8000/docs
```

Swagger UI allows you to:

* Explore API endpoints
* View request and response schemas
* Authorize protected requests
* Send requests directly from the browser
* Inspect API responses

### ReDoc

```text
http://127.0.0.1:8000/redoc
```

ReDoc provides a clean reference view of the API and its schemas.

---

## 🌐 Live Demo

The API is deployed on **Render**.

### 🔗 Swagger UI

[**Open Live Swagger Documentation →**](https://e-hrms-fastapi-backend.onrender.com/docs#/Employees/create_employee_employees__post)

### 🔗 ReDoc

[**Open Live ReDoc →**](https://e-hrms-fastapi-backend.onrender.com/redoc)

### 🔗 OpenAPI Specification

[**View OpenAPI JSON →**](https://e-hrms-fastapi-backend.onrender.com/openapi.json)

You can use the live Swagger UI to explore the available endpoints and interact with the deployed API.

> The free deployment may take some time to wake up after a period of inactivity.

---

## 🔐 Authentication

Protected endpoints require authentication.

Example:

```http
Authorization: Bearer <token>
```

Authentication credentials and secret keys should be provided through environment variables rather than committed to the repository.

---

## 📜 License

This project is licensed under the **MIT License**.

See the [`LICENSE`](LICENSE) file for details.





