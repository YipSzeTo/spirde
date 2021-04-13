import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scwz.items import ScwzItem, DetaItem  # 导入item


class ScSpider(CrawlSpider):
    name = 'sc'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://ly.scol.com.cn/welcome/showlist?keystr=wzrd']
    # 链接提取器，依据指定的正则规则（allow）进行提取
    link = LinkExtractor(allow=r'total=\d+&page=\d+')
    link_detial = LinkExtractor(allow=r'https://ly.scol.com.cn/thread\?tid=\d+')

    '''
    爬取规则解析器：将链接提取器提取到的链接进行规定规则
    LinkExtractor: 链接提取器
    callback：回调的数据解析函数
    follow：可以将链接提取器继续作用到 链接提取器 提取到的链接 所对应的页面中
    '''
    rules = (
        Rule(link, callback='parse_item', follow=False),  # 没有先后顺序
        Rule(link_detial, callback='parse_detail', follow=False),
    )

    # 解析全站页面的网页内容
    def parse_item(self, response):
        a_list = response.xpath('//div[@id="d_1"]/a')
        for a in a_list:
            title = a.xpath('./text()').extract_first()
            url = a.xpath('./@href').extract_first()
            # 找当前节点的兄弟节点
            # following-sibling::span[1]  获取当前节点之后的兄弟节点的 第一个span节点
            date = a.xpath('./following-sibling::span[1]/text()').extract_first()
            # print(f'标题：{title}，日期：{date}，链接：{url}')
            item = ScwzItem()
            item['title'] = title
            item['url'] = url
            item['date'] = date
            yield item

    # 解析详情页面
    def parse_detail(self, response):
        content = response.xpath('//div[@class="c1"]/p[2]/text()').extract_first()
        url = response.request.url
        # print(f'详情页面信息 url：{url}\n 内容：{content}')
        item = DetaItem()
        item['url'] = url
        item['content'] = content
        yield item