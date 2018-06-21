# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

from settings import IMAGES_STORE
from scrapy.pipelines.images import ImagesPipeline
from datetime import datetime

import json
import scrapy
import os
import logging

class DouyuJsonPipeline(object):
    def open_spider(self, spider):
        self.f = open("douyu.json", "w")

    def process_item(self, item, spider):
        item["utc_time"] = str(datetime.utcnow())
        item['source'] = spider.name
        content = json.dumps(dict(item)) + ",\n"
        self.f.write(content)
        return item  # 所以先执行这里在执行ImagePipeline

    def close_spider(self, spider):
        self.f.close()


class DouyuImagesPipeline(ImagesPipeline):
    # 重写下面的两个方法

    def get_media_requests(self, item, info):
        # 发送图片请求，响应保存到settings.py IMAGES_STORE指定的路径下
        yield scrapy.Request(item["image_src"])  # 配合IMAGES_STORE使用指定的存储目录下

    def item_completed(self, results, item, info):  # item_complated-->处理每一个item数据信息
        # result---->
        # info--->当前爬虫信息一个对象
        # 取出原始图片存储路径
        # print result-->测试
        # {url, path, checksum}
        # path--->图片 ok->true 返回path-->取x['path']取下标[0]
        # .....jpg-->图片路径
        image_path = [x["path"] for ok, x in results if ok][0]
        # 拼接新的指定的位置: data/ + item[人名] +.jpg
        item["image_path"] = IMAGES_STORE + item['nick_name'] + ".jpg"  # .jpg可以正则imag_path取图片路径的.png..等等
        #  通过图片原路径修改新名称
        #os.rename("old_name", "new_name")
        try:
            os.rename(
                IMAGES_STORE + image_path,
                item["image_path"]
            )
        except:
            logging.error("%s 图片修改失败.." % IMAGES_STORE + image_path)


        return item







