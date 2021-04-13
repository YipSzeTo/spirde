import asyncio
import time
import aiohttp

start_time = time.time()
# 定义协程函数，访问网络
async def get_page(url):
	'''爬取网页内容任务'''
	# aiohttp:基于异步的网络请求模块，在协程中用aiohttp访问网络
	async with aiohttp.ClientSession() as session:
		async with await session.get(url) as respone:
			# 对于阻塞的操作，需要挂起该操作
			page_text = await respone.text()
			print(f"{url}内容： \n {page_text}")

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
print('用时：', end_time-start_time)