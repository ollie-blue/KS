import requests
from bs4 import BeautifulSoup
import json

url = 'https://gasprices.aaa.com/state-gas-price-averages/'

def scrap_gas(url):
    """
    Scrap gas prices from AAA.com
    """
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36 Edg/101.0.1210.39',
    'Accept-Language': 'en-GB,en;q=0.5',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Referer': 'https://google.com/',
    }
      
    # get data from url 
    response = requests.get(url, headers = headers)
    print("Response status code:", response.status_code)
    if response.status_code == 200:
        # parse the HTML content of the response
        soup = BeautifulSoup(response.text, 'html.parser')
        # get the gas table on webpage
        gas_table = soup.find('table', {'id':'sortable'})
        rows = gas_table.find('tbody').find_all('tr')
        gas_price = {}

        for row in rows:
            # get the state name
            state = row.find('td').text.strip()

            # get the gas prices for each gas type
            regular_price = row.find('td', {'class': 'regular'}).text.strip()[1:]
            mid_grade_price = row.find('td', {'class': 'mid_grade'}).text.strip()[1:]
            premium_price = row.find('td', {'class': 'premium'}).text.strip()[1:]
            diesel_price = row.find('td', {'class': 'diesel'}).text.strip()[1:]

            # create a dictionary of gas prices for the state
            state_prices = {
                'Regular': regular_price,
                'Midgrade': mid_grade_price,
                'Premium': premium_price,
                'Diesel': diesel_price
            }    
            # add the state_price dictionary to the gas_price dictionary
            gas_price[state] = state_prices
            # print(state, "gas prices:", state_price)
        return gas_price

if __name__ == '__main__':
    print)scrap_gas(url)