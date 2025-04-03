import time

import requests
url = 'https://e621.net/posts.json'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0',
}
api_key = 'gmZj3wUtfRY5DmGNwBGZTePn'
login = 'Big_Jls'
limit = 100
count = 0
e621_url = url + '?api_key=' + api_key + '&limit=' + str(limit) + '&login=' + login

response = requests.get(e621_url, headers=headers)
data_json = response.json()
# print(data_json)
datas = data_json['posts']
for data in datas:
    count = count + 1
    file = data['file']
    ext = file['ext']
    url = file['url']
    img_id = data['id']
    img_response = requests.get(url, headers=headers)
    with open(f'./e621/{img_id}.{ext}', 'wb') as f:
        f.write(img_response.content)
    time.sleep(0.5)
    print(f'{img_id}.{ext}已被爬取这是第{count}张')
