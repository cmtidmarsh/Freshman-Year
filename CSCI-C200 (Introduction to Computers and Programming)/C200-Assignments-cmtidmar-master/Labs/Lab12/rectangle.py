class Rectangle:
    def __init__(self, pt1, pt2, color = "Black", move=(0,0)):
        """
        The constructor take in 2 tuples, one representing the top
        left corner and the bottom right corner

        The points are '(x, y)'
        """
        self.x1, self.y1 = pt1  #
        self.x2 = pt2[0]        # Can do either/or 
        self.y2 = pt2[1]        #

        self.width = abs(self.x1 - self.x2)
        self.height = abs(self.y1 - self.y2)
        self.color = color
        self.velocity = move
    def setVelocity(self, dx, dy):
        """
        Sets the velocity of aw moving rectangle"
        """
        self.velocity = (dx, dy)

    def move(self, v = None):
        """
        Update the position of the rectangle on the velocity is provided.
        If not provided, use the velocity of the current velocity.
        """
        
        if v == None: # evaluates to false is 'none' is provided
            changeX = self.velocity[0]
            changeY = self.velocity[1]
        else:
            changeX = v[0]
            changeY = v[1]

        self.x1 += changeX
        self.x2 += changeX
        self.y1 += changeY
        self.y2 += changeY



    def changeColor(self, color):
        """
        Sets the color of the rectangle to the new color
        """
        self.color = color
    
    def perimeter(self):
        """
        Perimeter of the rectangle
        """
        return (2 * self.width) + (2 * self.height)



    def area(self):
        """
        Area of the rectangle, the width * the height
        """
        return self.width * self.height

    def isintersection(self, r1):
        """
        Returns True is the current rectange intersects 'r1'
        Flase otherwise
        """
        xCheck1 = (self.x1 <= r1.x1 and r1.x1 <= self.x2)
        xCheck2 = (self.x1 <= r1.x2 and r1.x2 <= self.x2)
        # print(xCheck1, xCheck2)
        if xCheck1 or xCheck2:
            # print("Inside of x coordinates")
            yCheck1 = (self.y1 <= r1.y1 and r1.y1 <= self.y2)
            yCheck2 = (self.y1 <= r1.y2 and r1.y2 <= self.y2)
            if yCheck1 or yCheck2:
                # print("Inside of y coordinates")
                return True
        if r1.area() > self.area():
            return False or r1.isintersection(self)
        else:
            return False


    def __str__(self):
        pt1Str = str(self.x1) + "," + str(self.y1)
        pt2Str = str(self.x2) + "," + str(self.y2)
        return "Rectangle: P1 = " + pt1Str + "P2 = " + pt2Str

    def __repr__(self):
        return "Rect"

if __name__ == "__main__":
    testRec = Rectangle((3, 4), (5, 8))
    area = testRec.area()
    print(testRec)
    print(area)
    p = testRec.perimeter()
    print(p)

    t1 = Rectangle((0, 0), (10, 10), "Blue" )
    t2 = Rectangle((2, 2), (8, 8), color = "Green") #t2 = Rectangle((2,2), (8, 8). "Green")
    print(t1.isintersection(t2))
    print(t2.isintersection(t1))
    print(t1.color)
    print(t2.color)
