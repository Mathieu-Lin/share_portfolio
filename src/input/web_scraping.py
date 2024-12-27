import requests
from bs4 import BeautifulSoup
import re

def scrape_yahoo_finance(stock_symbol):
    """
    Scrape Yahoo Finance for a specific stock symbol.
    Args:
        stock_symbol (str): The stock symbol (e.g., "AMZN" for Amazon).
    Returns:
        dict: Scraped data including current price, change, and more.
    """
    try:
        # URL chosen for one share.
        url = f"https://finance.yahoo.com/quote/{stock_symbol}/"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        # Analysis a page with BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract the name of a share
        name_tag = soup.find('h1', {'class': 'yf-xxbei9'})
        name = name_tag.text if name_tag else "N/A"

        # Extract the actual price
        price_tag = soup.find('fin-streamer', {'data-field': 'regularMarketPrice'})
        price = price_tag.text if price_tag else "N/A"

        # Extract the variation by percentage
        change_tag = soup.find('fin-streamer', {'data-field': 'regularMarketChangePercent'})
        change = change_tag.text if change_tag else "N/A"

        # Extract the variation by number
        change_nb_tag = soup.find('fin-streamer', {'data-field': 'regularMarketChange'})
        change_nb = change_nb_tag.text if change_nb_tag else "N/A"

        # Extract the list of vars
        li_elements = soup.find_all('li', class_='yf-dudngy')
        pack_var = {}
        # Extract values and labels per li
        for li in li_elements:
            label = li.find('span', class_='label')
            value = li.find('span', class_='value')
            # Add these vars to pack_var
            if label and value:
                pack_var[label.get('title')] = value.get_text(strip=True)

        # Return the data in dictionary type
        return {
            'Name' : name,
            'Stock Symbol': stock_symbol,
            'Current Price': price,
            'Change (%)': change,
            'Change' : change_nb,
            'List' : pack_var
        }
    except Exception as e:
        print(f"Error from scrape_yahoo_finance : {e}")
        return None


def scrape_dividend_yahoo_finance(stock_symbol):
    """
    Scrape Dividend in Yahoo Finance for a specific stock symbol.
    Args:
        stock_symbol (str): The stock symbol (e.g., "AMZN" for Amazon).
    Returns:
        dict: Scraped data including dividend and more.
    """
    try:
        # URL chosen for one share.
        url = f"https://finance.yahoo.com/quote/{stock_symbol}/history/?filter=div&period1=1293235200&period2=1735165961"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        # Analysis a page with BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract the currency of a share
        currency_tag = soup.find('div', {'class': 'currency yf-j5d1ld'})
        currency = currency_tag.get_text(strip=True) if currency_tag else "N/A"

        # Extract the list of vars
        tr_elements = soup.find_all('tr', class_='yf-j5d1ld')
        pack = []
        # Extract values and labels per li
        for tr in tr_elements:
            pack_var = {}
            date = tr.find('td', class_='yf-j5d1ld')
            value = tr.find('td', class_='event yf-j5d1ld')
            # Add these vars to pack_var
            if date and value:
                pack_var["date"] = date.get_text()
                pack_var["value"] = value.get_text()
                pack.append(pack_var)
        # Return the data in dictionary type
        return {
            'Currency' : currency,
            'Dividends': pack
        }
    except Exception as e:
        print(f"Error from scraping : {e}")
        return None

def scrape_financials_yahoo_finance(stock_symbol):
    """
    Scrape financials in Yahoo Finance for a specific stock symbol.
    Args:
        stock_symbol (str): The stock symbol (e.g., "AMZN" for Amazon).
    Returns:
        dict: Scraped data including dividend and more.
    """
    try:
        # URL chosen for one share.
        url = f"https://finance.yahoo.com/quote/{stock_symbol}/financials/"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        # Analysis a page with BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract the currency of a share
        currency_tag = soup.find('span', {'class': 'currency yf-m6gtul'})
        currency = currency_tag.get_text(strip=True) if currency_tag else "N/A"

        # Extract the list of vars
        div_elements = soup.find_all('div', class_='row lv-0 yf-t22klz')
        pack = []
        # Extract values and labels per li
        for div in div_elements:
            pack_var = {}
            # Find all <div> tags
            div2_label = div.find('div', class_="column sticky yf-t22klz")
            div2_elements = div.find_all('div', class_="column yf-t22klz alt")
            div2_elements2 = div.find_all('div', class_="column yf-t22klz")

            div2_contents = []
            # Extract the text content from each <div>
            for i in range (len(div2_elements)) :
                for k in range (len(div2_elements2)):
                    if i == k:
                        cleaned_data = re.sub(r'\u202f', '', div2_elements[i].get_text())
                        div2_contents.append(cleaned_data)
                        cleaned_data2 = re.sub(r'\u202f', '', div2_elements2[k].get_text())
                        div2_contents.append(cleaned_data2)

            # Add these vars to pack_var
            if len(div2_contents) > 1:
                pack_var['label'] = div2_label.get_text().strip()
                pack_var['values'] = div2_contents
                pack.append(pack_var)

        # Return the data in dictionary type
        return {
            'Currency' : currency,
            'Financials': pack
        }
    except Exception as e:
        print(f"Error from scraping : {e}")
        return None

def scrape_all_yahoo(stock_symbol):
    """
    Scrape almost all in Yahoo Finance for a specific stock symbol.
    Args:
        stock_symbol (str): The stock symbol (e.g., "AMZN" for Amazon).
    Returns:
        dict: Scraped data including all and more.
    """
    temp = {"main": scrape_yahoo_finance(stock_symbol),
            "dividend": scrape_dividend_yahoo_finance(stock_symbol),
            "financials": scrape_financials_yahoo_finance(stock_symbol)}
    return temp

