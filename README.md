Org Management Service (Multi-Tenant Backend)

A production-ready FastAPI + MongoDB + JWT Auth backend that supports:

Multi-tenant organizations

Dynamic collection creation per organization

Admin authentication

Encrypted passwords

Docker + docker-compose deployment

Clean architecture (Routers → Services → Models → DB → Utils)

📁 Project Structure
org-management-service/
│
├── app/
│   ├── main.py
│   ├── config.py
│   ├── db.py
│   ├── exceptions.py
│   ├── middleware/
│   ├── models/
│   ├── schemas/
│   ├── routers/
│   ├── services/
│   └── utils/
│
├── tests/
├── .env.example
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md

⚙️ Features
✅ Multi-Tenant Architecture

Each organization gets its own MongoDB collection dynamically created during onboarding.

✅ Admin Authentication

Email + password login

Bcrypt password hashing

JWT access tokens

✅ Organization Management

Create organizations

Auto-create admin for each org

Auto-generate unique collection name per org

✅ MongoDB Indexes

Unique organization name

Unique admin email

✅ Fully Containerized

Works with Docker & docker-compose.

🧰 Tech Stack
Component	Technology
Backend Framework	FastAPI
Database	MongoDB
ORM/Driver	Motor (async MongoDB driver)
Auth	JWT (python-jose)
Password Hashing	Passlib (bcrypt)
Deployment	Docker
Environment	Python 3.11
📦 Installation
1. Clone the repository
git clone https://github.com/yourname/org-management-service.git
cd org-management-service

2. Create a virtual environment (optional)
python -m venv venv
source venv/bin/activate   # macOS / Linux
venv\Scripts\activate      # Windows

3. Install dependencies
pip install -r requirements.txt

🔧 Environment Variables

Create a .env file (or copy .env.example):

MONGO_URL=mongodb://mongo:27017
JWT_SECRET=SUPERSECRETJWTKEY

🐳 Run with Docker (Recommended)

Ensure Docker Desktop is running.

👉 Start the backend + MongoDB:
docker-compose up --build

Server runs at:
http://localhost:8000

Swagger Docs:
http://localhost:8000/docs

🛠 API Endpoints
🏢 1. Create Organization

POST /org/create

Request Body:
{
  "organization_name": "Akshay Pvt Ltd",
  "email": "admin@example.com",
  "password": "Admin@123"
}

Response:
{
  "id": "676fd12c912bf...",
  "organization_name": "Akshay Pvt Ltd",
  "collection_name": "org_akshay_pvt_ltd"
}

👤 2. Admin Login

POST /admin/login

Request Body:
{
  "email": "admin@example.com",
  "password": "Admin@123"
}

Response:
{
  "access_token": "<JWT_TOKEN>",
  "token_type": "bearer"
}

🧪 Running Tests
pytest

🧱 Architecture Overview
                +-------------------------+
                |    FASTAPI BACKEND      |
                +-------------------------+
                       |      |
     -------------------      ----------------------
     |                                             |
+---------+                                   +----------------+
| Org API |                                   | Admin API      |
+---------+                                   +----------------+
     |                                             |
+----------------+                         +---------------------+
| OrgService     |                         | AuthService         |
+----------------+                         +---------------------+
     |                                             |
+--------------------------+             +------------------------------+
| master_db.organizations |             | master_db.admins              |
+--------------------------+             +------------------------------+

         +-------------------------------------------+
         | Dynamic per-organization collections       |
         | org_<organization_name>                    |
         +-------------------------------------------+

🚨 Common Errors & Fixes
❌ ImportError: email-validator is not installed

Fix:

pip install email-validator

❌ MongoDB connection refused

Ensure Docker is running and container name is correct:

docker ps

📌 Production Deployment Guide

For production:

Use Gunicorn + Uvicorn workers

Use Mongo Atlas instead of local MongoDB

Add rate-limiting middleware

Add CORS rules

Use HTTPS behind reverse proxy (NGINX)

ERP-like systems

Organization management systems
