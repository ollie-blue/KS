import requests
from bs4 import BeautifulSoup

url = 'https://caredge.com/ranks/maintenance'

response = requests.get(url)    # retrieving data from the url

soup = BeautifulSoup(response.text, 'html.parser')

table = soup.find('table')  # get the 1st table on the page

tbody = table.tbody

rows = tbody.find_all('tr')

maintenance_cost = []
for row in rows:
    cols = row.find_all('td')
    for col in cols:
        col1, col2, col3 = cols
    print(col1.text, col2.text, col3.text, sep=' | ')
    
    
# print(table)
