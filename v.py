import requests
from bs4 import BeautifulSoup

# 设置登录信息
login_url = 'http://124.115.190.134:8501/View/login.htm'
index_url = 'http://124.115.190.134:8501/View/index.htm'
username = 'Hyadmin'
password = 'Hyadmin123'
captcha_code = 'P4EH'
# 创建会话
session = requests.Session()

# 获取验证码并手动输入
# captcha_response = session.get(login_url)
# captcha_soup = BeautifulSoup(captcha_response.text, 'html.parser')
# captcha_img = captcha_soup.find('img', id='captcha_img')
# print('请查看验证码图片：' + captcha_img['src'])
# captcha_code = input('请输入验证码：')

# 登录
login_data = {'username': username, 'password': password, 'captcha': captcha_code}
session.post(login_url, data=login_data)

# 爬取数据
response = session.get(index_url)
print(type(response))
print(dir(response))
print(response.content.decode('utf-8'))


soup = BeautifulSoup(response.text, 'html.parser')
# print(soup.decode(True))
# 在这里添加您的代码来爬取和处理数据
# 获取登录网页中所有的 rootItem
print('---------------')
root_items = soup.find_all('div', class_='rootItem')
for item in root_items:
    item.coding
