# 崔浩然
# 时间:2021/10/1 10:35
# 功能：模拟12306登录
from selenium import webdriver
import time
from PIL import Image
from chaojiying import main
from selenium.webdriver import ActionChains
bro = webdriver.Chrome(executable_path='../chromedriver.exe')

bro.get('https://kyfw.12306.cn/otn/resources/login.html')
time.sleep(1)

#save screenshot就是将当前页面进行截图且保存
bro.save_screenshot(('aa.png'))

code_img_ele = bro.find_element_by_xpath('')
#确定验证码图片对应的左上角和右下角的坐标
location =code_img_ele.location  #验证码图片左上角的坐标 x ， y
print('location：',location)
size = code_img_ele.size #验证码标签对应的长和宽
print('size',size)

#左上角和右下角坐标
rangle =(
    int(location['x'],int(location['y']),int(location['x']+size['width']),int(location['y']+size['height']))
)
i=Image.open('')
code_img_name=''
#crop根据指定区域进行图片裁剪
frame=i.crop(rangle)
frame.save(code_img_name)

result = main(code_img_name)

all_list= []#存放要被点击的点的坐标 [[x1,y1],[x2,y2]]
if '|' in result:
    list_1 = result.split('|')
    count_1 = len(list_1)
    for i in range(count_1):
        xy_list = []
        x = int(list_1[i].split(',')[0])
        y = int(list_1[i].split(',')[1])
        xy_list.append(x)
        xy_list.append(y)
        all_list.append(xy_list)
else:
    x = int(result.split(',')[0])
    y = int(result.split(',')[1])
    xy_list = []
    xy_list.append(x)
    xy_list.append(y)
    all_list.append(xy_list)
print(all_list)

#遍历列表，使用动作链对每一个列表元素对应的x，y指定的位置进行点击操作
for l in all_list:
    x = l[0]
    y = l[1]
    ActionChains(bro).move_to_element_with_offset(code_img_ele,x,y)
    
bro.find_element_by_id( ' username ').send_keys('xXXXXXX')
time.sleep(2)
bro.find_element_by_id( 'password ' ).send_keys('xxXxxXx')
time.sleep(2)
bro.find_element_by_id( 'loginSub ').click()
time.sleep(10)
bro.quit()

