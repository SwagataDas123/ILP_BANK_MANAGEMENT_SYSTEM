# 💰 Bank Management System (Python CLI Project)
A Bank Management System implemented in Python, providing a console-based interface for handling customer registration, account creation, deposits, withdrawals, employee management, and customer detail management. The system is designed for educational purposes to demonstrate object-oriented programming, validation, and simple data handling.

## 📚 Project Introduction
This project simulates a basic banking environment where:

Customers can register, log in, create accounts, deposit or withdraw money, and manage personal information.

Employees can register, log in, and view or update customer data (not perform transactions).

Admin-like functionality is available through employee access for CRUD operations on customers.

It is a self-contained system that runs in the terminal/command line and manages in-memory data without the need for a database.

## Built With
Python 3

random for ID generation

datetime for timestamping

re for validation (email, PAN, name formats)

## 🧩 Entities Created
1. Employee
Fields: employee_id, name, email, password, address, contact_number

Can log in and manage customer records (CRUD operations).

2. Customer
Fields: ssn_no, name, email, address, contact_number, aadhar_number, pan_number, password

Can register, log in, manage personal information, and own multiple accounts.

3. Account
Fields: account_number, account_type, balance, customer_ssn_no, date_of_creation

Linked to customers, supports deposit, withdrawal, and balance check operations.

## ✨ Features
✅ Validation
Name: must contain first and last name, ≤50 characters.

Email: proper format + uniqueness.

Contact: exactly 10 digits.

Aadhar: exactly 12 digits.

PAN: 10-character alphanumeric format (e.g., ABCDE1234F).

✅ Employee Panel
Register/Login securely.

Enter new customers.

View or update customer details.

Delete customers from the system.

✅ Customer Panel
Register/Login securely.

Manage account: deposit, withdraw, view balance.

View and update personal information.

✅ Account Handling
Multiple account support for a customer.

Enforces minimum balance and withdrawal limits.

## 🔁 Project Workflow
1.Startup

Initialize empty dictionaries: employees, customers, accounts.

2.Employee Operations

Registration with validation.

Login using email, password, and employee ID.

Enter, view, update, or delete customer records.

3.Customer Operations

Self-registration and SSN/account generation.

Login via SSN and password.

Deposit/Withdraw/Check balance.

View or update personal details.

4.Account Operations

Account creation on customer registration.

Balance updates via transactions.

## 🚧 Limitations & Future Improvements
❌ No persistent storage (data lost after program exit).

❌ No GUI or web interface.

✅ Possible future enhancements:

SQLite or PostgreSQL database integration.

GUI using Tkinter or PyQt.

Role-based authentication system.

Transaction logs.

## 🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to change.

## 📄 License
This project is open-source and available under the MIT License.

