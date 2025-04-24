import ddddocr
import base64
import requests
from DrissionPage import ChromiumPage

ocr = ddddocr.DdddOcr()
# tab = ChromiumPage().latest_tab
# url = 'https://www.bjcourt.gov.cn/yzm.jpg'
# tab.listen.start('https://www.bjcourt.gov.cn/yzm.jpg')
# tab.get('https://www.bjcourt.gov.cn/yzm.jpg')
# r = tab.listen.wait()
# # print(r.response.status)
# content = r.response.body
#
# # 确保 content 是 bytes 类型
# # if isinstance(content, str):
# byte_stream = base64.b64decode(content)
#
# result = ocr.classification(byte_stream)
# print(result)

with open('./code_images/yzm.jpg', 'rb') as rf:
    read = rf.read()
    result = ocr.classification(read)
    print(result)