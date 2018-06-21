# -*- coding:utf-8 -*-
import urllib2

def send_request():
    url = ''
    headers = {

    }
    # 构建请求对象,可以添加请求报头
    request = urllib2.Request(url, headers=headers)

    # 1. 添加请求报头
    # 两个参数, 分别是请求报头的键和值
    request.add_header('Connection', 'keep-alive')

    # 2. 获取指定的请求报头值, 返回字符串
    # 参数为请求报头的键,(只能是第一个字母的大写)
    print request.get_header('Connection')
    print request.get_header('User-Agent')

    response = urllib2.urlopen(request)

    # 3. 获取响应文件里的字符串

    print(response.read())

if __name__ == '__main__':
    send_request()

