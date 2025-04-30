# 文字点选
import json
import time
from selenium import webdriver
from DrissionPage import ChromiumPage
from day20.chaojiying_Python.chaojiying import Chaojiying_Client
import requests


def wenzi(url):
    # url = 'https://gt4.geetest.com/demov4/word-popup-zh.html'
    # url2 = 'https://gcaptcha4.geetest.com/load?captcha_id=54088bb07d2df3c46b79f80300b0abbe&challenge=da7c6756-1c00-486f-a727-a866362b1506&client_type=web&risk_type=word&lang=zho&callback=geetest_1745829414816'
    response = requests.get(url)
    with open(f'./imgs/{url.split("/")[-1]}', 'wb') as f:
        f.write(response.content)
    return response.content

def point(img_content):
    chaojiying = Chaojiying_Client('kjw1314', 'kjw20020311', '969575')  # 用户中心>>软件ID 生成一个替换 96001
    # im = open('a.jpg', 'rb').read()
    result = chaojiying.PostPic(img_content, 9004)
    # print chaojiying.PostPic(base64_str, 1902)  #此处为传入 base64代码
    pic_str = result['pic_str']
    points = []
    points_strs = pic_str.split('|')
    print(points_strs)
    for points_str in points_strs:
        x, y = points_str.split(',')
        points.append((int(x), int(y)))
    return points


def drissionpage_v():
    tab = ChromiumPage().latest_tab
    tab.get('https://gt4.geetest.com/demov4/word-popup-zh.html')
    # print(tab.html)
    time.sleep(3)
    geetest_btn_click = tab.ele('x=//div[@id="captcha"]')
    geetest_btn_click.click()
    time.sleep(3)
    geetest_bg = tab.ele('x=//div[contains(@class, "geetest_bg")]')
    url = geetest_bg.attrs.get('style')[23:-3]
    print(url)
    img_content = wenzi(url)
    points = point(img_content)
    for x, y in points:
        tab.actions.move_to(geetest_bg, x, y).click()
        time.sleep(1)
    geetest_submit_tips = tab.ele('x=//div[contains(@class, "geetest_submit_tips")]')
    geetest_submit_tips.click()


def selenium_v(img_content):
    driver = webdriver.Chrome()


if __name__ == '__main__':
    # img_content = wenzi()
    drissionpage_v()

