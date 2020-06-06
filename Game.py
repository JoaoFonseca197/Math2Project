import pygame
from pygame.math import Vector2
from Spaceship import *

def Play (screen):
    screen.fill((0,0,20))
    ship = Ship()
    while(True):
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                exit()
        pressedKey =  pygame.key.get_pressed()
        if pressedKey[pygame.K_w]:
            ship.MoveFront()
            ship.Render(screen)
        if pressedKey[pygame.K_s]:
            ship.MoveBack()
            ship.Render(screen)
        screen.fill((0,0,20))
        ship.Render(screen)
        ship.Update()


        pygame.display.flip()
