class Shape:

    def __init__(self, location, color):
        """
        Given the location, this represents the center of the shape. 

        The color is the color the shape will be filled
        """
        print(location)
        self.x, self.y = location
        self.color = color
    
    def draw(self, screen):
        """
        Given the screen, draw the shape based on the location and color. 
        """
        pass

    def __str__(self):
        """
        Returns a string with the class name, and the location of the center
        """
        return "Shape: {}, Location: {}, {}".format("SHAPE", self.x, self.y)

