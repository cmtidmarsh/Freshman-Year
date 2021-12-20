#Note: I'll take the L on this one

class Assignments:
    def __init__(self, name, username, points, totalpts, grade, instructions, questions):
        self.name = name # Every student has a name
        self.username = username # user name to canvas
        self.points = points # points earned of each class (which in my case will not be many)
        self.totalpts = totalpts # total points of each class
        self.grade = ((self.points / self.totalpts)*100) # the grade based on how many points you've earned divided by the total that you could have earned, but didn't.
                                                         # then multiply the result by 100 to get percentage
        self.instructions = instructions # need instructions on what you are wanting the student to do
        self.questions = questions # questions for quizzes and exams
    
    def heading(self): #heading to every assignment
        '{}, {}'.format(self.name, self.username)

    def gradeletter(self): # after converting points and totalpts, you have the grade letters
        if self.grade >= 90:
            return "A"
        elif self.grade < 90 and self.grade >= 80:
            return "B"
        elif self.grade < 80 and self.grade >= 70:
            return "C"
        elif self.grade < 70 and self.grade >= 60:
            return "D"
        else:
            return "F"

class Quizzes(Assignments): # Quizzes usually have majority have questions or fill ins
    def __init__(questions):
        super().__init__(points, totalpts, grade, questions)
        self.totalpts = 10
        self.questions = "'insert quiz questions here' "

        if self.points <= self.totalpts:
            return self.grade


class Exams(Assignments): # Exams are a combination of instructions and questions
    def __init__(self, questions)
    super().__init__(points, points, totalpts, grade, instructions, questions)
    self.totalpts = 500
    self.instructions = " instructions: 'insert here' "
    self. questions = "questions: 'insert here' "
class Labs(Assignments): # Usually just instructions/tutorials
    def __init__(self, instructions)
    super().__init__(points, totalpts, grade, instructions)
    self.totalpts = 10
    self.instructions = "'insert instructions here'"
        if self.points <= self.totalpts:
            return self.grade

class Homework(Assignments): #usually just instructions
    def __init__(self, instructions)
    super().__init__(name, points, totalpts, grade, instructions)
    self.totalpts = 250
    self.instructions = " instructions: 'insert here' "
        if self.points <= self.totalpts:
            return self.grade
    
    
class Attendence(Assignments):
    
    def __init__(self, roster)
    super().__init__(name, points, totalpts, grade)
    self.totalspts = 10
            if self.points <= self.totalpts:
            return self.grade
    def roster(self, student):
        self.roster = []
        for student in self.roster:
            self.roster.append(student)
        return self.roster
    


