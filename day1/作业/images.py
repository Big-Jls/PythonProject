import requests
import time

getData_url = 'https://api.zzzmh.cn/v2/bz/v3/getData'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0",
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Referer": "https://bz.zzzmh.cn/index",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive"
}
json_data = {
    "size": 24,
    "current": 1,
    "sort": 0,
    "category": 0,
    "resolution": 0,
    "color": 0,
    "categoryId": 0,
    "ratio": 0
}

# 发送 POST 请求获取图片列表数据
response = requests.post(getData_url, headers=headers, json=json_data)

# 检查响应状态码
if response.status_code == 200:
    try:
        img_list = response.json()['data']['list']
        for img_info in img_list:
            img_id = img_info['i']
            img_url = f'https://api.zzzmh.cn/v2/bz/v3/getUrl/{img_id}'

            # 发送 GET 请求
            response = requests.get(img_url, headers=headers)

            # 检查响应状态码
            if response.status_code == 200:
                try:
                    print(response.json())
                except requests.exceptions.JSONDecodeError:
                    print(f"获取图片 URL 的响应内容不是有效的 JSON 格式: {response.content.decode('utf-8')}")
            elif response.status_code == 403:
                print(
                    f"获取图片 URL 请求被禁止，状态码: {response.status_code}，响应内容: {response.content.decode('utf-8')}")
                # 可以在这里添加更换IP或者等待一段时间的逻辑
                time.sleep(5)  # 等待5秒后再继续
            else:
                print(
                    f"获取图片 URL 请求失败，状态码: {response.status_code}，响应内容: {response.content.decode('utf-8')}")
    except requests.exceptions.JSONDecodeError:
        print(f"获取图片列表的响应内容不是有效的 JSON 格式: {response.content.decode('utf-8')}")
else:
    print(f"请求失败，状态码: {response.status_code}，响应内容: {response.content.decode('utf-8')}")
