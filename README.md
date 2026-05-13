# 🏦 Simple Bank System

<div align="center">

A console-based banking application built with **Python**, designed to simulate core account management features such as authentication, balance tracking, deposits, withdrawals, password updates, interest calculation, and account statements.

<br>

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![CLI](https://img.shields.io/badge/CLI-Console%20Application-4B5563?style=for-the-badge)
![JSON](https://img.shields.io/badge/JSON-Data%20Storage-000000?style=for-the-badge&logo=json&logoColor=white)
![OOP](https://img.shields.io/badge/OOP-Account%20Management-2563EB?style=for-the-badge)

</div>

---

## ✨ Overview

**Simple Bank System** is a Python command-line application that models a basic banking workflow.  
Users can register, log in, manage their balance, change passwords, calculate projected interest, and display a simple account statement.

The project separates the user-facing menu logic from the account management logic, with account data stored in a local `users.json` file. :contentReference[oaicite:0]{index=0}

---

## 🚀 Features

### 🔐 Authentication
- User registration
- User login with first name, last name, and password
- Maximum of 3 login attempts before the program exits
- Newly registered users receive a default password based on their surname and are prompted to change it after logging in. :contentReference[oaicite:1]{index=1}

### 💰 Account Management
- Check current balance
- Lodge funds into the account
- Withdraw funds with insufficient-balance validation
- Balance updates are saved to `users.json`. :contentReference[oaicite:2]{index=2}

### 🔑 Password Management
- Change account password
- Verify the old password before updating
- Confirm new password entry before saving. :contentReference[oaicite:3]{index=3}

### 📈 Interest Calculation
- Calculates projected monthly interest over 12 months
- Uses:
  - **2% annual interest** for balances below €5,000
  - **4% annual interest** for balances of €5,000 or more
- Displays a month-by-month interest breakdown. :contentReference[oaicite:4]{index=4}

### 📄 Account Statement
- Shows:
  - Account ID
  - Account holder name
  - Current balance
  - Current applicable interest rate. :contentReference[oaicite:5]{index=5}

---

## 🧭 Application Menu

After login, the user can choose from:

```text
1. Check balance
2. Lodge funds
3. Withdraw
4. Change password
5. Calculate interest
6. Statement
7. Quit

These options are handled in the main application loop in main.py.

🏗 Project Structure
simple-bank-system/
│
├── main.py               # CLI interface and application flow
├── AccountManager.py     # User data operations and banking logic
├── users.json            # Local JSON data storage for users
├── requirements.txt      # Project dependencies
└── README.md
🔍 File Breakdown
main.py

Controls the overall user experience:

application startup;
login and registration menu;
banking options menu;
formatted success and error messages;
terminal clearing;
exit flow.
AccountManager.py

Handles the underlying account operations:

loading users from JSON;
user registration;
authentication;
deposits;
withdrawals;
password changes;
interest calculations.
users.json

Stores account records locally in JSON format.
The application reads and writes user data from this file whenever account details are created or updated.

⚙️ Setup
1. Clone the repository
git clone https://github.com/bohdankukuruza/simple-bank-system.git
cd simple-bank-system
2. Create a virtual environment
python -m venv venv
Windows
venv\Scripts\activate
macOS / Linux
source venv/bin/activate
3. Install dependencies
pip install -r requirements.txt
4. Run the application
python main.py
🧪 Example Workflow
1. Register a new user
2. Log in with the generated default password
3. Change the password
4. Lodge funds into the account
5. Withdraw part of the balance
6. Calculate projected monthly interest
7. View the final account statement
💾 Data Storage

The project uses a local JSON file instead of a database.

This makes the project lightweight and easy to run, while still demonstrating:

file handling;
persistent data updates;
structured user records;
simple account state management.
🧰 Tech Stack
Area	Technology
Language	Python
Interface	Command Line
Data Storage	JSON
Programming Style	Object-Oriented Programming
Terminal Styling	Colorama

The application uses colorama for colored terminal output.

🧭 Possible Improvements
Replace JSON storage with SQLite or PostgreSQL
Hash user passwords instead of storing them as plain text
Add transaction history
Add account transfer functionality
Add unit tests
Improve input validation
Build a graphical or web-based interface
👨‍💻 Author

Bohdan Kukuruza

<div align="center">

⭐ If you found this project useful, feel free to star the repository.

</div> ```
