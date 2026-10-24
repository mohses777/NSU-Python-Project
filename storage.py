import csv
import os

DEFAULT_FILE = "expenses.csv"
FIELDNAMES = ["date", "amount", "category", "description"]


def load_expenses(filename=DEFAULT_FILE):
    expenses = []
    
    if not os.path.exists(filename):
        print(f"File '{filename}' not found. Starting with empty list.")
        return expenses

    try:
        with open(filename, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    amount = float(row["amount"])
                    expenses.append({
                        "date": row["date"].strip(),
                        "amount": round(amount, 2),
                        "category": row["category"].strip(),
                        "description": row["description"].strip()
                    })
                except (ValueError, KeyError):
                    continue
    except PermissionError:
        print(f"Permission denied: unable to open '{filename}'.")
    except Exception as e:
        print(f"Error reading '{filename}': {e}")
    else:
        print(f"Loaded {len(expenses)} transactions from '{filename}'.")
    finally:
        pass

    return expenses


def save_expenses(expenses, filename=DEFAULT_FILE):
    try:
        with open(filename, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
            writer.writeheader()
            for item in expenses:
                writer.writerow(item)
        return True
    except PermissionError:
        print(f"Cannot save: '{filename}' might be open in another program.")
        return False
    except Exception as e:
        print(f"Failed to save to '{filename}': {e}")
        return False
