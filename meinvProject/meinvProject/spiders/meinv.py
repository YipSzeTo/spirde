import scrapy


class MeinvSpider(scrapy.Spider):
    name = 'meinv'
    # allowed_domains = ['www.521609    .com']
    start_urls = ['http://www.521609.com/meinvxiaohua/']

    base_url = 'http://www.521609.com/meinvxiaohua/list12%d.html'

    page_num = 2
    def parse(self, response):
        name_list = []
        li_list = response.xpath('//div[@id="content"]/div[2]/div[2]/ul/li')
        for li in li_list:
            img_name = li.xpath('./a[2]//text()').extract_first()
            name_list.append(img_name)
        if self.page_num <= 11:
            new_url = format(self.base_url % self.page_num)
            self.page_num += 1
            yield scrapy.Request(url=new_url, callback=self.parse, method='GET')
        print(name_list)
        print(len(name_list))