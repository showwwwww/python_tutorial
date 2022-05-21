import os.path
from bs4 import BeautifulSoup
import requests
import shutil

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.8",
    "Connection": "close",
    "Cookie": "_gauges_unique_hour=1; _gauges_unique_day=1; _gauges_unique_month=1; _gauges_unique_year=1; _gauges_unique=1",
    "Referer": "http://www.infoq.com",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36 LBBROWSER"
}

url = 'http://www.infoq.com/presentations'


def download_jpg(img_url, img_local_path):
    response = requests.get(img_url, stream=True)
    if response.status_code == 200:
        with open(img_local_path, 'wb') as f:
            response.raw.decode_content = True
            shutil.copyfileobj(response.raw, f)


# 获取图片
def craw3(url_name):
    response = requests.get(url_name, headers=headers)

    soup = BeautifulSoup(response.text, 'lxml')

    for title_href in soup.find_all('div', class_='news_type_video'):
        for pic in title_href.findall('img'):
            img_url = pic.get('src')
            dir_name = os.path.abspath('.')
            filename = os.path.basename(img_url)
            img_path = os.path.join(dir_name, filename)
            print('开始下载 %s' % img_url)
            download_jpg(img_url, img_path)


craw3(url)
