# 🛒 Smart Inventory & Billing Management System

A desktop-based inventory management and billing software built using **Python (Tkinter GUI)** and **MySQL Database**.  
This application helps shops and businesses maintain Products, Suppliers, Customers, Stock, and Billing efficiently in a single system.

---

## 🚀 Features

### 🔐 User Authentication
- Secure Login System
- Role Support (Admin / Staff)

### 📦 Inventory / Product Management
- Add, Update, Delete Products
- Maintain Stock Levels
- Auto Reduce Stock After Billing
- Low Stock Alerts

### 👥 Customer & Supplier Management
- Add and Manage Customer Records
- Manage Supplier Data

### 💳 Billing / POS System
- Add items to cart
- Automatic total calculation (Quantity × Price)
- Discount support
- Generates Invoice as **PDF**
- Auto updates stock after bill

### 📊 Reporting / Dashboard
- Summary on Dashboard
- Sales Report Module

---

## 🛠️ Technologies Used

| Component | Technology |
|----------|------------|
| **Language** | Python |
| **GUI Framework** | Tkinter |
| **Database** | MySQL |
| **PDF Generation** | ReportLab |
| **DB Library** | mysql-connector-python |

```
"""
Smart-Inventory-and-Billing-Management-System/
│
├── database/
│ └── db_connection.py # MySQL connection
│
├── modules/
│ ├── login.py # Login Page
│ ├── dashboard.py # Home Dashboard
│ ├── billing_module.py # POS Billing Module
│ ├── product_module.py # Product CRUD
│ ├── customer_module.py # Customer CRUD
│ ├── supplier_module.py # Supplier CRUD
│ ├── sales_report_module.py # Sales Reports
│ ├── NewStaff_module.py # Add New Staff
│ └── Back_module.py # Common Utilities
│
├── assets/ # Icons / Images (if any)
├── invoice_*.pdf # Generated Invoices
├── requirements.txt
└── main.py # Application Entry Point
```

###📦 Installation
##📍 Step 1: Clone the Repository
git clone https://github.com/BhupatiNadar/Smart-Inventory-and-Billing-Management-System.git
cd Smart-Inventory-and-Billing-Management-System

##📍 Step 2: Install Required Libraries
pip install -r requirements.txt

##📍 Step 3: Run the Application
python main.py

###📝 requirements.txt
mysql-connector-python
reportlab

###🤝 Contributing

Feel free to fork this repository and submit pull requests to enhance features or UI.

###📄 License

This project is intended for educational and business use.
You may modify or distribute it with proper credit.

⭐ If you like this project, don't forget to Star ⭐ the repository!

## 📁 Project Structure

