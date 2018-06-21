# -*- coding:utf-8 -*-

from selenium import webdriver
driver = webdriver.PhantomJS()

driver.get("http://www.baidu.com/")
driver.save_screenshot("nbaidu.png")
data = driver.find_element_by_name("tj_trnews").text
html = driver.page_source
driver.find_element_by_name("tj_trnews").click()
driver.save_screenshot("baidu.png")
driver.find_element_by_id("ww").send_keys(u"区块链")
driver.save_screenshot("baidu.png")
driver.find_element_by_class_name("btn").click()
driver.save_screenshot("baidu.png")
driver.find_element_by_xpath("//div[@id=1]//a").click()
driver.save_screenshot("baidu.png")

# 2. driver.window_handles
driver.switch_to_window(driver.window_handles[1])
driver.save_screenshot("baidu.png")
driver.switch_to_window(driver.window_handles[0])
# html = driver.page_source

# driver.title
print driver.title
driver.switch_to_window(driver.window_handles[1])
print driver.title # 获取当前标签页的标题
print driver.current_url # 获取当前标签页的url地址
print driver.get_cookies() # 获取Cookies
driver.close() # 关闭当前标签
driver.quit() # 退出浏览器
