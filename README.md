# 🧑‍💼 E-HRMS Backend API

A modular FastAPI backend for managing core Human Resource Management System (HRMS) operations through structured REST APIs. The project focuses on backend architecture, API design, authentication, data validation, and database-driven HR workflows.

---

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-API-green)

---

## 📚 Table of Contents

- [📌 Overview](#-overview)
- [✨ Features](#-features)
- [🏗️ Architecture](#️-architecture)
- [📡 API Modules](#-api-modules)
- [🔐 Authentication](#-authentication)
- [🛠️ Tech Stack](#️-tech-stack)
- [📁 Project Structure](#-project-structure)
- [🚀 Getting Started](#-getting-started)
- [🧪 API Documentation](#-api-documentation)
- [🌐 Live Demo](#-live-demo)
- [☁️ Deployment](#️-deployment)
- [📜 License](#-license)

---

## 📌 Overview

E-HRMS is a backend API designed to support common HR management workflows through modular REST endpoints.

The application is built with **FastAPI** and follows a structured backend architecture with separate modules for routing, data models, authentication, and application logic.

The project demonstrates practical backend development concepts including:

- REST API design
- Modular routing
- Request validation
- Database operations
- Authentication and authorization
- CRUD workflows
- Structured API responses
- API documentation
- Backend deployment

---

## ✨ Features

### 👥 Employee Management

- Create and manage employee records
- Retrieve employee information
- Update employee details
- Organize employee-related data through REST APIs

### 🔐 Authentication & Authorization

- Secure API access using authentication mechanisms
- Protected backend endpoints
- Role-based access where implemented

### 🕒 Attendance Management

- Manage employee attendance-related records
- Provide structured endpoints for attendance workflows
- Associate attendance information with employees

### 🏢 HR Management

- Support HR-related employee workflows
- Organize HR operations through modular API routes
- Maintain structured request and response models

### 🗄️ Data Management

- Database-backed data operations
- Structured models for application entities
- Validation of incoming API data

### 📚 API Documentation

- Automatic OpenAPI documentation
- Interactive Swagger UI
- ReDoc documentation
- Organized API routes and schemas

---

## 🏗️ Architecture

The backend follows a modular structure that separates API routes, application logic, models, and supporting components.

```text
Client
   │
   ▼
FastAPI Application
   │
   ├── Authentication
   │
   ├── API Routers
   │      ├── Employee APIs
   │      ├── Attendance APIs
   │      └── HR APIs
   │
   ├── Validation / Schemas
   │
   ├── Business Logic
   │
   └── Database Layer
            │
            ▼
        Database
````

This structure keeps individual API modules separated and makes the backend easier to maintain and extend.

---

## 📡 API Modules

The API is organized around core HRMS functionality.

### Employees

| Method   | Endpoint                   | Description                 |
| -------- | -------------------------- | --------------------------- |
| `POST`   | `/employees/`              | Create an employee          |
| `GET`    | `/employees/`              | Retrieve employees          |
| `GET`    | `/employees/{employee_id}` | Retrieve an employee        |
| `PUT`    | `/employees/{employee_id}` | Update employee information |
| `DELETE` | `/employees/{employee_id}` | Delete an employee          |

### Attendance

Attendance endpoints provide operations for managing employee attendance records.

### HR Operations

HR-related endpoints support employee and HR management workflows through structured API requests.

> Endpoint names and available operations are documented in the generated OpenAPI specification.

---

## 🔐 Authentication

Protected endpoints require authentication before access is granted.

Authentication is handled at the API layer, allowing protected routes to verify incoming requests before processing operations.

Example authenticated request:

```http
Authorization: Bearer <token>
```

The exact authentication flow and available protected endpoints can be tested through Swagger UI.

---

## 🛠️ Tech Stack

* **Python 3.10+** – Backend development
* **FastAPI** – REST API framework
* **Pydantic** – Request validation and data serialization
* **SQLAlchemy** – Database interaction
* **JWT** – Token-based authentication
* **bcrypt** – Password hashing
* **PostgreSQL / Neon** – Database
* **Uvicorn** – ASGI application server
* **OpenAPI / Swagger UI** – API documentation
* **ReDoc** – API reference documentation
* **Render** – Deployment platform

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
│
├── requirements.txt
├── render.yaml
├── LICENSE
└── README.md
```

> The structure above represents the modular organization of the backend. File and directory names may vary based on the current repository implementation.

---

## 🚀 Getting Started

### Prerequisites

Make sure the following are installed:

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

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

Activate it on macOS/Linux:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file and configure the environment variables required by the application.

Example:

```env
DATABASE_URL=your_database_url
SECRET_KEY=your_secret_key
```

Use the variable names defined by the application configuration.

### Run the Application

```bash
uvicorn main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

---

## 🧪 API Documentation

Once the application is running, interactive API documentation is available through FastAPI.

### Swagger UI

```text
http://127.0.0.1:8000/docs
```

### ReDoc

```text
http://127.0.0.1:8000/redoc
```

Swagger UI can be used to:

* Explore available endpoints
* Inspect request and response schemas
* Authenticate protected requests
* Send API requests
* Review response codes
* Test API workflows interactively

---

## 🌐 Live Demo

The API is deployed and available online.

**API Base URL:**  
[https://YOUR-EHRMS-URL.onrender.com](https://YOUR-EHRMS-URL.onrender.com)

**Swagger UI:**  
[https://YOUR-EHRMS-URL.onrender.com/docs](https://YOUR-EHRMS-URL.onrender.com/docs)

**ReDoc:**  
[https://YOUR-EHRMS-URL.onrender.com/redoc](https://YOUR-EHRMS-URL.onrender.com/redoc)

You can use Swagger UI to explore and test the available API endpoints interactively.
---


## ☁️ Deployment

The backend is configured for deployment using **Render**.

Deployment configuration is maintained through the project's deployment configuration files.

After deployment, the API documentation can be accessed through the deployed `/docs` endpoint.

---

## 🧩 Backend Concepts Demonstrated

This project demonstrates practical implementation of:

* RESTful API development
* Modular FastAPI architecture
* CRUD operations
* Pydantic validation
* Database integration
* Authentication
* Authorization
* Password security
* JWT-based access control
* Structured API responses
* Error handling
* OpenAPI documentation
* Cloud deployment

---

## 📜 License

This project is licensed under the **MIT License**.

See the [`LICENSE`](LICENSE) file for details.




