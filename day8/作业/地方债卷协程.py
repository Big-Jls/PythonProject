import aiohttp
import asyncio
import time
from fake_useragent import UserAgent
import json
import pymongo


async def fetch(session):
    while params:
        url = 'https://www.governbond.org.cn:4443/api/loadBondData.action'
        param = params.pop()
        headers = {
            'User-Agent': ua.random
        }
        async with session.get(url, params=param, headers=headers) as response:
            text = await response.text()
            json_text = json.loads(text)
            ZJ_datas = json_text['data']
            for ZJ_data in ZJ_datas:
                data = {
                    '债卷名称': ZJ_data['ZQ_NAME'],
                    '债卷编码': ZJ_data['ZQ_CODE'],
                    '发行地区': ZJ_data['AD_NAME'],
                    '发行时间': ZJ_data['ZQ_FXTIME'],
                    '发行期限': ZJ_data['ZQQX_NAME'],
                    '发行规模': ZJ_data['FX_AMT'],
                    '利润': ZJ_data['LL'],
                    '利息方式': ZJ_data['FXFS'] if 'FXFS' not in ZJ_data else '',
                    '起息日': ZJ_data['QX_DATE']
                }
                print(f'正在爬取第{param['page']}页{data}')
                collection.insert_one(data)
        await asyncio.sleep(1)


async def task():
    async with aiohttp.ClientSession() as session:
        return await fetch(session)


async def main():
    await asyncio.gather(*[asyncio.create_task(task()) for _ in range(12)])


if __name__ == '__main__':
    # print(int(time.time() * 1000))
    # 1744284246588.05
    # 1744283435715
    params = [{
        'timeStamp': f'{int(time.time() * 1000)}',
        'dataType': 'ZQFXLISTBYAD',
        'adList': '',
        'adCode': '87',
        'zqlx': '',
        'year': '',
        'fxfs': '',
        'qxr': '',
        'fxqx': '',
        'zqCode': '',
        'zqName': '',
        'page': f'{i}',
        'pageSize': '10'} for i in range(1, 1642)]
    ua = UserAgent()
    con = pymongo.MongoClient()
    db = con.get_database('zj')
    collection = db.get_collection('df')
    asyncio.run(main())
    con.close()
