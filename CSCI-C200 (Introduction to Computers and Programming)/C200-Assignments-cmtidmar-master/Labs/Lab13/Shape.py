class Shape:

    def __init__(self, pt1, pt2, width, height):
    self.x1, self.y1 = pt1
    self.x2, self.y2 = pt2

    self.width = abs(self.x1 - self.x2)
    self.height = abs(self.y1 - self.y2)

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        return (2*self.width + 2*self.height)

class Circle:
    def __init__(self, circumference, radius):
        self.radius =
    
class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height
        return (base*height*(1/2))
        

        