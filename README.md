# Task Management API

A full-stack backend API for managing tasks, built with Django REST Framework.
Users register, authenticate with JWT, and manage their own tasks (create,
read, update, delete, filter, search).

## Features

- **User registration & JWT authentication** (access + refresh tokens)
- **Task CRUD** scoped to the logged-in user (users only see their own tasks)
- **Filtering** by status, priority, and due date range
- **Search** across title/description
- **Ordering** by due date, priority, created date
- **Pagination** (10 per page)
- **Admin panel** for managing tasks/users
- **Unit tests** (10 tests covering auth and task CRUD) using DRF's `APITestCase`

## Tech Stack

- Django 5.x
- Django REST Framework
- djangorestframework-simplejwt (JWT auth)
- django-filter (filtering)
- SQLite (dev database)

## Setup

```bash
# 1. Clone and enter the project
git clone <your-repo-url>
cd taskapi

# 2. Create a virtual environment
python3 -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run migrations
python manage.py migrate

# 5. (Optional) create an admin user
python manage.py createsuperuser

# 6. Run the dev server
python manage.py runserver
```

API is now live at `http://127.0.0.1:8000/`.

## Run Tests

```bash
python manage.py test
```

## API Reference

### Auth

| Method | Endpoint                  | Auth | Description                     |
|--------|----------------------------|------|----------------------------------|
| POST   | `/api/auth/register/`      | No   | Create a new user account       |
| POST   | `/api/auth/login/`         | No   | Get JWT access + refresh tokens |
| POST   | `/api/auth/login/refresh/` | No   | Refresh an access token         |
| GET    | `/api/auth/me/`            | Yes  | Get current user's profile      |

**Register**
```bash
curl -X POST http://127.0.0.1:8000/api/auth/register/ \
  -H "Content-Type: application/json" \
  -d '{"username":"alice","email":"alice@example.com","password":"StrongPass123!","password2":"StrongPass123!"}'
```

**Login**
```bash
curl -X POST http://127.0.0.1:8000/api/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{"username":"alice","password":"StrongPass123!"}'
```
Returns `{"access": "...", "refresh": "..."}`. Use the access token in the
`Authorization: Bearer <token>` header for all task requests below.

### Tasks

All task endpoints require `Authorization: Bearer <access_token>` and are
scoped to the authenticated user.

| Method | Endpoint            | Description                  |
|--------|----------------------|-------------------------------|
| GET    | `/api/tasks/`        | List tasks (filter/search)   |
| POST   | `/api/tasks/`        | Create a task                |
| GET    | `/api/tasks/{id}/`   | Retrieve a task               |
| PUT    | `/api/tasks/{id}/`   | Full update                   |
| PATCH  | `/api/tasks/{id}/`   | Partial update                |
| DELETE | `/api/tasks/{id}/`   | Delete a task                 |

**Query parameters for list:**
- `status` — `pending` / `in_progress` / `completed`
- `priority` — `low` / `medium` / `high`
- `due_before`, `due_after` — `YYYY-MM-DD`
- `search` — matches title/description
- `ordering` — e.g. `due_date`, `-created_at`

**Create a task**
```bash
curl -X POST http://127.0.0.1:8000/api/tasks/ \
  -H "Authorization: Bearer <access_token>" \
  -H "Content-Type: application/json" \
  -d '{"title":"Write report","priority":"high","due_date":"2026-09-01"}'
```

**Filter completed, high-priority tasks**
```bash
curl "http://127.0.0.1:8000/api/tasks/?status=completed&priority=high" \
  -H "Authorization: Bearer <access_token>"
```

## Project Structure

```
taskapi/
├── config/          # Project settings, root URLs
├── accounts/        # Registration, JWT login, profile
├── tasks/           # Task model, CRUD API, filters, tests
├── manage.py
├── requirements.txt
└── README.md
```
