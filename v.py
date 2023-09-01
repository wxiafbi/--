import requests
from bs4 import BeautifulSoup
import json

# 设置登录信息
login_url = 'http://124.115.190.134:8501/View/login.htm'
index_url = 'http://124.115.190.134:8501/View/index.htm'
server_url = 'http://124.115.190.134:8501/ServerAPI'
username = 'Hyadmin'
password = 'Hyadmin123'
captcha_code = 'P4EH'
data = {'route': 'OilMonitor-GetOilMonitorInfoByWell', 'wellName': 'QL郑073平4'}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.0.0',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Content-Length': '74',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'HLOilFieldSCADAMID=hrjz5zdpifqpwbt1kv5mzn02',
    'Host': '124.115.190.134:8501',
    'Origin': 'http://124.115.190.134:8501',
    'Proxy-Connection': 'keep-alive',
    'Referer': 'http://124.115.190.134:8501/View/QiLiCunProject/DataCollectAndMonitor/DataCollectAndMonitor.htm',
    'Token': '1cMjAyMy0wOS0wMSAxNDozNzoxNjQ5NA==cDE2M19IeWFkbWluQDE0Mzc0OTQ=_1354'}
# 创建会话
session = requests.Session()

# 获取验证码并手动输入
# captcha_response = session.get(login_url)
# captcha_soup = BeautifulSoup(captcha_response.text, 'html.parser')
# captcha_img = captcha_soup.find('img', id='captcha_img')
# print('请查看验证码图片：' + captcha_img['src'])
# captcha_code = input('请输入验证码：')

# 登录
login_data = {'username': username,'password': password, 'captcha': captcha_code}
session.post(login_url, data=login_data, headers=headers)

# 爬取数据
response = session.post(server_url, data=data, headers=headers)
print(response.status_code)
with open('mun_well.html', 'w', encoding='utf-8') as f:
    answer = response.content.decode()
    print(answer)
    f.write(answer)
