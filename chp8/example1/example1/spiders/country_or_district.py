import scrapy


class CountryOrDistrictSpider(scrapy.Spider):
    name = 'country_or_district'
    allowed_domains = ['example.python-scraping.com']
    start_urls = ['http://example.python-scraping.com/']

    def parse(self, response):
        pass
class CountryOrDistrictSpider(Crawl.Spider):
    name = 'country_or_district'
    allowed_domains = ['example.python-scraping.com']
    start_urls = ['http://example.python-scraping.com']
    rules = (
        Rule(LinkExtractor(allow=r'Items/'), callback='parse_item',follow=True),
    )