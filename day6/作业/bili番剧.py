import time
import requests
import pymongo

headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36 Edg/135.0.0.0',
    'referer':'https://www.bilibili.com/anime/index/?from_spmid=666.4.index.0',
}

for i in range(21,49):
    print('-------------------')
    print(f'正在爬取第{i}页番剧')
    url = ('https://api.bilibili.com/pgc/season/index/result?st=1&order=3&season_version=-1&spoken_language_type=-1'
           f'&area=-1&is_finish=-1&copyright=-1&season_status=-1&season_month=-1&year=-1&style_id=-1&sort=0&page={i}'
           '&season_type=1&pagesize=20&type=1')
    response = requests.get(url, headers=headers)
    response_json = response.json()
    datas_list = response_json['data']['list']
    for data in datas_list:
        badge = data['badge']
        title = data['title']
        subTitle = data['subTitle']
        score = data['score']
        index_show = data['index_show']
        order = data['order']
        link = data['link']
        img_url = data['cover']
        img_id = img_url.split('/')[-1]
        img_path = f'./bili/{img_id}'
        with open(f'./bili/{img_id}', 'wb') as f:
            f.write(requests.get(img_url, headers=headers).content)

        data_d = {
            'title': title,
            'subTitle': subTitle,
            'score': score,
            'index_show': index_show,
            'order': order,
            'link': link,
            'img_path': img_path
        }
        print(f'{data_d}')

        con = pymongo.MongoClient()
        db = con.get_database('bili')
        collection = db.get_collection('anime')
        collection.insert_one(data_d)
        con.close()
        time.sleep(0.5)
    time.sleep(1)


