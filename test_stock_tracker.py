"""
Unit tests for Task 2: Stock Portfolio Tracker
"""

import os
import unittest
from stock_tracker import (
    STOCK_PRICES,
    calculate_portfolio_value,
    save_to_text,
    save_to_csv
)


class TestStockPortfolioTracker(unittest.TestCase):

    def setUp(self):
        self.mock_prices = {
            "AAPL": 180.0,
            "TSLA": 250.0,
            "MSFT": 400.0
        }
        self.test_portfolio = {
            "AAPL": 10,
            "TSLA": 5
        }
        self.test_txt = "test_portfolio.txt"
        self.test_csv = "test_portfolio.csv"

    def tearDown(self):
        if os.path.exists(self.test_txt):
            os.remove(self.test_txt)
        if os.path.exists(self.test_csv):
            os.remove(self.test_csv)

    def test_predefined_prices_exist(self):
        """Verify hardcoded dictionary includes requested AAPL and TSLA stocks."""
        self.assertIn("AAPL", STOCK_PRICES)
        self.assertIn("TSLA", STOCK_PRICES)
        self.assertEqual(STOCK_PRICES["AAPL"], 180.0)
        self.assertEqual(STOCK_PRICES["TSLA"], 250.0)

    def test_calculate_portfolio_value(self):
        """10 AAPL @ 180 = 1800; 5 TSLA @ 250 = 1250; Total = 3050."""
        total, breakdown = calculate_portfolio_value(self.test_portfolio, self.mock_prices)
        self.assertAlmostEqual(total, 3050.0)
        self.assertEqual(len(breakdown), 2)

        # Check weights sum to 100%
        total_percentage = sum(item["percentage"] for item in breakdown)
        self.assertAlmostEqual(total_percentage, 100.0)

    def test_empty_portfolio(self):
        """Empty portfolio should result in zero value."""
        total, breakdown = calculate_portfolio_value({}, self.mock_prices)
        self.assertEqual(total, 0.0)
        self.assertEqual(len(breakdown), 0)

    def test_save_to_text_file(self):
        """Check saving to text file creates the file and contains expected content."""
        saved_path = save_to_text(self.test_portfolio, self.test_txt, self.mock_prices)
        self.assertTrue(os.path.exists(saved_path))
        with open(saved_path, "r", encoding="utf-8") as f:
            content = f.read()
            self.assertIn("AAPL", content)
            self.assertIn("TSLA", content)
            self.assertIn("3050.00", content)

    def test_save_to_csv_file(self):
        """Check saving to CSV file formats rows and values properly."""
        saved_path = save_to_csv(self.test_portfolio, self.test_csv, self.mock_prices)
        self.assertTrue(os.path.exists(saved_path))
        with open(saved_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
            self.assertGreaterEqual(len(lines), 4)  # header + 2 stocks + total
            self.assertIn("AAPL", lines[1])


if __name__ == "__main__":
    unittest.main()
