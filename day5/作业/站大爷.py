import time
import requests
from lxml import etree
import re

test_url = 'https://www.zdaye.com/free/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36 Edg/135.0.0.0',
    'referer':'https://www.zdaye.com/free/'
}
proxies = {
    'http': 'http://{}'.format('39.107.249.241:3883'),
}
# html=requests.get(test_url, headers=headers, proxies=proxies, verify=False).text

for i in range(1,13):
    time.sleep(3)
    print(f'正在爬取第{i}页')
    url = f'https://www.zdaye.com/free/{i}/'
    html = requests.get(url, headers=headers, proxies=proxies, verify=False).text
    # print(html)
    try:
        tree = etree.HTML(html)
        table = tree.xpath('//table')[0]
        # print(table)
        trs = table.xpath('//tr')
        num = 0
        for tr in trs:
            ip = tr.xpath('./td[1]/text()')[0]
            port = tr.xpath('./td[2]/text()')[0]
            type = tr.xpath('./td[3]/text()')
            title = tr.xpath('./td[4]/text()')
            times = tr.xpath('./td[5]/text()')
            proxies = {
                'http': f'http://{ip}:{port}'
            }
            print(f'正在尝试第{num}ip:{ip}:{port}')
            test_response = requests.get(test_url, headers=headers, proxies=proxies, verify=False)
            test_response.encoding = test_response.apparent_encoding
            html = test_response.text
            if re.search('禁止', html, re.S):
                print(f'该{ip}:{port}被禁止')
            time.sleep(5)
    except IndexError as e:
        print(f'{e}')
    except requests.exceptions.SSLError as e:
        print(f'{e}')