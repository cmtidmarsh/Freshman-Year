class People:

    def __init__(self, string):
        """
        Given a string, take each item separated by a comma.

        There are 4 items in each string: Name, Favorite Color, Age, Age, Height

        The 'Name' and 'Favorite Color' will be strings.

        The 'Age' and 'Height' are floats

        Hint: Note the spaces and end of line characters
        """
        self.string = string
        self.lst = string.split(",")
        self.Name = self.lst[0]
        self.FavoriteColor = self.lst[1]
        self.Age = string.lst[2]
        self.Height = self.lst[3]

    def Age(self):
        return self.Age

    def __str__(self):
        age += "Age: " + self.Age
        return age