import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0",
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "zh-CN,zh;q=0.9"
}
# 使用测试版API密钥，实际应用中应替换为自己申请的有效密钥
api_key = "0df993c66c0c636e29ecbb5344252a4a"
url = f'http://api.douban.com/v2/movie/top250?apikey={api_key}'
response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"请求失败，状态码: {response.status_code}，错误信息: {response.text}")