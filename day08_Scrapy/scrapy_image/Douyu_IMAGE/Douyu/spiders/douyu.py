# coding:utf-8


import scrapy
import json

from Douyu.items import DouyuItem


class DouyuSpider(scrapy.Spider):
    name = "douyu"
    allowed_domains = ["douyucdn.cn"]

    # 返回的内容直接是json数据  所以内容可以直接去处理啊data["内容"]
    base_url = "http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=100&offset="
    offset = 0

    # 拼接URL
    start_urls = [base_url + str(offset)]


    def parse(self, response):
        # 先返回python数据类型
        # 直接去data数据 
        data_list = json.loads(response.body)["data"]

        # 当响应数据中的data为空列表时，表示数据提取结束，return parse方法立刻结束
        # 对应offset的在线主播, 空的时候说明翻页到头了没有人了
        if not len(data_list): # 没有数据返回
            return

        for data in data_list:
            item = DouyuItem()
            # 获取图片的路径url地址
            item["room_link"] = "http://www.douyu.com/" + data["room_id"]
            item["image_src"] = data["vertical_src"]
            item["nick_name"] = data["nickname"]
            item["city"] = data["anchor_city"]

            yield item
        # 控制翻页
        self.offset += 100
        yield scrapy.Request(self.base_url + str(self.offset), callback = self.parse)

