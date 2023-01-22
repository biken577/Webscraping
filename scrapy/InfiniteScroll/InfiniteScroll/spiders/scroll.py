import scrapy

base_url='https://quotes.toscrape.com/api/quotes?page={}'
class ScrollSpider(scrapy.Spider):
    name = 'scroll'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['https://quotes.toscrape.com/api/quotes?page=1']

    

    def parse(self, response):
        data=response.json()
        for quote in data["quotes"]:
            author=quote['author']["name"]
            text=quote['text']
            tags=quote['tags']

            yield{'Author':author,
                    "text":text,
                    "tags":tags}

        current_page=data['page']
        if data["has_next"]:
            next_page_url=base_url.format(current_page+1)
            yield scrapy.Request(next_page_url)