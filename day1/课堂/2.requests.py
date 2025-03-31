import requests

"""1.get请求"""
# url = 'http://httpbin.org/get'
# res = requests.get(url)
# print(res.json())
# print('-------------------')
# res2 = requests.get(url)
# print(res2.text)
# print('-------------------')
# res2 = requests.get(url)
# print(res2.content.decode('utf-8'))

# url = 'https://www.baidu.com'
# response = requests.get(url)
# print(response.content.decode('utf-8'))

"""1.post请求"""
url = 'http://httpbin.org/post'
response = requests.post(url,data={
    'name':'zs',
    'psw': 123456
})
print(response.json())

url = 'http://httpbin.org/post'
response2 = requests.post(url,json={'name':'zs',"pswd":"<PASSWORD>"})
print(response2.json())