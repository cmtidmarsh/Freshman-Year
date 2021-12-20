from Shape import Shape # HMMMMMMMMMMMMMMMMMMMMMM, wonder what this is for
import pygame

# TODO: Fill me in

# https://www.pygame.org/docs/

# Create the following:
# - Triangle Class:
# -- the point given represents the top of an (almost) equilateral triangle. 
# -- Given a length, that is the height.
# -- The width of the triangle is the height provides
class Triangle(Shape):
    def __init__(self, p1, color, height):
        super().__init__(p1, color)
        self.height = height

    def draw(self, screen):
        pygame.draw.polygon(screen, self.color, [[self.x, self.y], [self.x-self.height, self.y-self.height/2], [self.x-self.height, self.y+self.height/2]])

# - Square Class:
# -- Point represents the middle of the square
# -- Other info you might need?
class Square(Shape):
    def __init__(self, pt1, color, height):
        super().__init__(pt1, color)
        self.height = height
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, [self.x - self.height // 2, self.y - self.height // 2, self.height, self.height])

# - Rectangle Class:
# -- Point represents the middle of the rectangle
# -- Other info you might need?
class Rectangle(Shape): #Would be the same as square? Because square is a rectangle.
        def __init__(self, pt1, color, height, width):
            super().__init__(pt1, color)
            self.height = height
            self.width = width
        def draw(self, screen):
            pygame.draw.rect(screen, self.color, [self.x - self.width // 2, self.y - self.height // 2, self.width, self.height])

# - Circle Class:
# -- Point is in the center of circle
# -- length is the radius
class Circle(Shape):
    def __init__(self, pt, color, radius):
        super().__init__(pt, color)
        self.x1, self.y1 = pt

        self.radius = radius

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x1, self.y1), self.radius)
    

# For each class, modify the string method to be more filled in
