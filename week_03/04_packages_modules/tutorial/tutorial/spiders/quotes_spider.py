import scrapy


# class QuotesSpider(scrapy.Spider):
#     name = "quotes"
#
#     def start_requests(self):
#         urls = [
#             'http://quotes.toscrape.com/page/1/',
#         ]
#         for url in urls:
#             yield scrapy.Request(url=url, callback=self.parse)
#
#
#     # def parse(self, response):
#     #     page = response.url.split("/")[-2]
#     #     filename = 'quotes.txt'
#     #     quotes = {}
#     #
#     #     for quote in response.css('div.quote'):
#     #         with open(filename, 'a+') as f:
#     #             f.write(quote.css('span.text::text').get())
#     #             f.write(" - ")
#     #             f.write(quote.css('small.author::text').get())
#     #             f.write(" | ")
#     #             tag = ", ".join([str(x) for x in quote.css("div.tags a.tag::text").getall()])
#     #             f.write(tag)
#     #             f.write("\n")
#     #
#     #
#     #     next_page = response.css('li.next a::attr(href)').get()
#     #     if next_page is not None:
#     #         next_page = response.urljoin(next_page)
#     #         yield scrapy.Request(next_page, callback=self.parse)


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall(),
            }

        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)




