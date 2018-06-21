# -*- coding:utf-8 -*-
"""需要用户名密码的才可以访问的网站"""
import urllib2


def send_request():
    # 需要处理web验证的服务器url地址
    url = "http://192.168.72.82/"  # 测试url
    # web验证的账户
    username = 'bigcat'
    # web验证的密码
    password = '123456'

    # 1. 构建一个基于HTP账户验证的处理器对象
    passsmgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
    # 2. 添加web信息和账户密码
    passsmgr.add_password(None, url, username, password)

    # 3.构建处理器对象
    httpauth_handler = urllib2.HTTPBasicAuthHandler(passsmgr)
    # 4. 构建自定义opener对象
    opener = urllib2.build_opener(httpauth_handler)

    # 发送web服务器的请求, 同时附带了服务器的web验证信息，通过web验证，获取响应
    response = opener.open(url)
    print(response.read())


