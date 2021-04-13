import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from pymongo.mongo_client import MongoClient
from movie.items import MovieItem

class MymovieSpider(CrawlSpider):
    def __init__(self):
        # 调用父类的方法
        super().__init__(self)
        # 访问mongoDB数据库，创建客户对象
        self.client = MongoClient('localhost', 27017)
        # 创建或者打开urls集合，用来存储访问过的url信息
        self.url_connection = self.client['moviedb']['urls']

    # 销毁爬虫对象时，回调该方法
    def __del__(self):
        self.client.close()

    name = 'mymovie'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.4567kan.com/frim/index1.html']

    link = LinkExtractor(allow=r'index1-\d+.html')  # 链接提取器
    rules = (
        Rule(link, callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        li_list = response.xpath('/html/body/div[1]/div/div/div/div[2]/ul/li')
        for li in li_list:
            # 电影详情页面的url
            detial_url = 'http://www.4567kan.com' + li.xpath('./div/a/@href').extract_first()
            # 查询访问过的url信息  返回的是游标
            cursor = self.url_connection.find({'url': detial_url})
            if cursor.count() == 0:  # 当前的url没有访问过
                print('url没有被访问')
                # 把数据存储到数据库中
                self.url_connection.insert_one({'url': detial_url})
                # 发起一个新的请求，访问该url的电影详情页面
                yield scrapy.Request(url=detial_url, callback=self.parse_detail)
            else:
                print('当前url已经访问过，无需再访问')

    # 解析电影详情页面
    def parse_detail(self, response):
        # 电影名称
        name = response.xpath('/html/body/div[1]/div/div/div/div[2]/h1/text()').extract_first()
        # 电影简介
        desc = response.xpath('/html/body/div[1]/div/div/div/div[2]/p[5]/span[2]//text()').extract()
        desc = ''.join(desc)
        # print(f"电影名称{name}\n电影简介{desc}")
        item = MovieItem()
        item['name'] = name
        item['desc'] = desc
        yield item