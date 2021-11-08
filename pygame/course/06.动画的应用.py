# 崔浩然
# 时间:2021/10/31 21:34
# 功能：
import pygame
from time import sleep
WIN_WIDTH = 400  # 窗口宽度
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
while True:
    window.fill((255, 255, 255))
    y+=y_speed
    
    # 检测边界
    if y>= WIN_HEIGHT-r:
        y_speed=y_speed * -1
        
    if y<=r:
        y_speed = y_speed * -1
        
    pygame.draw.circle(window, (255, 0, 0), (100, y), r)
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
