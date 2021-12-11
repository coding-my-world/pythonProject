# 崔浩然
# 时间:2021/11/30 22:32
# 功能
import pygame
from pygame.locals import *
class Plane(object):
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('images/me1.png')
        self.x = 250
        self.y = 597
       
    def display(self):
        self.screen.blit(self.image, (self.x, self.y))
        if self.x < -51:
            self.x = -51
        elif self.x > 589:
            self.x = 589
        elif self.y < 0:
            self.y = 0
        elif self.y > 649:
            self.y = 649
        return False
    
    def hang_move(self, move_x):
        self.x += move_x
    
    def lie_move(self, move_y):
        self.y += move_y
    

if __name__ == '__main__':
    move_x, move_y = 0, 0
    screen = pygame.display.set_mode((480, 700), 0, 32)
    background = pygame.image.load('images/background.png')
    pygame.display.set_caption("飞机大战")
    interface_background = pygame.image.load('images/background.png')
    hero = Plane(screen)
    pygame.init()
    n_start = True
    while True:
        while n_start:
            screen.blit(interface_background, (0, 0))
            
            buttons = pygame.mouse.get_pressed()
            x, y = pygame.mouse.get_pos()
            if 170 <= x <= 470 and 350 - 91 <= y <= 350:
                if buttons[0]:
                    n_start = False
            
            elif 170 <= x <= 470 and 350 + 91 <= y <= 350 + 91 + 91:
                if buttons[0]:
                    exit()
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == QUIT:
                    exit()
        screen.blit(background, (0, 0))
        n = hero.display()
        
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            if event.type == KEYDOWN:
                if event.key == K_a or event.key == K_LEFT:
                    move_x = -20
                    hero.hang_move(move_x)
                elif event.key == K_d or event.key == K_RIGHT:
                    move_x = 20
                    hero.hang_move(move_x)
                elif event.key == K_w or event.key == K_UP:
                    move_y = -20
                    hero.lie_move(move_y)
                elif event.key == K_s or event.key == K_DOWN:
                    move_y = 20
                    hero.lie_move(move_y)
        
        pygame.display.update()
        
      

