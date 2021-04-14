import scrapy
from yiquwang.items import YiquwangItem


class PjSpider(scrapy.Spider):
    name = 'pj'
    # allowed_domains = ['www.xxx.com']
    start_urls = []
    for num in range(1, 11):
        start_urls.append('https://www.topratedseller.com/ebay?page={}'.format(num))

    def parse(self, response):
        div = response.xpath('//table[@id="report"]/tbody/tr')
        for i in div:
            # 排名
            rank = i.xpath('./td[1]/text()')[0].extract()
            rank = rank.replace(' ', '')
            rank = rank.replace('\n', '')
            # 排名的升降
            rank_a = i.xpath('./td[1]/abbr/@style').extract()  # 1ed760为绿色  cd1a2b为红色  9b9b9b或者空为排名不变
            if rank_a == ['color: #cd1a2b;']:
                rank_a = '下降'
            elif rank_a == ['color: #1ed760;']:
                rank_a = '上升'
            else:
                rank_a = '不变'
            # 卖方
            seller = i.xpath('./td[2]/a/text()')[0].extract()
            # 30天评论数
            month_reviews = i.xpath('./td[3]/text()')[0].extract()
            a = month_reviews.split(',')
            month_reviews = ''.join(a)
            # 终身评论数
            lifetime_reviews = i.xpath('./td[4]/text()')[0].extract()
            b = lifetime_reviews.split(',')
            lifetime_reviews = ''.join(b)
            # 地点
            location = i.xpath('./td[5]/text()')[0].extract()
            print('排名：{}，排名变化：{}，卖方：{}，30天：{}，终身：{}，地点：{}'.format(rank, rank_a, seller, month_reviews, lifetime_reviews, location))
            # 把数据放在item中封装起来
            item = YiquwangItem()
            item['rank'] = rank
            item['rank_a'] = rank_a
            item['seller'] = seller
            item['month_reviews'] = month_reviews
            item['lifetime_reviews'] = lifetime_reviews
            item['location'] = location
            yield item