Stroke Prediction System – Secure Flask Web Application
Project Overview

The project is a secure web-based Stroke Prediction System implemented using Python Flask. This system will enable hospital workers to safely store and access patient information using a stroke prediction dataset given by the module leader. This project will show how to implement secure software development, database management, and web programming.
Features

The system includes the following features:

User registration and login system
Secure password hashing
Dashboard for system navigation
Add patient records
View patient records
Edit patient information
Delete patient records
View stroke prediction dataset
Secure session management
Clean and professional user interface
Technologies Used

Backend:

Python
Flask Framework

Frontend:

HTML
CSS

Database:

SQLite

Libraries:

Pandas
Werkzeug Security

Development Tools:

Visual Studio Code
GitHub
Project Structure
StrokePredictionSystem
│
├── app.py
├── create_database.py
├── database.db
├── stroke_prediction_dataset.csv
│
├── templates
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   ├── add_patient.html
│   ├── patients.html
│   ├── edit_patient.html
│   └── dataset.html
│
├── static
│   └── style.css
│
└── README.md
How to Run the Project

Follow these steps to run the system:

Step 1: Install Python
Make sure Python is installed on your computer.

Step 2: Install required libraries

pip install flask pandas

Step 3: Create the database

python create_database.py

Step 4: Run the application

python app.py

Step 5: Open in browser

http://127.0.0.1:5000/
Security Features

The system includes the following security features:

Password hashing using Werkzeug
Secure user sessions
Input validation
Protected dashboard access
Secure database storage
Testing

The system has been tested to ensure the following functions work correctly:

User registration
User login
Add patient
View patient
Edit patient
Delete patient
Dataset display
Future Improvements

The system can be improved in the future by adding:

Machine learning stroke prediction model
Patient search functionality
Role-based login system (Admin/Doctor)
Cloud deployment
Improved security using HTTPS
Author

Student Name: Manish Subedi
Student ID: 2511080
Module Name: Secure Software Development
University: Leeds Trinity University

Conclusion

This project illustrates how secure web applications can be created using Python’s Flask framework. The application also successfully enables users to manage patient information in a secure fashion by following secure software development principles.
