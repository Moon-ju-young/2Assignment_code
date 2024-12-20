import pygame
from math import sin, cos, pi, atan2, sqrt
import setting as s

class Objects:
    mass = 0     # 최댓값 1000
    x = 0
    y = 0
    velx = 0
    vely = 0
    shape_type = None

    def update (self) -> None:
        self.x += self.velx
        self.y += self.vely
    
        angle = atan2(self.vely,self.velx)
        vel = sqrt(self.velx**2 + self.vely**2)
        if (vel - s.FRICTION) < 0:
            vel = 0
        else:
            vel -= s.FRICTION
        self.velx = vel * cos(angle)
        self.vely = vel * sin(angle)

    def view (self) -> None:
        pass

class Circles(Objects):
    def __init__(self,screen,radius,mass,x,y):
        self.screen = screen
        self.radius = radius
        self.mass = mass
        self.x = x
        self.y = y
        self.velx = 0
        self.vely = 0
        self.shape_type = "Circle"

    def update(self):
        return super().update()

    def view(self):
        pygame.draw.circle(self.screen,(250-self.mass/4,0,0),(self.x,self.y),self.radius)