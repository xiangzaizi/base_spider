#!/usr/bin/env python
# -*- coding:utf-8 -*-

import unittest
import pymongo
import time
from selenium import webdriver
from bs4 import BeautifulSoup

class DouyuSpider(unittest.TestCase):
    # 方法名固定
    def setUp(self):
        self.driver = webdriver.PhantomJS()
        self.client = pymongo.MongoClient(host="127.0.0.1", port=27017)
        self.db = self.client["douyu"]
        self.collection = self.db["directory"]
        self.count = 0
    # 必须以test开头，测试方法
    def testDouyu(self):
        self.driver.get("https://www.douyu.com/directory/all")
        while True:
            html = self.driver.page_source
            soup = BeautifulSoup(html, "lxml")

            node = soup.find("div", {"id" : "live-list-content"})

            #房间标题
            room_list = node.find_all("h3", {"class":"ellipsis"})
            #分类
            tag_list = node.find_all("span", {"class":"tag ellipsis"})
            #主播名
            name_list = node.find_all("span", {"class":"dy-name ellipsis fl"})
            #观众人数
            people_list = node.find_all("span", {"class":"dy-num fr"})

            for room, tag, name, people in zip(room_list, tag_list, name_list, people_list):
                item = {}
                item["room"] = room.get_text().strip()
                item["tag"] = tag.get_text().strip()
                item["name"] = name.get_text().strip()
                item["people"] = people.get_text().strip()
                print item["room"] + "\t" + item["tag"] + "\t" + item["name"] + "\t" + item["people"]
                self.count += 1
                self.collection.insert(item)


            if soup.find("a", {"class": "shark-pager-disable-next"}):
                break
            else:
                self.driver.find_element_by_class_name("shark-pager-next").click()
                time.sleep(0.5)
                print "[INFO] 正在获取下一页"
    # 方法名固定
    def tearDown(self):
        self.driver.quit()
        print "[INFO] 当前主播人数%d" % self.count

if __name__ == "__main__":
    unittest.main()


