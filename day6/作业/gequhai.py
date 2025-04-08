import time
import requests
from lxml import etree
import re

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36 Edg/135.0.0.0',
    'cookie': 'Hm_lvt_49c19bcfda4e5fdfea1a9bb225456abe=17440  71739; HMACCOUNT=5891988AF2D1CB79; Hm_tf_no8z3ihhnja=1744071739; Hm_lvt_no8z3ihhnja=1744071739; PHPSESSID=cq346gp3jcti6dso5p0o8502u7; Hm_lpvt_49c19bcfda4e5fdfea1a9bb225456abe=1744080032; Hm_ck_1744073781591=42; Hm_lpvt_no8z3ihhnja=1744084284',
    'host': 'www.gequhai.com',
    'x-custom-header': 'SecretKey',
    'x-requested-with': 'XMLHttpRequest'
}

for i in range(1, 11):
    print(f'正在爬取第{i}页的歌曲')
    print()
    url = f'https://www.gequhai.com/hot-music/{i}'
    response = requests.get(url, headers=headers)
    html = response.content.decode()
    tree = etree.HTML(html)
    trs = tree.xpath('//table/tbody/tr')
    for tr in trs:
        id = tr.xpath('./td[1]')
        image_url = tr.xpath('./td[2]/img/@src')[0]
        title = tr.xpath('./td[3]/a/text()')[0].strip()
        sing_url = tr.xpath('./td[3]/a/@href')[0]
        sing_url = 'https://www.gequhai.com' + sing_url
        singer = tr.xpath('./td[4]/text()')
        print('---------------------')
        # 获取mp3
        print(f'正在下载{singer}的{title}歌曲')
        sing_response = requests.get(sing_url, headers=headers)
        html = sing_response.content.decode('utf-8')
        sing_id = re.search("window.play_id = '(.*?)'", html, re.S).group(0)[18:-1]
        data = {
            'id': sing_id
        }
        sing_d_response = requests.post('https://www.gequhai.com/api/music', data=data, headers=headers)
        if sing_d_response.status_code == 200:
            try:
                sing_d_response_json = sing_d_response.json()
                # print(sing_d_response_json)
                sing_d_url = sing_d_response_json['data']['url']
                sing_d_url_response = requests.get(sing_d_url)
                with open(f'./musics/{sing_url.split("/")[-1]}.mp3', 'wb') as f:
                    f.write(sing_d_url_response.content)
            except Exception as e:
                print(f"处理响应时出错: {e}")
        else:
            print(f"请求失败，状态码: {sing_d_response.status_code}")
        time.sleep(3)

        # 获取图片
        print(f'正在下载{singer}的{title}图片')
        img_response = requests.get(image_url)
        with open(f'./images/{image_url.split("/")[-1]}', 'wb') as imgf:
            imgf.write(img_response.content)
        time.sleep(3)
    time.sleep(3)
