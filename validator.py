from datetime import datetime
import re


def validate_date(date_str):
    date_str = date_str.strip()
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", date_str):
        return False, "Date must follow YYYY-MM-DD format (e.g. 2026-10-24)."
    
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True, ""
    except ValueError:
        return False, "Invalid calendar date (check month or day)."


def validate_amount(amount_str):
    amount_str = str(amount_str).strip()
    if not re.fullmatch(r"\d+(\.\d{1,2})?", amount_str):
        return False, "Amount must be a positive number with up to 2 decimal places."
    
    val = float(amount_str)
    if val <= 0:
        return False, "Amount must be greater than zero."
    
    return True, round(val, 2)


def validate_text(text, field_name="Field"):
    text = text.strip()
    if not text:
        return False, f"{field_name} cannot be empty."
    return True, text
