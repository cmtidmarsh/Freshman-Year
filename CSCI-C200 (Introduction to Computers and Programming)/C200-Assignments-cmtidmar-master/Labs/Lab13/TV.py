class TV:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

        self.volume = 0
        self.channel = 0
        self.state = False

    def power(self):
        self.state = not self.state