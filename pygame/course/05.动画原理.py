# 崔浩然
# 时间:2021/10/31 20:04
# 功能


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

# 1显示静态球
y = 100
r=50
pygame.draw.circle(window,(255, 0, 0), (100, y), 50)

while True:
    sleep(0.01)
    # 1.移动动画
    # pygame.draw.circle(window, (255, 255, 255), (100, y), 50)
    # y=y+1;
    # pygame.draw.circle(window, (255, 0, 0), (100, y), 50)
    # pygame.display.update()
    
    # 2.缩放动画
    
    pygame.draw.circle(window, (255, 255, 255), (100, y), r)
    r=r+1
    pygame.draw.circle(window, (255, 0, 0), (100, y), r)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()