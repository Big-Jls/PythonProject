from typing import Iterable
import scrapy
from scrapy import Request


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    # allowed_domains = ["quotes.com"]
    # start_urls = ["https://quotes.com"]

    def start_requests(self):
        url = 'https://quotes.toscrape.com/page/1/'
        yield scrapy.Request(url)

    def parse(self, response):
        quotes = response.xpath('//div[@class="quote"]')
        for quote in quotes:
            # print(quote)
            title = quote.xpath('./span[@class="text"]/text()').extract_first()
            author = quote.xpath('./small[@class="author"]/text()').extract_first()
            tags = quote.xpath('./div[@class="tags"]/a/text()').extract()
            data = {
                'title': title,
                'author': author,
                'tags': tags
            }
            print(data)
            yield {
                'title': title,
                'author': author,
                'tags': tags
            }
        next_page_url = response.xpath('//li[@class="next"]/a/@href').extract_first()
        if next_page_url:
            yield response.follow(next_page_url, callback=self.parse)