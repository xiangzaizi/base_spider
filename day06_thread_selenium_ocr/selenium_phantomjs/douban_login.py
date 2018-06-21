#!/usr/bin/env python
# -*- coding:utf-8 -*-

from selenium import webdriver
import time


def login(email, password):
    driver = webdriver.PhantomJS()
    print "正在获取页面"
    driver.get("https://www.douban.com/")
    # 保存页面快照
    driver.save_screenshot("douban_index.png")

    # 传入账号  密码
    driver.find_element_by_name("form_email").send_keys(email)
    driver.find_element_by_name("form_password").send_keys(password)

    # 当如果需要验证码的时候
    try:
        driver.find_element_by_id("captcha").send_keys(raw_input("请输入验证码:"))
    except:
        print "没有验证码"

    driver.find_element_by_class_name("bn-submit").click()

    time.sleep(1)
    driver.save_screenshot("douban_login.png")
    # 获取登录后的页面, 从HTML里面获取数据
    html = driver.page_source
    with open("douban.html", "w") as f:
        # 对页面的内容进行编码
        f.write(html.encode("utf-8"))


if __name__ == "__main__":
    email = "mr.mao.tony@gmail.com"
    password = "ALARMCHIME"
    login(email, password)
