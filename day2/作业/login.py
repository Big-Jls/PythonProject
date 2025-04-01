import time

import requests
import re
import json

session = requests.Session()
login_url = 'https://quotes.toscrape.com/login'
data = {
    'username': 'admin',
    'password': 'admin'
}
response = session.post(login_url, data=data, allow_redirects=False)
print(response.cookies)
d = {

}
d['tags'] = []
count = 0
for i in range(1, 11):
    url = f'https://quotes.toscrape.com/page/{i}/'
    response1 = session.get(url)
    html = response1.content.decode()
    datas = re.findall('<div class="quote" itemscope itemtype="http://schema.org/CreativeWork">(.*?)</div>', html, re.S)
    # print(datas[0])
    for data in datas:
        count = count + 1
        text = re.search('<span class="text" itemprop="text">(.*?)</span>', data, re.S).group(1)
        author = re.search('<small class="author" itemprop="author">(.*?)</small>', data, re.S).group(1)
        tags = re.findall('<a class="tag" href="/tag/([^/]+)/page/1/">(.*?)</a>', data, re.S)
        for tag in tags:
            d['tags'].append(tag[0])
        url = 'https://quotes.toscrape.com/' + re.search('<a\s+href="([^"]+)"', data, re.S).group(1)
        d['text'] = text
        d['author'] = author
        d['url'] = url
        print(d)
        with open(f'./quotes/{count}.json',encoding='utf-8') as f:
            json.dump(d, f, ensure_ascii=False, indent=4)
        time.sleep(0.5)

