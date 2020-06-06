import pygame
from pygame.math import Vector2


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

        #Mass of the sheep. Random value
        self.mass = 20
        #Force "added" when pressed the key 
        self.force = 1
    #Renders the sheep
    """It's a polygon and each row corresponds to one of the vertices"""
    def Render(self, screen):
        pygame.draw.polygon(screen, (0,255,0),
        #Down Vertice
        [(self.position.x-20,self.position.y-20),
        #Up Vertice
        (self.position.x-20,self.position.y+20),
        #Front Vertice
        (self.position.x+40,self.position.y)])

    #Updates the position of the sheep
    """For some reason you can't sum Vector soo you need to use the position.x
    """
    def Update(self):
        self.position.x = self.position.x + self.velocity.x

    #Gives velocity
    """Calculates the velocity by adding the current velocity with the 
    acceleration multiplied by the time(time still in development) and 
    multiplies by the angle = 1(supposed to me the cos(time still in development))"""
    def MoveFront (self):
        self.acceleration.x = (self.force/self.mass)
        self.velocity.x = self.velocity.x + (0.5 * self.acceleration.x * 0.2)*1

    #Gives velocity
     """Calculates the velocity by adding the current velocity with the 
    acceleration multiplied by the time(time still in development) and 
    multiplies by the angle = -1(supposed to me the cos(time still in development))"""
    def MoveBack(self):
        self.velocity.x = self.velocity.x + (0.5 * self.acceleration.x * 0.2)*-1