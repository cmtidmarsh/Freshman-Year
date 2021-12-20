import pygame as pg, sys, random as rn
from Shapes import Rectangle, Polygon, Circle


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

def start():
    pg.font.init()
    display = 500, 750
    screen = pg.display.set_mode((display))
    caption = pg.display.set_caption("Rainbow Runner")
    screen.fill(BLACK)

    
    
    startbutton = pg.draw.rect(screen, BLACK, (150, 300, 200, 100))
    instructionbutton = pg.draw.rect(screen, BLACK, (150, 425, 200, 50))
    scorebutton = pg.draw.rect(screen, BLACK, (150, 500, 200, 80))
    
    scores = []
    try:
        while True:

            pg.time.wait(200)

            screen.fill(BLACK)

            for event in pg.event.get():

                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()

                if event.type == pg.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    
                    if scorebutton.collidepoint(mouse_pos):
                        scoreFile = open('Documentations/scores.txt', 'r')
                        for score in scoreFile.readlines():
                            scores.append(int(score.strip()))

                        print("High Score: ",max(scores))
                    
                    if instructionbutton.collidepoint(mouse_pos):
                        with open('Documentations/instructions.txt', 'r') as f:
                            print(f.read())
                    
                    if startbutton.collidepoint(mouse_pos):
                        main()
            
            font1 = pg.font.SysFont(None, 45)
            text = font1.render("Instructions", True, LIGHTYELLOW)
            screen.blit(text, (160, 435))

            font2 = pg.font.SysFont(None, 100)
            textstart = font2.render("Start", True, LIGHTRED)
            screen.blit(textstart, (168, 320))

            font3 = pg.font.SysFont(None, 80)
            title = font3.render("Rainbow Runner", True, rn.choice(colorChoices))
            screen.blit(title, (25, 150))

            font4 = pg.font.SysFont(None, 45)
            score = font4.render("Scores", True, LIGHTPINK)
            screen.blit(score, (195, 525))

            pg.display.flip()
    
    except: print("Exited Game")

def lineGeneration(y):

    #generating random gap position
    gapPos = rn.randint(1,400)
    gapSize = rn.randint(40,120)

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
    
    pg.font.init()
    #-----------------------------------------

    #sprite
    sp = Rectangle((250,20),WHITE,20,20)
    sp.draw(screen)

    #list of lines, starting y at 100
    lines = []
    y = 300

    #generating lines
    for i in range(8):
        #generate a line at y and add to y
        lines.append(lineGeneration(y))
        y += 100
    
    y = 800

    leftLines = []
    rightLines = []
    for line in lines:
        for index in range(len(line)):
            #get the left and right line
            if index == 0: leftLines.append(line[index])  
            else: rightLines.append(line[index])
    
    #speeds
    xspeed = 99999/100000
    yspeed = 6
    riseSpeed = -1

    #detecting if the sprite is on a line
    onLine = False

    #score
    score = 0
    scoreFont = pg.font.SysFont(None, 45)
    scoreText = scoreFont.render(str(score), True, rn.choice(colorChoices))
    screen.blit(scoreText, (480, 0))

    try:
        while True:

            pg.time.delay(7)
            pg.event.pump()
            
            #quit
            if pg.event.get(pg.QUIT): pg.quit()
            
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

                leftLines[i].draw(screen)
                rightLines[i].draw(screen)

                # if sprite hits a line
                if sp.rectangle.bottom >= leftLines[i].rectangle.top and (sp.rectangle.left <= leftLines[i].rectangle.right or sp.rectangle.right >= rightLines[i].rectangle.left):
                    
                    #change the color of the sprite to the color of the line that it hits
                    if sp.rectangle.right <= leftLines[i].rectangle.right:
                        sp.color = leftLines[i].color
                    elif sp.rectangle.left >= rightLines[i].rectangle.left:
                        sp.color = rightLines[i].color

                    #reset yspeed and onLine
                    yspeed = 0
                    onLine = True
                
                #if the sprite goes through the gap
                if sp.rectangle.bottom >= leftLines[i].rectangle.top and sp.rectangle.left >= leftLines[i].rectangle.right and sp.rectangle.right <= rightLines[i].rectangle.left:
                    
                    #reset yspeed and onLine
                    yspeed = 6
                    onLine = False
                
                leftLines[i].rectangle.bottom += riseSpeed
                rightLines[i].rectangle.bottom += riseSpeed
            
            #stop the sprite from going off screen
            if sp.rectangle.left <= 0: sp.rectangle.left = 0
            if sp.rectangle.right >= 500: sp.rectangle.right = 500
            
            #sprite naturally drops
            if onLine: sp.move(0,riseSpeed)
            else: sp.move(0,6)
            
            #create new line when the first line reaches the top
            if leftLines[0].rectangle.bottom <= 0: 
                leftLines.pop(0)
                rightLines.pop(0)
                newLine = lineGeneration(y)
                leftLines.append(newLine[0])
                rightLines.append(newLine[1])
                score += 1

            # when sprite hits top of screen, game over
            if sp.rectangle.top <= 0: 

                with open('Documentations/scores.txt', 'a') as f:
                    f.write(str(score) + "\n")

                break
        
            #displaying score
            scoreText = scoreFont.render(str(score), True, rn.choice(colorChoices))
            if score < 10: 
                screen.blit(scoreText, (480, 0))
            elif score >= 10 and score < 100:
                screen.blit(scoreText, (463, 0))
            else:
                screen.blit(scoreText, (443, 0))

            #change the difficulty 
            if score > 50 : riseSpeed = -2
            elif score > 100 : riseSpeed = -3

            sp.draw(screen)      
                
            pg.display.flip()

    except: print("Exited Game")

if __name__ == "__main__":
    start()
