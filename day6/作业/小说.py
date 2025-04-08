import re
import requests
from lxml import etree
import time
import pymongo
import os

for i in range(1,101):
    url = 'https://www.zongheng.com/api2/catefine/storeSearch'
    data = {
        'worksTypes': 0,
        'bookType': 1,
        'subWorksTypes': 0,
        'totalWord': 0,
        'serialStatus': 1,
        'vip': 9,
        'pageNum': i,
        'pageSize': 20,
        'categoryId': 0,
        'categoryPid': 0,
        'order': 'weekOrder',
        'naodongFilter': 0,
    }

    book_response = requests.post(url, data=data)
    # 主页返回book简易信息的json
    book_list = book_response.json()['result']['bookList']
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
        print(f'正在爬取第{i}页第{count}小说《{book_name}》')

        # 根据id获取小说详情页html进而获得每章节url进去爬取每章节内容
        # book_detail_url = f'https://huayu.zongheng.com/showchapter/{book_id}.html'
        # book_detail_response = requests.get(book_detail_url)
        # book_detail_html = book_detail_response.content.decode()
        # book_detail_tree = etree.HTML(book_detail_html)
        # book_chapter_lis = book_detail_tree.xpath('//ul[@class="chapter-list clearfix"]/li[@class=" col-4"]')
        # for book_chapter_li in book_chapter_lis:
        #     book_chapter_url = book_chapter_li.xpath('//a/@href')[0]
        #     book_content_response = requests.get(book_chapter_url)

        # 根据bookid添加到data查询更详细的信息json
        book_chapter_url = 'https://bookapi.zongheng.com/api/chapter/getChapterList'
        data = {
            'bookId': book_id
        }
        book_chapter_response = requests.post(book_chapter_url, data=data)
        book_chapter_list = book_chapter_response.json()['result']['chapterList']
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
                book_content_response = requests.get(book_content_url)
                book_content_html = book_content_response.content.decode('utf-8')
                # print(book_content_html)
                book_content_tree = etree.HTML(book_content_html)
                # 将得到的<p>拼接成一个完整的字符串
                book_contents = ''.join(book_content_tree.xpath('//div[contains(@class,"content")]/p/text()'))
                book_data = {
                    'book_name':book_name,
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
                chaptername = re.sub(r'[\\/:*?"<>|]', '', chaptername)
                with open(f'./notes/{book_name}/{chaptername}.txt', 'w', encoding='utf-8') as f:
                    f.write(book_contents)
                time.sleep(0.5)
            time.sleep(0.5)
        con = pymongo.MongoClient()
        db = con.get_database('notes')
        collection = db.get_collection('woman')
        collection.insert_one(book_datas)
        con.close()
        time.sleep(1)
    time.sleep(1)