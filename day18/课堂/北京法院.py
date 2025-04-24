import time
import ddddocr
import requests
from fake_useragent import UserAgent
ocr = ddddocr.DdddOcr(show_ad=False)
ua = UserAgent(os='Windows')
headers = {
    'User-Agent': ua.random
}
session = requests.Session()
page = 1
while page < 20:
    url = f'https://www.bjcourt.gov.cn/zxxx/indexOld.htm?st=1&zxxxlx=100013007&bzxrlx=&bzxrxm=&zrr=&frhqtzz=&jbfyId=&ah=&dqxh=26&page={page}'
    response = session.get(url, headers=headers)
    if '验证码' in response.text:
        print("开始破解验证码  ......")
        img_res = session.get("https://www.bjcourt.gov.cn/yzm.jpg?n=0", headers=headers)
        code = ocr.classification(img_res.content)
        print(f"原始code {code}  ")
        code = code[-5:]
        print(f"处理code {code}  ")
        with open(f"./codes/bjfy_{code}.png", "wb") as f:
            f.write(img_res.content)

        post_res = session.post("https://www.bjcourt.gov.cn/cpws/checkkaptcha.htm", data={
            "yzm": f"{code}"
        }, headers=headers)
        print(post_res.status_code)
        if post_res.status_code == 200:
            pass
        else:
            break
    else:
        print(f'{page}页不用处理验证码')
    page += 1
    time.sleep(1)