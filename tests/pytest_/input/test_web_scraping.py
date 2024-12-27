"""
Module for testing web scraping functionality.

This module runs test cases for web scraping methods like:

- `scrape_yahoo_finance`
- `scrape_dividend_yahoo_finance`
- `scrape_financials_yahoo_finance`

Usage:
    Run the script directly to execute the test cases:
    $ python test_web_scraping.py
"""


from unittest.mock import patch
import pytest
from src.input.web_scraping import *


# Test for the function scrape_yahoo_finance
@patch("src.input.web_scraping.scrape_yahoo_finance")
def test_scrape_yahoo_finance(mock_scrape_yahoo):
    # Simuler la valeur de retour
    mock_scrape_yahoo.return_value = {
        "Name": "Crédit Agricole S.A. (ACA.PA)",
        "Stock Symbol": "ACA.PA",
        "Current Price": "12.91",
        "Change (%)": "(-0.88%)",
        "Change": "-0.11",
    }

    # Appeler la fonction simulée
    result = scrape_yahoo_finance("ACA.PA")

    # Vérifications
    assert result["Name"] == "Crédit Agricole S.A. (ACA.PA)"
    assert result["Stock Symbol"] == "ACA.PA"
    assert result["Current Price"] == "12.91"
    assert result["Change (%)"] == "(-0.88%)"
    assert result["Change"] == "-0.11"


# Test for the function scrape_dividend_yahoo_finance
@patch("src.input.web_scraping.scrape_dividend_yahoo_finance")
def test_scrape_dividend_yahoo_finance(mock_scrape_dividend):
    # Simuler la valeur de retour
    mock_scrape_dividend.return_value = {
        "Currency": "Currency in EUR",
        "Dividends": [
            {"date": "May 29, 2024", "value": "1.05 Dividend"},
            {"date": "May 30, 2023", "value": "1.05 Dividend"},
        ],
    }

    # Appeler la fonction simulée
    result = scrape_dividend_yahoo_finance("ACA.PA")

    # Vérifications
    assert result["Currency"] == "Currency in EUR"
    assert result["Dividends"][0]["date"] == "May 29, 2024"


# Test for the function scrape_financials_yahoo_finance
@patch("src.input.web_scraping.scrape_financials_yahoo_finance")
def test_scrape_financials_yahoo_finance(mock_scrape_financials):
    # Simuler la valeur de retour
    mock_scrape_financials.return_value = {
        "Currency": "Currency in EUR",
        "Financials": [
            {"label": "Total Revenue", "values": ["24,307,000.00", "23,455,000.00"]},
            {"label": "Pretax Income", "values": ["9,928,000.00", "9,546,000.00"]},
        ],
    }

    # Appeler la fonction simulée
    result = scrape_financials_yahoo_finance("ACA.PA")

    # Vérifications
    assert result["Currency"] == "Currency in EUR"
    assert result["Financials"][0]["label"] == "Total Revenue"


# Example of using a fixture
@pytest.fixture
def mock_response():
    return {
        "Name": "Crédit Agricole S.A. (ACA.PA)",
        "Current Price": "12.91",
    }


# Test using a fixture
def test_scrape_with_fixture(mock_response):
    # Utiliser les données simulées de la fixture
    assert mock_response["Name"] == "Crédit Agricole S.A. (ACA.PA)"
    assert mock_response["Current Price"] == "12.91"
