import pygame
from pygame.math import Vector2
from Spaceship import *
import time

def Play (screen):
    #Color of the screen
    screen.fill((0,0,20))

    #Creates the spaceship
    ship = Ship()



    while(True):
        #Checks for events
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                exit()
        #Gets the pressed key
        pressedKey =  pygame.key.get_pressed()

        #Checks if the pressed key is W
        if pressedKey[pygame.K_w]:
            #Calls the MoveFront function
            ship.MoveFront()
        if pressedKey[pygame.K_s]:
            #Calls the MoveBack function
            ship.MoveBack()
        if pressedKey[pygame.K_a]:
            ship.RotateLeft()

        #Cleans the screen 
        screen.fill((0,0,20))
        #Calls the render function
        """Needs to pass the screen as argument or else the system doesn't
        know where to print"""
        ship.Render(screen)
        #Constant update
        """If we don't use this function the system will only render when we
        press keys, but with this function we will do all the movement"""
        ship.Update()
        #ship.UpdateRot()


        pygame.display.flip()
