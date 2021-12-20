import pygame
import sys

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

def main():
    pygame.init() #Initalizing all the pygame modules
    screenSize = [750, 500]
    ourScreen = pygame.display.set_mode(screenSize) #Setting the window size
    r2 = pygame.Rect(20, 20, 40, 40) #Square
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    changeY = -5
                if event.key == pygame.K_DOWN:
                    changeY = +5
                if event.key == pygame.K_LEFT:
                    changeX = -5
                if event.key == pygame.K_RIGHT:
                    changeX = +5
                # print(event)
        ourScreen.fill(RED)
        

        r1 = [ 10, 10, 50, 50]
        r2.move_ip(changeX, changeY)
        pygame.draw.rect(ourScreen, WHITE, r1)
        pygame.draw.rect(ourScreen, (0, 255, 0), r2)
        
        pygame.draw.polygon(ourScreen, (0, 0, 255), [(30, 30), (30, 90), (90, 90)])
        pygame.display.update()
        # print(r2.x, r2.y)

if __name__ == '__main__':
    main()

