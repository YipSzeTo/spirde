from lxml import etree
import time
import asyncio
import aiohttp  # aiohttp:基于异步的网络请求模块，在协程中用aiohttp访问网络


start_time = time.time()
# 伪装成浏览器
headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'
}

names = []  # 用于存放图片名称


# 准备一个任务函数，用于下载图片
async def download_img(url):
	# 获取网页的源码字符串
	async with aiohttp.ClientSession() as session:
		async with session.get(url=url, headers=headers) as response:
			# 获取网页源码的二进制字符串
			bytes = await response.read()  # 要把阻塞的方法挂起来
			page_text = bytes.decode(encoding='gbk')  # 将二进制字符串转为gbk
			tree = etree.HTML(page_text)
			li_list = tree.xpath('//div[@class="slist"]/ul/li')
			for li in li_list:
				img_src = "http://pic.netbian.com" + li.xpath('./a/img/@src')[0]
				name = img_src.split('/')[-1]
				names.append(name)

tasks = []  # 用于封装协程的任务列表
for page in range(2, 51):
	new_url = f'https://pic.netbian.com/4kfengjing/index_{page}.html'
	c = download_img(new_url)
	task = asyncio.ensure_future(c)
	tasks.append(task)


# 创建一个事件循环对象
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))

print(len(names))
print(names)
end_time = time.time()
print('耗时：', end_time - start_time)
