"""
Author : sunshicheng 
DateTime : 19-12-1 下午7:06
FileName : urllib_splide.py

使用urllib 模块的爬虫学习

"""

"""
#urlopen 函数

import urllib.request

response = urllib.request.urlopen("https://www.python.org")

print(type(response))
print(response.read())
print(response.status)
print(response.getheaders())
print(response.getheader('Server'))

#data()

import urllib.parse
import urllib.request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

data = bytes(urllib.parse.urlencode({'name':'hello','pass':'123'}),encoding='utf-8')
response = urllib.request.urlopen('http://www.iqianyue.com/mypost',data=data)
print(response.read())


#timeout

import urllib.request
# response = urllib.request.urlopen('http://www.python.org',timeout=1)
# print(response.text)

import socket
import urllib.request
import urllib.error

try:
    response = urllib.request.urlopen('http://httpbin.org/get',timeout=1)
except urllib.error.URLError as e:
    if isinstance(e.reason,socket.timeout):
        print('TIME OUT')
"""

import urllib.request

request = urllib.request.Request("http://www.baidu.com")

response = urllib.request.urlopen(request)

print(response.read().decode('utf-8'))

