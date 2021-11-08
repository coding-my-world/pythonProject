# 崔浩然
# 时间:2021/10/31 21:53
# 功能:
import pygame
from time import sleep

WIN_WIDTH = 400   # 窗口宽度
WIN_HEIGHT = 600  # 窗口高度
# 1.初始化游戏
pygame.init()

# 2.创建游戏窗口
window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

# 设置游戏标题
pygame.display.set_caption('mygame')
window.fill((255, 255, 255))
pygame.display.flip()

# 1显示静态球
y = 100
r = 50
y_speed = 2
pygame.draw.circle(window, (255, 0, 0), (100, y), r)
pygame.display.update()
count=0
while True:
    for event in pygame.event.get():
        # 鼠标事件
       
        if event.type == pygame.QUIT:
            exit()
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            print('鼠标按下',event.pos)
            mx,my=event.pos  # 取出鼠标的x坐标和y坐标
        if event.type == pygame.MOUSEBUTTONUP:
            print('鼠标弹起')
        
        if event.type == pygame.MOUSEMOTION:
            print('鼠标移动')
            
        #  键盘事件
        if event.type == pygame.KEYDOWN:
            print('按键被按下', event.key, chr(event.key))
            
        if event.type == pygame.KEYUP:
            print('按钮弹起')