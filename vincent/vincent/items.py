# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class Stock(Item):
    name = Field()
    search_code = Field()
    scraping_date_time = Field()
    rating = Field()
    value_rank = Field()
    growth_rank = Field()
    safety_rank = Field()
    combined_rank = Field()
