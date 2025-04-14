import scrapy


class QidianSpider(scrapy.Spider):
    name = "qidian"
    # allowed_domains = ["qidian.com"]
    # start_urls = ["https://qidian.com"]

    def start_requests(self):
        url = "https://www.qidian.com/finish/"
        yield scrapy.Request(url=url)

    def parse(self, response):
        response.xpath('//')
