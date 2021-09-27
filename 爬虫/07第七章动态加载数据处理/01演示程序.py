# 崔浩然
# 时间:2021/9/27 14:23
# 功能：演示selenium模块的使用
from selenium import webdriver
from time import sleep
#后面是你的浏览器驱动位置，记得前面加r'', 'r'是防止字符转义的
driver = webdriver.Chrome(r'chromedriver.exe')
#用get打开百度页面
driver.get( "http://www.baidu.com")
#查找页面的“设置"选项,并进行点击
driver.find_elements_by_link_text('设置')[0].click()
sleep(2)
##打开设置后找到“搜索设置”选项,设置为每页显示50条
driver.find_elements_by_link_text('搜索设置')[0].click()
sleep(2)
#选中每页显示50条
m=driver.find_element_by_id('nr')
sleep(2)
m.find_element_by_xpath('//*[@id="nr"]/option[3]').click()
m.find_element_by_xpath('.//option [3] ').click()
sleep(2)
#点击保存设置
driver.find_elements_by_class_name( "prefpanelgo")[0].click()
sleep(2)
#处理弹出的警告页面确定accept() 和取消dismiss()
driver.switch_to_alert().accept()
sleep(2)
#找到百度的输入框,并输入1234567
driver.find_element_by_id('kw').send_keys('1234567')
sleep(2)
#点击搜索按钮
driver.find_element_by_id('su').click()
sleep(2)
#_在打开的页面中找到“Selenium-开源中国社区”．并打开这个而面
driver.find_element_by_link_text('23456')[0].click()
sleep(3)

