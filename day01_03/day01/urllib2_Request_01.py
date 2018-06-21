# -*- coding:utf-8 -*-
import urllib2

def send_request():

    url = ''
    headers = {

    }
    # 构建请求对象, 可以添加请求报头
    request = urllib2.Request(url, headers=headers)
    response = urllib2.urlopen(request).read()

    print(response)


if __name__ == '__main__':
    send_request()
