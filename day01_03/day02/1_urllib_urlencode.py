# -*- coding:utf-8 -*-
import urllib
import urllib2

def send_request():
    base_url = 'https://www.baidu.com/s?'
    keyword = raw_input("请输入需要查询的内容:")

    # 将字典转换为url编码的字符串
    url_str = urllib.urlopen({'wd': keyword})
    # 在和固定url进行拼接
    full_url = base_url + url_str

    headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}
    # 构建请求, 发送
    request = urllib2.Request(full_url, headers=headers)

    print(urllib2.urlopen(request).read())

if __name__ == '__main__':
    send_request()



