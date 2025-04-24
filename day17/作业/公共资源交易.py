import time
import execjs
import requests
import hashlib
headers={
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36 Edg/135.0.0.0'
}

tmp = int(time.time() * 1000)
content_json = {
  "AREACODE": "",
  "BeginTime": "2024-10-24 00:00:00",
  "EndTime": "2025-04-24 23:59:59",
  "GGTYPE": "1",
  "KIND": "GCJS",
  "M_PROJECT_TYPE": "",
  "PROTYPE": "",
  "createTime": "",
  "pageNo": "1",
  "pageSize": "20",
  "timeType": "6",
  "total": "2810",
  "ts": f"{tmp}"
}

with open('test.js', 'r', encoding='utf-8') as jsfile:
  js = jsfile.read()
  exe = execjs.compile(js)
  r = exe.call('get_sign',content_json)
  md5_hash = hashlib.md5()
  md5_hash.update(r.encode('utf-8'))
  sig_result = md5_hash.hexdigest()
  # print(sig_result)

url = 'https://ggzyfw.fujian.gov.cn/FwPortalApi/Trade/TradeInfo'
# session = requests.Session()

headers.update({'Portal-Sign':f'{sig_result}'})
print(headers)
response = requests.post(url, headers=headers, json=content_json)
datas = response.json()['Data']
result = exe.call('get_dats', datas)
print(result)
