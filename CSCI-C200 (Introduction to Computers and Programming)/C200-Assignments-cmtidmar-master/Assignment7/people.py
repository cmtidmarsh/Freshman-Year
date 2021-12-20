class Person:
    def __init__(self, name, yearOfBirth):
        self.name = name
        self.yearOfBirth = yearOfBirth
    
    def __str__(self):
        return '{}, {}'.format(self.name, self.yearOfBirth)
    
class Student(Person):
    def __init__(self, name, yearOfBirth, major, creditsEarned):
        super().__init__(name, yearOfBirth)
        self.major = major
        self.creditsEarned = creditsEarned
    
    def __str__(self):
        return '{}, {}, {}, {}'.format(self.name, self.yearOfBirth, self.major, self.creditsEarned)


class Instructor(Person):
    def __init__(self, name, yearOfBirth, salary, officeHours):
        super().__init__(name, yearOfBirth)
        self.salary = salary
        self.officeHours = day, room
        
    def studentLst(self):
        super().__init_subclass__(name, yearOfBirth, major, creditsEarned)
        lst = []
        for i in Student:
            lst.append[Student]
        return lst

    def office(self, day, room):
        self.day = day
        self.room = room
    
    def __str__(self):
        return '{}, {}, {}, {}, {}'.format(self.name, self.yearOfBirth, self.salary, self.day, self.room)

if __name__ == "__main__":
    person1 = Person("Amanda Brewster", 1998)
    person2 = Person("Alexa Johnson", 1963)
    print(person1)
    print(person2)
    student1 = Student("Amanda Brester", 1998, "Spanish", 35)
    student2 = Student("Nathan Jindra", 1999, "Poli Sci", 2)
    print(student1)
    print(student2)
    # instructor1 = Instructor("Dr. Clark", 1958, 45000, "Monday", "Rm1112")
    # print(instructor1)
