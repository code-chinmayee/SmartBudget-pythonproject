💰 Smart Budget & Savings Manager# 💰 Smart Budget & Savings Manager

A console-based Python application to manage salary, categorized expenses, and savings using SQLite.  
The project follows a modular architecture with separate database, business logic, and frontend layers.

---

## 🚀 Features

- Salary management
- Automatic savings allocation (15% of salary increment)
- Category-wise expense tracking
- Financial summary (salary, expenses, savings, balance)
- SQLite database integration
- CRUD operations
- Input validation
- Modular project structure

---

## 🧠 Savings Logic



A console-based Python application to manage salary, categorized expenses, and savings using SQLite.
The project follows a modular architecture, separating database, business logic, and frontend layers for better maintainability.

🚀 Features

📌 Salary management with update option

💰 Automatic savings allocation (15% of salary increment)

📊 Category-wise expense tracking

📈 Financial summary (salary, expenses, savings, balance)

🗄️ SQLite database for persistent storage

🔁 Full CRUD operations

✅ Input validation

🧱 Modular project structure

🧠 Savings Logic

When salary is updated:

Savings += 15% of (New Salary − Old Salary)

📁 Project Structure
SmartBudgetManager/
│
├── database.py        # Database connection & table creation
├── models.py          # Business logic and CRUD operations
├── frontend.py        # Console-based user interface
├── main.py            # Application entry point
├── budget.db          # SQLite database (auto-generated)
└── README.md          # Project documentation

🛠️ Technologies Used

Python 3

SQLite (sqlite3 module)

Console-based UI

▶️ How to Run the Project
1️⃣ Clone the Repository
git clone https://github.com/your-username/SmartBudgetManager.git

2️⃣ Navigate to Project Folder
cd SmartBudgetManager

3️⃣ Run the Application
python main.py


💡 Make sure Python 3 is installed on your system.

📌 Application Menu
1. Update Salary
2. Add Expense
3. View Category-wise Expenses
4. View Financial Summary
5. Exit

📊 Sample Output
Salary   : ₹50000.00
Savings  : ₹7500.00
Expenses : ₹12000.00
Balance  : ₹30500.00

🎯 Learning Outcomes

Python modular programming

SQLite database integration

CRUD operations

Data validation

Separation of concerns (Database / Logic / UI)

Real-world financial logic implementation.
