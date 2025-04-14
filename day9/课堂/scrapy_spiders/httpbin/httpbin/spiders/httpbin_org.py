import random
import scrapy



class HttpbinOrgSpider(scrapy.Spider):
    name = "httpbin"
    # allowed_domains = ["httpbin.org"]
    start_urls = [f"https://httpbin.org/get?age={random.randint(1,10)}" for age in range(10)]

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url)


    def parse(self, response):
        print(response.text)
