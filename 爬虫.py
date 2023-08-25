import requests
from bs4 import BeautifulSoup

def simple_web_crawler(url):
    try:
        # 发送GET请求获取网页内容
        response = requests.get(url)

        # 检查是否成功获取网页内容
        if response.status_code == 200:
            # 使用BeautifulSoup解析网页内容
            soup = BeautifulSoup(response.text, 'html.parser')

            # 获取网页的标题
            title = soup.title.text.strip()

            # 获取网页中的所有链接
            links = []
            for link in soup.find_all('a'):
                href = link.get('href')
                if href and href.startswith('http'):
                    links.append(href)

            return title, links
        else:
            print(f"请求失败，状态码：{response.status_code}")
            return None
    except Exception as e:
        print(f"发生异常：{e}")
        return None

if __name__ == "__main__":
    # 要爬取的网页地址
    target_url = "https://www.example.com"  # 将example.com替换为你想爬取的网页地址

    # 调用爬虫函数并获取结果
    result = simple_web_crawler(target_url)

    if result:
        title, links = result
        print(f"网页标题：{title}")
        print("网页中的链接：")
        for link in links:
            print(link)
    else:
        print("爬取失败，请检查网页地址或网络连接。")
