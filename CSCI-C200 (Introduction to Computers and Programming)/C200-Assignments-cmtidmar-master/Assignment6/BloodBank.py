class BloodBank:

    # https://www.disabled-world.com/calculators-charts/blood-chart.php
    # Dontate Blood To table s
    DONATE_TO = { "A+": ["A+", "AB+"],
                  "O+": ["O+", "A+", "B+", "AB+"],
                  "B+": ["B+", "AB+"],
                  "AB+": ["AB+"],
                  "A-": ["A+", "A-", "AB+", "AB-"],
                  "O-": ["A+", "O+", "B+", "AB+", "A-", "O-", "B-", "AB-"],
                  "B-": ["B+", "B-", "AB+", "AB-"],
                  "AB-": ["AB+", "AB-"]}
     


    DONATE_FROM = { "A+": ["A+", "A-", "O+", "O-"],
                    "O+": ["O+", "O-"],
                    "B+": ["B+", "B-", "O+", "O-"],
                    "AB+": ["A+", "O+", "B+", "AB+", "A-", "O-", "B-", "AB-"],
                    "A-": ["A-", "O-"],
                    "O-": ["O-"],
                    "B-": ["B-", "O-"],
                    "AB-": ["AB-", "A-", "B-", "O-"]}



    def __init__(self, name, location):
        """
        Creates an instance of a of a BloodBank

        A blood bank will have a `name`, `location`, a list of `users`, and a bank of blood 
        to keep track of how much of each blood type they have. 
        """
        self.name = name
        self.location = location
        self.users = []
        self.bank = {"A+": 0,
                     "O+": 0,
                     "B+": 0,
                     "AB+": 0,
                     "A-": 0,
                     "O-": 0,
                     "B-": 0,
                     "AB-": 0}




    
    def totalUnitsOfBlood(self, bType=None):
        """
        Returns the total number of units of blood in the bank. 

        Unless specified, returns the total for all units. Can be provided a type.
        """
        # TODO: Implement this
        
        return sum(self.bank.values())
    
    def findPeople(self, bType):
        """
        For the given blood type `bType`, return a list of people 
        that have bloods types that `bType` can receive

        Example: A+ can receive from A+, A-, O+, O-
        """
        
        bloodTypes = self.DONATE_FROM[bType]
        
        lst = []    
        
        for user in self.users:
            if user.bloodType in bloodTypes:
                lst.append(user)
                
            return lst
            
                
            
    def addPerson(self, p):
        """
        Adds the given `Person` object to the Bank. 
        Assumes no Person will be given twice 
        (no need to check for repeats)
        """
        # TODO: Implement this
        self.users.append(p)
    
    def giveBlood(self, p, quantity=5):
        """
        Given that there is enough blood in the bank for the given person, 
        transfer the blood to the person. Assuming the blood can be GIVEN to the person, 
        subtract the quantity from the bank and return 0. 

        If there is not enough blood in the bank to transfer, return -1.

        If you are unable to transferBlood for the given person, return -2. 
        """
        # TODO: Implement this
        
        bloodTypes = self.DONATE_FROM[p.bloodType]
        
        blood = 0
        for bloodType in bloodTypes:
            blood = blood + self.bank[bloodType]
        
        if blood < quantity:
            return -1
        elif p.transferBlood(quantity) == -1:
            return -2
        else:
            for bloodType in bloodTypes:
                blood = self.bank[bloodType]
                if quantity > blood:
                    self.bank[bloodType] = 0
                    quantity = quantity - blood
                else:
                    self.bank[bloodType] = blood - quantity
                    break
                    
            return 0
    
    def receiveBlood(self, p, quantity=5):
        """
        Takes blood from the provided person and if you are able to 
        successfully transfer blood from the person, then remove that from the 
        the current banks blood bank. Return 0. 

        If you are unable to transfer blood from the person, return -1 since you can't add 
        blood the bank if the you can't get blood from the person.
        """
        
        if p.transferBlood(quantity) == -1:
            return -1
        else:
            self.bank[p.bloodType] = self.bank[p.bloodType] + quantity
            return 0
    
    def registeredUsers(self):
        """
        Returns the number of people r
       registered in this 
        blood bank
        """
        return len(self.users)

    def __str__(self):
        """
        Returns the name of the bank and the number of 
        registered users
        """
        return self.name + ",Users: " + str(self.registeredUsers()) + ",Blood Total: " + str(self.totalUnitsOfBlood()) 


if __name__ == "__main__":
    testing = BloodBank("Who", "Where")
    pass # Can do some testing without running all the code
