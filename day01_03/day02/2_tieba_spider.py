# -*- coding:utf-8 -*-

import urllib
import urllib2


def send_request(url):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}
    request = urllib2.Request(url, headers=headers)
    print "[INFO] 正在发送请求...." + url

    try:
        response = urllib2.urlopen(request).read()
        return response  # 返回的, 对响应的数据写到本地
    except Exception as e:
        print(e)


def write_page(html, filename):
    print('[INFO]正在写入内容' + filename)
    with open(filename, 'w') as f:
        f.write(html)


def main(tieba_name, begin_page, end_page):
    # 查询多少页的数据?
    for page in range(begin_page, end_page+1):
        base_url = "https://tieba.baidu.com/f?"
        pn = (page - 1)*50
        query_data = {'kw': tieba_name, 'pn': pn}
        query_str = urllib.urlencode(query_data)

        full_url = base_url + query_str

        filename = tieba_name + str(page) + '.html'  # 存储下来的文件名
        # 发送请求, 获取响应
        html = send_request(full_url)

        # 将响应内容存下来
        write_page(html, filename)


if __name__ == '__main__':
    tieba_name = raw_input('请输入贴吧名:')
    begin_page = int(raw_input('请输入起始页:'))
    end_page = int(raw_input('请输入结束页:'))

    main(tieba_name, begin_page, end_page)

