import scrapy


class Bl(scrapy.Spider):
    name = "bl"
    allowed_domains = ['bukalapak.com']
    start_urls = [
        'https://www.bukalapak.com/p/fashion-pria/jam-tangan-171/1psev4-jual-jam-tangan-pria-dan-wanita-casio-mq-24-1b3-original',
    ]

    def parse(self, response):
        yield {
                'title': response.xpath("//h1[@class='c-product-detail__name']/text()").extract(),
                'price': response.xpath("//span[@class='c-product-detail-price__reduced'][@class='amount']/text()").extract(),
                'description': response.xpath("//div[@class='qa-pd-description']").extract(),
                # 'image': response.css('div.c-product-image-gallery__image js-product-image-gallery__image img::attr(src)').extract()
        }

