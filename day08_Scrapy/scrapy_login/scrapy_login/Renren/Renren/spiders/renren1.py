# coding=utf-8

import scrapy


class RenrenSpider(scrapy.Spider):
    name = "renren1"
    allowed_domains = ["renren.com"]

    # 1. 如果重写了父类的start_requests()方法，那么start_urls可有可无
    # start_urls = ["http://www.renren.com/PLogin.do"]

    def start_requests(self):
        # for url in self.start_urls:
            # yield scrapy.Request(url, callback=self.parse)

        # 2. 如果不写start_urls，可以自己构建发送请求的url

        # 发送post请求的url
        url = "http://www.renren.com/PLogin.do"

        # user_name = raw_input("请输入账户")
        # pass_word = raw_input("请输入密码")

        # 3. 通过FormReqeust() 发送post请求，尝试登录，并交给parse()方法解析
        # 如果登录成功，Scrapy会记录登录状态的Cookie，并自动管理传递
        yield scrapy.FormRequest(
            url,
            formdata = {"email" : "mr_mao_hacker@163.com", "password" : "alarmchime"},
            callback = self.parse
        )

    def parse(self, response):
        # 4. start_requests()里模拟登录成功，获取的登录状态Cookie由Scrapy管理，
        # （注意，需要在settings.py里启用 COOKIES_ENABLED（默认启用）
        # 即可直接发送其他需要登录权限的页面请求，并交给指定回调函数解析
        url_list = ["http://www.renren.com/327550029/profile"]
        for url in url_list:
            yield scrapy.Request(url, callback = self.parse_page)

    # 解析响应，处理数据
    def parse_page(self, response):
        with open("myrenren.html", "w") as f:
            f.write(response.body)

