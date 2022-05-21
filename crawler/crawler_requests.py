# get 请求
import requests
url = 'http://httpbin.org/get'
data = {'key': 'value', 'abc': 'xyz'}
# .get 是使用 get 方式请求 url，字典类型的 data不用进行额外处理
response = requests.get(url, data)
print(response.text)

# post 请求
url = 'http://httpbin.org/post'
data = {'key': 'value', 'abc': 'xyz'}
# .post 表示 post 方法
response = requests.post(url, data)
# 返回类型为 json 格式
print(response.json())
