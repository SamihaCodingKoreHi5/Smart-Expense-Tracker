import json
from datetime import datetime


class Expense:
    def __init__(self, amount, category, description):
        self.amount = amount
        self.category = category
        self.description = description
        self.date = datetime.now().strftime("%Y-%m-%d")

    def to_dict(self):
        return {
            "amount": self.amount,
            "category": self.category,
            "description": self.description,
            "date": self.date
        }


class ExpenseTracker:
    def __init__(self):
        self.expenses = []
        self.load_expenses()

    def load_expenses(self):
        try:
            with open("expenses.json", "r") as file:
                self.expenses = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.expenses = []

    def save_expenses(self):
        with open("expenses.json", "w") as file:
            json.dump(self.expenses, file, indent=4)

    def add_expense(self):
        try:
            amount = float(input("Enter amount: "))
            category = input("Enter category: ")
            description = input("Enter description: ")

            expense = Expense(amount, category, description)

            self.expenses.append(expense.to_dict())
            self.save_expenses()

            print("Expense added successfully!")

        except ValueError:
            print("Please enter a valid amount.")

    def view_expenses(self):
        if not self.expenses:
            print("No expenses found.")
            return

        print("\n===== ALL EXPENSES =====")

        for expense in self.expenses:
            print(f"""
Date: {expense['date']}
Amount: ৳{expense['amount']}
Category: {expense['category']}
Description: {expense['description']}
----------------------------
""")

    def search_expense(self):
        keyword = input("Enter category to search: ").lower()

        found = False

        for expense in self.expenses:
            if keyword in expense["category"].lower():

                print(f"""
Date: {expense['date']}
Amount: ৳{expense['amount']}
Category: {expense['category']}
Description: {expense['description']}
----------------------------
""")

                found = True

        if not found:
            print("No matching expenses found.")

    def total_expense(self):
        total = sum(expense["amount"] for expense in self.expenses)

        print(f"\nTotal Expense: ৳{total:.2f}")

    def category_summary(self):
        if not self.expenses:
            print("No expenses available.")
            return

        summary = {}

        for expense in self.expenses:
            category = expense["category"]

            if category not in summary:
                summary[category] = 0

            summary[category] += expense["amount"]

        print("\n===== CATEGORY SUMMARY =====")

        for category, total in summary.items():
            print(f"{category}: ৳{total:.2f}")

    def monthly_report(self):
        if not self.expenses:
            print("No expenses available.")
            return

        report = {}

        for expense in self.expenses:
            month = expense["date"][:7]

            if month not in report:
                report[month] = 0

            report[month] += expense["amount"]

        print("\n===== MONTHLY REPORT =====")

        for month, total in report.items():
            print(f"{month}: ৳{total:.2f}")


tracker = ExpenseTracker()

while True:
    print("\n===== SMART EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Search Expense")
    print("4. Total Expense")
    print("5. Category Summary")
    print("6. Monthly Report")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        tracker.add_expense()

    elif choice == "2":
        tracker.view_expenses()

    elif choice == "3":
        tracker.search_expense()

    elif choice == "4":
        tracker.total_expense()

    elif choice == "5":
        tracker.category_summary()

    elif choice == "6":
        tracker.monthly_report()

    elif choice == "7":
        print("Thank you for using Smart Expense Tracker!")
        break

    else:
        print("Invalid choice. Please try again.")
