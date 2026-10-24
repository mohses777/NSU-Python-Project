import re


def get_total_spending(expenses):
    return round(sum(item["amount"] for item in expenses), 2)


def get_category_totals(expenses):
    totals = {}
    for item in expenses:
        cat = item["category"]
        totals[cat] = totals.get(cat, 0.0) + item["amount"]
    return {cat: round(amt, 2) for cat, amt in totals.items()}


def get_monthly_totals(expenses):
    totals = {}
    for item in expenses:
        month = item["date"][:7]
        totals[month] = totals.get(month, 0.0) + item["amount"]
    return {month: round(amt, 2) for month, amt in sorted(totals.items())}


def get_largest_expenses(expenses, limit=5):
    return sorted(expenses, key=lambda x: x["amount"], reverse=True)[:limit]


def filter_by_category(expenses, category):
    return list(filter(lambda x: x["category"].lower() == category.lower(), expenses))


def search_by_keyword(expenses, query):
    results = []
    pattern = re.compile(re.escape(query), re.IGNORECASE)
    for item in expenses:
        if pattern.search(item["description"]) or pattern.search(item["category"]):
            results.append(item)
    return results
