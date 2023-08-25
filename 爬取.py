import requests

url = "http://www.baidu.com"

res = requests.get(url)
#不进行解码，直接输出
print(res.content)
print('-----------')
print(res.json)
