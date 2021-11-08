# 崔浩然
# 时间:2021/11/1 10:32
# 功能
import pygame

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

font = pygame.font.Font('images/方正粗黑宋简体.ttf', 30)
# 1. 确定按钮
bx1, by1, bw, bh = 30, 100, 100, 50
pygame.draw.rect(window, (255, 0, 0), (bx1, by1, bw, bh))
text1 = font.render('ok', True, (255, 255, 255))
tw1, th1 = text1.get_size()
tx1 = bx1 + bw / 2 - tw1 / 2
ty1 = by1 + bh / 2 - th1 / 2
window.blit(text1, (tx1, ty1))

# 2.取消按钮
bx2, by2 = 30, 200
pygame.draw.rect(window, (0, 255, 0), (bx2, by2, bw, bh))
text2 = font.render('cancel', True, (255, 255, 255))
tw2, th2 = text1.get_size()
tx2 = bx2 + bw / 2 - tw2 / 2
ty2 = by2 + bh / 2 - th2 / 2
window.blit(text2, (tx2 - 22, ty2))
pygame.display.update()
count = 0
while True:
    for event in pygame.event.get():
        # 鼠标事件
        if event.type == pygame.QUIT:
            exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = event.pos
            # 是否点击了确定按钮
            if bx1 <= mx <= bx1 + bw and by1 <= my <= by1 + bh:
                pygame.draw.rect(window, (200, 200, 200), (bx1, by1, bw, bh))
                window.blit(text1, (tx1, ty1))
                print('ok button has been push')
                pygame.display.update()
            # 是否点击了取消按钮
            if bx2 <= mx <= bx2 + bw and by2 <= my <= by2 + bh:
                print('cancel button has been click')
                pygame.draw.rect(window, (200, 200, 200), (bx2, by2, bw, bh))
                window.blit(text2, (tx2 - 22, ty2))
                pygame.display.update()
