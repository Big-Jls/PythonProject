from lxml import etree
import requests

url = 'https://quotes.toscrape.com/page/1/'
response = requests.get(url)
print(response.text)