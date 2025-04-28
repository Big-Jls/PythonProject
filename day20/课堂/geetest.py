# 文字点选
import json
from DrissionPage import ChromiumPage
from day20.chaojiying_Python.chaojiying import Chaojiying_Client
import requests


def wenzi():
    # url = 'https://gt4.geetest.com/demov4/word-popup-zh.html'
    url2 = 'https://gcaptcha4.geetest.com/load?captcha_id=54088bb07d2df3c46b79f80300b0abbe&challenge=da7c6756-1c00-486f-a727-a866362b1506&client_type=web&risk_type=word&lang=zho&callback=geetest_1745829414816'
    response = requests.get(url2)
    html = response.text
    json_data = json.loads(html[22:-1])
    img = json_data['data']['imgs']
    with open(f'./imgs/{img.split("/")[-1]}', 'wb') as f:
        b_response = requests.get(f'https://static.geetest.com/{img}')
        f.write(b_response.content)
    return b_response.content



if __name__ == '__main__':
    img_content = wenzi()
    chaojiying = Chaojiying_Client('kjw1314', 'kjw20020311', '969575')  # 用户中心>>软件ID 生成一个替换 96001
    # im = open('a.jpg', 'rb').read()
    result = chaojiying.PostPic(img_content, 9004)
    # print chaojiying.PostPic(base64_str, 1902)  #此处为传入 base64代码
    pic_str = result['pic_str']
    points = []
    points_strs = pic_str.split('|')
    for points_str in points_strs:
        x, y = points_str.split(',')
        points.append((int(x), int(y)))
    tab = ChromiumPage().latest_tab
