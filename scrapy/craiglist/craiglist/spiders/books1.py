import scrapy
from scrapy import Request

class BooksSpider(scrapy.Spider):
    name = 'books'
    allowed_domains = ['dallas.craigslist.org']
    start_urls = ['https://dallas.craigslist.org/search/bka']

    def parse(self, response):
        books=response.xpath('//*[@class="result-info"]')
        for book in books:
            Name=book.xpath('.//*[@class="result-heading"]/a/text()').extract_first()
            Price=book.xpath('.//*[@class="result-price"]/text()').extract_first()
            Link= book.xpath('//*[@class="result-heading"]/a/@href').extract_first()
            yield scrapy.Request(Link,callback=self.parse_listing,
                                meta={"Name": Name, "Price": Price})
            

        next_page_url=response.xpath('//*[@title="next page"]/@href').extract_first()
        absolute_next_page_url=response.urljoin(next_page_url)
        yield scrapy.Request(absolute_next_page_url,callback=self.parse)

    def parse_listing(self,response):
        Name=reponse.meta['Name']
        Price=response.meta['Price']

        address=response.xpath('//*[@class="mapaddress"]/text()').extract_first()
        description=response.xpath('//*[@id="postingbody"]//text()').extract()

        images=response.xpath('//*[@class="thumb"]//@src').extract()
        images=[image.replace("50x50c","600x450")for image in images]

        yield{'Name':Name,
                'Price':Price,
                "Address":address,
                "Description":description,
                "Images":images}