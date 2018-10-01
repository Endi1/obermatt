# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem


class EvalPipeline(object):
    def process_item(self, item, spider):
        if not item['name']:
            errorMessage = "Missing name"
            self._dropSpider(errorMessage, item)

        if not item['rating']:
            errorMessage = "Missing rating"
            self._dropSpider(errorMessage, item)

        if not item['value_rank']:
            errorMessage = "Missing Value Rank"
            self._dropSpider(errorMessage, item)

        if not item['growth_rank']:
            errorMessage = "Missing Growth Rank"
            self._dropSpider(errorMessage, item)

        if not item['safety_rank']:
            errorMessage = "Missing Safety Rank"
            self._dropSpider(errorMessage, item)

        if not item['combined_rank']:
            errorMessage = "Missing Combined Rank"
            self._dropSpider(errorMessage, item)

        return item

    def _dropSpider(self, message, item):
        raise DropItem(message)
