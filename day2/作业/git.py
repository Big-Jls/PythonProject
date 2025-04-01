import requests
import pandas as pd
import json

datas = pd.read_excel('python2411爬虫网站.xlsx', sheet_name='python2411爬虫网站')

students = {}
# try:
for name, num, data_url in zip(datas['姓名'], datas['编号'], datas['仓库地址']):
    if isinstance(data_url,str):
        name = name.strip()
        owner = data_url.split('/')[-2]
        repo = data_url.split('/')[-1].split('.')[0]
        students[name] = {
            'sha': 'master',
            'id': int(num),
            'owner': owner,
            'repo': repo
        }

print(students)
for student,datas in students:
    gitee_events_url = 'https://gitee.com/api/v5/repos/{owner}/{repo}/events'
