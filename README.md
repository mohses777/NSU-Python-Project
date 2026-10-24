# Personal Expense Analyzer
**Author:** Moses Idiong

A terminal-based personal expense tracking and analysis system written in Python. The application enables users to record, search, validate, and analyze daily expenses with summary statistics and file export capabilities.

---

## Features
- **Transaction Management**: Add, view, and search expenses with date, amount, category, and description.
- **Data Validation**: Validates date formats (`YYYY-MM-DD`) and positive numerical amounts using regular expressions and datetime.
- **Expense Analysis**: Calculates overall totals, category totals, monthly breakdown, and identifies top expenses.
- **Reporting**: Generates tabular summaries and calculates statistical measures (mean, median, standard deviation) using Pandas and NumPy.
- **File Persistence**: Reads and saves transaction data to `expenses.csv` using context managers and error handling.
- **Exporting**: Exports formatted spending reports directly to a text file.

---

## Project Structure
- `main.py` - Interactive terminal menu for the user.
- `storage.py` - Functions for reading and writing data to CSV.
- `analyzer.py` - Filtering, sorting, and core aggregation functions.
- `validator.py` - Input validation for dates, amounts, and text.
- `reports.py` - Tabular report generation using Pandas and NumPy.
- `expenses.csv` - Sample dataset with 32 realistic expense records.

---

## Installation & Setup

1. **Create a virtual environment (`venv`):**
   ```bash
   python -m venv venv
   ```

2. **Activate the virtual environment:**
   - On **Windows** (PowerShell):
     ```bash
     .\venv\Scripts\Activate.ps1
     ```
   - On **Windows** (Command Prompt / CMD):
     ```cmd
     venv\Scripts\activate.bat
     ```
   - On **macOS / Linux**:
     ```bash
     source venv/bin/activate
     ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

---

## Running the Project

```bash
python main.py
```

