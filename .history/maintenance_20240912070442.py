import requests
from bs4 import BeautifulSoup

url = 'https://caredge.com/ranks/maintenance'

response = requests.get(url)    # retrieving data from the url

soup = BeautifulSoup(response.text, 'html.parser')

table = soup.find('table')  # get the 1st table on the page

tbody = table.tbody

rows = tbody.find_all('tr')


for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    print(cols)
    
    
# print(table)
