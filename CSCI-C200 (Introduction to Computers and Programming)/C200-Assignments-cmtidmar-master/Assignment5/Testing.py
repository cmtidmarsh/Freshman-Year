import Reading


loc = "C200/C200-Assignments-cmtidmar/Assignment5/people.csv" # I keep getting a FileNotFoundError, no matter if I have Assignment5/people.csv or anything else
listOfPeople = Reading.fileRead(loc)
count = Reading.getAge(listOfPeople, 15)
print("The number of people are or below the age of {} is {}".format(15, count))

count = Reading.getAge(listOfPeople, 30)
print("The number of people are or below the age of {} is {}".format(30, count))
