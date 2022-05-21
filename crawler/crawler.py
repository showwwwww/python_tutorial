import socket
import urllib.error
from urllib import request
from urllib import parse

# url = 'http://www.baidu.com'
# response = request.urlopen(url, timeout=1)
# print(response.read().decode('utf-8'))

# data = bytes(parse.urlencode({'world': 'hello'}), encoding='utf8')
#
# response = request.urlopen('http://httpbin.org/post', data=data)
# print(response.read().decode('utf-8'))

# response2 = request.urlopen('http://httpbin.org/get', timeout=1)
# print('get', response2.read().decode('utf-8'))

try:
    response = request.urlopen('http://httpbin.org/get', timeout=0.1)
except urllib.error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        print('TIME OUT')
