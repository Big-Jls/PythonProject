from DrissionPage import ChromiumPage
import requests
import execjs
# tab = ChromiumPage().latest_tab
# tab.listen.start('wyiosapi.qimingpian.cn/web/webSiteCaNews')
#
data = {
    'page': 1,
    'num': 20,
    'type': '榜单'
}
# tab.post('https://wyiosapi.qimingpian.cn/web/webSiteCaNews', data=data)
# res = tab.listen.wait()
# print(res.response.body)

response = requests.post('https://wyiosapi.qimingpian.cn/web/webSiteCaNews', data=data)
print(response.text)