
#========Clare's Mockup Design=============

import pygame
import sys

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

RED = (255, 0, 0)
LIGHTRED = (255, 102, 102)
ORANGE = (255, 128, 0)
LIGHTORANGE = (225, 178, 102)
YELLOW = (255, 255, 0)
LIGHTYELLOW = (255, 255, 102)
GREEN = (0, 255, 0)
LIGHTGREEN = (102, 255, 102)
BLUE = (0, 0, 255)
LIGHTBLUE = (102, 178, 255)
PURPLE = (127, 0, 255)
LIGHTPURPLE = (178, 102, 255)
PINK = (225, 0, 255)
LIGHTPINK = (225, 102, 178)


def main():
#------------Creating Window--------------
    display = width, height = 500, 750
    screen = pygame.display.set_mode((display))
    caption = pygame.display.set_caption("Rainbow Runner Inspiration")

    screen.fill(BLACK)
#-----------------------------------------



#-----------Drawing Objects to avoid---------------
    pygame.draw.line(screen, (RED),(700,490),(350,490), 2)
    pygame.draw.line(screen, (RED),(5,490),(250,490), 2)

    pygame.draw.line(screen, (LIGHTRED),(5,450),(210,450), 2)
    pygame.draw.line(screen, (LIGHTRED),(700,450),(250,450), 2)

    pygame.draw.line(screen, (ORANGE),(5,425),(350,425), 2)
    pygame.draw.line(screen, (ORANGE),(700,425),(400,425), 2)

    pygame.draw.line(screen, (LIGHTORANGE),(5,375),(250,375), 2)
    pygame.draw.line(screen, (LIGHTORANGE),(700,375),(300,375), 2)

    pygame.draw.line(screen, (YELLOW), (700,350),(100,350), 2)
    pygame.draw.line(screen, (YELLOW), (5,350),(50,350), 2)

    pygame.draw.line(screen, (LIGHTYELLOW),(5,335),(600,335), 2)

    pygame.draw.line(screen, (GREEN),(5,300),(100,300), 2)
    pygame.draw.line(screen, (GREEN),(700,300),(150,300), 2)


    pygame.draw.line(screen, (LIGHTGREEN), (700,275),(250,275), 2)
    pygame.draw.line(screen, (LIGHTGREEN), (5,250),(250,250), 2)


    m1 = pygame.draw.line(screen, (BLUE), (70,225),(250,225), 2)
    m2 = pygame.draw.line(screen, (BLUE), (400,225),(570,225), 2)

    pygame.draw.line(screen, (LIGHTBLUE), (275, 200), (375,200), 2)
    pygame.draw.line(screen, (LIGHTBLUE), (500,200),(600,200), 2)

    pygame.draw.line(screen, (PURPLE), (0,175),(100,175), 2)
    pygame.draw.line(screen, (PURPLE), (200,175),(300,175), 2)
    pygame.draw.line(screen, (PURPLE), (400,175),(500,175), 2)
    pygame.draw.line(screen, (PURPLE), (600,175),(700,175), 2)

    pygame.draw.line(screen, (LIGHTPURPLE), (550,150),(600,150), 2)
    pygame.draw.line(screen, (LIGHTPURPLE), (450,150),(500,150), 2)
    pygame.draw.line(screen, (LIGHTPURPLE), (350,150),(400,150), 2)
    pygame.draw.line(screen, (LIGHTPURPLE), (250,150),(300,150), 2)
    pygame.draw.line(screen, (LIGHTPURPLE), (150,150),(200,150), 2)
    pygame.draw.line(screen, (LIGHTPURPLE), (50,150),(100,150), 2)

    pygame.draw.line(screen, (PINK), (475,125),(600,125), 2)
    pygame.draw.line(screen, (PINK), (275,125),(400,125), 2)
    pygame.draw.line(screen, (PINK), (75,125),(200,125), 2)

    pygame.draw.line(screen, (LIGHTPINK), (0,75),(250, 75), 2)
    pygame.draw.line(screen, (LIGHTPINK), (700,75),(275, 75), 2)
    
    #-------------------Reward--------------------------------
    # pygame.draw.rect(screen, ((255, 204, 229)), (350, 20, 20, 20))

    #---------------------------------------------------------

    clock = pygame.time.Clock()
    #-----------------Sprite----------------------------------
# class Sprite():
#     def __init__(self, x, y):

    sprite = pygame.draw.rect(screen, ((255, 102, 102)), (350, 20, 10, 10))


    #---------------------------------------------------------
    pygame.display.flip()


    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


main()
