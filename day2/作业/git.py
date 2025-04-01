import requests
import pandas as pd
import json
import time

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

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 '
                  'Safari/537.36 Edg/134.0.0.0'
}
try:
    for key in students.keys():
        gitee_events_url = ('https://gitee.com/api/v5/repos/{owner}/{'
                            'repo}/events?access_token=d17034ca6efd435626f18e8dd770db33&limit=20').format(**students[
            key])
        response = requests.get(gitee_events_url, headers=headers)
        json_datas = response.json()
        print(f'学生{key}总共有{len(json_datas)}次提交，终端仅显示最近5次，后续请见./git学生对应json文件')
        if len(json_datas) > 5:
            for i in range(5):
                data = {
                    'time': json_datas[i]['created_at'],
                    'type': json_datas[i]['type'],
                    'payload': json_datas[i]['payload']
                }
                print(data)
        else:
            for i in range(len(json_datas)):
                data = {
                    'time': json_datas[i]['created_at'],
                    'type': json_datas[i]['type'],
                    'payload': json_datas[i]['payload']
                }
                print(data)
        with open(f'./git/{key}.json', 'w', encoding='utf-8') as json1:
            json.dump(json_datas, json1, indent=4, ensure_ascii=False)
        time.sleep(0.5)
except Exception as e:
    print(e)