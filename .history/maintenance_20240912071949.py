import requests
from bs4 import BeautifulSoup

url = 'https://caredge.com/ranks/maintenance'

response = requests.get(url)    # retrieving data from the url

soup = BeautifulSoup(response.text, 'html.parser')

table = soup.find('table')  # get the 1st table on the page

tbody = table.tbody

rows = tbody.find_all('tr')

car_maintenance_cost = []
for row in rows:
    cols = row.find_all('td')
    car_maintenance_cost.append({
        'brand': cols[1].text,
        'cost': float(cols[2].text.replace('$', '').replace('.', ''), 2)
    })
    
    
print(car_maintenance_cost)
