import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.0.0'}
url = 'http://124.115.190.134:8501/ServerAPI'

data = {'route': 'OilMonitor-GetOilMonitorInfoByWell', 'wellName': 'QL郑073平4'}

response = requests.post(url, headers=headers, data=data)
staut = response.status_code
txt = response.content.decode()
print(staut)
print(txt)
