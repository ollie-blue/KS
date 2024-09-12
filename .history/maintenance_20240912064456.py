import requests

url = 'https://caredge.com/ranks/maintenance'

response = requests.get(url)    # retrieving data from the url

print(response.text)
