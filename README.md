# Task Management REST API

A secure and scalable RESTful Task Management API built using **Django REST Framework (DRF)** with **JWT-based authentication**. The application allows authenticated users to create, view, update, delete, and filter their tasks through REST API endpoints.

---

## 🚀 Features

* User registration
* JWT-based authentication
* User login and token generation
* Protected API endpoints
* Create tasks
* Retrieve tasks
* Update tasks
* Delete tasks
* User-specific task management
* Filter tasks by status
* Filter tasks by priority
* SQLite database integration
* Django ORM
* Automated API testing
* Postman API testing
* Clean modular project structure

---

## 🛠️ Technologies Used

| Technology            | Purpose              |
| --------------------- | -------------------- |
| Python                | Programming language |
| Django                | Web framework        |
| Django REST Framework | REST API development |
| Simple JWT            | JWT authentication   |
| SQLite                | Database             |
| django-filter         | API filtering        |
| Postman               | API testing          |
| Git                   | Version control      |
| GitHub                | Source code hosting  |

---

## 📁 Project Structure

```text
django-task-management-api/
│
├── accounts/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   └── views.py
│
├── tasks/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── filters.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── config/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── screenshots/
│   ├── 01-registration.png
│   ├── 02-jwt-login.png
│   ├── 03-create-task.png
│   ├── 04-get-tasks.png
│   ├── 05-update-task.png
│   ├── 06-delete-task.png
│   ├── 07-status-filter.png
│   ├── 08-priority-filter.png
│   └── 09-automated-tests.png
│
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/kumarsumitsohan/django-task-management-api.git
```

### 2. Navigate to the project directory

```bash
cd django-task-management-api
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

For Windows:

```powershell
venv\Scripts\activate
```

For macOS/Linux:

```bash
source venv/bin/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Apply database migrations

```bash
python manage.py migrate
```

### 7. Run the development server

```bash
python manage.py runserver
```

The application will be available at:

```text
http://127.0.0.1:8000/
```

---

# 🔐 Authentication

The API uses **JSON Web Token (JWT)** authentication.

Authentication flow:

```text
User Registration
       ↓
     Login
       ↓
JWT Access + Refresh Token
       ↓
Authorization Header
       ↓
Protected Task APIs
```

For protected endpoints, include the access token in the request header:

```text
Authorization: Bearer <access_token>
```

---

# 👤 User Authentication APIs

## Register User

**Method:**

```text
POST
```

**Endpoint:**

```text
/api/auth/register/
```

### Example Request

```json
{
    "username": "username",
    "email": "user@example.com",
    "password": "StrongPass123!",
    "password2": "StrongPass123!"
}
```

### Response

A successful registration returns:

```text
201 Created
```

---

## Login

**Method:**

```text
POST
```

**Endpoint:**

```text
/api/auth/login/
```

### Example Request

```json
{
    "username": "username",
    "password": "StrongPass123!"
}
```

### Response

The API returns JWT tokens:

```json
{
    "refresh": "<refresh_token>",
    "access": "<access_token>"
}
```

The access token is used for authenticated requests.

---

# 📋 Task Management APIs

## Create Task

**Method:**

```text
POST
```

**Endpoint:**

```text
/api/tasks/
```

### Example Request

```json
{
    "title": "Prepare Interview",
    "description": "Prepare Django REST API questions",
    "status": "pending",
    "priority": "high",
    "due_date": "2026-09-15"
}
```

### Response

```text
201 Created
```

The API automatically associates the task with the authenticated user.

---

## Get Tasks

**Method:**

```text
GET
```

**Endpoint:**

```text
/api/tasks/
```

### Response

```text
200 OK
```

The endpoint returns the authenticated user's tasks.

Example:

```json
{
    "count": 2,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "owner": "username",
            "title": "Learn Django",
            "description": "Study Django REST Framework",
            "status": "pending",
            "priority": "high",
            "due_date": "2026-09-01"
        }
    ]
}
```

---

## Update Task

**Method:**

```text
PUT
```

**Endpoint:**

```text
/api/tasks/<id>/
```

### Example

```text
/api/tasks/1/
```

### Example Request

```json
{
    "title": "Learn Django REST Framework",
    "description": "Complete Django REST API preparation",
    "status": "completed",
    "priority": "high",
    "due_date": "2026-09-05"
}
```

### Response

```text
200 OK
```

---

## Delete Task

**Method:**

```text
DELETE
```

**Endpoint:**

