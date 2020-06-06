import pygame
from pygame.math import Vector2


class Ship:
    
    def __init__ (self):
        self.velocity = Vector2(0,0)
        self.acceleration = Vector2(0,0)
        self.position = Vector2(720,400)
        self.Frontposition = Vector2(self.position.x+40,self.position.y)

        self.acceleration = Vector2(0,0)
        #self.time
        # Valores quando estão a zero graus
        
        self.mass = 20
        self.force = 1
    def Render(self, screen):
        pygame.draw.polygon(screen, (0,255,0),
        [(self.position.x-20,self.position.y-20),
        (self.position.x-20,self.position.y+20),
        (self.position.x+40,self.position.y)])

    def Update(self):
        self.position.x = self.position.x + self.velocity.x

    def MoveFront (self):
        self.acceleration.x = (self.force/self.mass)
        self.velocity.x = self.velocity.x + (0.5 * self.acceleration.x * 0.2)*1
    
    def MoveBack(self):
        self.velocity.x = self.velocity.x + (0.5 * self.acceleration.x * 0.2)*-1