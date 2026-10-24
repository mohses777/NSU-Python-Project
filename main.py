import sys
import storage
import analyzer
import validator
import reports


def display_transactions(expenses):
    if not expenses:
        print("\nNo expenses found.")
        return

    print("\n" + "-" * 75)
    print(f"{'#':<4} {'Date':<12} {'Category':<15} {'Amount ($)':<12} {'Description'}")
    print("-" * 75)
    for idx, item in enumerate(expenses, start=1):
        print(f"{idx:<4} {item['date']:<12} {item['category']:<15} {item['amount']:<12.2f} {item['description']}")
    print("-" * 75)
    print(f"Total: {len(expenses)} items | Overall Sum: ${analyzer.get_total_spending(expenses):.2f}\n")


def add_transaction_flow(expenses):
    print("\n--- Add New Transaction ---")
    
    while True:
        date_input = input("Enter date (YYYY-MM-DD) or 'c' to cancel: ").strip()
        if date_input.lower() == 'c':
            return
        is_valid, msg = validator.validate_date(date_input)
        if is_valid:
            break
        print(f"Error: {msg}")

    while True:
        category_input = input("Enter category (e.g. Food, Transport, Rent): ").strip()
        is_valid, clean_cat = validator.validate_text(category_input, "Category")
        if is_valid:
            break
        print(f"Error: {clean_cat}")

    while True:
        amount_input = input("Enter amount: ").strip()
        is_valid, result = validator.validate_amount(amount_input)
        if is_valid:
            amount_val = result
            break
        print(f"Error: {result}")

    while True:
        desc_input = input("Enter description: ").strip()
        is_valid, clean_desc = validator.validate_text(desc_input, "Description")
        if is_valid:
            break
        print(f"Error: {clean_desc}")

    new_record = {
        "date": date_input,
        "amount": amount_val,
        "category": clean_cat.capitalize(),
        "description": clean_desc
    }
    expenses.append(new_record)
    print(f"\nTransaction added: {new_record['date']} | {new_record['category']} | ${new_record['amount']:.2f}")


def search_flow(expenses):
    query = input("\nEnter keyword to search in category or description: ").strip()
    if not query:
        print("Search cancelled (empty query).")
        return
    
    matches = analyzer.search_by_keyword(expenses, query)
    print(f"\nFound {len(matches)} match(es) for '{query}':")
    display_transactions(matches)


def filter_flow(expenses):
    cat = input("\nEnter category name to filter by: ").strip()
    matches = analyzer.filter_by_category(expenses, cat)
    print(f"\nFound {len(matches)} transaction(s) in category '{cat}':")
    display_transactions(matches)


def top_expenses_flow(expenses):
    while True:
        limit_str = input("\nHow many top expenses would you like to see? (e.g. 5): ").strip()
        if not limit_str:
            limit = 5
            break
        if limit_str.isdigit() and int(limit_str) > 0:
            limit = int(limit_str)
            break
        print("Please enter a valid positive whole number.")

    top_items = analyzer.get_largest_expenses(expenses, limit)
    print(f"\n--- Top {limit} Largest Expenses ---")
    display_transactions(top_items)


def print_menu():
    print("""
======================================
     PERSONAL EXPENSE ANALYZER
======================================
 1. View all transactions
 2. Add a new transaction
 3. Search transactions by keyword
 4. Filter transactions by category
 5. View largest expenses
 6. Show spending report (Pandas & NumPy)
 7. Export spending report to file
 8. Save changes
 9. Exit
======================================
""")


def main():
    expenses = storage.load_expenses()
    has_unsaved_changes = False

    while True:
        print_menu()
        choice = input("Select an option (1-9): ").strip()

        if choice == "1":
            display_transactions(expenses)

        elif choice == "2":
            initial_count = len(expenses)
            add_transaction_flow(expenses)
            if len(expenses) > initial_count:
                has_unsaved_changes = True

        elif choice == "3":
            search_flow(expenses)

        elif choice == "4":
            filter_flow(expenses)

        elif choice == "5":
            top_expenses_flow(expenses)

        elif choice == "6":
            reports.generate_tabular_report(expenses)

        elif choice == "7":
            export_name = "spending_report.txt"
            success = reports.export_report_to_file(expenses, export_name)
            if success:
                print(f"\nReport successfully exported to '{export_name}'.")

        elif choice == "8":
            if storage.save_expenses(expenses):
                has_unsaved_changes = False

        elif choice == "9":
            if has_unsaved_changes:
                confirm = input("You have unsaved changes. Save before exiting? (y/n): ").strip().lower()
                if confirm == "y":
                    storage.save_expenses(expenses)
            print("Thank you for using Personal Expense Analyzer. Goodbye!")
            sys.exit(0)

        else:
            print("Invalid option. Please enter a number between 1 and 9.")


if __name__ == "__main__":
    main()
