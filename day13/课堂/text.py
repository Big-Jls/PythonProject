import time
from selenium import webdriver
from selenium.webdriver.common.by import By

webdriver = webdriver.Chrome()
webdriver.maximize_window()
webdriver.get("https://quotes.toscrape.com/")
# time.sleep(1)
# login_entry = webdriver.find_element(By.XPATH,'//a[@href="/login"]')
# login_entry.click()
# time.sleep(1)
# username_input = webdriver.find_element(By.ID, 'username')
# username_input.send_keys("admin")
# password_input = webdriver.find_element(By.ID, 'password')
# password_input.send_keys('123456')
# time.sleep(1)
# submit_button = webdriver.find_element(By.CSS_SELECTOR, '.container>form>input[type="submit"]')
# submit_button.click()
# time.sleep(5)
datas = []
num = 0
while True:
    quotes = webdriver.find_elements(By.XPATH, "//div[@class='quote']")
    for quote in quotes:
        num += 1
        content = quote.find_element(By.XPATH, './span[@class="text"]').text
        author = quote.find_element(By.XPATH, './span/small[@class="author"]').text
        tags = quote.find_elements(By.XPATH, './div/a[@class="tag"]')
        quote_data = {
            'num': num,
            "content": content,
            "author": author,
            "tags": [tag.text for tag in tags]
        }
        # print(quote_data)
        datas.append(quote_data)
        # print(content.text)
    try:
        next_button = webdriver.find_element(By.XPATH, '//li[@class="next"]/a')
        next_button.click()
    except Exception as e:
        print(datas)
        break
webdriver.quit()


