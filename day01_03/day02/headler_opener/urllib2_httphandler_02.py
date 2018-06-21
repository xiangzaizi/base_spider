# -*- coding:utf-8 -*-
import urllib2

def send_request():
    url = ''
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}

    request = urllib2.Request(url, headers=headers)

    # 1.构建处理器对象
    http_handler = urllib2.HTTPHandler()
    # 2. 使用bulid_opener使用处理器对象, 返回自定义opener对象
    opener = urllib2.build_opener(http_handler)
    # 3. opener.open()  发送请求即可
    response = opener.open(request).read()

    print response


if __name__ == '__main__':
    send_request()

