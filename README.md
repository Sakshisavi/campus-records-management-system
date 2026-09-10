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
#SCREENSHOTS
##1.Login: It's the First Pagw
![Login Page]<img width="1905" height="967" alt="login" src="https://github.com/user-attachments/assets/bf571f93-e7c0-43aa-8228-7ed193733595" />

###2.Signup:
![Login Page]<img width="1902" height="953" alt="signup" src="https://github.com/user-attachments/assets/7e8f6742-36f8-489e-b923-bfe9514ea42e" />

###3.Log_now: after signing up you can log in
![Login Page]<img width="1907" height="970" alt="login_now" src="https://github.com/user-attachments/assets/e9d0f68c-5829-44ee-a1c3-3d219be17adf" />

##4.Home/Index Page: Where students Records are kept.
![Login Page]<img width="1917" height="967" alt="index" src="https://github.com/user-attachments/assets/99de60f9-fec5-41b6-ab40-45ed5aa01113" />

##5.Add Page: Add a new student to the record:
![Login Page]<img width="1915" height="982" alt="add" src="https://github.com/user-attachments/assets/bad67184-335a-4904-9c8c-6218fb55de8d" />

##6.Indec/Home Page: After adding, a new record is displayed here
<img width="1915" height="977" alt="after_add" src="https://github.com/user-attachments/assets/640bf2b5-fb3a-472d-86a2-360953bf60fa" />

##7.Edit Page: To make changes to the records stored.
![Login Page]<img width="1912" height="967" alt="edit" src="https://github.com/user-attachments/assets/0e9a1260-f47f-417a-9ffa-6ab77f113186" />

##8.Index/Home Page: to check the updated record
![Login Page]<img width="1912" height="976" alt="after_edit" src="https://github.com/user-attachments/assets/3c1eafc9-45ce-4c90-a5f0-48f2158a9366" />

##9.Profile Page: To see the admin information
![Login Page]<img width="1913" height="962" alt="profile" src="https://github.com/user-attachments/assets/2ca184a2-f98c-4dae-af35-0009cbfbe8fc" />






