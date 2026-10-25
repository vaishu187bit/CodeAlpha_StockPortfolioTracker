# CodeAlpha_StockPortfolioTracker

A financial console application built in Python that tracks stock investments, computes real-time portfolio valuation, and exports detailed reports to `.txt` and `.csv` files. Developed for the **CodeAlpha Python Programming Internship**.

---

## 📌 Project Overview
- **Student Name:** Akshita singh
- **Student ID:** CA/DF1/316239
- **Domain:** Python Programming
- **Batch:** 10th October 2026 to 10th November 2026
- **Task 2:** Stock Portfolio Tracker

---

## 🎯 Goal & Specifications
The goal is to build a stock tracker that calculates total investment based on predefined stock prices with user inputs.

### Simplified Scope:
- **Interactive Stock Input:** Users enter stock ticker symbols and quantities.
- **Predefined Price Dictionary:** Uses hardcoded stock prices for industry leaders (e.g. `AAPL`: \$180, `TSLA`: \$250, `MSFT`: \$420, `GOOGL`: \$140, `AMZN`: \$185, `NVDA`: \$130, `META`: \$500).
- **Valuation & Allocation:** Computes total portfolio investment value, position values, and percentage weight of each asset.
- **File Handling:** Supports saving formatted reports to plain text (`.txt`) and tabular spreadsheets (`.csv`).

---

## 🧠 Key Concepts Used
- **Dictionaries:** Maps tickers to prices, manages current holdings, and tracks aggregated share counts.
- **Input / Output:** Provides a menu-driven CLI interface with input sanitization and formatted tables.
- **Basic Arithmetic:** Calculates position values (`quantity * price`), total investment sums, and percentage weights.
- **File Handling:** Uses Python's native `open()` and `csv` library for report generation and data export.

---

## 🚀 How to Run

### Prerequisites
- Python 3.8 or higher installed on your system.

### Running the Application
Open your terminal or command prompt, navigate to this project directory, and run:

```bash
python stock_tracker.py
```

### Running Unit Tests
To verify test coverage and calculation logic:

```bash
python -m unittest test_stock_tracker.py
```

---

## 📊 Sample Output
```text
======================================================================
                  PORTFOLIO INVESTMENT SUMMARY
======================================================================
Stock    |   Quantity |    Price ($) |        Value ($) |     Weight
----------------------------------------------------------------------
AAPL     |         10 | $     180.00 | $        1800.00 |     59.02%
TSLA     |          5 | $     250.00 | $        1250.00 |     40.98%
======================================================================
TOTAL INVESTMENT VALUE:             $                       3050.00
======================================================================
```

---

## 📄 License
This project is licensed under the MIT License.
