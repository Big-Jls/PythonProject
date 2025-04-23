import requests
import re
from fake_useragent import UserAgent
ua = UserAgent()
url = 'https://zhengzhou.anjuke.com/sale/p1/'
response = requests.get(url,headers={'User-Agent': ua.random})
html = response.text
print(html)
json_str = re.search(r'list:\[(.*)],ca',html, re.S).group(0)[:-3]
print(json_str)