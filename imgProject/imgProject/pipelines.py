# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


# class ImgprojectPipeline:
#     def process_item(self, item, spider):
#         return item

from scrapy.pipelines.images import ImagesPipeline
import scrapy


class MyImagePipeline(ImagesPipeline):
    # 返回当前图片的Request请求
    def get_media_requests(self, item, info):
        yield scrapy.Request('https:' + item['src'])

    # 当item处理完毕后，传给下一个管道
    def item_completed(self, results, item, info):
        return item

    # 返回图片文件的路径，就是返回文件名
    def file_path(self, request, response=None, info=None, *, item=None):
        url = item['src']
        img_filename = url.split('/')[-1]
        return img_filename