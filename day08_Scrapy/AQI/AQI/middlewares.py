# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

from selenium import webdriver
from scrapy.http import HtmlResponse
import time
import random
from fake_useragent import UserAgent
from .settings import USER_AGENT_LIST


class AqiSeleniumMiddleware(object):
    def __init__(self):
        self.driver = webdriver.Chrome()

    def process_request(self, request, spider):

        if "daydata" in request.url or "monthdata" in request.url:
            #driver = webdriver.Chrome()
            self.driver.get(request.url)
            for count in range(18):
                try:
                    self.driver.find_element_by_xpath("//div[@class='row']//tbody/tr//td[1]")
                    html = self.driver.page_source
                    return HtmlResponse(url = request.url, body = html.encode("utf-8"), encoding="utf-8", request = request)
                except:
                    time.sleep(0.5)

    def __del__(self):
        self.driver.quit()
        # response.url
        # response.encoding
        # response.body
        # response.request

"""1. 添加随机的请求头信息"""


class UserAgentMiddleware(object):
    def process_request(self, request, spider):
        # 方式一: 使用setting中的代理池
        # user_agent = random.choice(USER_AGENT_LIST)

        # 不需要return request，如果返回就是返回给引擎处理
        # print request.headers["User-Agent"]

        # 方式二: 使用fake_agent中的请求头信息
        ua = UserAgent()
        user_agent = ua.random

        # 最后添加请求头信息
        request.headers["User-Agent"] = user_agent



"""2. 添加IP 代理信息"""


class ProxyMiddleware(object):
    def process_request(self, request, spider):
        """
        # 免费透明代理：
        proxy = "114.67.224.167:16819"
        request.meta['proxy'] = "http://" + proxy
        """
        # 验证代理使用：
        proxy = "maozhaojun:ntkn0npx@114.67.224.167:16819"
        request.meta['proxy'] = proxy

        # 早期Scrapy中用验证代理的方法：
        """
        user_passwd = "maozhaojun:ntkn0npx"
        ip_port = "@114.67.224.167:168191"
        base64_user_passwd = base64.b64encode(user_passwd)
        request.headers['Proxy-Authorization'] = "Basic " + base64_user_passwd
        request.meta['proxy'] = "http://" + proxy
        """








