# 化妆品生产许可信息管理系统服务平台
# 爬各个公司的生产许可证明
import requests
import json
import time

start_url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'}
id1 = []
info = []

# 爬取参数（id）
for page in range(1, 8):
	data = {
		'on': 'true',
		'page': '',
		'pageSize': 15,
		'productName': '',
		'conditionType': 1,
		'applyname': '',
		'applysn': '',
	}
	response = requests.post(url=start_url, data=data, headers=headers).json()  # 发起请求，获取响应
	time.sleep(1)  # 反反爬虫，设置时间间隔为一秒
	for dict in response['list']:  # 将爬到的id存储在id1字典中
		id1.append(dict['ID'])

	url2 = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById'
	headers2 = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'}
	time.sleep(1)  # 反反爬虫，设置时间间隔为一秒
	for idv in id1:
		data2 = {'id': idv}  # 遍历id1字典
		response2 = requests.post(url=url2, data=data2, headers=headers2).json()  # 发起请求，获取响应
		info.append(response2)  # 将数据存储到info字典中

# 存储数据
fp = open('a.json', 'w', encoding='utf-8')
json.dump(info, fp=fp, ensure_ascii=False)
fp.close()  # 关闭文件
print('完成')