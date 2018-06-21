# -*- coding:utf-8 -*-

import urllib2
import ssl

# 1. 忽略ca证书
context = ssl._create_unverified_context()

def send_request():
    headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}
    url = "https://www.12306.cn/mormhweb/"

    request = urllib2.Request(url, headers)
    # 添加context忽略ca证书
    response = urllib2.urlopen(request, context=context)
    print(response.read())

if __name__ == '__main__':
    send_request()