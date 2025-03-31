from urllib import request
from urllib import parse
import json
"""1.urllib请求工具"""
# url = 'http://httpbin.org/get'
# response = request.urlopen(url)
# # 获得字节流http对象
# content_bytes = response.read()
# # print(content_bytes)
# # 字节流转换成utf-8的字符串格式
# content_str = content_bytes.decode('utf-8')
# # print(content_str)
# # 字符串转json
# content_json = json.loads(content_str)
# # print(content_json)


# url = 'http://httpbin.org/get?name=user&password=123456'
# response = request.urlopen(url)
# content_bytes = response.read()
# content_str = content_bytes.decode('utf-8')
# content_json = json.loads(content_str)
# print(content_json)
# print(content_json['headers']['User-Agent'])

"""2.get请求"""
# header = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 '
#                   'Safari/537.36 Edg/134.0.0.0'
# }
#
# data = parse.urlencode({
#     "name":"张三",
#     "password":"<PASSWORD>"
# })
# url = f'http://httpbin.org/get?{data}'
# # print(url)
# req = request.Request(url, headers=header)
# # 请求头
# print(req.headers)
# print('==='*30)
# res = request.urlopen(req)
# # 响应头
# print(res.headers)
# # 响应数据
# print(res.read().decode('utf-8'))

"""3.post请求 """
# header = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 '
#                   'Safari/537.36 Edg/134.0.0.0'
# }
#
# data = parse.urlencode({
#     "name":"张三",
#     "password":"<PASSWORD>"
# }).encode()
# url = 'http://httpbin.org/post'
# # print(url)
# req = request.Request(url, headers=header, method='POST', data=data)
# # 请求头
# print(req.headers)
# print('==='*30)
# res = request.urlopen(req)
# # 响应头
# print(res.headers)
# # 响应数据
# print(res.read().decode('utf-8'))