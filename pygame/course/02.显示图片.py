# 崔浩然
# 时间:2021/10/30 21:05
# 功能：显示图片
import pygame

# 1.初始化操作
pygame.init()

# 2.创建游戏窗口
window = pygame.display.set_mode((400, 600))

# 设置游戏标题
pygame.display.set_caption('显示图片')

# 设置背景颜色
window.fill((255, 255, 255))

# 加载图片
image1 = pygame.image.load('images/img_1.png')
# 渲染图片 blit(渲染对象，坐标）
window.blit(image1, (0, 0))

# 操作图片
# 1）获取图片大小
w, h = image1.get_size()

window.blit(image1, (400 - w, 600 - h))

# 旋转和缩放
# scale（缩放对象，目标大小）
new1 = pygame.transform.scale(image1, (100, 100))
window.blit(new1, (210, 0))

# rotozoom(缩放/旋转对象，旋转角度，缩放比例)
new2 = pygame.transform.rotozoom(image1, 0, 0.5)
window.blit(new2, (0, 200))

# 刷新显示界面
pygame.display.flip()  # 第一次刷新
# pygame.display.update() 第二次之后刷新

# 3.让游戏保持运行状态
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
