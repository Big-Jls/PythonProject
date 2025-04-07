import requests
from lxml import etree

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36 Edg/135.0.0.0',
    'referer':'https://movie.douban.com/top250'
}
proxies = {
    'http': 'http://{}'.format('109.109.166.176:8104'),
    'https': 'http://{}'.format('109.109.166.176:8104')
}


for i in range(0,250,25):
    url = f'https://movie.douban.com/top250?start={i}&filter='
    response = requests.get(url, headers=headers, proxies=proxies)
    print(response.content.decode('utf-8'))
    tree = etree.HTML(response.content.decode('utf-8'))