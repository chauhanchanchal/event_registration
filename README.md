#  Campus Event Registration System

##  Project Description
This is a web-based event registration system built using **Flask** and **MySQL**.  
Users can register for different college events, while duplicate registrations are prevented.  
An admin dashboard allows viewing, searching, and managing all registrations.

---

## 📸 Preview
![Dashboard](screenshots/dashboard.png)

---

## Required Software
Before running the project, ensure you have:

1. **MySQL Server** – https://dev.mysql.com/downloads/installer/  
2. **MySQL Workbench (Optional)** – https://dev.mysql.com/downloads/workbench/  
3. **Python** – https://www.python.org/downloads/  
4. **pip** – python -m ensurepip --upgrade  
5. **Git** – https://git-scm.com/download/win  
6. **VS Code** – https://code.visualstudio.com/  

---

##  Features
- Event registration form  
- Duplicate email prevention (per event)  
- Admin dashboard to view registrations  
- Search and filter functionality  
- Real-time registration count  
- Clean and responsive UI  

---


##  Frontend (UI)

### 🔹 Overview
- Built using HTML, CSS, JavaScript  
- User-friendly and responsive interface  

### 🔹 Features
- Registration form (Name, Email, Event)  
- Uses fetch() API for backend communication  
- Displays success/error messages  
- Admin dashboard UI  
- Search and filter support  

### 🔹 Flow
1. User fills the form  
2. Clicks Register  
3. Data sent via fetch() API  
4. Response displayed to user  

---

##  Backend (Flask API)

### 🔹 Overview
- Built using Flask (Python)  
- Handles logic, validation, and database operations  

### 🔹 Features
- REST API endpoints  
- MySQL database integration  
- Duplicate registration prevention  
- JSON responses  



### 🔹 Flow
1. Receive request from frontend  
2. Validate input  
3. Check duplicate email  
4. Store data in MySQL  
5. Send response  

---

##  Frontend ↔ Backend Flow
- Frontend sends requests using fetch()  
- Backend processes via Flask routes  
- Data stored in MySQL  
- Response returned to frontend  

---

##  Tech Stack

### Frontend
- HTML  
- CSS  
- JavaScript  

### Backend
- Python (Flask)  
- Flask-CORS  

### Database
- MySQL (Localhost)  

---

##  Installation & Setup

### 1️ Clone the Repository
git clone  https://github.com/chauhanchanchal/event_registration.git                                                            


---

### 2️ Install Dependencies
pip install flask flask-cors mysql-connector-python  

---

### 3️ Setup MySQL Database

```sql
CREATE DATABASE college_events;

USE college_events;

CREATE TABLE registrations (
    id INT AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(100),
    email VARCHAR(100),
    event_name VARCHAR(100),
    registered_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

```
---

### 4️ Configure Database in app.py
```
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Chanchal55Pass.',
    'database': 'college_events'
}
```
---

##  Run the Application
```
py app.py  
```
Open in browser: 

http://127.0.0.1:5000  


---


##  How to View Data

### 🔹 Using Website
- Open Admin Dashboard  
- View all registrations in table  

### 🔹 Using MySQL
SELECT * FROM registrations;

### 🔹 Using API

http://127.0.0.1:5000/api/registrations

---

## 📸 Screenshots

### Registration Form
![Form](screenshots/form.png)

### Confirmation Message
![Success](screenshots/success.png)

### Admin Dashboard
![Dashboard](screenshots/dashboard.png)

---

## 🎥 Demo Video

▶️ Click the image below to watch demo:

[![Watch Demo](screenshots/form.png)](https://drive.google.com/file/d/1pGBMSj3qtzhnmIr7qNftph8JPV4-ItX1/view?usp=drive_link)

---


## Conclusion
This project demonstrates full-stack development using **Flask + MySQL** with frontend-backend integration.  
It provides a complete workflow from user input to database storage and admin-level data management.
