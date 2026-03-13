# FastAPI CI/CD Pipeline with Automated Deployment

![CI Pipeline](https://github.com/your-username/your-repo/actions/workflows/ci.yml/badge.svg)

## Project Overview

This project demonstrates a **Continuous Integration and Continuous Deployment (CI/CD) pipeline** for a Python-based web application.

The application is built using **FastAPI** and automatically **builds, tests, and deploys** whenever code is pushed to the repository.

The CI pipeline ensures code quality through automated testing, while the CD pipeline deploys the application to a cloud environment.

---

## Features

* FastAPI REST API
* Health monitoring endpoint
* Automated testing using pytest
* CI pipeline using GitHub Actions
* Automatic cloud deployment
* Version control using GitHub

---

## Tech Stack

Backend

* Python
* FastAPI

DevOps / CI-CD

* GitHub
* GitHub Actions

Deployment

* Render Cloud Platform

Testing

* Pytest

---

## System Architecture

```
Developer
   │
   ▼
Push Code to GitHub
   │
   ▼
GitHub Actions (CI Pipeline)
   │
   ├── Install Dependencies
   ├── Run Tests
   └── Build Application
   │
   ▼
Render Cloud Platform
   │
   ▼
Live FastAPI Application
```

---

## Project Structure

```
cicd-fastapi-project
│
├── main.py
├── requirements.txt
├── test_main.py
├── README.md
│
└── .github
    └── workflows
        └── ci.yml
```

---

## API Endpoints

### Home Endpoint

```
GET /
```

Response

```
{
  "message": "CI/CD Deployment Successful"
}
```

---

### Health Check Endpoint

```
GET /health
```

Response

```
{
  "status": "healthy"
}
```

---

## Running the Project Locally

### 1 Clone the Repository

```
git clone https://github.com/your-username/repository-name.git
cd repository-name
```

### 2 Create Virtual Environment

```
python -m venv venv
```

Activate environment

Windows

```
venv\Scripts\activate
```

Linux / Mac

```
source venv/bin/activate
```

---

### 3 Install Dependencies

```
pip install -r requirements.txt
```

---

### 4 Run the Server

```
uvicorn main:app --reload
```

Open browser

```
http://127.0.0.1:8000
```

API Docs

```
http://127.0.0.1:8000/docs
```

---

## Running Tests

```
pytest
```

Tests run automatically in the CI pipeline.

---

## CI/CD Workflow

The CI/CD workflow is implemented using **GitHub Actions**.

Workflow steps:

1. Developer pushes code to repository.
2. GitHub Actions triggers the CI pipeline.
3. Dependencies are installed.
4. Automated tests are executed.
5. If tests pass, the application is deployed automatically.

---

## Deployment

The application is deployed on **Render Cloud Platform**.

Render automatically redeploys the application when changes are pushed to the repository.
