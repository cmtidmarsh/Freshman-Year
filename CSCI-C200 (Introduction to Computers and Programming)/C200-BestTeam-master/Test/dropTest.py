import pygame as pg

def main():

    display = 500, 750
    screen = pg.display.set_mode((display))
    caption = pg.display.set_caption("Rainbow Runner")

    BLACK = (0,0,0)
    screen.fill(BLACK)



#---------------Instructions------------
    pg.font.init()
    instructionbutton = pg.draw.rect(screen, ((255, 204, 229)), (5, 5, 60, 30))
    font = pg.font.SysFont(None, 15)
    text = font.render("Instructions", True, BLACK)
    screen.blit(text, (7, 12))
#-----------------------------------------

    sp = pg.Rect(250,20,20,20)
    pg.draw.rect(screen,(255,255,255),sp)

    line = pg.Rect(0,700,500,20)
    pg.draw.rect(screen,(0,255,0), line)

    xspeed = 0
    yspeed = 10

    while True:

        pg.time.wait(40)
        
        if pg.event.get(pg.QUIT): break
        
        pg.event.pump()
            
        keys = pg.key.get_pressed()

                
        # if keys[pygame.K_w]: p1.move(screen,True)
                
        # if keys[pygame.K_s]: p1.move(screen,False)

        # if keys[pygame.K_UP]: p2.move(screen,True)
                
        # if keys[pygame.K_DOWN]: p2.move(screen,False)

        
        if pg.event.get(pg.MOUSEBUTTONDOWN):
            if instructionbutton.collidepoint(pg.mouse.get_pos()):
                with open('Documentations/instructions.txt', 'r') as f:
                    print(f.read())

            

        
        screen.fill(BLACK)

        pg.draw.rect(screen,(0,255,0), line)

        sp.move_ip(xspeed,yspeed)
        pg.draw.rect(screen,(255,255,255),sp)

        if sp.bottom >= line.top:
            sp.bottom = line.top
            yspeed = 0
            
        pg.display.flip()

if __name__ == "__main__":

    main()