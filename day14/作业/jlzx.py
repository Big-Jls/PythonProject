from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

driver_path = 'C:\\Program Files (x86)\\chromedriver-win64\\chromedriver.exe'
service = Service(driver_path)

driver = webdriver.Chrome(service=service)
try:

    driver.maximize_window()

    driver.get("https://www.cninfo.com.cn/new/commonUrl/pageOfSearch?url=disclosure/list/search")

    driver.implicitly_wait(10)

    trs = driver.find_elements(By.XPATH, '//tr[@class="el-table__row"]')
    for tr in trs:
        try:

            tds = tr.find_elements(By.XPATH, './td')
            print(tds)
            _id = tds[0].text.strip()
            name = tds[1].text.strip()
            title = tds[2].text.strip()
            file = tds[2].find_element(By.XPATH,'.//a')
            time = tds[3].text.strip()
            file.click()
            driver.switch_to.window((driver.window_handles[-1]))
            button = driver.find_element(By.XPATH, '//i[contains(@class,"iconfont")]')

            page_source = driver.page_source

            # 打印网页源代码
            print(page_source)
            # print(button)
            button.click()
            break
        except NoSuchElementException as e:
            print(f"元素未找到: {e}")
except Exception as e:
    print(f"发生错误: {e}")
finally:

    driver.close()
