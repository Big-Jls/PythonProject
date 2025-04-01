import requests

# url = 'https://api.zzzmh.cn/v2/bz/v3/getUrl/37aa5dc36d88444786b6b543845963ba21'
#
# r = requests.get(url,allow_redirects=False)
# if r.status_code == 302:
#     res_url = r.headers['Location']
#     res = requests.get(res_url)
#     with open('res.jpg', 'wb') as f:
#         f.write(res.content)

"""Cookies"""

"""第一种方法"""
# url = 'https://vip.hdbz.net/auth/ajaxlogin'
# favorite_url = 'https://vip.hdbz.net/site/FavoriteList?page=1&limit=10'
# data = {
#     "username": "15138001200",
#     "userpwd": "pckzzy101"
# }
# response = requests.post(url, data=data)
# res = requests.get(favorite_url,cookies=response.cookies)
# print(res.json())

"""第二种"""
# url = 'https://vip.hdbz.net/auth/ajaxlogin'
# favorite_url = 'https://vip.hdbz.net/site/FavoriteList?page=1&limit=10'
# data = {
#     "username": "15138001200",
#     "userpwd": "pckzzy101"
# }
# res = requests.post(url, data=data)
# cookies = {
#     "uid": res.cookies.get("uid"),
#     "uname": res.cookies.get("uname"),
#     "unotify": res.cookies.get("unotify"),
# }
#
# res = requests.get(favorite_url,cookies=cookies)
# print(res.json())

"""第三种直接粘贴到headers，有效期看网页而定"""

"""Session"""
url = 'https://vip.hdbz.net/auth/ajaxlogin'
favorite_url = 'https://vip.hdbz.net/site/FavoriteList?page=1&limit=10'
session = requests.Session()
data = {
    "username": "15138001200",
    "userpwd": "pckzzy101"
}
res = session.request(url=url, data=data, method='post')
print(res.cookies)
res1 = session.request(url = favorite_url, method='get')
print(res1.json())