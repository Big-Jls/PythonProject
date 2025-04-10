import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import pymongo

ua = UserAgent()

# 请求地址
proxy_url = "https://sch.shanchendaili.com/api.html?action=get_ip&key=HUed9923215886768260wEFy&time=10&count=1&type=json&only=0"
proxy_response = requests.get(proxy_url)
proxy_json = proxy_response.json()
print(proxy_json)
ip = proxy_json['list'][0]['sever']
port = proxy_json['list'][0]['port']
proxy = "http://%(ip)s:%(port)s" % {
    "ip": ip,
    "port": port,
}
proxies = {

    "http": proxy,
    "https": proxy,
}

book_url = 'https://www.biq03.cc/top/'

book_response = requests.get(book_url, headers={
    'User-Agent': ua.random,
    'referer': 'https://www.biq03.cc/read/103768/1.html'
}, proxies=proxies)
# print(response.text)
book_soup = BeautifulSoup(book_response.text, 'lxml')
blocks = book_soup.find_all('div', class_='blocks')
for block in blocks:
    category = block.find('h2').text
    a_s = block.find_all('a')
    # print(a_s)
    for a in a_s:
        book_name = a.text
        book_chapter_url = 'https://www.biq03.cc' + a.get('href')
        book_chapter_response = requests.get(book_chapter_url, headers={
            'User-Agent': ua.random
        }, proxies=proxies)
        print(book_chapter_response.text)
        book_chapter_soup = BeautifulSoup(book_chapter_response.text, 'lxml')
        # print(book_chapter_soup.prettify())
        listmain = book_chapter_soup.find('div', attrs={'class': 'listmain'})
        dd_as = listmain.find_all('a')
        for dd_a in dd_as:
            chapter_name = dd_a.text
            # print(f'章节{chapter_name}正在爬取')
            book_detial_url = 'https://www.biq03.cc' + dd_a.get('href')
            # print(book_detial_url)
            con = pymongo.MongoClient()
            db = con.get_database('bqg')
            collection = db.get_collection('xs')
            collection.insert_one({
                'chapter_name': chapter_name,
                'book_name': book_name,
                'book_detial_url': book_detial_url
            })
            con.close()
        break
    # book_url =
    break

