import People


def fileRead(loc):
    """
    Given a path to a file, read the file. 
    For each line in the file, create an instance of a `People`.
    Once the whole file has been walked through, 
    return a list of all instances of `People` class that have been 
    generated. 
    """
    peopleList = []
    files = open(loc, 'r')
    data = files.readlines()
    for i in data:
        peopleList.append(People.People(i))
    files.close()
    return peopleList



def getAge(lop, age):
    """
    Given a list of `People` objects, return the number of `People` instances 
    that are less than or equal to the age passed in
    """
    Age = 0

    for people in lop:
        if int(people.getAge()) <= int(age): Age += 1
    return Age
