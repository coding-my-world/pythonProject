# 崔浩然
# 时间:2021/10/31 10:53
# 功能：画图形
import pygame
# 1.初始化操作
pygame.init()

# 2.创建游戏窗口
window = pygame.display.set_mode((400,600))

# 设置游戏标题
pygame.display.set_caption('mygame')
window.fill((255,255,255))
# 画直线
# line（画在哪，线的颜色，线的起点，线的终点，线宽=1）
pygame.draw.line(window, (255, 0, 0), (10, 20), (200, 20))

#画折线
#lines(花在哪，线的颜色，是否闭合,多个点，线宽）
points=[(10, 300), (100, 160), (180, 260), (300, 100)]
pygame.draw.lines(window, (0, 255, 0), False, points, 3)

#画圆
#circle(画在哪，线的颜色,圆心坐标，半径，线宽）
pygame.draw.circle(window, (0, 0, 255), (200, 250), 100, 2)

# 4.画矩形
# rect(画在哪， 线的颜色， 矩形范围， 线宽）
pygame.draw.rect(window, (120, 20, 60), (30, 70, 100, 200), 2)

# 5.画椭圆
# ellipse(画在哪， 线的颜色， 矩形范围， 线宽）
pygame.draw.ellipse(window, (255, 0, 0), (30, 70, 100, 200), 2)

# 6. 画弧线
# arc(画在哪， 线的颜色， 矩形范围， 起始弧度， 终止弧度）
pygame.draw.arc(window, (0, 0, 0), (30, 70, 100, 200), 0, 3.1415926, 4)
pygame.display.flip()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()