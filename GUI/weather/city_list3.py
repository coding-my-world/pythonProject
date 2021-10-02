# 崔浩然
# 时间:2021/10/1 20:51
# 功能
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from time import sleep

#通过利用python的异常捕获机制和循环语句，使程序在一定时间内即使selenium执行命令失败，也会继续重复执行同一条命令多次，直到成功为止。
def smart_wait(dl_list,element_xpath,shuxin):  # 智能等待时间，60秒超时
    for i in range(60):            # 循环60次，从0至59
        if i >= 59 :               # 当i大于等于59时，打印提示时间超时
            print("timeout")
            break
        try:                       # try代码块中出现找不到特定元素的异常会执行except中的代码
            if dl_list.find_element_by_xpath('%s'%element_xpath).get_attribute('%s'%shuxin): # 如果能查找到特定的元素id就提前退出循环
                return dl_list.find_element_by_xpath('%s'%element_xpath).get_attribute('%s'%shuxin)
                break
        except:                    # 上面try代码块中出现异常，except中的代码会执行打印提示会继续尝试查找特定的元素id
            print("wait for find element")
        sleep(1)

# desired_capabilities = DesiredCapabilities.CHROME  # 修改页面加载策略
# desired_capabilities["pageLoadStrategy"] = "eager"  # 注释这两行会导致最后输出结果的延迟，即等待页面加载完成再输出
bro = webdriver.Chrome(executable_path='./chromedriver.exe')
bro.get('https://m.tianqi.com/')
dl_list = bro.find_elements_by_xpath('//*[@id="body"]/div[6]/dl')
weather_data = []


for i in range(0,7):
    #print(dl.text())
    data = {}
    
    print(smart_wait(dl_list[i], './a', 'title'))
    #weather_data.append(data)
    #print(weather_data)