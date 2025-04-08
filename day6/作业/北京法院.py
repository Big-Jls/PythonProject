import time
import requests
from lxml import etree
import csv

headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36 Edg/135.0.0.0',
    'referer':'https://www.bjcourt.gov.cn/zxxx/indexOld.htm?',
}

for i in range(1,439):
    print('--------------------------')
    print(f'正在爬取第{i}页数据')
    datas = []
    url = f'https://www.bjcourt.gov.cn/zxxx/indexOld.htm?st=1&zxxxlx=100013007&bzxrlx=&bzxrxm=&zrr=&frhqtzz=&jbfyId=&ah=&dqxh=26&page={i}'
    response = requests.get(url, headers=headers)
    html = response.content.decode('utf-8')
    tree = etree.HTML(html)
    # print(html)
    table = tree.xpath('//table[@class="table_list_02"]')[0]
    fieldnames = table.xpath('//tr[1]/th/text()')
    # print(fieldnames)
    trs = table.xpath('//tr[position() > 1]')
    for tr in trs:
        id = tr.xpath('./td[1]/text()')[0]
        name = tr.xpath('./td[2]/@title')[0].strip()
        id_type = tr.xpath('./td[3]/text()')[0]
        id_num = tr.xpath('./td[4]/text()')[0]
        number = tr.xpath('./td[5]/text()')[0]
        address = tr.xpath('./td[6]/text()')[0]
        times = tr.xpath('./td[7]/text()')[0]
        data = {
            '序号':id,
            '姓名/名称':name,
            '证件类型':id_type,
            '证件号码/组织机构代码':id_num,
            '执行案号':number,
            '执行法院':address,
            '立案时间':times
        }
        datas.append(data)

    print(datas)
    with open(f'./gov/第{i}页.csv', 'w', newline='',encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(datas)
    time.sleep(2)