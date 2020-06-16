import pygame
from pygame.math import *
from BlackHole import *
import math


class Ship:
    
    def __init__ (self):
        #Velocity of the Ship
        self.velocity = Vector2(0,0)

        #Aceleration of the ship
        self.acceleration = Vector2(0,0)

        #Position on the screen
        self.position = Vector2(720,400)
        #Mass of the sheep. Random value
        self.mass = 20

        #Force "added" when pressed the key 
        self.force = 0.5

        self.frontVertice = Vector2(740,400)

        self.leftVertice = Vector2(710,410)

        self.rightVertice = Vector2(710,390)

        self.direction = Vector2(self.frontVertice,self.position)


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
    def Update(self, BlackHole):
        if(BlackHole.magnitude <= BlackHole.radius):
            self.acceleration = 0.01 * BlackHole.normdirection
        
        else:
            self.acceleration = 0 * self.direction
        
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
        self.direction = pygame.math.Vector2.normalize(self.frontVertice-self.position)
        self.acceleration = (self.force/self.mass) * self.direction
        self.velocity = self.velocity + (self.acceleration * 0.2)

    #Gives velocity
    """Calculates the velocity by adding the current velocity with the 
    acceleration multiplied by the time(time still in development) and 
    multiplies by the angle = -1(supposed to me the cos(time still in development))"""
    def MoveBack(self):
        self.direction = pygame.math.Vector2.normalize(self.frontVertice-self.position)*-1
        self.acceleration = (self.force/self.mass) * self.direction
        self.velocity = self.velocity + (self.acceleration * 0.2)
    
    def RotateRight(self):
        relPos = self.frontVertice - self.position
        self.frontVertice = Vector2.rotate(relPos, 1)+ self.position
 
        relPos = self.leftVertice - self.position
        self.leftVertice = Vector2.rotate(relPos, 1)+ self.position

        relPos = self.rightVertice - self.position
        self.rightVertice = Vector2.rotate(relPos, 1)+ self.position
    
    def RotateLeft(self):
        relPos = self.frontVertice - self.position
        self.frontVertice = Vector2.rotate(relPos, -1)+ self.position
 
        relPos = self.leftVertice - self.position
        self.leftVertice = Vector2.rotate(relPos, -1)+ self.position

        relPos = self.rightVertice - self.position
        self.rightVertice = Vector2.rotate(relPos, -1)+ self.position


        

