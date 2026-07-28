# Django REST Framework (DRF) Practice APIs

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Django](https://img.shields.io/badge/Django-4.x-green?style=for-the-badge&logo=django)
![DRF](https://img.shields.io/badge/DRF-REST_API-red?style=for-the-badge&logo=django)
![Postman](https://img.shields.io/badge/Postman-API_Testing-orange?style=for-the-badge&logo=postman)

A comprehensive Django REST Framework practice repository featuring **2 Django Apps** and **4 Database Models**. This project demonstrates complete RESTful API development using both **Class-Based Views (CBVs)** and **Function-Based Views (FBVs)**, handling CRUD operations, data validation, and status codes.

---

## 🚀 Key Features

- **Multi-App Architecture:** Cleanly organized into two distinct domain apps.
- **Dual Implementation:** Includes practice implementation of both **APIView (CBV)** and `@api_view` decorator **(FBV)**.
- **Full CRUD Operations:** Support for `GET`, `POST`, `PUT`, `PATCH`, and `DELETE` HTTP methods.
- **Data Validation:** Implemented using DRF `Serializers` with unique constraints (Email, Roll Number, etc.).
- **Response Handling:** Custom and standardized JSON HTTP responses with proper status codes (`200 OK`, `201 Created`, `400 Bad Request`, `404 Not Found`).

---

## 🛠️ Tech Stack & Tools

- **Language:** Python
- **Framework:** Django, Django REST Framework (DRF)
- **Database:** SQLite / PostgreSQL
- **API Testing:** Postman / Thunder Client

---

## 📂 Project Structure & Models

The project is split into two applications, each containing two models:

### 📱 App 1: Student / Academic App
1. **Student Model** *(Class-Based View Implementation - `APIView`)*
   - `first_name` (CharField)
   - `last_name` (CharField)
   - `email` (EmailField, unique=True)
   - `roll_number` (IntegerField, unique=True)
   - `age` (IntegerField)

2. **Teacher Model** *(Function-Based View Implementation)*
   - `name` (CharField)
   - `subject` (CharField)
   - `salary` (DecimalField)
   - `joining_date` (DateField)

---

### 📱 App 2: Store / Management App
3. **Product / Store Models** *(Practiced with CRUD Operations & Partial Updates using `PUT` and `PATCH`)*
   - Dynamic schema models for handling product list and category management.

---

## 📌 API Endpoints Overview

| App / Feature | Endpoint | Method | View Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| **Student** | `/apic/student/` | `GET`, `POST` | CBV (`APIView`) | Fetch all students or create a new student |
| **Student** | `/apic/student/<id>/` | `GET`, `PUT`, `PATCH`, `DELETE` | CBV (`APIView`) | Retrieve, update, or delete a student record |
| **Teacher** | `/apic/teacher/` | `GET`, `POST` | FBV (`@api_view`) | List teachers or register a new teacher |
| **Teacher** | `/apic/teacher/<id>/` | `GET`, `PUT`, `DELETE` | FBV (`@api_view`) | Manage individual teacher details |

---

## 💻 Local Setup & Installation

Follow these steps to run the project locally on your machine:

1. **Clone the Repository:**
   ```bash
   git clone [https://github.com/mostakim-billah-shamim/API-testing-both-CBV-and-FBV-with-2-apps-28-7](https://github.com/yourusername/your-repository-name.git](https://github.com/mostakim-billah-shamim/API-testing-both-CBV-and-FBV-with-2-apps-28-7)
   cd API-testing-both-CBV-and-FBV-with-2-apps-28-7


   Create and Activate Virtual Environment:

Bash
# Windows
python -m venv env
env\Scripts\activate

# Linux/macOS
python3 -m venv env
source env/bin/activate
Install Dependencies:

Bash
pip install django djangorestframework
Apply Database Migrations:

Bash
python manage.py makemigrations
python manage.py migrate
Run Development Server:

Bash
python manage.py runserver
The server will start at http://127.0.0.1:8000/

🧪 Testing the APIs
You can test all endpoints using Postman or Thunder Client.

Example Request Body for Student POST (/apic/student/):
JSON
{
  "first_name": "Akil",
  "last_name": "Hossain",
  "email": "akil.hossain@example.com",
  "roll_number": 101,
  "age": 20
}
👨‍💻 Author
