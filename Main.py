import pygame
from pygame.math import Vector2
import pygame.freetype


from Spaceship import *
import Game




def main():

    pygame.init()

    res = (1080,720)

    my_font = pygame.freetype.Font("NotoSans-Regular.ttf", 24)

    screen = pygame.display.set_mode(res)

    screen.fill((0,0,20))

    my_font.render_to(screen, (480,275), "Play", (255,255,0))
    my_font.render_to(screen, (480,315), "Quit", (255,255,0))
    pygame.draw.rect(screen, (255, 255, 0), (450,270,100,30), 4)
    pygame.draw.rect(screen, (255, 255, 0), (450,310,100,30), 4)


    while(True):
        mp = pygame.mouse.get_pos()
        mb = pygame.mouse.get_pressed()
        for event in pygame.event.get():
            
            if(event.type == pygame.QUIT):
                exit()

        mp = pygame.mouse.get_pos()
        mb = pygame.mouse.get_pressed()    

        screen.fill((0,0,20))



        my_font.render_to(screen, (480,275), "Play", (255,255,0))
        my_font.render_to(screen, (480,315), "Quit", (255,255,0))
        pygame.draw.rect(screen, (255, 255, 0), (450,270,100,30), 4)
        pygame.draw.rect(screen, (255, 255, 0), (450,310,100,30), 4)

        if(mp[0] >= 450 and mp[0] <= 550 ):
            if (mp[1] >= 270 and mp[1] <= 300):
                if(mb[0]):
                    Game.Play(screen)
            elif ((mp[1] >= 310 and mp[1] <= 340)and mb[0]):
                exit()


        pygame.display.flip()


main()