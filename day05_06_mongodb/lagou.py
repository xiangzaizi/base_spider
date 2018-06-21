# -*- coding:utf-8 -*-
import requests
import random
import jsonpath
import time
import pymongo
import urllib


class LagouSpider(object):
    def __init__(self):
        self.base_url = "https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false"
        self.headers = {
            "Accept" : "application/json, text/javascript, */*; q=0.01",
            #"Accept-Encoding" : "gzip, deflate, br",
            "Accept-Language" : "zh-CN,zh;q=0.9,en;q=0.8",
            "Connection" : "keep-alive",
            "Content-Length" : "25",
            "Content-Type" : "application/x-www-form-urlencoded; charset=UTF-8",
            "Cookie" : "user_trace_token=20170923184359-1ba5fe6f-a04c-11e7-a60e-525400f775ce; LGUID=20170923184359-1ba6010d-a04c-11e7-a60e-525400f775ce; _ga=GA1.2.136733168.1506163440; JSESSIONID=ABAAABAAADEAAFI1C9E375C87BADDE83A937A6BF3C1BF27; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1524107694; LGSID=20180419111456-d625724c-437f-11e8-8b39-525400f775ce; PRE_UTM=; PRE_HOST=; PRE_SITE=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; index_location_city=%E5%85%A8%E5%9B%BD; TG-TRACK-CODE=index_search; _gat=1; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1524108318; LGRID=20180419112517-4864ae65-4381-11e8-b8aa-5254005c3644; SEARCH_ID=d8df553f4886426ab31471e5f8a42762",
            "Host" : "www.lagou.com",
            "Origin" : "https://www.lagou.com",
            "Referer" : "https://www.lagou.com/jobs/list_python?px=default&city=%E5%8C%97%E4%BA%AC",
            "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
            "X-Anit-Forge-Code" : "0",
            "X-Anit-Forge-Token" : "None",
            "X-Requested-With" : "XMLHttpRequest"
        }
        self.page = 1
        self.position = raw_input("请输入需要抓取的职位:")
        self.city = raw_input("请输入需要抓取的城市:")
        self.proxy_list = [{"http" : "http://maozhaojun:ntkn0npx@114.67.224.167:16819"}, {}]
        self.item_list = []
        self.is_work = True

    def send_request(self):
        # 查询字符串
        query_data = {
            "px" : "default",
            "city" : self.city,
            "needAddtionalResult" : "false"
        }
        # form表单数据
        form_data = {
            "first": "false",
            "pn": self.page,
            "kd": "python"
        }

        # 修改请求报头字段值
        self.headers["Content-Length"] = str(len(urllib.urlencode(form_data)))

        print "[INFO] 正在获取第%s页" % self.page
        response = requests.post(self.base_url, headers = self.headers, params = query_data, data = form_data, proxies = random.choice(self.proxy_list))

        return response

    def parse_page(self, response):
         # response.json() 将json文件的响应转为Python数据类型
        dict_obj = response.json()
        #json_str = urllib2.Request().read()
        #dict_obj = json.loads(json_str)

        #result_list = json_data["content"]["positionResult"]["result"]
        # jsonpath 永远返回列表
        result_list = jsonpath.jsonpath(dict_obj, "$..result")[0]
        print len(result_list)
        if not len(result_list):
            self.is_work = False
            return
        #print result_list
        for result in result_list:
            item = {}
            item["salary"] = result["salary"]
            item["financeStage"] = result["financeStage"]
            item["positionName"] = result["positionName"]
            item["companySize"] = result["companySize"]
            item["district"] = result["district"]
            item["city"] = result["city"]
            item["companyFullName"] = result["companyFullName"]
            self.item_list.append(item)

    def __open(self):
        self.client = pymongo.MongoClient(host="127.0.0.1", port=27017)
        self.db = self.client["lagou"]
        self.collection = self.db["position"]

    def save_mongo(self):
        self.__open()
        try:
            print "[INFO] 正在写入MongoDB"
            self.collection.insert(self.item_list)
            print "[INFO] 写入成功!"
        except Exception as e:
            print e


    def main(self):
        while self.is_work:
            try:
                # 发送请求，获取响应
                response = self.send_request()
                time.sleep(random.randint(1, 2))
                if response:
                    try:
                        # 解析响应
                        self.parse_page(response)
                    except:
                        print "[ERROR] 第%s页面解析失败.." %self.page
                self.page += 1
            except Exception as e:
                print "[ERROR] 第 %s页请求处理失败.." % self.page

        # 将解析数据存入数据库中
        self.save_mongo()

if __name__ == "__main__":
    spider = LagouSpider()
    spider.main()
