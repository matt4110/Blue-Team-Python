import scrapy

class DescriptionSpider(scrapy.Spider):
    name = 'description'
    start_urls = ['https://letsdefend.io']

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url)

    def parse(self, response):
        description = response.xpath('//meta[@name="description"]/@content').get()
        print("Description: ", description)