import json
import time
from urllib.parse import urlencode

import scrapy


class DfzSpider(scrapy.Spider):
    name = "dfz"
    # allowed_domains = ["dfz.com"]
    # start_urls = ["https://dfz.com"]

    def start_requests(self):
        timeStamp = int(time.time() * 1000)
        params_list = [{
            'timeStamp': timeStamp,
            'dataType': 'ZQFXLISTBYAD',
            'adCode': '87',
            'page': f'{i}',
            'pageSize': 10
        } for i in range(1, 5)]
        url = 'https://www.governbond.org.cn:4443/api/loadBondData.action'
        for params in params_list:
            # 将参数拼接到 URL 上
            full_url = url + '?' + urlencode(params)
            yield scrapy.Request(url=full_url, callback=self.parse)

    def detail_request(self, ZQ_CODE, AD_CODE):
        url = 'https://www.celma.org.cn/zqgkxq/index.jhtml'
        params = {
            'pcCode': ZQ_CODE,
            'adCode': AD_CODE
        }
        full_url = url + '?' + urlencode(params)
        return scrapy.Request(url=full_url, callback=self.detail_parse)

    def file_request(self,a):
        full_url = a
        return scrapy.Request(url=full_url, callback=self.file_parse)

    def download_file(self, a):
        full_url = a
        return scrapy.Request(url=full_url, callback=self.download_parse)

    def parse(self, response):
        # print(response.text)
        json_data = json.loads(response.text)
        datas = json_data['data']
        for data in datas:
            ZQ_CODE = data['ZQ_CODE']
            AD_CODE = data['AD_CODE']
            # print(ZQ_CODE, AD_CODE)
            yield self.detail_request(ZQ_CODE, AD_CODE)


    def detail_parse(self, response):
        # print(response.text)
        divs = response.xpath('//div[@class="col-md-11"]')
        # print(divs)
        for div in divs:
            a_s = div.xpath('./a/@href').extract()
            for a in a_s:
                yield self.file_request(a)

    def file_parse(self, response):
        content_fjs = response.xpath('//div[@class="content-fj"]')
        # print(content_fj)
        for content_fj in content_fjs:
            # print(content_fj.extract())
            a_s = content_fj.xpath('.//a/@href')
            # print(a_s)
            for a in a_s:
                # print(a)
                yield self.download_file(a.extract())

    def download_parse(self, response):
        yield {
            'content': response.body,
            'url': response.url
        }