import pygame
from pygame.math import *
import math


class Ship:
    
    def __init__ (self):
        #Velocity of the Ship
        self.velocity = Vector2(0,0)

        #Aceleration of the ship
        self.acceleration = Vector2(0,0)

        #Position on the screen
        self.position = Vector2(720,400)

        """Confused about what is direction in this system I tried to 
        use the front of the ship as direction by subtracting the Frontposition
        with the position."""
        #self.Frontposition = Vector2(self.position.x+40,self.position.y)

        self.direction = Vector2(math.cos(0),math.sin(0))

        #Mass of the sheep. Random value
        self.mass = 20

        #Force "added" when pressed the key 
        self.force = 1

        self.frontVertice = Vector2(760,400)

        self.leftVertice = Vector2(700,420)

        self.rightVertice = Vector2(700,380)

        self.time = 0
    #Renders the sheep
    """It's a polygon and each row corresponds to one of the vertices"""
    def Render(self, screen):
        pygame.draw.polygon(screen, (0,255,0),
        #Down Vertice
        [self.leftVertice,
        #Up Vertice
        self.rightVertice,
        #Front Vertice
        self.frontVertice])

    #Updates the position of the sheep
    """For some reason you can't sum Vector soo you need to use the position.x
    """
    def Update(self):
        if(self.force > 0) : 
            self.force = 0
        self.acceleration = 0 * self.direction
        #if(self.velocity>0):
        self.velocity = self.velocity + (self.acceleration * 0.2) 
        self.position = self.position + (self.velocity* 0.2) 
        self.frontVertice = self.frontVertice + (self.velocity* 0.2) 
        self.leftVertice = self.leftVertice + (self.velocity* 0.2) 
        self.rightVertice = self.rightVertice + (self.velocity* 0.2) 

    #Gives velocity
    """Calculates the velocity by adding the current velocity with the 
    acceleration multiplied by the time(time still in development) and 
    multiplies by the angle = 1(supposed to me the cos(time still in development))"""
    def MoveFront (self):
        self.force = 5
        self.direction = pygame.math.Vector2.normalize(self.frontVertice-self.position)
        self.acceleration = (self.force/self.mass) * self.direction
        self.velocity = self.velocity + (0.5 * self.acceleration * 0.2)

    #Gives velocity
    """Calculates the velocity by adding the current velocity with the 
    acceleration multiplied by the time(time still in development) and 
    multiplies by the angle = -1(supposed to me the cos(time still in development))"""
    def MoveBack(self):
        self.force = 5
        self.direction = pygame.math.Vector2.normalize(self.frontVertice-self.position)*-1
        self.acceleration = (self.force/self.mass) * Vector2(-1,0)
        self.velocity = self.velocity + (self.acceleration * 0.2)
    
    def RotateLeft(self):
        relPos = Vector2(0,0)
        relPos = self.frontVertice - self.position
        #print(relPos)
        relPos = Vector2((relPos.x  *math.cos(math.radians(60))),(relPos.x *math.sin(math.radians(60))))
        # print(relPos)
        self.frontVertice = self.position + relPos
        #print(self.frontVertice.y)
        rilPos = self.leftVertice - self.position
        rilPos = ((rilPos.x  *math.cos(60)),(rilPos.y *math.sin(60)))
        self.leftVertice = relPos + self.position
        ralPos = self.rightVertice - self.position
        ralPos = ((ralPos.x  *math.cos(10)),(ralPos.y *math.sin(60)))
        self.rightVertice = ralPos + self.position
        
    # def UpdateRot():
    #     self.rotPos = self.rotPos+ self.rotVel
