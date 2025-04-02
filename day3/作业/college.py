import time

import requests
import re
from lxml import etree

url = 'https://tieba.baidu.com/t/f/?class=college'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0'
}
response = requests.get(url,headers=headers)
college_url_html = response.text
# print(college_url_html)
college_url_div = re.search(r'<div class="each_topic_entrance_list">(.*?)</div>', college_url_html, re.S).group(1)
college_url_list = re.findall(r'<a class="each_topic_entrance_item" href="(.*?)" data-fid=".*?">.*?</a>', college_url_div, re.S)
print(college_url_list)
for eurl in college_url_list:
    each_url = 'https:' + eurl
    each_college_response = requests.get(each_url, headers=headers)
    tree = etree.HTML(each_college_response.text)
    college_title = tree.xpath('//h1[@class="forum_name"]/text()')
    titles = tree.xpath('//a[@class="thread_title"]/text()')
    print(f'贴吧 {college_title[0]} 如下:')
    print(titles)
    time.sleep(1)
    # break