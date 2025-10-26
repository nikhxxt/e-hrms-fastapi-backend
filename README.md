
# 🧑‍💼 E-HRMS Backend API

A scalable FastAPI backend designed for enterprise-grade human resource management. This project automates core HR workflows including employee onboarding, attendance tracking, payroll computation, performance appraisal, and recruitment—all built with modular architecture and production-ready standards.

---

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Render Status](https://img.shields.io/badge/Render-Live-blue)
![Repo Size](https://img.shields.io/github/repo-size/nikhxxt/e-hrms-fastapi-backend)
![GitHub Stars](https://img.shields.io/github/stars/nikhxxt/e-hrms-fastapi-backend?style=social)
![GitHub Forks](https://img.shields.io/github/forks/nikhxxt/e-hrms-fastapi-backend?style=social)

---

## 📚 Table of Contents

- [📚 Project Description](#project-description)
- [🎯 Objectives](#objectives)
- [🔑 Core Features](#core-features)
- [🛠️ Tech Stack](#tech-stack)
- [📁 Project Structure](#project-structure)
- [📡 Live Demo](#live-demo)
- [🚀 Getting Started](#getting-started)
- [🔐 Authentication Example](#authentication-example)
- [📝 License](#license)

---

## 📚 Project Description

This API serves as the backend engine for a centralized HRMS platform. It enables HR teams to:
- Manage employee records and roles
- Track attendance and leave requests
- Automate payroll generation and tax deductions
- Store and evaluate performance KPIs
- Handle recruitment workflows and candidate tracking

Built with **FastAPI**, it emphasizes:
- Modular routing and validation
- JWT-based authentication
- Role-based access control
- Background tasks and caching (Redis optional)
- Auto-generated documentation

---

## 🎯 Objectives

- Build a modular, cloud-deployable FastAPI backend  
- Implement secure CRUD operations across HR domains  
- Validate inputs and responses using Pydantic  
- Automate payroll logic and appraisal summaries  
- Enable scalable deployment via Render  
- Showcase recruiter-ready documentation and code clarity  

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
- **SQLAlchemy** – ORM for PostgreSQL/MySQL  
- **Pydantic** – Data validation and serialization  
- **Uvicorn** – ASGI server  
- **Redis** – Optional caching and background tasks  
- **JWT** – Secure authentication  
- **Render** – Cloud deployment platform  

---

## 📁 Project Structure

```
e_hrms/
├── app/
│   ├── main.py
│   ├── core/               # Auth, config, permissions
│   ├── models/             # SQLAlchemy models
│   ├── schemas/            # Pydantic schemas
│   ├── routers/            # Modular API routes
│   ├── services/           # Business logic (payroll, appraisal)
│   ├── utils/              # Email/SMS hooks, helpers
│   └── db/                 # DB session, init
├── tests/
├── requirements.txt
├── README.md
├── .env
└── render.yaml
```

---

## 📡 Live Demo

Deployed on Render:  
🔗 [e-hrms-fastapi-backend](https://e-hrms-fastapi-backend.onrender.com/docs)

> Note: Free Render services may take 30–60 seconds to wake up after inactivity.

---

## 🚀 Getting Started

### Clone & Run Locally

```bash
git clone https://github.com/nikhxxt/e-hrms-fastapi-backend.git
cd e-hrms-fastapi-backend

# Install dependencies
pip install -r requirements.txt

# Run the server
uvicorn app.main:app --reload
```

---

## 🔐 Authentication Example

Include this header in secured requests:

```
Authorization: Bearer <your_jwt_token>
```

---

## 📝 License

This project is licensed under the **MIT License** — see [`LICENSE`](LICENSE).
