import time
import requests
from lxml import etree
import csv
import aiohttp
from fake_useragent import UserAgent
import asyncio

ua = UserAgent()

urls = [
    f"https://www.bjcourt.gov.cn/zxxx/indexOld.htm?st=1&zxxxlx=100013007&bzxrlx=&bzxrxm=&zrr=&frhqtzz=&jbfyId=&ah=&dqxh=26&page={page}"
    for page in range(1, 439)]

headers = {
    'user-agent': ua.random,
    'referer': 'https://www.bjcourt.gov.cn/zxxx/indexOld.htm?',
}


async def request(session):
    while urls:
        url = urls.pop()
        async with session.get(url, headers=headers) as res:
            r = await res.text()
            tree = etree.HTML(r)
            items = tree.xpath('//table[@class="table_list_02"]/tr[position()>1]')
            datas = []
            for item in items:
                tds = item.xpath('./td/text()')
                data = {
                    "id": tds[0],
                    "name": tds[1].strip(),
                    "type": tds[2],
                    "value": tds[3],
                    "no": tds[4],
                    "address": tds[5],
                    "time": tds[6] if len(tds) > 6 else ''
                }
                datas.append(data)
        print(datas)


async def task():
    async with aiohttp.ClientSession() as session:
        return await request(session)


async def main():
    await asyncio.gather(*[asyncio.create_task(task()) for i in range(10)])


asyncio.run(main())
