import asyncio
import time

# 定义协程函数
async def download(url):
	print('正在下载...', url)
	# time.sleep(2)  # 模拟耗时的操作，休眠2秒，但在事件循环中，不能识别为阻塞的操作
	# 当遇到阻塞操作时需要手动挂起该操作，使用await进行挂起
	await asyncio.sleep(2)  # 模拟耗时的操作，休眠2秒，但在事件循环中，可识别为阻塞的操作
	print('下载完毕...', url)

# 准备urls列表
urls = ["www.sina.com.cn", "www.baidu.com", "www.taobao.com"]
start_time = time.time()  # 开始时间
# 任务列表
tasks = []
for url in urls:
	# 创建一个协程对象
	c = download(url)
	task = asyncio.ensure_future(c)
	tasks.append(task)

# 创建一个事件循环对象
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))  # 需加一个阻塞wait

end_time = time.time()  # 结束时间
print('耗时：', end_time-start_time)