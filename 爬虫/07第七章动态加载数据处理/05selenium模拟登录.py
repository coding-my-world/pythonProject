# 崔浩然
# 时间:2021/9/30 8:16
# 功能：selenium模拟登录
from selenium import  webdriver
from time import sleep
bro = webdriver.Chrome(executable_path='chromedriver.exe')
bro.get('https://qzone.qq.com/')

bro.switch_to.frame('login_frame')

a_tag = bro.find_element_by_id('switcher_plogin')
a_tag.click()

username= bro.find_element_by_id('u')
password = bro.find_element_by_id('p')
sleep(1)
username.send_keys('1950274892')
sleep(1)
password.send_keys('codingcode0208')
login_button = bro.find_element_by_id('login_button')
login_button.click()

sleep(3)

bro.quit()
