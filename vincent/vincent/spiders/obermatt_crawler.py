import scrapy

from .obermatt import Obermatt


class ObermattCrawler(scrapy.Spider):
    name = 'obermatt-crawler'
    input_strings = [
        "SWX:ADEN",
        "DE:SZG",
        "SWX:SRCG",
        "SET:CPF",
        "SET:BA",
        "LSE:GLEN"
    ]

    # we use this index to keep track of what input strings we have
    # alredy searched
    input_index = 0
    start_urls = [
        f'https://www.google.com/search?q={input_strings[input_index]}+!site:obermatt.com'
    ]

    def parse(self, response):
        url = response.css(
            'a::attr(href)'
        ).re_first(r'q=(https://www\.obermatt\.com\/.+\/stock-research.html)')

        search_code = self.input_strings[self.input_index]
        obermattSpider = Obermatt(search_code)
        yield response.follow(url, obermattSpider.parse)

        # Crawl the other inputs
        self.input_index += 1
        if self.input_index == len(self.input_strings):
            # We are done crawling
            return

        yield response.follow(
            f'https://www.google.com/search?q={self.input_strings[self.input_index]}+!site:obermatt.com'
        )
