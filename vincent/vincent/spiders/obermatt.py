import scrapy
from datetime import datetime

from vincent.items import Stock


class Obermatt(scrapy.Spider):
    name = 'obermatt-spider'
    start_urls = [
        # 'https://www.obermatt.com/en/stocks/adecco-aden-vx/stock-research.html'
        # 'https://www.obermatt.com/en/stocks/salzgitter-szg-ff/stock-research.html'
        'https://www.obermatt.com/en/stocks/sunrise-communications-group-swx-srcg/stock-research.html'
    ]

    def __init__(self, search_code):
        self.search_code = search_code

    def parse(self, response):
        stock = Stock()
        stock['name'] = response.css(
            '.company_summary meta[itemprop="name"]::attr(content)'
        ).extract_first()
        stock['search_code'] = self.search_code
        stock['scraping_date_time'] = str(datetime.now())
        stock['rating'] = self._extract_rating(response)

        tableData = self._extract_table(response)

        stock['value_rank'] = tableData['Value Rank']
        stock['growth_rank'] = tableData['Growth Rank']
        stock['safety_rank'] = tableData['Safety Rank']
        stock['combined_rank'] = tableData['Combined Rank']

        yield stock

    def _extract_rating(self, response):
        ratingRegex = r'have a (.+) rating'
        rating = response.css(
            '.company_summary div[itemprop="review"] p[itemprop="reviewBody"]'
        ).xpath('normalize-space()').re_first(ratingRegex)

        return rating

    def _extract_table(self, response):
        tableData = {}
        tableRows = response.css('table.stock.summary tr')

        for row in tableRows:
            ratingName = row.css('td.name_summary').xpath(
                'normalize-space()'
            ).extract_first()
            ratingValue = row.css(
                'td.summary_value_no_link'
            ).xpath('normalize-space()').extract_first()

            if ratingName and ratingValue:
                try:
                    tableData[ratingName] = float(ratingValue)
                except ValueError:
                    pass

        return tableData
