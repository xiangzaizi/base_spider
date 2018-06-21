# -*- coding:utf-8 -*-
"""ajax提交的获取数据
如何抓包获取的数据？步骤重要
# E:\itcast\第八阶段_大猫\Python爬虫-第02天（请求处理和JS逆向工程与urllib2高级）\video
"""
import urllib
import urllib2



def send_request():
    # 发送请求url
    base_url = "https://movie.douban.com/j/chart/top_list?"
    # 查询字符串参数, 也是通过抓包查找出来的
    query_data = {'type': '24',
        'interval_id': '100:90',
        'action': '',
        'start': '0',
        'limit': '20'
    }
    query_str = urllib.urlencode(query_data)

    full_url = base_url + query_str

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}

    request = urllib2.Request(full_url, headers=headers)
    response = urllib2.urlopen(request).read()

    print(response)


if __name__ == '__main__':
    send_request()

