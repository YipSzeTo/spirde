import scrapy
from imgProject.items import ImgprojectItem

class ImgspiredSpider(scrapy.Spider):
    name = 'imgspired'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://sc.chinaz.com/tupian/index.html']
    def parse(self, response):
        # 输出请求头
        print(response.request.headers)
        # 获取图片的src
        div_list = response.xpath('//div[@id="container"]/div')
        for div in div_list:
            # 获取图片的src值
            # 直接访问src属性，为空，需要访问伪属性src2，当前伪属性的好处在于可以实现图片的懒加载
            src = div.xpath('./div/a/img/@src2').extract_first()
            # 创建item对象
            item = ImgprojectItem()
            item['src'] = src
            yield item