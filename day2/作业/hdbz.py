import time
import requests
import re
url = 'https://www.hdbz.net/'
response = requests.get(url)
html = response.content.decode('utf-8')
m = re.search('<div class="clearfix pic-auto pic-list">(.*?)<div class="layout auto mt15">', html, re.S)
# print(m.group(1),type(m.group(1)))
m_group = m.group(1)
m1 = re.findall('data-original="(.*?)"',m_group, re.S)
# print(m1)
for img_thumbs_url in m1:
    response = requests.get(img_thumbs_url)
    match = re.search(r'/(\d+)\.(jpg|png)', img_thumbs_url)
    if match:
        img_id = match.group(1)
        img_ext = match.group(2)
        with open(f'./images/thumbs/{img_id}.{img_ext}', 'wb') as f:
            f.write(response.content)
        print(f"成功保存图片: {img_id}.{img_ext}")
        time.sleep(0.5)