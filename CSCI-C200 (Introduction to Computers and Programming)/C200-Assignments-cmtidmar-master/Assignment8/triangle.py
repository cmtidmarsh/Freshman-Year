import pygame, sys
import math
from pygame.locals import *
import random as rn
pygame.init()

BLUE = (0,0,255)
WHITE = (255,255,255)


DISPLAYSURF = pygame.display.set_mode((500, 400), 0, 32)

pygame.display.set_caption('S-Triangle')


def triangle(loc,width):
    """
    Takes in a location to draw the triangle, and width of each side of the 
    the equilateral triangle. 

    Follow the image presented in the documentation. 

    Return a tuple of 3 points, representing the triangle. 
    """
    # TODO: Implement function
    x, y = loc
    left = (loc)
    right = x + width, y
    bottom = (x+width/2), (y + math.sqrt(width**2 - ((width/2)**2)))
    return (left, right, bottom)
    
    
DISPLAYSURF.fill(WHITE)

#Draws Triangle
#(triangle(loc,w)) is a tuple of tuples...)
def draw_triangle(loc, w):
    pygame.draw.polygon(DISPLAYSURF, BLUE , (triangle(loc,w)),1)

#INPUT location and width
#RETURN nothing -- follows algorithm
def s(loc,width):
    """
    Given the starting drawing location, and width of each side of the triangle.

    Complete the recursive function.
    """
    # TODO: Implement Function
    x, y = loc
    if width > 1:
#         s(bottomTriangle, width/2)
#         s(leftTriangle, width /2)
#         s(rightTriangle, width /2)
        draw_triangle(loc, width)
        s(loc, width/2)
        s((x+width/2, y), width/2)
        s((x+width/4, y + (math.sqrt(width**2 - (width/2)**2))/2), width/2)


s((10,10),440)

while True:
    pygame.draw.rect(DISPLAYSURF, (0, 0, 0), [0, 0, 500, 400], 2) # Used to show the bounds
    for event in pygame.event.get():
         if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
	
