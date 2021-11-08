# 崔浩然
# 时间:2021/10/30 20:51
# 功能:初学pygame库
import pygame
# 1.初始化操作
pygame.init()

# 2.创建游戏窗口
window = pygame.display.set_mode((400,600))

# 设置游戏标题
pygame.display.set_caption('mygame')
# 3.让游戏保持运行状态
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
