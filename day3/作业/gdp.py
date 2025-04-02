import json
import csv
import requests

base_url = (
    'https://datacenter-web.eastmoney.com/api/data/v1/get?callback=datatable3892859&columns=REPORT_DATE%2CTIME'
    '%2CDOMESTICL_PRODUCT_BASE%2CFIRST_PRODUCT_BASE%2CSECOND_PRODUCT_BASE%2CTHIRD_PRODUCT_BASE%2CSUM_SAME'
    '%2CFIRST_SAME%2CSECOND_SAME%2CTHIRD_SAME&pageSize=20&sortColumns=REPORT_DATE&sortTypes=-1&source'
    '=WEB&client=WEB&reportName=RPT_ECONOMY_GDP&p=2&pageNo=2&pageNum=2&_=1743597038982'
)

with open('gdp.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['REPORT_DATE', 'TIME', 'DOMESTICL_PRODUCT_BASE', 'FIRST_PRODUCT_BASE', 'SECOND_PRODUCT_BASE',
                  'THIRD_PRODUCT_BASE', 'SUM_SAME', 'FIRST_SAME', 'SECOND_SAME', 'THIRD_SAME']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for i in range(1, 5):
        url = f'{base_url}&pageNumber={i}'
        response = requests.get(url)
        text = response.text[17:-2]
        data = json.loads(text)
        if data.get('success'):
            for item in data['result']['data']:
                writer.writerow(item)