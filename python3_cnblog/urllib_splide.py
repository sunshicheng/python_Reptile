"""
Author : sunshicheng 
DateTime : 19-12-1 下午7:06
FileName : urllib_splide.py

使用urllib 模块的爬虫学习

"""

"""
使用urlopen函数打开网页



import urllib.request

response = urllib.request.urlopen("https://www.python.org")

print(type(response))
print(response.read())
print(response.status)
print(response.getheaders())
print(response.getheader('Server'))
"""

import urllib.parse
import urllib.request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

data = bytes(urllib.parse.urlencode({'name':'hello','pass':'123'}),encoding='utf-8')
response = urllib.request.urlopen('http://www.iqianyue.com/mypost',data=data)
print(response.read())