```text
/api/tasks/<id>/
```

### Example

```text
/api/tasks/1/
```

### Successful Response

```text
204 No Content
```

---

# 🔎 Filtering

The API supports filtering tasks based on their attributes.

## Filter by Status

### Pending Tasks

```text
GET /api/tasks/?status=pending
```

### Completed Tasks

```text
GET /api/tasks/?status=completed
```

---

## Filter by Priority

### High Priority

```text
GET /api/tasks/?priority=high
```

### Medium Priority

```text
GET /api/tasks/?priority=medium
```

---

# 🧪 Testing

The project includes automated tests for validating application functionality.

Run the test suite using:

```bash
python manage.py test
```

A successful test execution should display:

```text
OK
```

The API endpoints were also manually tested using **Postman**.

### Tested Functionality

* User registration
* JWT login
* Authentication
* Task creation
* Task retrieval
* Task update
* Task deletion
* Status filtering
* Priority filtering

---

# 📸 API Testing Screenshots

The following screenshots demonstrate the successful testing of the API.

## 1. User Registration

Successful user registration using the REST API.

![User Registration](screenshots/01-registration.png)

---

## 2. JWT Authentication

Successful login and JWT token generation.

![JWT Login](screenshots/02-jwt-login.png)

---

## 3. Create Task

Successful task creation using the POST endpoint.

![Create Task](screenshots/03-create-task.png)

---

## 4. Retrieve Tasks

Successful retrieval of authenticated user's tasks.

![Get Tasks](screenshots/04-get-tasks.png)

---

## 5. Update Task

Successful task update using the PUT endpoint.

![Update Task](screenshots/05-update-task.png)

---

## 6. Delete Task

Successful task deletion using the DELETE endpoint.

![Delete Task](screenshots/06-delete-task.png)

---

## 7. Filter by Status

Successful filtering of tasks based on status.

![Status Filter](screenshots/07-status-filter.png)

---

## 8. Filter by Priority

Successful filtering of tasks based on priority.

![Priority Filter](screenshots/08-priority-filter.png)

---

## 9. Automated Tests

Successful execution of the Django automated test suite.

![Automated Tests](screenshots/09-automated-tests.png)

---

# 🔄 API Workflow

```text
                 ┌─────────────────┐
                 │   Register User │
                 └────────┬────────┘
                          ↓
                 ┌─────────────────┐
                 │      Login      │
                 └────────┬────────┘
                          ↓
                 ┌─────────────────┐
                 │   JWT Token     │
                 └────────┬────────┘
                          ↓
                 ┌─────────────────┐
                 │ Authenticated   │
                 │   Task APIs     │
                 └────────┬────────┘
                          ↓
          ┌───────────────┼───────────────┐
          ↓               ↓               ↓
       Create           Read            Update
          │               │               │
          └───────────────┼───────────────┘
                          ↓
                       Delete
                          ↓
                    Filter Tasks
```

---

# 🔒 Security

The application uses JWT authentication to protect task-related endpoints.

Important security practices include:

* Protected task APIs
* User-specific task access
* Password authentication
* JWT access tokens
* Sensitive files excluded through `.gitignore`

> **Note:** Never commit real passwords, JWT tokens, API keys, or Django secret keys to a public repository.

---

# 🗄️ Database

The project uses **SQLite** for development and testing.

Django ORM is used for database interaction, allowing the application to work with database models without writing raw SQL queries for normal operations.

---

# 📌 Future Improvements

The project can be extended with:

* PostgreSQL database
* Docker support
* API documentation using Swagger/OpenAPI
* Task search functionality
* Pagination customization
* Task categories and labels
* Email notifications
* Role-based permissions
* Cloud deployment
* CI/CD using GitHub Actions
* Production WSGI/ASGI deployment

---

# 🎯 Learning Outcomes

Through this project, the following concepts were implemented and practiced:

* Django project structure
* Django REST Framework
* RESTful API design
* HTTP methods
* CRUD operations
* JWT authentication
* Serializers
* Django models and ORM
* API filtering
* Database migrations
* Automated testing
* Postman API testing
* Git version control
* GitHub repository management

---

# 👨‍💻 Author

**Sumit Sohan**

GitHub: [@kumarsumitsohan](https://github.com/kumarsumitsohan)

Repository: [django-task-management-api](https://github.com/kumarsumitsohan/django-task-management-api)

---

## ⭐ Project Status

**Completed and tested successfully.**

The project has been tested using both automated Django tests and manual Postman API testing.
