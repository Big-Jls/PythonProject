import time

from DrissionPage import Chromium

tab = Chromium().latest_tab
tab.get('https://bm.ruankao.org.cn/sign/in?type=query&s=query/score/main')
time.sleep(1)
a_button = tab.ele('x=//a[@class="change_login"]')
a_button.click()

id_input = tab.ele('x=//input[@placeholder="请输入证件号码"]')
id_input.input('410402200203115519')

password_input = tab.ele('x=//input[@placeholder="请输入密码"]')
password_input.input('')