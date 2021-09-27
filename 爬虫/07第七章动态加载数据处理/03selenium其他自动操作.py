# 崔浩然
# 时间:2021/9/28 17:33
# 功能selenium其他自动操作
from selenium import webdriver
from time import sleep
bro = webdriver.Chrome(executable_path='./chromedriver.exe')
bro.get('https://www.taobao.com/')

# 标签定位
search_input = bro.find_element_by_id('q')
search_input.send_keys('iphone')

#执行一组js程序
bro.execute_script('window.scrollTo(0,document.body.scrollHeight)')
sleep(2)
# 点击搜索按钮
button = bro.find_element_by_class_name('btn-search')
button.click()

bro.get('https://www.baidu.com')
sleep(2)

#回退
bro.back()
sleep(2)

#前进
bro.forward()
sleep(5)

bro.quit()
