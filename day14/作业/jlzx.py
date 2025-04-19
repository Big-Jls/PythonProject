from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

# 指定 ChromeDriver 的路径
driver_path = 'C:\Program Files (x86)\chromedriver-win64\chromedriver.exe'
service = Service(driver_path)

# 创建 Chrome 浏览器实例
driver = webdriver.Chrome(service=service)
try:
    # 最大化窗口
    driver.maximize_window()
    # 打开指定网页
    driver.get("https://www.cninfo.com.cn/new/commonUrl/pageOfSearch?url=disclosure/list/search")
    # 设置隐式等待时间
    driver.implicitly_wait(10)
    # 查找所有符合条件的 tr 元素
    trs = driver.find_elements(By.XPATH, '//tr[@class="el-table__row"]')
    for tr in trs:
        try:
            # 查找 tr 元素下的所有 td 元素
            tds = tr.find_elements(By.CSS_SELECTOR, 'td')
            _id = tds[0].text.strip()
            name = tds[1].text.strip()
            title = tds[2].text.strip()
            file = tds[2]
            time = tds[3].text.strip()
            # 点击文件链接
            file.click()
            # 查找按钮元素并点击
            button = driver.find_element(By.XPATH, '//i[contains(@class,"iconfont")]')
            print(button)
            button.click()
            break
        except NoSuchElementException as e:
            print(f"元素未找到: {e}")
except Exception as e:
    print(f"发生错误: {e}")
finally:
    # 关闭浏览器
    driver.close()