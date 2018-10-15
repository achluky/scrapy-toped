import scrapy


class Toped(scrapy.Spider):
    name = "toped"
    allowed_domains = ['tokopedia.com']
    def parse(self, response):
        yield {
                'title': response.xpath("//span[@itemprop='name']/text()").extract(),
                'price': response.xpath("//input[contains(@id,'product_price_int')]/@value").extract(),
                'description': response.xpath("//div[@id='info']").extract(),
                'image': response.css('div.content-img-relative img::attr(src)').extract()
        }

