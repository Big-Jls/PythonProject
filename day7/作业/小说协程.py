import re
import time
from lxml import etree
import pymongo
import os
import asyncio
import aiohttp
from fake_useragent import UserAgent


async def fetch(session):
    while datas:
        url = 'https://www.zongheng.com/api2/catefine/storeSearch'
        data = datas.pop()
        # print(data)
        async with session.post(url, data=data, headers = {'user-agent': ua.random}) as book_response:
            book_json = await book_response.json()
            book_list = book_json['result']['bookList']
            count = 0
            for book in book_list:
                count += 1
                # 获得bookid
                book_id = book['bookId']
                book_name = book['name']
                book_datas = {
                    book_name: []
                }
                book_description = book['description']
                categoryName = book['categoryName']
                totalWords = book['totalWords']
                authorName = book['authorName']
                print('-------------------------------')
                print(f'正在爬取小说《{book_name}》')

                book_chapter_url = 'https://bookapi.zongheng.com/api/chapter/getChapterList'
                data = {
                    'bookId': book_id
                }
                async with session.post(book_chapter_url, data=data, headers = {'user-agent':ua.random}) as book_chapter_response:
                    book_chapter_json = await book_chapter_response.json()
                    book_chapter_list = book_chapter_json['result']['chapterList']
                    for chapter in book_chapter_list:
                        chapterviewlist = chapter['chapterViewList']
                        for view in chapterviewlist:
                            # print(view)
                            # 判断是否是VIP付费类型
                            if view['level'] == 1:
                                break
                            # 章节名
                            chaptername = view['chapterName']
                            print(f'{chaptername}')
                            # 章节id
                            chapterid = view['chapterId']
                            # 将书本id和章节id拼成该书本该章节完整URL
                            book_content_url = f'https://read.zongheng.com/chapter/{book_id}/{chapterid}.html'
                            async with session.get(book_content_url, headers = {'user-agent':ua.random}) as book_content_response:
                                book_content_html = await book_content_response.text()
                                # print(book_content_html)
                                book_content_tree = etree.HTML(book_content_html)
                                # 将得到的<p>拼接成一个完整的字符串
                                book_contents = ''.join(
                                    book_content_tree.xpath('//div[contains(@class,"content")]/p/text()'))
                                book_data = {
                                    'book_name': book_name,
                                    'bookId': book_id,
                                    'chapterid': chapterid,
                                    'chapterName': chaptername,
                                    'authorName': authorName,
                                    'book_description': book_description,
                                    'categoryName': categoryName,
                                    'totalWords': totalWords,
                                    'bookContent': book_contents
                                }
                                book_datas[book_name] = book_data

                                os.makedirs(f'./notes/{book_name}', exist_ok=True)
                                # 正则判断不能保存的字符
                                chaptername = re.sub(r'[\\/:*?"<>| \t\n]', '', chaptername)
                                with open(f'./notes/{book_name}/{chaptername}.txt', 'w', encoding='utf-8') as f:
                                    f.write(book_contents)
                                await asyncio.sleep(0.5)
                    await asyncio.sleep(0.5)
                con = pymongo.MongoClient()
                db = con.get_database('notes')
                collection = db.get_collection('woman')
                collection.insert_one(book_datas)
                con.close()
            await asyncio.sleep(0.5)


async def task():
    async with aiohttp.ClientSession() as session:
        return await fetch(session)


async def main():
    await asyncio.gather(*[asyncio.create_task(task()) for i in range(10)])


if __name__ == '__main__':
    datas = [{
        'worksTypes': 0,
        'bookType': 1,
        'subWorksTypes': 0,
        'totalWord': 0,
        'serialStatus': 1,
        'vip': 9,
        'pageNum': i + 3,
        'pageSize': 20,
        'categoryId': 0,
        'categoryPid': 0,
        'order': 'weekOrder',
        'naodongFilter': 0,
    } for i in range(101)]
    ua = UserAgent()
    asyncio.run(main())
    time.sleep(3)
