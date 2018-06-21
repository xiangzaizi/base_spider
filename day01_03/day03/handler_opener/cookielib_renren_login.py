#!/usr/bin/env python
# -*- coding:utf-8 -*-

import urllib
import urllib2
import cookielib


def login():
    """
        登录模块，产生可以保存Cookie的opener对象
    """
    # 1. 创建保存Cookie的cookiejar对象
    cookie_jar = cookielib.CookieJar()
    # 2. 使用Cookiejar对象，构建hanlder处理器
    cookie_handler = urllib2.HTTPCookieProcessor(cookie_jar)
    # 3. 再通过handler处理器，构建自定义opener对象
    opener = urllib2.build_opener(cookie_handler)

    # 登录post请求的url地址
    login_url = "http://www.renren.com/PLogin.do"
    # 构建表单数据
    form_data = {"email" : "mr_mao_hacker@163.com", "password" : "alarmchime"}
    # 转换为url编码字符
    data = urllib.urlencode(form_data)

    headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}

    request = urllib2.Request(login_url, data, headers)

    # 发送登录的post请求，登录成功则自动保存Cookie
    opener.open(request)

    # 1. 返回opener对象，传递给其他函数使用
    #return opener
    # 2. 通过install_opener将自定义opener加载为全局权限，这样在代码的任何地方使用urlopen() 都具有opener的功能
    urllib2.install_opener(opener)


def main():
    """
        通过opener对象处理并传递Cookie，获取需要登录权限的页面数据
    """
    # 如果是login()是return的话则接收opener对象
    #opener = login()
    login()

    url_list = [
        "http://www.renren.com/327550029/profile",
        "http://www.renren.com/410043129/profile"
    ]

    headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}
    for index, url in enumerate(url_list):
        request = urllib2.Request(url, headers = headers)
        # 发送其他页面的get请求（附带了登录状态的Cookie）
        #response = opener.open(request)
        response = urllib2.urlopen(request)

        with open(str(index) + "_renren.html", "w") as f:
            f.write(response.read())


if __name__ == "__main__":
    main()

