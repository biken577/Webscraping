import scrapy


class BooksSpider(scrapy.Spider):
    name = 'books'
    allowed_domains = ['dallas.craigslist.org']
    start_urls = ['https://dallas.craigslist.org/search/bka']

    def parse(self, response):
        books=response.xpath('//*[@class="result-info"]')
        for book in books:
            Name=book.xpath('.//*[@class="result-heading"]/a/text()').extract_first()
            Price=book.xpath('.//*[@class="result-price"]/text()').extract_first()

            yield {"Name": Name, "Price": Price}

        next_page_url=response.xpath('//*[@title="next page"]/@href').extract_first()
        absolute_next_page_url=response.urljoin(next_page_url)
        yield scrapy.Request(absolute_next_page_url)