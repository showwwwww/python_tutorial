from bs4 import BeautifulSoup
import requests

headers = {
    "Accept": "text/html.application/xhtml,application/xhmtl+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, sdch",
    "Accept-Language": "zh-CN,zh:q=0.8",
    "Connection": "close",
    "Cookie": "_gauges_unique_hour=1; _gauges_unique_day=1; _gauges_unique_month=1; _gauges_unique_month=1; _gauges_unique_year=1; _gauges_unique=1",
    "Referer": "http://httpbin.org/",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.1"
}

url = 'http://www.infoq.com/cn/news/30'

# 获取新闻标题
def craw2(url):
    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, 'lxml')

    print(soup.prettify())

    for title_href in soup.find_all('div', class_='news_type_block'):
        print(title.get('title')
            for title in title_href.findall('a') if title.get('title'))


craw2(url)
