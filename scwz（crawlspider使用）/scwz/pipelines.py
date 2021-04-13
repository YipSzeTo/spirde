# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql
from scwz.items import ScwzItem, DetaItem


class ScwzPipeline:
    def open_spider(self, spider):
        print('开启mysql')
        self.conn = pymysql.Connect(host='localhost', port=3306, database='scwz_db', user='root', password='1234qwer', charset='utf8')
        self.cursor = self.conn.cursor()

    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()
        print('关闭MySQL')

    def process_item(self, item, spider):
        if isinstance(item, ScwzItem):
            try:
                sql_str = 'insert into tb_scwz(title, url, date) value ("%s", "%s", "%s")' % (item['title'], item['url'], item['date'])
                self.cursor.execute(sql_str)
                self.conn.commit()
            except Exception as e:
                print(e)
                self.conn.rollback()
            return item
        if isinstance(item, DetaItem):
            try:
                sql_str = 'update tb_scwz set content="%s" where url="%s"' % (item['content'], item['url'])
                self.cursor.execute(sql_str)
                self.conn.commit()
            except Exception as e:
                print(e)
                self.conn.rollback()
            return item
        return item