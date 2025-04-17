import requests
import pandas as pd
import json
import time
import logging
import pymongo
import math
# token跟登录授权时间有关系
# 自定义格式化器，用于设置日志颜色
class CustomFormatter(logging.Formatter):
    grey = "\x1b[38;20m"
    yellow = "\x1b[33;20m"
    red = "\x1b[31;20m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"

    def __init__(self, fmt):
        super().__init__()
        self.fmt = fmt
        self.FORMATS = {
            logging.DEBUG: self.grey + self.fmt + self.reset,
            logging.INFO: self.grey + self.fmt + self.reset,
            logging.WARNING: self.yellow + self.fmt + self.reset,
            logging.ERROR: self.red + self.fmt + self.reset,
            logging.CRITICAL: self.bold_red + self.fmt + self.reset
        }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)

# 创建日志记录器
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# 创建文件处理器
file_handler = logging.FileHandler('GITEE_log.txt', encoding='utf-8')
file_handler.setLevel(logging.INFO)

# 创建控制台处理器
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# 创建日志格式
fmt = '%(asctime)s - %(levelname)s - %(message)s'
# 使用自定义格式化器
file_handler.setFormatter(CustomFormatter(fmt))
console_handler.setFormatter(CustomFormatter(fmt))

# 将处理器添加到日志记录器
logger.addHandler(file_handler)
logger.addHandler(console_handler)

client = pymongo.MongoClient()
db = client.get_database('git')
collection = db.get_collection('gitee')
datas = pd.read_excel('python2411爬虫网站.xlsx', sheet_name='python2411爬虫网站')

students = {}
for name, num, data_url in zip(datas['姓名'], datas['编号'], datas['仓库地址']):
    # 检查姓名和编号是否为 nan
    if isinstance(name, str) and not math.isnan(num):
        name = name.strip()
        owner = data_url.split('/')[-2]
        repo = data_url.split('/')[-1].split('.')[0]
        students[name] = {
           'sha':'master',
            'id': int(num),
            'owner': owner,
           'repo': repo
        }

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0'
}
try:
    for key in students.keys():
        gitee_events_url = ('https://gitee.com/api/v5/repos/{owner}/{repo}/events?access_token=6cadc8597166ed23cfe27ff83c4422b7&limit=20').format(**students[key])
        response = requests.get(gitee_events_url, headers=headers)
        json_datas = response.json()
        logger.info(f'学生{key}总共有{len(json_datas)}次提交，终端仅显示最近5次，后续请见./git学生对应json文件或MongoDB')
        logger.info(f'{gitee_events_url}')
        if len(json_datas) > 5:
            for i in range(5):
                data = {
                    'time': json_datas[i]['created_at'],
                    'type': json_datas[i]['type'],
                    'payload': json_datas[i]['payload']
                }
                logger.info(f'{data}')
        elif json_datas.get('message') == 'Not Found Project':
            logger.warning(f'学生{key}git访问受限！')
        else:
            for i in range(len(json_datas)):
                data = {
                    'time': json_datas[i]['created_at'],
                    'type': json_datas[i]['type'],
                    'payload': json_datas[i]['payload']
                }
                # print(data)
        with open(f'./git/{key}.json', 'w', encoding='utf-8') as json1:
            json.dump(json_datas, json1, indent=4, ensure_ascii=False)
        if isinstance(json_datas, list):
            data = {
                key: json_datas
            }
            collection.insert_one(data)
        elif isinstance(json_datas, dict):
            data = {
                key: json_datas
            }
            collection.insert_one(data)
        time.sleep(0.5)
except Exception as e:
    logger.error(e)
finally:
    client.close()