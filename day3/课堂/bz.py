import re
import time
import requests

url = 'https://www.bizhihui.com/page/'

for i in range(1,11):
    r_url = url + f'{i}/'
    r = requests.get(r_url)
    index_html = r.content.decode('utf-8')
    ul_html = re.search('<ul id="item-lists" class="clear">(.*?)</ul>', index_html, re.S).group(1)
    # print(ul_html)
    preview_urls = re.findall('<a class="item-img" href="(.*?)" title=".*?" target="_blank">', ul_html, re.S)
    for preview_url in preview_urls:
        preview_html = requests.get(preview_url).content.decode('utf-8')
        # print(preview_html)
        HD_url = re.search(r'<a href="([^"]+)" id="changeTxt2" onclick="getyt\(\)">.*?</a>', preview_html, re.S).group(1)
        img_id = HD_url[45:]
        img_response = requests.get(HD_url)
        with open(f'./bz/{img_id}','wb') as f:
            f.write(img_response.content)
        print(f'{img_id}爬取成功')
        time.sleep(0.5)
        # hd_url = re.search('<a class="item-img" href="(.*?)')
    time.sleep(1)