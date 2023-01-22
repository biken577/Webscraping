import scrapy


class CitiesSpider(scrapy.Spider):
    name = 'cities'
    allowed_domains = ['en.wikipedia.org']
    start_urls = ['https://en.wikipedia.org/wiki/List_of_United_States_cities_by_population']

    def parse(self, response):
        table=response.xpath('//table')[4]
        trs=table.xpath('.//tr')[1:]

        for tr in trs:
            city=tr.xpath('.//td')[0].xpath('.//a/text()').extract_first()
            state=tr.xpath('.//td')[1].xpath('.//a/text()').extract_first()
            #2020_popn=tr.xpath('.//td')[2].xpath('.//text()').extract_first().strip()
            #2010_popn=tr.xpath('.//td')[3].xpath('.//text()').extract_first().strip()
            change=tr.xpath('.//td')[4].xpath('.//span/text()').extract_first()
            
            yield{
            "City":city,
            "State":state,
            #"2020_popn":2020_popn,
            #"2010_popn":2010_popn,
            "change":change}
