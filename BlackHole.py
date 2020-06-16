import pygame
from pygame.math import Vector2

class BlackHole:

    def __init__ (self, x, y, r):
        #Variables
        self.pos = (x,y)
        self.radius = r
        self.magnitude = 0
        self.normdirection = Vector2(0,0)


    #function to draw the circles
    def Render (self, screen):
        blackholecolor = (115, 47, 193)
        pygame.draw.circle(screen, blackholecolor, self.pos, self.radius, 1)  

    #function to pull the ship towards de center of the circle
    def attraction (self, ship):
        direction = self.pos - ship.position
        self.magnitude = pygame.Vector2.magnitude(direction)
        self.normdirection = pygame.Vector2.normalize(direction)
   
    
            