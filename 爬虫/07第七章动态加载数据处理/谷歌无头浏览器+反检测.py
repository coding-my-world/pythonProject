# 崔浩然
# 时间:2021/9/30 9:28
# 功能：
from selenium import webdriver
from time import sleep
#实现无可视化界面的
from selenium.webdriver.chrome.options import Options
#实现规避检测
from selenium.webdriver import ChromeOptions

#实现无可视化界面的操作
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
#实现规避检测
chrome_options.add_experimental_option('excludeSwitches',['enable-automation'])

bro = webdriver.Chrome(executable_path='chromedriver.exe',options=chrome_options)

#无可视化界面（无头浏览器）
bro.get('https://www.baidu.com')

print(bro.page_source)
sleep(2)
bro.quit()
