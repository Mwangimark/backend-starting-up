# 🧑‍💻 User Management API

This is a simple RESTful API built with **Flask** and **SQLAlchemy** for managing users. 
It includes features like creating users, updating information, deleting accounts,
and changing passwords. Passwords are securely hashed before storage.

---

## 🚀 Getting Started

### 1. Clone the Repository
2. Set Up Virtual Environment

[//]: # (python3 -m venv venv)

source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install Dependencies

[//]: # (pip install -r requirements.txt)

4. Run the Flask App

[//]: # (python main.py)
[//]: # (The app will start on http://127.0.0.1:5000)

```bash
git clone https://github.com/yourusername/user-management-api.git
cd user-management-api

== Project structure ==
backend-user/
├── main.py               # Entry point and routes
├── models.py             # User model
├── extensions.py         # SQLAlchemy initialization (if used)
├── config.py             # App config (optional)
├── requirements.txt      # Project dependencies
└── README.md             # Project documentation

API ENDPOINTS

| Method | Endpoint          | Description               |
| ------ | ----------------- | ------------------------- |
| POST   | `/users`          | Create a new user         |
| GET    | `/all_users`      | View all registered users |
| GET    | `/all_users/<id>` | Get a specific user by ID |
| PUT    | `/users/<id>`     | Change a user's password  |
| DELETE | `/users/<id>`     | Delete a user             |


🧪 Testing
You can test endpoints using:

Postman

Thunder Client (VS Code)

curl

✅ Features Implemented
 Create user

 Read users (all and specific)

 Update password

 Delete user

 Password hashing