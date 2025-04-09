import re
import time
from lxml import etree
import pymongo
import os
import threading
import requests
from fake_useragent import UserAgent
from queue import Queue

# 第一个生产者函数，负责获取小说列表
def producer1(task_queue1):
    ua = UserAgent()
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

    for data in datas:
        url = 'https://www.zongheng.com/api2/catefine/storeSearch'
        headers = {'user-agent': ua.random}
        try:
            response = requests.post(url, data=data, headers=headers)
            book_json = response.json()
            book_list = book_json['result']['bookList']
            for book in book_list:
                task_queue1.put(book)
        except Exception as e:
            print(f"生产者1出错: {e}")
        time.sleep(0.5)

# 第二个生产者函数，负责获取小说的章节列表
def producer2(task_queue1, task_queue2):
    ua = UserAgent()
    while True:
        book = task_queue1.get()
        if book is None:
            break
        book_id = book['bookId']
        book_name = book['name']
        book_description = book['description']
        categoryName = book['categoryName']
        totalWords = book['totalWords']
        authorName = book['authorName']
        print('-------------------------------')
        print(f'正在获取小说《{book_name}》的章节列表')

        book_chapter_url = 'https://bookapi.zongheng.com/api/chapter/getChapterList'
        data = {
            'bookId': book_id
        }
        headers = {'user-agent': ua.random}
        try:
            book_chapter_response = requests.post(book_chapter_url, data=data, headers=headers)
            book_chapter_json = book_chapter_response.json()
            book_chapter_list = book_chapter_json['result']['chapterList']
            book_datas = {
                book_name: []
            }
            for chapter in book_chapter_list:
                chapterviewlist = chapter['chapterViewList']
                for view in chapterviewlist:
                    if view['level'] == 1:
                        break
                    chaptername = view['chapterName']
                    chapterid = view['chapterId']
                    book_content_url = f'https://read.zongheng.com/chapter/{book_id}/{chapterid}.html'
                    chapter_data = {
                        'book_name': book_name,
                        'bookId': book_id,
                        'chapterid': chapterid,
                        'chapterName': chaptername,
                        'authorName': authorName,
                        'book_description': book_description,
                        'categoryName': categoryName,
                        'totalWords': totalWords,
                        'book_content_url': book_content_url
                    }
                    task_queue2.put(chapter_data)
        except Exception as e:
            print(f"生产者2出错: {e}")
        task_queue1.task_done()
        time.sleep(0.5)

# 消费者函数，负责下载小说章节内容并保存到本地和 MongoDB
def consumer(task_queue2):
    ua = UserAgent()
    while True:
        chapter_data = task_queue2.get()
        if chapter_data is None:
            break
        book_name = chapter_data['book_name']
        bookId = chapter_data['bookId']
        chapterid = chapter_data['chapterid']
        chaptername = chapter_data['chapterName']
        authorName = chapter_data['authorName']
        book_description = chapter_data['book_description']
        categoryName = chapter_data['categoryName']
        totalWords = chapter_data['totalWords']
        book_content_url = chapter_data['book_content_url']

        print(f'正在爬取小说《{book_name}》的章节《{chaptername}》')

        headers = {'user-agent': ua.random}
        try:
            book_content_response = requests.get(book_content_url, headers=headers)
            book_content_html = book_content_response.content.decode('utf-8')
            print(book_content_html)
            book_content_tree = etree.HTML(book_content_html)
            book_contents = ''.join(
                book_content_tree.xpath('//div[contains(@class,"content")]/p/text()'))
            book_data = {
                'book_name': book_name,
                'bookId': bookId,
                'chapterid': chapterid,
                'chapterName': chaptername,
                'authorName': authorName,
                'book_description': book_description,
                'categoryName': categoryName,
                'totalWords': totalWords,
                'bookContent': book_contents
            }
            # print(book_contents)
            os.makedirs(f'./notes/{book_name}', exist_ok=True)
            chaptername = re.sub(r'[\\/:*?"<>| \t\n]', '', chaptername)
            with open(f'./notes/{book_name}/{chaptername}.txt', 'w', encoding='utf-8') as f:
                f.write(book_contents)
            con = pymongo.MongoClient()
            db = con.get_database('notes')
            collection = db.get_collection('woman')
            collection.insert_one(book_data)
            con.close()
        except Exception as e:
            print(f"消费者出错: {e}")
        task_queue2.task_done()
        time.sleep(0.5)

if __name__ == '__main__':
    task_queue1 = Queue()
    task_queue2 = Queue()
    producer1_threads = [threading.Thread(target=producer1, args=(task_queue1,)) for _ in range(5)]
    producer2_threads = [threading.Thread(target=producer2, args=(task_queue1, task_queue2)) for _ in range(5)]
    consumer_threads = [threading.Thread(target=consumer, args=(task_queue2,)) for _ in range(10)]

    for producer1_thread in producer1_threads:
        producer1_thread.start()
    for producer2_thread in producer2_threads:
        producer2_thread.start()
    for consumer_thread in consumer_threads:
        consumer_thread.start()

    for producer1_thread in producer1_threads:
        producer1_thread.join()

    # 向队列中放入 None 信号，表示任务结束
    for _ in range(5):
        task_queue1.put(None)

    for producer2_thread in producer2_threads:
        producer2_thread.join()

    for _ in range(10):
        task_queue2.put(None)

    for consumer_thread in consumer_threads:
        consumer_thread.join()

    time.sleep(3)