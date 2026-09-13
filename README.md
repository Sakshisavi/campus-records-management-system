# Campus Records Management System

A web application designed to manage student records and administrative authentication. Built with Python, Flask, and MySQL, this project demonstrates structured MVC architecture, secure user authentication with password hashing, session management, and CRUD operations.

---

## Technical Stack & Architecture

* **Backend:** Python, Flask
* **Database:** MySQL
* **Database Driver:** `Flask-MySQLdb` / `mysqlclient`
* **Security & Auth:** Werkzeug Security (SHA-256 password hashing), Flask Sessions
* **Frontend Templating:** Jinja2, HTML5

---

## Features

* **Authentication & Authorization:**
  * Secure Admin Signup with automatic unique `Admin_id` generation.
  * Password hashing using Werkzeug’s security helpers.
  * Protected routes verifying active user sessions before granting access.
  * Admin profile management and session control (Logout).

* **Student CRUD Operations:**
  * **Create:** Add new student profiles (Name, Email, Course).
  * **Read:** Display all registered student records in a centralized dashboard.
  * **Update:** Modify existing student information by record ID.
  * **Delete:** Remove student records from the database.

* **Security & Config Isolation:**
  * Environment variable management using `.env` for sensitive database credentials.
  * Route modularization using Flask Blueprints (`auth_bp`).

---

## Database Schema Setup

Before running the application, set up the MySQL database and required tables.

```sql
CREATE DATABASE flask_crud;
USE flask_crud;

-- Admins Table
CREATE TABLE admins_record (
    Admin_id INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Department VARCHAR(100) NOT NULL,
    Email VARCHAR(100) UNIQUE NOT NULL,
    Password VARCHAR(255) NOT NULL
);

-- Students Table
CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    course VARCHAR(100) NOT NULL
);
Installation & Setup
1. Clone the Repository:

Bash
git clone [https://github.com/your-username/student-management-system.git](https://github.com/your-username/student-management-system.git)
cd student-management-system
2. Create and Activate a Virtual Environment:

Bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
3. Install Dependencies:

Bash
pip install Flask Flask-MySQLdb python-dotenv werkzeug
4. Configure Environment Variables:
Create a .env file in the root directory with your MySQL credentials:

Code snippet
MYSQL_HOST=localhost
MYSQL_USER=root
MYSQL_PASSWORD=your_mysql_password
MYSQL_DB=flask_crud
5.Run the Application:

Bash
python app.py
Navigate to http://127.0.0.1:5000 in your web browser.

#Project Structure
Plaintext
├── app.py              # Application entry point, main routes, and CRUD operations
├── auth.py             # Authentication Blueprint (Signup, Login, Profile, Logout)
├── config.py           # Configuration loader reading from environment variables
├── .env                # Environment variables (Git-ignored)
└── templates/          # Jinja2 HTML templates
    ├── add.html
    ├── edit.html
    ├── index.html
    ├── login.html
    ├── profile.html
    └── signup.html

## Screenshots

### 1. Signup Page
<img width="1915" height="982" alt="add" src="https://github.com/user-attachments/assets/ab23a0f3-d770-42bc-abbf-5301bd6dd956" />

### 2. Login Page
![Login Page](https://github.com/user-attachments/assets/bb71306b-921b-4903-a1df-b8efd824d773)

### 3. Dashboard
![Dashboard](https://github.com/user-attachments/assets/1ffae746-036d-4929-a1b7-e21a221f181f)

### 4. Add Record
![Add Record](https://github.com/user-attachments/assets/da83f382-e1d8-4c43-85f7-640a3ddb4a7d)

### 5. Edit Record
![Edit Record](https://github.com/user-attachments/assets/514d1ef4-564e-499c-b173-95cf8951dbec)

### 6. Profile Page
![Profile Page](https://github.com/user-attachments/assets/cb4e57d4-99fd-42ee-8959-1dd94e2ea407)


<img width="1905" height="967" alt="login" src="https://github.com/user-attachments/assets/23f55cd9-4e1d-49f4-9b17-1dced2f170c8" />







