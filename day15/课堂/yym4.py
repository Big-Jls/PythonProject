import requests
url = 'https://www.yym4.com/search/%E8%B7%B3%E6%A5%BC%E6%9C%BA-LBI%E5%88%A9%E6%AF%94%EF%BC%88%E6%97%B6%E6%9F%8F%E5%B0%98%EF%BC%89'

response = requests.get(url)
print(response.text)