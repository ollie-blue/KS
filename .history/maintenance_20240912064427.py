import requests

url = 'https://caredge.com/ranks/maintenance'

response = requests.get(url)

print(response.text)
