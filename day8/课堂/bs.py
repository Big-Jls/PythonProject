import time
from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent
ua = UserAgent()

url = 'https://movie.douban.com/top250?start=0&filter='
response = requests.get(url,headers={'User-Agent':ua.random})
soup = BeautifulSoup(response.text,features='lxml')
ol = soup.find('ol', class_='grid_view')
items = ol.find_all('div', class_='item')
for item in items:
    movie_num = item.find('em').text
    image_url = item.find('img').get('src')
    movie_url = item.find_all('a')[0].get('href')
    zh_movie_title = item.find_all('span',attrs={'class':'title'})[0].text.strip()
    bd = item.find('div',attrs={'class':'bd'})
    # ps = item.find_all('p')[0]
    author = item.find_all('p')[0].text.strip().split('/')[0].split(':')[-1].strip()
    director = item.find_all('p')[0].text.strip().split('/')[0].split(':')[1].strip()[:-5]
    rating_num = item.find('span',attrs={'class':'rating_num'}).text
    quote = item.find('p',attrs={'class':'quote'}).find('span').text
    data = {
        'zh_movie_title':zh_movie_title,
        'movie_url':movie_url,
        'image_url':image_url,
        'movie_num':movie_num,
        'author':author,
        'director':director,
        'rating_num': rating_num,
        'quote':quote
    }
    print('-----------------------')
    print(data)
    time.sleep(1)
