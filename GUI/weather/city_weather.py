# 崔浩然
# 时间:2021/10/1 19:27
# 功能：爬取城市的天气信息
from selenium import webdriver
from time import sleep
#实现无可视化界面的
from selenium.webdriver.chrome.options import Options


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

def smart_wait2(dl_list,element_xpath):  #处理文本内容
    for i in range(60):
        if i >= 59 :
            print("timeout")
            break
        try:
            if dl_list.find_element_by_xpath('%s'%element_xpath).text:
                return dl_list.find_element_by_xpath('%s'%element_xpath).text
                break
        except:
            print("wait for find element")
        sleep(1)
def get_weather(city_name):
    #实现无可视化界面的操作
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    #实现规避检测
    chrome_options.add_experimental_option('excludeSwitches',['enable-automation'])
    
    bro = webdriver.Chrome(executable_path='chromedriver.exe',options=chrome_options)
    
    #无可视化界面（无头浏览器）
    bro.get('https://m.tianqi.com/')
    page_text=bro.page_source
    sleep(1)
    # 找到切换城市
    select_city = bro.find_element_by_xpath('//*[@id="body"]/div[5]/div[1]/div[1]/a')
    select_city.click()

    # 找到输入城市按钮
    input_button = bro.find_element_by_name('keyword')
    input_button.click()
    sleep(1)
    input = bro.find_element_by_id('serch_text')
    input.send_keys(city_name)
    search = bro.find_element_by_class_name('tianqi_search_btn')
    search.click()
    sleep(1)
    dl_list = bro.find_elements_by_xpath('//*[@id="body"]/div[6]/dl')
    weather_data = []
    for i in range(0,7):
        data = {}
    
        data['title'] = smart_wait(dl_list[i], './a', 'title')
        data['text'] = smart_wait2(dl_list[i], './a')
        data['text'] = data['text'].replace('\n', ' ')
        weather_data.append(data)
    return weather_data
    bro.quit()

