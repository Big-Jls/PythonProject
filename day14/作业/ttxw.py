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
# url = f'https://www.pingxiang.gov.cn/1ywuKELSO2ahQuWZ/pr/Tifz8hd5p4O3AB%2BivrbJpEo1POesm6WwmcI7FwTxxKk%3D/ws/20paaenj0b/6dbbe219-f756-4000-be3d-45a3c67234e0/717/pp2nhdak/xhr_streaming?t={t}'
# response = requests.post(url, headers=headers)
# html = response.text
# print(html)
# # 'https://www.pingxiang.gov.cn/1ywuKELSO2ahQuWZ/pr/Tifz8hd5p4O3AB%2BivrbJpBxnx5tQ3zLV%2BrLmeksvPKs%3D/ws/aknjj2csj7/a2b24147-d0ba-4ba5-b4c7-97d80ff7411f/384/3pellgim/xhr_send?t=1745028528808'

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
driver_path = 'C:\Program Files (x86)\chromedriver-win64\chromedriver.exe'
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.get('https://www.pingxiang.gov.cn/col/col15/index.html?uid=127&pageNum=3')
driver.find_elements()