import scrapy
class QuotesSpider(scrapy.Spider):
    name = "quotes"
    # allowed_domains = ["quotes.com"]
    # start_urls = ["https://quotes.com"]

    def start_requests(self):
        url = "https://quotes.toscrape.com/page/1"
        yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        quotes = response.css('div.quote')
        for quote in quotes:
            content = quote.css('.text::text').extract_first()
            author = quote.css('.author::text').extract_first()
            tags = quote.css('.tags .tag::text').extract()

            yield {
                'content': content,
                'author': author,
                'tags': tags
            }

        next_page_url = response.css('.next>a::attr("href")').extract_first()
        if next_page_url:
            yield response.follow(next_page_url)
