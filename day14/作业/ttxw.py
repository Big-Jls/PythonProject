# import requests
# from bs4 import BeautifulSoup
# from fake_useragent import UserAgent
# import time
#
# t = time.time()
# t = int(t * 1000)
# ua = UserAgent(os='Windows')
#
# headers = {
#     'User-Agent': ua.random,
#     'referer':'https://www.pingxiang.gov.cn/col/col15/index.html?uid=127&pageNum=1',
#     'origin':'https://www.pingxiang.gov.cn',
#     'content-type': 'application/json',
#     'cookie':'FW9uCWqlVzC22m1KfCMCjfvFHpRMsgt=6dbbe219-f756-4000-be3d-45a3c67234e0; dGg2aCfMMK97Ro270mqBFu5qjC8TQbL2opnHvbEpM=Tifz8hd5p4O3AB%2BivrbJpEo1POesm6WwmcI7FwTxxKk%3D; dGg2aCfMMK97Ro270mqBFu5qjC8TQbL2opnHvbEpM=Tifz8hd5p4O3AB%2BivrbJpEo1POesm6WwmcI7FwTxxKk%3D; FW9uCWqlVzC22m1KfCMCjfvFHpRMsgt=6dbbe219-f756-4000-be3d-45a3c67234e0'
# }
# url = f'https://www.pingxiang.gov.cn/col/col15/index.html?uid=127&pageNum=1'
# response = requests.post(url, headers=headers)
# html = response.text
# print(html)
# 'https://www.pingxiang.gov.cn/1ywuKELSO2ahQuWZ/pr/Tifz8hd5p4O3AB%2BivrbJpBxnx5tQ3zLV%2BrLmeksvPKs%3D/ws/aknjj2csj7/a2b24147-d0ba-4ba5-b4c7-97d80ff7411f/384/3pellgim/xhr_send?t=1745028528808'
import random
import time

# selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By




options = Options()
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36 Edg/135.0.0.0")
options.add_argument('--disable-blink-features=AutomationControlled')

driver_path = 'C:\\Program Files (x86)\\chromedriver-win64\\chromedriver.exe'
service = Service(driver_path)
driver = webdriver.Chrome(service=service, options=options)
# driver.maximize_window()
driver.get('https://www.pingxiang.gov.cn/col/col15/index.html?uid=127&pageNum=1')

# 修改 window.navigator.webdriver 属性
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
time.sleep(random.uniform(5, 8))

# print(driver.page_source)
default_pgContainer = driver.find_element(By.XPATH, '//div[@class="default_pgContainer "]')
li = default_pgContainer.find_element(By.XPATH, './/li[1]')
a = li.find_element(By.CSS_SELECTOR, 'a')
# date = li.find_element(By.CSS_SELECTOR, '.bt-data-time ')
# print(f'《{a.get_attribute('title')}》------{date.get_attribute('title').strip()}')
a.click()
time.sleep(random.uniform(6, 12))

while True:
    title_div = driver.find_element(By.XPATH, '//div[@class="zw_title "]')
    title = title_div.find_element(By.XPATH, './p')
    date = title_div.find_element(By.XPATH, './span[1]')
    print(f'《{title.text}》------{date.text}')
    # print(driver.page_source)
    ps = driver.find_elements(By.XPATH, '//div[@id="zoom"]/p[@style="text-align: left; text-indent: 2em;"]')
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    for p in ps:
        print(p.text)
    print('-------------------------------------------------')
    time.sleep(random.uniform(6, 12))

    try:
        next_div = driver.find_element(By.XPATH, '//div[@class="sxwz "]')
        next_href = next_div.find_element(By.XPATH, './p[2]/a')
        next_href.click()
        time.sleep(random.uniform(6, 12))
    except Exception as e:
        print(e)
        break
