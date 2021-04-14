# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from pymongo.mongo_client import MongoClient

class YiquwangPipeline:

    # 开始爬虫时 回调该方法
    def open_spider(self,spider):
        # 创建mongodb客户端
        self.client = MongoClient('localhost', 27017)
        # 创建集合对象
        self.conection = self.client['yqw']['python']  # yqw:数据库名  python：表名

    def process_item(self, item, spider):
        self.conection.insert_one({"rank": item['rank'], 'rank_a': item['rank_a'], 'seller': item['seller'], 'month_reviews': item['month_reviews'], 'lifetime_reviews': item['lifetime_reviews'], 'location': item['location']})
        return item

    # 关闭mongodb客户端
    def close_spider(self,spider):
        self.client.close()


