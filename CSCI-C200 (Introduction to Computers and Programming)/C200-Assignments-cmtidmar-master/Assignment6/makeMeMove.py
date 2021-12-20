import pygame
import sys
import random as rn

 
BLACK  = (  0,   0,   0)
WHITE  = (255, 255, 255)
BLUE   = (  0,   0, 255)
GREEN  = (  0, 255,   0)
RED    = (255,   0,   0)
YELLOW = (255, 255,   0)

DARKGREEN = (0, 51, 0)
DARKYELLOW = (153, 153, 0)
LIGHTBLUE = (204, 255, 255)
ORANGE = (255, 128, 0)


def main():
    pygame.init()

    size = width, height = [300, 300]
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("C200 CHANGE")
    color = RED

    r = pygame.Rect(10, 10, 10, 10)
    x = 0 #Starting position x
    y = 0 #Starting position y
    changeX = rn.randint(1, 5)
    changeY = rn.randint(1, 5) * -1

    while True:
        pygame.time.wait(40)
        
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                pygame.quit()
                sys.exit()

        r.x += changeX
        r.y += changeY

        if r.y > height:
            changeX = rn.randint(1, 5) if changeX > 0 else rn.randint(1, 5) * -1
            changeY = rn.randint(1, 5) * -1
            color = DARKGREEN
        elif r.y < 0:
            changeX = rn.randint(1, 5) if changeX > 0 else rn.randint(1, 5) * -1
            changeY = rn.randint(1, 5)
            color = LIGHTBLUE
        elif r.x > width:
            changeX = rn.randint(1, 5) * -1
            changeY = rn.randint(1, 5) if changeY > 0 else rn.randint(1, 5) * -1
            color = ORANGE
        elif r.x < 0:
            changeX = rn.randint(1, 5)
            changeY = rn.randint(1, 5) if changeY > 0 else rn.randint(1, 5) * - 1
            color = DARKYELLOW

        screen.fill(WHITE)

        r.move_ip(changeX, changeY)

        pygame.draw.rect(screen, color, r)
        pygame.display.flip()

    

if __name__ == "__main__":
    main()



