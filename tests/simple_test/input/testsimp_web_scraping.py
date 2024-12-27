"""
Module for testing web scraping functionality.

This module runs test cases for web scraping methods like:

- `scrape_yahoo_finance`
- `scrape_dividend_yahoo_finance`
- `scrape_financials_yahoo_finance`

Usage:
    Run the script directly to execute the test cases:
    $ python testsimp_web_scraping.py
"""


from src.input.web_scraping import *

if __name__ == "__main__":
    stock_data = scrape_yahoo_finance("ACA.PA")

    if stock_data:
        print("Data :")
        for key, value in stock_data.items():
            print(f"{key}: {value}")
    else:
        print("Failure on scraping.")


    stock_data_dividend = scrape_dividend_yahoo_finance("ACA.PA")

    if stock_data_dividend:
        print("Data dividend :")
        for key, value in stock_data_dividend.items():
            print(f"{key}: {value}")
    else:
        print("Failure on scraping.")

    stock_data_financials = scrape_financials_yahoo_finance("ACA.PA")

    if stock_data_financials:
        print("Data dividend :")
        for key, value in stock_data_financials.items():
            print(f"{key}: {value}")
    else:
        print("Failure on scraping.")

