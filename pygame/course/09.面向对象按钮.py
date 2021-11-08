# 崔浩然
# 时间:2021/11/1 18:36
# 功能
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
count=0
while True:
    for event in pygame.event.get():
        # 鼠标事件
        if event.type == pygame.QUIT:
            exit()