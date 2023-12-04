import pygame
import os
import random as r
import time as tt
import sys
width,height = 1400,750
win = pygame.display.set_mode((width,height))
pygame.display.set_caption("SOLAR STRIKER")
pygame.font.init()

f1 = pygame.font.SysFont('comicsans', 20)
f3 = pygame.font.SysFont('comicsans', 64)

fps = 60
sp_w = 150
sp_h = 135

yellow_sp_im = pygame.image.load(os.path.join('Assets','spaceship_yellow.png'))
yellow_sp_im = pygame.transform.scale(yellow_sp_im,(sp_w,sp_h))
yellow_sp_im = pygame.transform.rotate(yellow_sp_im,90)
red_sp_im = pygame.image.load(os.path.join('Assets','spaceship_red.png'))
red_sp_im = pygame.transform.scale(red_sp_im,(sp_w,sp_h))
red_sp_im = pygame.transform.rotate(red_sp_im,270)

space = pygame.image.load(os.path.join("Assets","space.png"))
space = pygame.transform.scale(space,(1400,750))

bomb = pygame.image.load(os.path.join('Assets','bomb.png'))
bomb = pygame.transform.scale(bomb,(sp_w,sp_h))

def draw(yellow,red):
    win.blit(space,(0,0))
    score = f1.render(f'Score = {samay1}', 1, (255,255,255))
    win.blit(score,(20,5))
    win.blit(yellow_sp_im,(yellow.x, yellow.y))
    win.blit(red_sp_im,(red.x, red.y))
    pygame.display.update()

def check(yellow,red):
    global run
    x1 = yellow.x
    y1 = yellow.y
    x2 = red.x
    y2 = red.y
    if x1-60<x2<x1+60 and y1-60<y2<y1+60:
        run=False
        x3=(x1+x2)/2
        y3 = (y1+y2)/2
        win.blit(bomb, (x3,y3))
        game_over_text = f3.render("Game Over", True, (255, 255, 255))
        win.blit(game_over_text, (width // 2 - 120, height // 2))
        run = False
        pygame.display.update()
        pygame.time.wait(2000)
        pygame.quit()
        sys.exit()

def move_yellow(keys,yellow):
    global st
    if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and yellow.x>50:
        st = tt.time()
        yellow.x-=10
    if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and yellow.x<1250:
        st = tt.time()
        yellow.x+=10

    if (keys[pygame.K_UP] or keys[pygame.K_w]) and yellow.y>50:
        st = tt.time()
        yellow.y-=10
    if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and yellow.y<580:
        st = tt.time()
        yellow.y+=10

def move_red(red,samay,yellow):
   global run
   num1 = r.randint(1,2)
   num2 = r.randint(1,2)
   s1 = r.randint(1,50)
   s2 = r.randint(1,50)
   if samay!=5:
    if num1==1:
        if 50<red.x+s1<1250:
         red.x = red.x + s1
    elif num1==2:
        if 50 < red.x - s1 < 1250:
          red.x = red.x - s1
    if num2==1:
        if 50 < red.y + s2 < 580:
          red.y = red.y + s2
    elif num2==2:
        if 50 < red.y - s2 < 580:
          red.y = red.y - s2
   else:
        win.blit(bomb,(red.x,red.y))
        win.blit(bomb, (yellow.x, yellow.y))
        game_over_text = f3.render("Game Over", True, (255, 255, 255))
        win.blit(game_over_text, (width // 2 - 120, height // 2))
        run=False
        pygame.display.update()
        pygame.time.wait(2000)
        pygame.quit()
        sys.exit()


def move(keys,yellow,red):
    move_yellow(keys,yellow)
    move_red(red,samay,yellow)
    check(yellow,red)
def main():
    global st
    st = tt.time()
    global run
    global samay
    global samay1
    yellow = pygame.Rect(50,375, sp_w, sp_h)
    red = pygame.Rect(1250,375, sp_w, sp_h)
    clock = pygame.time.Clock()
    run = True
    samay1 = 0
    while run:
        ct = tt.time()
        samay = int(ct-st)
        x1 = red.x
        x2 = yellow.x
        y1 = red.y
        y2 = yellow.y
        d = ((x2-x1)**2 + (y2-y1)**2)**0.5
        d=int(d)
        if 100>d>0:
            a = 10
        elif 300>d>100:
            a = 5
        elif 500>d>300:
            a = 3
        elif 700>d>500:
            a = 2
        elif 800>d>700:
            a = 1
        elif d>800:
            a=0
        samay1 = samay1+a
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
        draw(yellow,red)
        keys = pygame.key.get_pressed()
        move(keys,yellow,red)
    pygame.quit()

if __name__ == "__main__":
    main()


