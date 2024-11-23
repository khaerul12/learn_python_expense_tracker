import json
from datetime import datetime
from collections import defaultdict

class ExpenseTracker:
    def __init__(self):
        self.expenses = []
        self.budget = defaultdict(float)

    def add_expense(self, description, amount, category):
        expense = {
            'description': description,
            'amount': amount,
            'category': category,
            'date': datetime.now().isoformat()
        }
        self.expenses.append(expense)
        print(f"Added expense: {expense}")

    def update_expense(self, index, description=None, amount=None, category=None):
        if 0 <= index < len(self.expenses):
            if description:
                self.expenses[index]['description'] = description
            if amount:
                self.expenses[index]['amount'] = amount
            if category:
                self.expenses[index]['category'] = category
            print(f"Updated expense: {self.expenses[index]}")
        else:
            print("Expense not found.")

    def delete_expense(self, index):
        if 0 <= index < len(self.expenses):
            removed = self.expenses.pop(index)
            print(f"Deleted expense: {removed}")
        else:
            print("Expense not found.")

    def view_all_expenses(self):
        for i, expense in enumerate(self.expenses):
            print(f"{i}: {expense}")

    def view_summary(self):
        total = sum(expense['amount'] for expense in self.expenses)
        print(f"Total expenses: {total}")

    def view_monthly_summary(self, month):
        total = sum(expense['amount'] for expense in self.expenses if datetime.fromisoformat(expense['date']).month == month)
        print(f"Total expenses for month {month}: {total}")

    def set_budget(self, month, amount):
        self.budget[month] = amount
        print(f"Budget set for month {month}: {amount}")

    def check_budget(self, month):
        total = sum(expense['amount'] for expense in self.expenses if datetime.fromisoformat(expense['date']).month == month)
        if month in self.budget and total > self.budget[month]:
            print(f"Warning: You have exceeded your budget for month {month} by {total - self.budget[month]}")
        else:
            print(f"You are within your budget for month {month}.")

    def export_to_csv(self, filename):
        import csv
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Description", "Amount", "Category", "Date"])
            for expense in self.expenses:
                writer.writerow([expense['description'], expense['amount'], expense['category'], expense['date']])
        print(f"Expenses exported to {filename}")


def main():
    tracker = ExpenseTracker()
    
    while True:
        command = input("Enter command (add, update, delete, view, summary, monthly, budget, export, exit): ").strip().lower()
        
        if command == "add":
            description = input("Enter description: ")
            amount = float(input("Enter amount: "))
            category = input("Enter category: ")
            tracker.add_expense(description, amount, category)

        elif command == "update":
            index = int(input("Enter expense index to update: "))
            description = input("Enter new description (leave blank to keep current): ") or None
            amount = input("Enter new amount (leave blank to keep current): ")
            amount = float(amount) if amount else None
            category = input("Enter new category (leave blank to keep current): ") or None
            tracker.update_expense(index, description, amount, category)

        elif command == "delete":
            index = int(input("Enter expense index to delete: "))
            tracker.delete_expense(index)

        elif command == "view":
            tracker.view_all_expenses()

        elif command == "summary":
            tracker.view_summary()

        elif command == "monthly":
            month = int(input("Enter month (1-12): "))
            tracker.view_monthly_summary(month)

        elif command == "budget":
            month = int(input("Enter month (1-12): "))
            amount = float(input("Enter budget amount: "))
            tracker.set_budget(month, amount)
            tracker.check_budget(month)

        elif command == "export":
            filename = input("Enter filename to export to (e.g., expenses.csv): ")
            tracker.export_to_csv(filename)

        elif command == "exit":
            break

        else:
            print("Unknown command.")

if __name__ == "__main__":
    main()
