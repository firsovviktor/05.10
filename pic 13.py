import pygame
import math
import random
from pygame.draw import *

def draw():
    background()
    tree(400, 100, 80)
    tree(270, 0, 30)
    tree(260, 260, 40)
    tree(300, 340, 50)
    #mushroom(200, 200, 0, 2)
    sonic(200, 300)
    sonic (100, 350)
    sonic (300, 270)
    mushroom (300, 400, -1, 3)
    mushroom (60, 350, 0.2, 1)

def background():
    x = 250
    e_colour = (64, 64, 64)
    s_colour = (32, 32, 255)
    h_colour = (128, 128, 128)
    rect(screen, e_colour, (0, x, 400, 400))
    rect(screen, s_colour, (0, 0, 400, x))
    line(screen, h_colour, (0, x), (400, x))

def tree(y, x, w):
    t_colour = (200, 200, 0)
    rect(screen, t_colour, (x, 0, w, y))

def elps(x1, y1, x2, y2, a, cl):
    for i in range (400):
        for j in range (400):
            if (((x1-i)**2+(y1-j)**2)**0.5+((x2-i)**2+(y2-j)**2)**0.5<a):
                rect(screen, cl, (i, j, 1, 1))

def mushroom (x1, y1, a, s):
    w_mushroom = (255, 255, 255)
    r_mushroom = (255, 0, 0)
    h1 = 50
    w1 = 55
    h1 *= s
    w1 *= s
    elps(x1, y1, x1+h1*math.sin(a), y1-h1*math.cos(a), w1, w_mushroom)
    h2 = 50
    w2 = 60
    h2 *= s
    w2 *= s
    e1=h1*math.sin(a)
    e2=-h2*0.5*math.cos(a)
    b1=-h1*math.cos(a)
    b2=-h2*0.5*math.sin(a)
    c1=h1*math.sin(a)
    c2=h2*0.5*math.cos(a)
    d1=-h1*math.cos(a)
    d2=h2*0.5*math.sin(a)
    elps(x1+e1+e2, y1+b1+b2, x1+c1+c2, y1+d1+d2, w2, r_mushroom)
    elps(x1+e1+e2/2, y1+b1+b2/2, x1+e1+e2/2, y1+b1+b2/2, 6*s, w_mushroom)
    elps(x1+c1+2*c2/3, y1+d1+2*d2/3, x1+c1+2*c2/3, y1+d1+2*d2/3, 6*s, w_mushroom)
    elps(x1+e1, y1+b1, x1+e1, y1+b1, 6*s, w_mushroom)

def body(x, y):
    x -= 200
    y -= 200
    b_colour = (140, 140, 140)
    d_colour = (0, 0, 0)
    l_colour = (180, 180, 180)
    elps(x+200, y+200, x+270, y+200, 85, b_colour)
    elps(x+260, y+205, x+290, y+205, 35, b_colour)
    elps(x+290, y+205, x+290, y+205, 3, d_colour)
    elps(x+278, y+205, x+278, y+205, 5, d_colour)
    elps(x+285, y+202, x+285, y+202, 5, d_colour)
    elps(x+260, y+220, x+270, y+220, 15, l_colour)
    elps(x+270, y+215, x+275, y+215, 10, l_colour)
    elps(x+200, y+220, x+210, y+220, 15, l_colour)

def spike(x, y):
    for i in range (20):
        a = random.randint(0, 60)
        b = random.randint(-10, 20)
        polygon(screen, (0, 0, 0), [[x+a, y+b], [x+a+3, y+b-60], [x+a+6, y+b]], 0)
        polygon(screen, (255, 255, 255), [[x+a, y+b], [x+a+3, y+b-60], [x+a+6, y+b]], 1)

def sonic(x, y):
    body(x, y)
    mushroom(x, y, 1, 0.5)
    mushroom(x+70, y-20, -1, 0.7)
    spike(x, y)

pygame.init()
FPS = 30
screen = pygame.display.set_mode((400, 400))

draw() # - function for drawing

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
