import requests
import asyncio
import time

# 定义协程函数，访问网络
async def get_page(url):
	'''爬取网页内容任务'''
	respone = requests.get(url=url)
	page_text = respone.text
	print(f'url:{url},内容；{page_text}')

start_time = time.time()
tasks = []  # 声明任务列表
urls = ['http://127.0.0.1:5000/', 'http://127.0.0.1:5000/nihao', 'http://127.0.0.1:5000/happy']
# 把各个协程封装到任务列表中
for url in urls:
	c = get_page(url)
	task = asyncio.ensure_future(c)
	tasks.append(task)

# 创建事件循环对象
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
end_time = time.time()
print('耗时：', end_time - start_time)

# todo 文件执行前先把‘web服务器.py’文件开启