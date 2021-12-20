import pygame, sys
from random import randint
from Shape import Shape
from shapes import Triangle, Square, Rectangle, Circle

WHITE  = (255, 255, 255)

PINK   = (255, 192, 203)
RED    = (255,   0,   0)
ORANGE = (139,  90,   0)
YELLOW = (255, 255,   0)
GREEN  = (  0, 255,   0)
BLUE   = (  0,   0, 255)
PURPLE = (102,   0, 102)
BROWN  = (165,  42,  42)
BLACK  = (  0,   0,   0)

COLORS = [PINK, RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE, BROWN, BLACK]


def createShapes():
    shapes = []
    for i in range(randint(5, 10)):
        v = randint(1, 4)
        x, y = randint(0, 700), randint(0, 700)
        length = randint(10, 100)
        width = randint(10, 100)
        colorChoice = COLORS[randint(0, len(COLORS) - 1)]

        if v == 1:
            pass
            shapes.append(Triangle((x, y), colorChoice, length))
        if v == 2:
            shapes.append(Rectangle((x,y), colorChoice, length, width))
        if v == 3:
            shapes.append(Square((x, y), colorChoice, length))
        if v == 4:
            shapes.append(Circle((x, y), colorChoice, length))
    
    return shapes

def main():
    pygame.init()
    size = [750, 750]
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Inheritance")

    shapesToDraw = createShapes()
    for s in shapesToDraw:
        if not isinstance(s, Shape):
            print("Inheritance not done correctly")

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(WHITE)
        
        for s in shapesToDraw:
            s.draw(screen)

        pygame.display.flip()




if __name__ == "__main__":
    main()
