# 崔浩然
# 时间:2021/10/31 9:37
# 功能：显示文字
import pygame

pygame.init()

window = pygame.display.set_mode((400,600))


pygame.display.set_caption('显示文字')
window.fill((255,255,255))

#1.创建字体对象
#字体文件路径，字号
font=pygame.font.Font("images/方正粗黑宋简体.ttf",30)

# 2.创建字体对象
#render（文字内容，True，字体颜色，背景颜色）
text=font.render('你好',True,(255,0,0),(255,255,0))

#3.渲染到窗口上
window.blit(text,(0,0))
pygame.display.flip()

# 4. 操作文字对象
#1）获取大小
w,h=text.get_size()
window.blit(text,(400-w,600-h))

#2）旋转和缩放
new_t1=pygame.transform.scale(text,(200,50))
window.blit(new_t1,(0,60))

new_t2=pygame.transform.rotozoom(text,0,2)
window.blit(new_t2,(0,120))
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
