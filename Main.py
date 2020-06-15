import pygame
from pygame.math import Vector2
import pygame.freetype


from Spaceship import *
import Game




def main():

    pygame.init()

    #Screen Resolution
    res = (1080,720)
    #Font
    my_font = pygame.freetype.Font("NotoSans-Regular.ttf", 24)

    screen = pygame.display.set_mode(res)

    #Color of the screen
    screen.fill((0,0,20))




    while(True):

        #Checks for events
        for event in pygame.event.get():

            if(event.type == pygame.QUIT):
                exit()


        #Gets position of the mouse
        mp = pygame.mouse.get_pos()

        #Checks if mouse got pressed
        mb = pygame.mouse.get_pressed()

        # fps = pygame.time.Clock.get_fps()
        # print(fps)


        screen.fill((0,0,20))


        #displays 2 squares with the message Play and Quit
        my_font.render_to(screen, (480,275), "Play", (255,255,0))
        my_font.render_to(screen, (480,315), "Quit", (255,255,0))
        pygame.draw.rect(screen, (255, 255, 0), (450,270,100,30), 4)
        pygame.draw.rect(screen, (255, 255, 0), (450,310,100,30), 4)

        #Checks if the position of the mouse is above the square
        if(mp[0] >= 450 and mp[0] <= 550 ):
            if (mp[1] >= 270 and mp[1] <= 300):
                #Checks if he pressed the mouse while inside the square
                if(mb[0]):
                    #Plays the game
                    Game.Play(screen)
            #Checks if he has the mouse above the square and if he pressed it
            elif ((mp[1] >= 310 and mp[1] <= 340)and mb[0]):
                exit()


        pygame.display.flip()


main()