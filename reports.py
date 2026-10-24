import numpy as np
import pandas as pd


def generate_tabular_report(expenses):
    if not expenses:
        print("No expense data available to generate report.")
        return None

    df = pd.DataFrame(expenses)
    
    amounts = np.array([item["amount"] for item in expenses])
    mean_val = round(float(np.mean(amounts)), 2)
    median_val = round(float(np.median(amounts)), 2)
    std_val = round(float(np.std(amounts)), 2)
    
    print("\n" + "=" * 50)
    print("           EXPENSE SUMMARY REPORT")
    print("=" * 50)
    print(f"Total Transactions : {len(expenses)}")
    print(f"Total Spent        : ${amounts.sum():.2f}")
    print(f"Average Expense    : ${mean_val:.2f}")
    print(f"Median Expense     : ${median_val:.2f}")
    print(f"Standard Deviation : ${std_val:.2f}")
    print("-" * 50)
    
    cat_summary = df.groupby("category")["amount"].agg(["count", "sum"]).reset_index()
    cat_summary.columns = ["Category", "Count", "Total ($)"]
    cat_summary["Total ($)"] = cat_summary["Total ($)"].round(2)
    cat_summary = cat_summary.sort_values(by="Total ($)", ascending=False)
    
    print("\n--- Spending by Category ---")
    print(cat_summary.to_string(index=False))
    
    df["Month"] = df["date"].str.slice(0, 7)
    month_summary = df.groupby("Month")["amount"].agg(["count", "sum"]).reset_index()
    month_summary.columns = ["Month", "Count", "Total ($)"]
    month_summary["Total ($)"] = month_summary["Total ($)"].round(2)
    
    print("\n--- Spending by Month ---")
    print(month_summary.to_string(index=False))
    print("=" * 50)
    
    return {
        "mean": mean_val,
        "median": median_val,
        "std": std_val,
        "by_category": cat_summary,
        "by_month": month_summary
    }


def export_report_to_file(expenses, export_filename="spending_report.txt"):
    if not expenses:
        return False

    df = pd.DataFrame(expenses)
    amounts = np.array([item["amount"] for item in expenses])
    
    with open(export_filename, "w", encoding="utf-8") as f:
        f.write("PERSONAL EXPENSE ANALYZER - SUMMARY REPORT\n")
        f.write("=" * 45 + "\n\n")
        f.write(f"Total Transactions : {len(expenses)}\n")
        f.write(f"Total Spent        : ${amounts.sum():.2f}\n")
        f.write(f"Average Expense    : ${np.mean(amounts):.2f}\n")
        f.write(f"Median Expense     : ${np.median(amounts):.2f}\n\n")
        
        f.write("SPENDING BY CATEGORY:\n")
        cat_df = df.groupby("category")["amount"].sum().round(2).reset_index()
        f.write(cat_df.to_string(index=False))
        f.write("\n\n")
        
        f.write("SPENDING BY MONTH:\n")
        df["Month"] = df["date"].str.slice(0, 7)
        month_df = df.groupby("Month")["amount"].sum().round(2).reset_index()
        f.write(month_df.to_string(index=False))
        f.write("\n")
        
    return True
