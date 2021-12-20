import datetime

class Person:
    
    # https://www.simplifiedpython.net/python-convert-string-to-datetime/
    #Tool to help with date

    def __init__(self, name, address, birthday, bloodType):
        """
        Given a name (string), an address (string), birthday (string), and 
        blood type (string), store the parameters in instance variables as 
        name (string), address (string), birthday (datetime, in the format of month-day-year), 
        and bloodType (string). 

        You must keep track of the number of milliliters in the body. 

        You must keep track of if the person is injuried. A person is considered injured 
        if they have less than 5200 ml of blood in the body or has more than 5600 ml in
        the body.

        The bloodInBody is 5500 units
        """
        self.name = name
        self.address = address
        self.birthday = datetime.datetime.strptime(birthday, "%m-%d-%Y")
        self.bloodType = bloodType
        self.bloodInBody = 5500


    
    def getAge(self):
        """
        Returns the number of years the person is. 
        """
        today = datetime.date.today()
        age = today.year - self.birthday.year - ((today.month, today.day) < (self.birthday.month, self.birthday.date))
        return age
    

    def isInjured(self):
        """
        Returns a boolean value. 

        True if the person is injured (less than 5200 or more than 5600 ml)
        False if the person is not injured
        """
        # TODO: Implement this
        if self.bloodInBody >= 5200 and self.bloodInBody <= 5600:
            return False
        else:
            return True
        

    def getBloodCount(self):
        """
        Returns the amount of blood in the person's body
        """
         # TODO: Implement this
        return self.bloodInBody
    
    def transferBlood(self, count):
        """
        For a given amount of blood, transfer a safe amount to the current 
        person or FROM the person. 

        If the provided amount of blood GIVEN (+) to the person is dangerous, do 
        not transfer any of it and return -1

        If the provided amount of blood TAKEN (-) from the person is dangerous, 
        do not take any of the blood and return -1

        Otherwise, complete the transfer and return 0
        """
        # TODO: Implement this
        if self.bloodInBody + count > 5600:
            return -1
        
        elif self.bloodInBody + count < 5200:
            return -1
        else:
            self.bloodInBody = self.bloodInBody + count
            return 0
        
    

    def resetBloodCount(self):
        """
        Sets the number of units for blood back to 
        the amount of blood in the body that a body normally has.

        Simulates a person recovering after donating.
        """
        # TODO: Implement this
        self.bloodInBody = 5500
    


    def __repr__(self):
        """
        Provided the name and blood type for the user.
        """
        return "< " + self.name + " ~ " + self.bloodType  +" >"

    def __str__(self):
        """
        Return the name, the age, and the blood type as follows:

        Larry Bates ~ 19 ~ A-
        """
        return self.name + " ~ " + str(self.getAge()) + " ~ " + self.bloodType

if __name__ == "__main__":
    p = Person("Hello", "from the other", "05-05-1995", "side")
    # Can do some testing without running all the code
