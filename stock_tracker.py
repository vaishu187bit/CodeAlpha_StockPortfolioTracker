"""
CodeAlpha Internship - Task 2: Stock Portfolio Tracker
Student Name: Akshita singh
Student ID: CA/DF1/316239
Domain: Python Programming

Key Concepts Used:
- dictionary: for mapping stock symbols to current prices and tracking portfolio holdings
- input/output: for user interaction via interactive CLI menu
- basic arithmetic: for calculating position values, total portfolio worth, and percentage weights
- file handling: for exporting portfolio reports into .txt and .csv formats
"""

import os
import csv
from datetime import datetime

# Hardcoded dictionary of stock symbols and prices (in USD) as per project requirements
STOCK_PRICES = {
    "AAPL": 180.00,
    "TSLA": 250.00,
    "GOOGL": 140.00,
    "MSFT": 420.00,
    "AMZN": 185.00,
    "NVDA": 130.00,
    "META": 500.00
}


def display_market_prices(prices=STOCK_PRICES):
    """Display all available stock symbols and their predefined market prices."""
    print("\n" + "=" * 45)
    print("        AVAILABLE STOCKS & MARKET PRICES")
    print("=" * 45)
    print(f"{'Ticker Symbol':<18} | {'Price per Share (USD)':>22}")
    print("-" * 45)
    for ticker, price in sorted(prices.items()):
        print(f"{ticker:<18} | ${price:>21.2f}")
    print("=" * 45)


def calculate_portfolio_value(portfolio, prices=STOCK_PRICES):
    """
    Calculate the individual holding values and total investment value.
    Returns:
        total_value (float): sum of all positions
        breakdown (list of dict): details for each stock
    """
    breakdown = []
    total_value = 0.0

    for ticker, quantity in portfolio.items():
        price = prices.get(ticker, 0.0)
        position_value = quantity * price
        total_value += position_value
        breakdown.append({
            "ticker": ticker,
            "quantity": quantity,
            "price": price,
            "value": position_value
        })

    # Add percentage allocation for each stock
    for item in breakdown:
        if total_value > 0:
            item["percentage"] = (item["value"] / total_value) * 100.0
        else:
            item["percentage"] = 0.0

    return total_value, breakdown


def display_portfolio_summary(portfolio, prices=STOCK_PRICES):
    """Print a neatly formatted portfolio summary table to the console."""
    if not portfolio:
        print("\n>> Your portfolio is currently empty. Add stocks to get started!")
        return 0.0, []

    total_value, breakdown = calculate_portfolio_value(portfolio, prices)

    print("\n" + "=" * 70)
    print("                  PORTFOLIO INVESTMENT SUMMARY")
    print("=" * 70)
    print(f"{'Stock':<8} | {'Quantity':>10} | {'Price ($)':>12} | {'Value ($)':>15} | {'Weight':>10}")
    print("-" * 70)

    for item in breakdown:
        print(
            f"{item['ticker']:<8} | "
            f"{item['quantity']:>10} | "
            f"${item['price']:>11.2f} | "
            f"${item['value']:>14.2f} | "
            f"{item['percentage']:>9.2f}%"
        )
    print("=" * 70)
    print(f"{'TOTAL INVESTMENT VALUE:':<35} ${total_value:>30.2f}")
    print("=" * 70)

    return total_value, breakdown


def save_to_text(portfolio, filepath="portfolio_summary.txt", prices=STOCK_PRICES):
    """Export the portfolio report to a readable plain text file."""
    total_value, breakdown = calculate_portfolio_value(portfolio, prices)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(filepath, "w", encoding="utf-8") as f:
        f.write("=" * 70 + "\n")
        f.write("         CODEALPHA - STOCK PORTFOLIO REPORT\n")
        f.write(f"         Generated on: {timestamp}\n")
        f.write("=" * 70 + "\n")
        f.write(f"{'Stock':<8} | {'Quantity':>10} | {'Price ($)':>12} | {'Value ($)':>15} | {'Weight':>10}\n")
        f.write("-" * 70 + "\n")
        for item in breakdown:
            f.write(
                f"{item['ticker']:<8} | "
                f"{item['quantity']:>10} | "
                f"${item['price']:>11.2f} | "
                f"${item['value']:>14.2f} | "
                f"{item['percentage']:>9.2f}%\n"
            )
        f.write("=" * 70 + "\n")
        f.write(f"{'TOTAL INVESTMENT VALUE:':<35} ${total_value:>30.2f}\n")
        f.write("=" * 70 + "\n")

    return filepath


