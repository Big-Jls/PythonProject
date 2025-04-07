import pymongo
import requests
import json
import time

url = 'https://news.cctv.com/2019/07/gaiban/cmsdatainterface/page/news_1.jsonp?cb=news'
response = requests.get(url)
datas_json = json.loads(response.content.decode()[5:-1])
total = datas_json['data']['total']
for i in range(1,(500 % 80 +1)):
    news = []
    time.sleep(1)
    url = f'https://news.cctv.com/2019/07/gaiban/cmsdatainterface/page/news_{i}.jsonp?cb=news'
    response = requests.get(url)
    datas_json = json.loads(response.content.decode()[5:-1])
    datas_list = datas_json['data']['list']
    for data in datas_list:
        image_urls = []
        title = data['title']
        print(f'正在爬取第{i}页,title={title}的新闻')
        brief = data['brief']
        image_url = data['image']
        # print(f'{image_url[53:]}')
        if data['image2']:
            image_url2 = data['image2']
            image_urls.append(image_url2)
            with open(f'./cctvimages/{image_url[53:]}', 'wb') as f:
                f.write(requests.get(data['image']).content)
        if data['image3']:
            image_url3 = data['image3']
            image_urls.append(image_url3)
            with open(f'./cctvimages/{image_url[53:]}', 'wb') as f:
                f.write(requests.get(data['image']).content)
        with open(f'./cctvimages/{image_url[53:]}', 'wb') as f:
            f.write(requests.get(data['image']).content)
        image_urls.append(image_url)
        new = {
            'title': title,
            'brief': brief,
            'image_url': image_urls
        }
        news.append(new)
        time.sleep(1)
    print(f'正在第{i}次写入mongodb数据库')
    client = pymongo.MongoClient()
    db = client.get_database('cctv')
    con = db.get_collection('news')
    con.insert_many(news)
