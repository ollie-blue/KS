import requests
from bs4 import BeautifulSoup

url = 'https://caredge.com/ranks/maintenance'

response = requests.get(url)    # retrieving data from the url

soup = beautifulsoup4(response.text, 'html.parser')

print(response.text)
