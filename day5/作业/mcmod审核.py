import requests
from lxml import etree
import time
import pymongo

import pymysql

start_time = '2025-3-1'
end_time = '2025-3-30'

start_time = time.mktime(time.strptime(start_time, '%Y-%m-%d'))
end_time = time.mktime(time.strptime(end_time, '%Y-%m-%d'))
i = 0

datas = []

while(True):
    i = i + 1
    j = 0
    j = j + 1
    print(f'正在爬取第{i}条')
    time.sleep(1)
    url = f'https://www.mcmod.cn/verify.html?starttime={start_time}&endtime={end_time}&order=verifytime&page={i}'
    response = requests.get(url)
    try:
        data = {
            'name': '',
            'active_part': '',
            'time': '2025-4-7',
            'audit': {
                'state': '',
                'info': '',
                'num': 0,
                'assessor': '',
                'finish_time': ''
            }
        }
        temp = {}
        html = response.content.decode('utf-8')
        # print(html)
        tree = etree.HTML(html)
        table_html = tree.xpath('//table[@class="table table-bordered table-striped table-condensed table-sm verify-list-list-table"]')
        # print(table_html[0])
        title = table_html[0].xpath('//th/text()')
        # print(th)
        name = table_html[0].xpath(f'//tr[{i}]/td[{j}]/a/text()')[0]
        # print(name)
        active_part1 = table_html[0].xpath(f'//tr[{i}]/td[{j+1}]/text()')
        active_part2 = table_html[0].xpath(f'//tr[{i}]/td[{j+1}]/a/text()')
        # print(active_part2)
        if len(active_part1) == 1 and len(active_part2) == 1:
            active_part = str(active_part1[0]).strip() + str(active_part2[0]).strip()
        elif len(active_part1) == 2 and len(active_part2) == 1:
            active_part = str(active_part1[0]).strip() + str(active_part2[0]).strip() + str(active_part1[1]).strip()
        elif len(active_part1) == 3 and len(active_part2) == 2:
            active_part = str(active_part1[0]).strip() + str(active_part2[0]).strip() + str(active_part1[1]).strip() + str(active_part2[1]).strip() + str(active_part1[2]).strip()
        else:
            active_part = ""
            # print(active_part)
        times = table_html[0].xpath(f'//tr[{i}]/td[{j+2}]/p/span/text()')[0]
        is_message = table_html[0].xpath(f'//tr[{i}]/td[{j + 3}]')[0]
        if len(is_message) == 3:
            state = table_html[0].xpath(f'//tr[{i}]/td[{j + 3}]/p[1]/text()')[0]
            num = 0
            info = ''
            assessor = table_html[0].xpath(f'//tr[{i}]/td[{j + 3}]/p[2]/a/text()')[0]
            finish_time = table_html[0].xpath(f'//tr[{i}]/td[{j + 3}]/p[3]/text()')[0][5:]
        elif len(is_message) == 4:
            state = table_html[0].xpath(f'//tr[{i}]/td[{j + 3}]/p[1]/text()')[0]
            num = 0
            info = table_html[0].xpath(f'//tr[{i}]/td[{j + 3}]/p[2]/text()')[0][4:]
            assessor = table_html[0].xpath(f'//tr[{i}]/td[{j + 3}]/p[3]/a/text()')[0]
            finish_time = table_html[0].xpath(f'//tr[{i}]/td[{j + 3}]/p[4]/text()')[0][5:]
        elif len(is_message) == 5:
            state = table_html[0].xpath(f'//tr[{i}]/td[{j + 3}]/p[1]/text()')[0]
            num =  table_html[0].xpath(f'//tr[{i}]/td[{j + 3}]/p[2]/text()')[0][4:]
            info = table_html[0].xpath(f'//tr[{i}]/td[{j + 3}]/p[3]/text()')[0][4:]
            assessor = table_html[0].xpath(f'//tr[{i}]/td[{j + 3}]/p[4]/a/text()')[0]
            finish_time = table_html[0].xpath(f'//tr[{i}]/td[{j + 3}]/p[5]/text()')[0][5:]
        else:
            raise IndexError
        temp = {
            'state':state,
            'info':info,
            'num': num,
            'assessor':assessor,
            'finish_time':finish_time
        }
        data['name'] = name
        data['time'] = times
        data['active_part'] = active_part
        # print(active_part)
        data['audit'] = temp
        datas.append(data)
    except IndexError as e:
        print(e)
        break

con = pymongo.MongoClient()
db = con.get_database('mcmod')
collection = db.get_collection('mcmod_audit')
collection.insert_many(datas)
con.close()


