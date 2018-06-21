# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup

html = requests.get("https://hr.tencent.com/position.php?&start=0", headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}).content


# html = requests.get("https://hr.tencent.com/position.php?&start=0", headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}).content

soup = BeautifulSoup(html, "lxml")
node_list = soup.select(".even, .odd")
print(node_list)
len(node_list)
for node in node_list:
    print(node.select("td a"))
for node in node_list:
    print(node.select("td a")[0].get_text())
for node in node_list:
    print(node.select("td a")[0].get("href"))
for node in node_list:
    print(node.select("td")[1].get_text())
for node in node_list:
    print(node.select("td")[2].get_text())
for node in node_list:
    print(node.select("td")[2].get_text())
# 将ipython中测试的内容存起来 %hist -f tencent_test.py
