import scrapy
from scrapy.crawler import CrawlerProcess

class QuotesSpider(scrapy.Spider):
    name = 'authors'

    custom_settings = {"FEED_FORMAT": "json", "FEED_URI": "json_files/quotes.json"}

    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        for quote in response.xpath("/html//div[@class='quote']"):
            yield {
                "tags": quote.xpath("div[@class='tags']/a/text()").extract(),
                "author": quote.xpath("span/small/text()").get(),
                "quote": quote.xpath("span[@class='text']/text()").get()
            }
        
        next_link = response.xpath("//li[@class='next']/a/@href").get()

        if next_link:
            yield scrapy.Request(url=self.start_urls[0] + next_link)
            
# run spider
process = CrawlerProcess()
process.crawl(QuotesSpider)
process.start()