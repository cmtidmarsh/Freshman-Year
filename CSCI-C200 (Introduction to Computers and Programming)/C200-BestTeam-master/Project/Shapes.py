import pygame as pg

class Shapes:

    def __init__(self, location, color):
        self.x, self.y = location
        self.color = color
    
    def draw(self, screen):
        pass

class Rectangle(Shapes):

    def __init__(self, location, color, width, height):
        super().__init__(location, color)
        
        self.width = width

        self.height = height
    
        self.rectangle = pg.Rect(self.x,self.y,self.width,self.height)

    def draw(self, screen):
        pg.draw.rect(screen, self.color, self.rectangle)
    
    def move(self,xspeed,yspeed):

        self.rectangle.move_ip(xspeed,yspeed)


class Circle(Shapes):


    def __init__(self, location, color, radius):
        super().__init__(location, color)
        self.radius = radius

    def draw(self, screen):
        pg.draw.circle(screen, self.color, (self.x, self.y), self.radius)
    
    def move(self,screen,xspeed,yspeed):
        
        self.x += xspeed
        self.y += yspeed
        
        pg.draw.circle(screen, self.color, (self.x, self.y), self.radius)

class Polygon(Shapes):

    def __init__(self, location, color, height):
        super().__init__(location, color)
        self.height = height

    def draw(self, screen):
        pygame.draw.polygon(screen, self.color, [[self.x, self.y],[self.x - self.height/2, self.y + self.height], [self.x + self.height/2, self.y + self.height]])
        pg.draw.polygon(screen, self.color, [[self.x, self.y],[self.x - self.height/2, self.y + self.height], [self.x + self.height/2, self.y + self.height]])
    
    def move(self,screen,xspeed,yspeed):
        
        self.x += xspeed
        self.y += yspeed
        
        pygame.draw.polygon(screen, self.color, [[self.x, self.y],[self.x - self.height/2, self.y + self.height], [self.x + self.height/2, self.y + self.height]])
        pg.draw.polygon(screen, self.color, [[self.x, self.y],[self.x - self.height/2, self.y + self.height], [self.x + self.height/2, self.y + self.height]])
