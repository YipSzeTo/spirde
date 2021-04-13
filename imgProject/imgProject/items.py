# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ImgprojectItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 图片的url值
    src = scrapy.Field()
    pass
