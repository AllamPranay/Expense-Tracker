import csv
import os
from datetime import datetime
from prettytable import PrettyTable

EXPENSES_FILE = 'expenses.csv'

# Initialize CSV if not exists
if not os.path.exists(EXPENSES_FILE):
    with open(EXPENSES_FILE, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Date', 'Category', 'Description', 'Amount'])


def add_expense():
    while True:
        try:
            date_input = input("Enter the date (YYYY-MM-DD): ")
            datetime.strptime(date_input, "%Y-%m-%d")  # Validate date
            break
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")

    category = input("Enter the category (Food, Transport, Entertainment, etc.): ")
    description = input("Enter description: ")

    while True:
        try:
            amount = float(input("Enter the amount: "))
            break
        except ValueError:
            print("Invalid amount. Please enter a number.")

    with open(EXPENSES_FILE, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date_input, category, description, amount])

    print("Expense added successfully!\n")


def view_expenses():
    table = PrettyTable(["Date", "Category", "Description", "Amount"])
    try:
        with open(EXPENSES_FILE, 'r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                if len(row) == 4:
                    table.add_row(row)
        print(table)
    except Exception as e:
        print(f"Error reading expenses: {e}")


def category_summary():
    category_totals = {}
    try:
        with open(EXPENSES_FILE, 'r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                if len(row) != 4:
                    continue  # Skip corrupted rows
                category = row[1]
                try:
                    amount = float(row[3])
                except ValueError:
                    continue  # Skip rows with invalid amounts
                category_totals[category] = category_totals.get(category, 0) + amount

        print("\nCategory-wise Summary:")
        for category, total in category_totals.items():
            print(f"{category}: Rs.{total}")

    except Exception as e:
        print(f"Error in summary: {e}")


def monthly_summary():
    month_totals = {}
    try:
        with open(EXPENSES_FILE, 'r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                if len(row) != 4:
                    continue  # Skip corrupted rows
                try:
                    date = datetime.strptime(row[0], "%Y-%m-%d")
                    amount = float(row[3])
                except ValueError:
                    continue  # Skip invalid rows
                month = date.strftime("%Y-%m")
                month_totals[month] = month_totals.get(month, 0) + amount

        print("\nMonthly Summary:")
        for month, total in month_totals.items():
            print(f"{month}: Rs.{total}")

    except Exception as e:
        print(f"Error in monthly summary: {e}")


def main():
    while True:
        print("\n===== Personal Expense Tracker =====")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Category Summary")
        print("4. View Monthly Summary")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            category_summary()
        elif choice == '4':
            monthly_summary()
        elif choice == '5':
            print("Thank you for using the Expense Tracker!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