def save_to_csv(portfolio, filepath="portfolio_summary.csv", prices=STOCK_PRICES):
    """Export the portfolio holdings and calculation to a CSV spreadsheet."""
    total_value, breakdown = calculate_portfolio_value(portfolio, prices)

    with open(filepath, "w", newline="", encoding="utf-8") as csvfile:
        fieldnames = ["Ticker", "Quantity", "PricePerShare_USD", "PositionValue_USD", "WeightPercentage"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for item in breakdown:
            writer.writerow({
                "Ticker": item["ticker"],
                "Quantity": item["quantity"],
                "PricePerShare_USD": f"{item['price']:.2f}",
                "PositionValue_USD": f"{item['value']:.2f}",
                "WeightPercentage": f"{item['percentage']:.2f}%"
            })

        # Append Total row
        writer.writerow({
            "Ticker": "TOTAL",
            "Quantity": sum(item["quantity"] for item in breakdown),
            "PricePerShare_USD": "-",
            "PositionValue_USD": f"{total_value:.2f}",
            "WeightPercentage": "100.00%"
        })

    return filepath


def main():
    """Interactive Command Line Interface for Stock Portfolio Tracker."""
    portfolio = {}

    while True:
        print("\n" + "=" * 45)
        print("     CODEALPHA STOCK PORTFOLIO TRACKER")
        print("=" * 45)
        print("1. View Available Stocks & Prices")
        print("2. Add / Update Stock in Portfolio")
        print("3. View Current Portfolio & Total Investment")
        print("4. Save Portfolio to Text File (.txt)")
        print("5. Save Portfolio to CSV File (.csv)")
        print("6. Reset Portfolio")
        print("7. Exit")
        print("=" * 45)

        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            display_market_prices(STOCK_PRICES)

        elif choice == "2":
            ticker = input("\nEnter Stock Ticker (e.g. AAPL, TSLA, MSFT): ").strip().upper()
            if ticker not in STOCK_PRICES:
                print(f">> Unknown ticker symbol '{ticker}'.")
                print(f"Supported tickers are: {', '.join(sorted(STOCK_PRICES.keys()))}")
                continue

            qty_input = input(f"Enter quantity of shares for {ticker}: ").strip()
            try:
                quantity = int(qty_input)
                if quantity <= 0:
                    print(">> Quantity must be a positive integer greater than 0.")
                    continue
            except ValueError:
                print(">> Invalid quantity! Please enter an integer number.")
                continue

            portfolio[ticker] = portfolio.get(ticker, 0) + quantity
            print(f">> Successfully added {quantity} share(s) of {ticker}. Total {ticker}: {portfolio[ticker]}")

        elif choice == "3":
            display_portfolio_summary(portfolio, STOCK_PRICES)

        elif choice == "4":
            if not portfolio:
                print(">> Portfolio is empty! Nothing to save.")
                continue
            fname = save_to_text(portfolio)
            print(f">> Portfolio successfully saved to '{os.path.abspath(fname)}'")

        elif choice == "5":
            if not portfolio:
                print(">> Portfolio is empty! Nothing to save.")
                continue
            fname = save_to_csv(portfolio)
            print(f">> Portfolio successfully saved to '{os.path.abspath(fname)}'")

        elif choice == "6":
            confirm = input("Are you sure you want to clear your portfolio? (y/n): ").strip().lower()
            if confirm in ('y', 'yes'):
                portfolio.clear()
                print(">> Portfolio has been reset.")

        elif choice == "7":
            print("\nThank you for using CodeAlpha Stock Portfolio Tracker. Goodbye!")
            break

        else:
            print(">> Invalid option selected. Please choose between 1 and 7.")


if __name__ == "__main__":
    main()
