#coding:utf-8


import scrapy


class RenrenSpider(scrapy.Spider):
    name = "renren2"
    allowed_domians = ["renren.com"]
    start_urls = [
        "http://www.renren.com/327550029/profile",
        "http://www.renren.com/410043129/profile"
    ]

    cookies = {
        "anonymid" : "j7wsz80ibwp8x3",
        "_r01_" : "1",
        "ln_uact" : "mr_mao_hacker@163.com",
        "depovince" : "GW",
        "ick_login" : "f7797cc0-a32e-485e-8489-ddb8f82a7059",
        "first_login_flag" : "1",
        "ln_hurl" : "http://hdn.xnimg.cn/photos/hdn121/20180415/1020/main_rHkm_0aac00000249195a.jpg",
        "loginfrom" : "syshome",
        "ch_id" : "10016",
        "wp_fold" : "0",
        "JSESSIONID" : "abc2PDs6fNLVe8Uu2Remw",
        "jebecookies" : "cfedffe2-24e9-4e8c-903e-6afb5c794046|||||",
        "_de" : "BF09EE3A28DED52E6B65F6A4705D973F1383380866D39FF5",
        "p" : "4c0fb45df758dfda72b89e109319b0d89",
        "t" : "49f6554231403675f1a0d73179c1572c9",
        "societyguester" : "49f6554231403675f1a0d73179c1572c9",
        "id" : "327550029",
        "xnsid" : "fb31b3f7"
    }

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, headers = self.headers, callback = self.parse)
            #yield scrapy.Request(url, cookies = self.cookies, callback = self.parse)


    def parse(self, response):
        file_name = response.xpath("//head/title/text()").extract_first()
        with open(file_name, "w") as f:
            f.write(response.body)



