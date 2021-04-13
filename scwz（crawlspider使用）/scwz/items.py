# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


#  问政项
class ScwzItem(scrapy.Item):
    title = scrapy.Field()
    date = scrapy.Field()
    url = scrapy.Field()


# 详情项
class DetaItem(scrapy.Item):
    url = scrapy.Field()
    content = scrapy.Field()