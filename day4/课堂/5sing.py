import requests

# 获取session,session不一致
# session_url = 'https://www.jamendo.com/Client/manifest.2040001655.json'
# response = requests.get(session_url)
# jammusicsession = dict(response.cookies).get('jammusicsession')
# print(jammusicsession)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0',
    'referer':'https://www.jamendo.com/start',
    'cookie':'jammusiclang=en; _ga=GA1.2.1882840065.1743664584; _gid=GA1.2.2117383487.1743664584; jamapplication=true; jamAcceptCookie=true; _hjSession_837371=eyJpZCI6Ijg3M2UyOGVkLTA1NjgtNDUwZi05NGNlLWI3Yjk4MTFiM2EzNiIsImMiOjE3NDM2NjQ2MTUxNjgsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MH0=; _hjSessionUser_837371=eyJpZCI6IjY5M2Q4MGY5LTFkODctNWQ0Mi1iM2M3LTIwZTBmYzZmY2NjNiIsImNyZWF0ZWQiOjE3NDM2NjQ2MTUxNjcsImV4aXN0aW5nIjp0cnVlfQ==; jammusicsession=s%3AONLW2Z8L1gSWRJekLymggAvW5Ykxmy1g.zVKJ6uGGEVKusL43r7qolLrkHuXMnq%2BmVHjyjN0y2Qs; jammusicconnection=9217964; connection=9217964; _ga_6XE4DBPD2H=GS1.2.1743664585.1.1.1743666024.8.0.0; _gat_UA-108987-19=1'
}
#
# login_url = 'https://www.jamendo.com/api/oauth/grant'
# json = {
#     "newsletterPreferences": [],
#     "username": "921447735@qq.com",
#     "password": "Kjw20020311?"
# }
# session = requests.Session()
# login_response = session.post(login_url, json=json, headers=headers, cookies=cookies)
# print(login_response.content.decode('utf-8'))

host_url = 'https://www.jamendo.com/api/charts/track?type[]=track&limit=100'
response = requests.get(host_url, headers=headers)
print(response.text)
music_d_url = 'https://prod-1.storage.jamendo.com/download/track/2016794/mp32/'
# response = requests.get(music_d_url, headers=headers, cookies=cookies)

