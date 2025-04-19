import hashlib
import execjs
import requests
import json

payload = {
    "sort": 1,
    "start": 20,
    "limit": 20
}
_keyStr = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
_p = "W5D80NFZHAYB8EUI2T649RT2MNRMVE2O"

with open('data.js', 'r', encoding='utf-8') as jsfile:
    jsfile_str = jsfile.read()
    jsfile_str = execjs.compile(jsfile_str)
    payload = jsfile_str.call('get_payload', payload)
    sig = hashlib.md5(f'{payload}{_p}'.encode()).hexdigest()
    request_json = {
        'payload': payload,
        'sig': sig,
        'v': 1
    }
    response = requests.post("https://www.xiniudata.com/api2/service/x_service/person_industry_list/list_industries_by_sort", json=request_json)
    decode_datas = response.json()
    # decode_datas_str = json.dumps(decode_datas)
    encode_datas = jsfile_str.call('get_datas', decode_datas['d'])
    # encode_datas = json.loads(encode_datas)
    print(encode_datas)
    for item in encode_datas['list']:
        print(item)