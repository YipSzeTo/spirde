import requests
from lxml import etree
import time

start_time = time.time()
# 伪装成浏览器
headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'
}

names = []  # 用于存放图片名称


# 准备一个任务函数，用于下载图片
def download_img(url):
	# 获取网页的源码字符串
	page_text = requests.get(url=url, headers=headers).text
	tree = etree.HTML(page_text)
	li_list = tree.xpath('//div[@class="slist"]/ul/li')
	for li in li_list:
		img_src = "http://pic.netbian.com" + li.xpath('./a/img/@src')[0]
		name = img_src.split('/')[-1]
		names.append(name)


for page in range(2, 51):
	new_url = f'https://pic.netbian.com/4kfengjing/index_{page}.html'
	download_img(new_url)

print(len(names))
print(names)
end_time = time.time()
print('耗时：', end_time - start_time)
