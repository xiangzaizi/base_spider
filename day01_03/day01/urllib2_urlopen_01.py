# -*- coding:utf-8 -*-
import urllib2


def send_request():
    url = ''
    response = urllib2.urlopen(url)
    html = response.read()
    print(html)


if __name__ == '__main__':
    send_request()