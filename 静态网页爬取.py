import requests

# 1.指定url
url = 'https://www.sogou.com/web?'

# 参数
word = input('请你输入你想查找的网页：')
param = {'query': word}
head = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'
}
proxies = {
	'http': '183.166.103.118:9999',  # IP代理
}

# 发起请求
response = requests.get(url=url, params=param, headers=head, proxies=proxies)

# 3.获取响应 （数据类型是text）看content—type是什么数据类型
page_text = response.text
print(page_text)

# 4.存储
# f = open('a.html', 'w', encoding='utf-8')
# f.write(page_text)
# f.close()
word1 = word + '.html'
with open(word1, 'w', encoding='utf-8') as file:
	file.write(page_text)
print('结束')
