import requests
import json

# 指定url
url = 'https://fanyi.baidu.com/sug'
# 发起请求
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'}
word = input('请输入你要翻译的词语：')
data = {'kw': word}
reponse = requests.post(url=url, data=data, headers=headers)
# 获取响应 （数据类型是json）看content—type是什么数据类型
requests = reponse.json()
print(requests)
# 存储
with open(word, 'w', encoding='utf-8') as f:
	json.dump(requests, fp=f, ensure_ascii=False)
print('完成')
