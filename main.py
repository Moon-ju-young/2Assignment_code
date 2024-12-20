import pygame
import random
from math import pi
from Objects import Circles
from Collision import Collsion
import setting as s

GameQuit = False
FPS = 60
clock = pygame.time.Clock()

pygame.init()
pygame.display.set_caption("Physics Engine")

screen = pygame.display.set_mode((s.WIDTH,s.HEIGHT))
screen.fill((255,255,255))


col = Collsion()
for i in range(10):
    col.object_list.append(Circles(screen,random.randrange(20,50),random.randrange(10,1000),random.randrange(100,500),random.randrange(100,500)))
    col.object_list[i].velx = random.random()*10
    col.object_list[i].vely = random.random()*10


while not GameQuit:

    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            GameQuit = True

    for i in col.object_list:
        i.update()
    
    col.collide_all()
    col.collide_wall()

    for i in col.object_list:
        i.view()

    pygame.display.flip()
    screen.fill((255,255,255))
    clock.tick(FPS)