import re
import json
import requests

url = 'https://data.eastmoney.com/cjsj/gdp.html'
for i in range(1, 5):
    gdp = (
        'https://datacenter-web.eastmoney.com/api/data/v1/get?callback=datatable3892859&columns=REPORT_DATE%2CTIME'
        '%2CDOMESTICL_PRODUCT_BASE%2CFIRST_PRODUCT_BASE%2CSECOND_PRODUCT_BASE%2CTHIRD_PRODUCT_BASE%2CSUM_SAME'
        f'%2CFIRST_SAME%2CSECOND_SAME%2CTHIRD_SAME&pageNumber={i}&pageSize=20&sortColumns=REPORT_DATE&sortTypes=-1&source'
        '=WEB&client=WEB&reportName=RPT_ECONOMY_GDP&p=2&pageNo=2&pageNum=2&_=1743597038982')
    response = requests.get(gdp)
    text = response.text
    datas_json = json.dumps(text[17:-2])
    print(datas_json)
