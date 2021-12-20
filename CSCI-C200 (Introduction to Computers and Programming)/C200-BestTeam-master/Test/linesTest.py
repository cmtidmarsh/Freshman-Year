import pygame as pg
import sys
from Shapes import Rectangle
from Shapes import Polygon
from Shapes import Circle
import random as rn
import numpy as np


#===================A Few Color Options: Clare====================
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
ORANGE = (255, 128, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (127, 0, 255)
PINK = (225, 0, 255)


LIGHTRED = (255, 102, 102)
LIGHTORANGE = (225, 178, 102)
LIGHTYELLOW = (255, 255, 102)
LIGHTGREEN = (102, 255, 102)
LIGHTBLUE = (102, 178, 255)
LIGHTPURPLE = (178, 102, 255)
LIGHTPINK = (225, 102, 178)

#==============LYDIA WAS HERE. Did randomly generating colors=========
colorChoices = [LIGHTPINK, LIGHTPURPLE, LIGHTBLUE, LIGHTGREEN, LIGHTYELLOW, LIGHTORANGE, LIGHTRED, PINK, PURPLE, BLUE, GREEN, YELLOW, ORANGE, RED, WHITE]


#-------------------------------------and gaps and movement---
def lineGeneration(y):

    #generating random gap position
    gapPos = rn.randint(1,400)
    gapSize = 40

    #left side of the gap
    leftLine = Rectangle((0,y),rn.choice(colorChoices),gapPos,2)

    #right side of the gap
    x = gapPos+gapSize
    rightLine = Rectangle((x,y),rn.choice(colorChoices),500-x,2)

    return [leftLine, rightLine]



def main():

    display = 500, 750
    screen = pg.display.set_mode((display))
    caption = pg.display.set_caption("Rainbow Runner")

    screen.fill(BLACK)


    #---------------Instructions------------
    pg.font.init()
    instructionbutton = Rectangle((5,5),WHITE, 30, 60)
    font = pg.font.SysFont(None, 15)
    text = font.render("Instructions", True, BLACK)
    screen.blit(text, (7, 12))

    #-----------------------------------------

    #sprite
    sp = Rectangle((250,20),WHITE,20,20)
    sp.draw(screen)

    #test line
    # line = Rectangle((0,700),GREEN,2,500)
    # line.draw(screen)

    #list of lines, starting y at 100
    lines = []
    y = 100

    #generating lines
    for i in range(11):
        #generate a line at y and add to y
        lines.append(lineGeneration(y))
        y += 60
    
    leftLines = []
    rightLines = []
    for line in lines:
        for index in range(len(line)):
            #get the left and right line
            if index == 0: leftLines.append(line[index])  
            else: rightLines.append(line[index])
    
    print(len(leftLines))
    print(len(rightLines))
    #speeds
    xspeed = 1/2
    yspeed = 2

    #detecting if the sprite is on a line
    onLine = False
    while True:

        pg.time.wait(4)
        pg.event.pump()

        instructionbutton.draw(screen)
        screen.blit(text, (7, 12))
        
        #quit
        if pg.event.get(pg.QUIT): break
        
        #instructions printing button
        if pg.event.get(pg.MOUSEBUTTONDOWN):
            if instructionbutton.rectangle.collidepoint(pg.mouse.get_pos()):
                with open('Documentations/instructions.txt', 'r') as f:
                    print(f.read())
            
        keys = pg.key.get_pressed()

        #the sprite moves slower in air and faster when landed
        if keys[pg.K_LEFT]: sp.move(-(xspeed*4),0) if onLine else sp.move(-xspeed,0)
        if keys[pg.K_RIGHT]: sp.move((xspeed*4),0) if onLine else sp.move(xspeed,0)

        screen.fill(BLACK)

        for i in range(len(leftLines)):

            #remove = False

            leftLines[i].draw(screen)
            rightLines[i].draw(screen)

            # if sprite hits a line
            if sp.rectangle.bottom >= leftLines[i].rectangle.top and (sp.rectangle.left <= leftLines[i].rectangle.right or sp.rectangle.right >= rightLines[i].rectangle.left):
                #sp.rectangle.bottom = leftLine.rectangle.top
                yspeed = 0
                onLine = True
                
            if sp.rectangle.bottom >= leftLines[i].rectangle.top and sp.rectangle.left >= leftLines[i].rectangle.right and sp.rectangle.right <= rightLines[i].rectangle.left:

                # print("Rightline Left side:",rightLines[i].rectangle.left)
                # print("Sprite right side:",sp.rectangle.right)
                yspeed = 2
                onLine = False
                #remove = True
            
            # if remove: 
            #     # leftLines.remove(leftLines[i])
            #     # rightLines.remove(rightLines[i])
            #     onLine = False

        if sp.rectangle.y >= 720: sp.rectangle.y = 1
        
        #stop the sprite from going off screen
        if sp.rectangle.left <= 0: sp.rectangle.left = 0
        if sp.rectangle.right >= 500: sp.rectangle.right = 500
        
        #sprite naturally drops
        if onLine: sp.move(0,0)
        else: sp.move(0,2)

    

        sp.draw(screen)      
            
        pg.display.flip()


if __name__ == "__main__":

    main()