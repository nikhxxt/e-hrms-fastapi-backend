
# 🧑‍💼 E-HRMS Backend API

A scalable, cloud-native FastAPI backend designed for enterprise-grade human resource management. This project automates core HR workflows including employee onboarding, attendance tracking, payroll computation, performance appraisal, and recruitment — all built with modular architecture, rigorous validation, and production-ready deployment.

---

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg) ![Render Status](https://img.shields.io/badge/Render-Live-blue) ![NeonDB](https://img.shields.io/badge/Neon-Postgres-green) ![Repo Size](https://img.shields.io/github/repo-size/nikhxxt/e-hrms-fastapi-backend)  ![GitHub Stars](https://img.shields.io/github/stars/nikhxxt/e-hrms-fastapi-backend?style=social)  ![GitHub Forks](https://img.shields.io/github/forks/nikhxxt/e-hrms-fastapi-backend?style=social)

---

## 📚 Table of Contents

- [📚 Project Description](#project-description)
- [🎯 Objectives](#objectives)
- [🔑 Core Features](#core-features)
- [🛠️ Tech Stack](#tech-stack)
- [📁 Project Structure](#project-structure)
- [🌐 Deployment Overview](#deployment-overview)
- [📡 Live Demo](#live-demo)
- [🚀 Getting Started](#getting-started)
- [🔐 Authentication Example](#authentication-example)
- [📝 License](#license)

---

## 📚 Project Description

This API powers a centralized HRMS platform tailored for medium-to-large enterprises. It enables HR teams to:

- Manage employee records and roles
- Track attendance and leave requests
- Automate payroll generation and tax deductions
- Store and evaluate performance KPIs
- Handle recruitment workflows and candidate tracking
- Send notifications and generate HR analytics

Built with **FastAPI**, it emphasizes:

- Modular routing and validation
- JWT-based authentication
- Role-based access control (Admin, HR, Employee)
- Background tasks and caching (Redis optional)
- Cloud-native deployment with **Render** and **NeonDB**
- Auto-generated OpenAPI documentation

---

## 🎯 Objectives

- Build a modular, cloud-deployable FastAPI backend  
- Implement secure CRUD operations across HR domains  
- Validate inputs and responses using Pydantic  
- Automate payroll logic and appraisal summaries  
- Enable scalable deployment via Render + Neon  
- Showcase recruiter-grade documentation and technical polish  
- Ensure reproducibility and environment isolation with `.env` and `render.yaml`

---

## 🔑 Core Features

### 👥 Employee Management
- Create, read, update, delete employee records
- Assign roles and departments
- Onboarding APIs

### 🕒 Attendance & Leave
- Clock-in/out endpoints (geo-tag optional)
- Leave request and approval workflows

### 💰 Payroll Automation
- Salary computation APIs
- Tax and deduction logic
- Background payroll generation

### 📈 Performance & Appraisal
- Store KPIs and goals
- Generate appraisal summaries

### 🧑‍💻 Recruitment
- Candidate resume upload
- Interview scheduling
- Status tracking

### 📬 Notifications & Reports
- Email/SMS hooks
- HR dashboard analytics endpoints

---

## 🛠️ Tech Stack

- **FastAPI** – High-performance Python framework  
- **SQLAlchemy** – ORM for PostgreSQL  
- **Pydantic** – Data validation and serialization  
- **Uvicorn** – ASGI server  
- **NeonDB** – Serverless Postgres with connection pooling  
- **Redis** – Optional caching and background tasks  
- **JWT** – Secure authentication  
- **Render** – Cloud deployment platform  
- **dotenv** – Environment variable management  
- **Pytest** – Unit testing framework

---

## 📁 Project Structure

```
e_hrms/
├── app/
│   ├── main.py                     # FastAPI app initialization
│   ├── core/                       # Core logic: auth, config, permissions
│   │   └── auth.py                 # JWT creation, validation, role checks
│   ├── db/                         # Database setup and session
│   │   └── session.py              # SQLAlchemy engine and get_db()
│   ├── models/                     # SQLAlchemy ORM models
│   │   └── employee.py             # Employee table schema
│   ├── routers/                    # API route definitions
│   │   ├── employees.py            # Employee CRUD endpoints
│   │   ├── attendance.py           # Attendance APIs
│   │   ├── payroll.py              # Payroll endpoints
│   │   ├── appraisal.py            # Performance APIs
│   │   ├── recruitment.py          # Candidate APIs
│   │   └── auth.py                 # Login/signup routes
│   ├── schemas/                    # Pydantic request/response models
│   │   └── employee.py             # EmployeeCreate, EmployeeOut, etc.
│   ├── services/                   # Business logic layer
│   │   └── payroll.py              # Salary computation, tax logic
│   ├── utils/                      # Helper functions
│   │   └── notifications.py        # Email/SMS hooks
├── tests/                          # Unit and integration tests
│   └── test_employee.py            # Sample test for employee endpoints
├── README.md                       # Project overview and usage
├── render.yaml                     # Render deployment configuration
├── requirements.txt                # Python dependencies
├── .env                            # Local environment variables (not committed)
```

---

## 🌐 Deployment Overview

- **Backend**: Deployed on [Render](https://render.com) using `render.yaml`
- **Database**: Managed Postgres via [Neon](https://neon.tech) with connection pooling
- **Environment Variables**: Managed securely via Render dashboard
- **Startup Logs**: Debug prints for `DATABASE_URL` and engine status
- **Health Check**: `/ping` endpoints for each router

---

## 📡 Live Demo

Deployed on Render:  
🔗 [e-hrms-fastapi-backend.onrender.com/docs](https://e-hrms-fastapi-backend.onrender.com/docs)

> ⚠️ Note: Free Render services may take 30–60 seconds to wake up after inactivity.

---

## 🚀 Getting Started

### Clone & Run Locally

```bash
git clone https://github.com/nikhxxt/e-hrms-fastapi-backend.git
cd e-hrms-fastapi-backend

# Install dependencies
pip install -r requirements.txt

# Create .env file and add your DATABASE_URL
touch .env
echo "DATABASE_URL=postgresql+psycopg2://..." >> .env

# Run the server
uvicorn app.main:app --reload
```

---

## 🔐 Authentication Example

Include this header in secured requests:

```http
Authorization: Bearer <your_jwt_token>
```

---

## 📝 License

This project is licensed under the **MIT License** — see [`LICENSE`](LICENSE).

