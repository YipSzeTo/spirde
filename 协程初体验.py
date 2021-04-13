import asyncio

# 定义协程函数
async def download(url):
	print(f'下载:{url}')
	print('已完成')

# 通过协程函数创建协程
c = download('www.taobao.com')

# 创建事件循环对象
loop = asyncio.get_event_loop()

# 创建任务
# task = loop.create_task(c)
# 创建future
task = asyncio.ensure_future(c)

# 通过事件循环函数注册且启动协程
loop.run_until_complete(task)