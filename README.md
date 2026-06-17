# 💰 Smart Expense Tracker

A Python-based personal finance management application that helps users track, organize, and analyze their daily expenses.

Smart Expense Tracker allows users to record expenses, categorize spending, calculate total expenses, generate category-wise summaries, and view monthly spending reports. All data is stored locally using JSON files, ensuring that expense records remain available even after the program is closed.

---

## 🚀 Features

- Add New Expenses
- View All Expenses
- Search Expenses by Category
- Calculate Total Expenses
- Category-Wise Expense Summary
- Monthly Expense Reports
- Persistent JSON Data Storage
- Object-Oriented Programming (OOP)

---

## 🎯 Why This Project?

Managing personal expenses manually can be difficult and time-consuming.

This project helps users:

- Keep track of daily spending
- Understand where money is being spent
- Analyze spending habits
- Generate quick financial summaries
- Store expense records safely

Whether you're a student, freelancer, or professional, this tool can help organize personal finances more effectively.

---

## 🛠️ Technologies Used

- Python
- JSON
- Datetime Module
- File Handling
- Object-Oriented Programming (OOP)

---

## 📂 Project Structure

```text
Smart-Expense-Tracker/
│
├── app.py
├── expenses.json
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/Smart-Expense-Tracker.git
```

### 2. Navigate to the Project Folder

```bash
cd Smart-Expense-Tracker
```

### 3. Run the Application

```bash
python app.py
```

---

## 📖 How to Use

After running the application, the following menu will appear:

```text
===== SMART EXPENSE TRACKER =====

1. Add Expense
2. View Expenses
3. Search Expense
4. Total Expense
5. Category Summary
6. Monthly Report
7. Exit
```

---

### 1️⃣ Add an Expense

Select:

```text
1
```

Example:

```text
Enter amount: 500
Enter category: Food
Enter description: Burger
```

Output:

```text
Expense added successfully!
```

The expense will automatically be saved to `expenses.json`.

---

### 2️⃣ View All Expenses

Select:

```text
2
```

Example Output:

```text
Date: 2026-06-17
Amount: ৳500
Category: Food
Description: Burger
```

Displays all recorded expenses.

---

### 3️⃣ Search Expenses

Select:

```text
3
```

Example:

```text
Enter category to search: Food
```

The application will display all expenses related to the selected category.

---

### 4️⃣ Calculate Total Expenses

Select:

```text
4
```

Example Output:

```text
Total Expense: ৳1800.00
```

Calculates the total amount spent across all recorded expenses.

---

### 5️⃣ View Category Summary

Select:

```text
5
```

Example Output:

```text
Food: ৳500.00
Transport: ৳300.00
Shopping: ৳1000.00
```

Displays spending totals grouped by category.

---

### 6️⃣ Generate Monthly Report

Select:

```text
6
```

Example Output:

```text
2026-06: ৳1800.00
```

Shows the total expenses for each month.

---

### 7️⃣ Exit the Application

Select:

```text
7
```

Output:

```text
Thank you for using Smart Expense Tracker!
```

Closes the application safely.

---

## 📊 Example Use Cases

### Student Expense Tracking

```text
Food: ৳2500
Transport: ৳1200
Books: ৳1800
```

### Monthly Spending Analysis

```text
June 2026: ৳5500
July 2026: ৳7200
```

### Budget Monitoring

Track spending habits and identify categories where expenses are highest.

---

## 🎓 Learning Outcomes

This project demonstrates:

- Python Programming
- Object-Oriented Programming (OOP)
- JSON Data Handling
- File Handling
- CRUD Operations
- Data Persistence
- Financial Data Management

---

## 🔮 Future Improvements

- Expense Deletion Feature
- Expense Editing Feature
- Budget Limits & Alerts
- Expense Visualization Charts
- CSV Export
- SQLite Database Integration
- GUI Version with Tkinter
- Web Version with Flask

---

## 👩‍💻 Author

Developed by Samiha Fatima

If you found this project useful, consider giving it a ⭐ on GitHub.
