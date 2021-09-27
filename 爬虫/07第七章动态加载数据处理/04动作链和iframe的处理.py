# 崔浩然
# 时间:2021/9/29 7:27
# 功能:动作链和iframe的处理
from selenium import webdriver
from time import sleep
#导入动作链对应的类
from selenium.webdriver import ActionChains
bro = webdriver.Chrome(executable_path='./chromedriver.exe')
bro.get( 'https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')

#如果定位的标签是存在于iframe标签之中的则必须通过如下操作在进行标签定位
bro.switch_to_frame("iframeResult") #切换浏览器标签的作用域
div=bro.find_element_by_id("draggable")

#实例化一个动作链对象
action = ActionChains(bro)
#点击长按指定的标签
action.click_and_hold(div)

for i in range(5):
    #perform()立即执行动作链操作
    action.move_by_offset(17,0).perform()
    sleep(0.5)
bro.quit()
