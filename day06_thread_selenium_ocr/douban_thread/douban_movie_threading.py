#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests
import threading
from lxml import etree
from Queue import Queue
import time

class DoubanSpider(object):
    def __init__(self):
        self.start_urls = ["https://movie.douban.com/top250?start=" + str(page) for page in range(0, 226, 25)]
        self.headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}
        self.data_queue = Queue()
        self.proxy = {"http" : "http://maozhaojun:ntkn0npx@114.67.224.167:16819"}

        self.count = 0

    def send_request(self, url):
        try:
            print "[INFO]: 正在抓取 %s" % url
            response = requests.get(url, headers = self.headers, proxies = self.proxy)
            time.sleep(1)
            self.parse_page(response)
        except Exception as e:
            print "[ERROR]  %s 请求发送失败" % url
            print e

    def parse_page(self, response):
        html_obj = etree.HTML(response.content)
        # 取每一个电影结点
        node_list = html_obj.xpath("//div[@class='info']")
        for node in node_list:
            title = node.xpath(".//div[@class='hd']/a/span[1]/text()")[0]
            score = node.xpath(".//span[@class='rating_num']/text()")[0]
            try:
                info = node.xpath(".//span[@class='inq']/text()")[0]
            except:
                info = "None"
            self.count += 1
            self.data_queue.put(title + "\t" + score + "\t" + info)



    def main(self):
        """
        for url in self.start_urls:
            self.send_request(url)
        """

        thread_list = []
        for url in self.start_urls:
            thread = threading.Thread(target = self.send_request, args = [url])
            thread.start()
            thread_list.append(thread)

        # 让主线程等待所有的子线程执行结束，再继续向下执行
        for thread in thread_list:
            thread.join()
        # 判断队列为空时，循环取值结束
        while not self.data_queue.empty():
            print(self.data_queue.get())
        print self.count

if __name__ == "__main__":
    spider = DoubanSpider()
    start = time.time()
    spider.main()
    print "[INFO] : 程序执行时间为 %f" % (time.time() - start)

