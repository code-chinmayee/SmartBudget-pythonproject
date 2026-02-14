from models import update_salary, add_expense, get_category_expenses, get_summary

def show_menu():
    print("\n==== Smart Budget & Savings Manager ====")
    print("1. Update Salary")
    print("2. Add Expense")
    print("3. View Category-wise Expenses")
    print("4. View Summary")
    print("5. Exit")

def handle_user_choice():
    while True:
        show_menu()
        choice = input("Enter choice: ")

        if choice == "1":
            salary = float(input("Enter new salary: "))
            success, result = update_salary(salary)
            if success:
                print(f"✅ Savings increased by ₹{result:.2f}")
            else:
                print("❌", result)

        elif choice == "2":
            cat = input("Category: ")
            amt = float(input("Amount: "))
            if add_expense(cat, amt):
                print("✅ Expense added")
            else:
                print("❌ Invalid amount")

        elif choice == "3":
            print("\n📊 Expenses by Category")
            for cat, amt in get_category_expenses():
                print(f"{cat}: ₹{amt:.2f}")

        elif choice == "4":
            salary, savings, expenses = get_summary()
            balance = salary - savings - expenses
            print("\n📈 Financial Summary")
            print(f"Salary   : ₹{salary:.2f}")
            print(f"Savings  : ₹{savings:.2f}")
            print(f"Expenses : ₹{expenses:.2f}")
            print(f"Balance  : ₹{balance:.2f}")

        elif choice == "5":
            print("👋 Thank you!")
            break

        else:
            print("❌ Invalid choice")

