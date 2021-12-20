from os import listdir # TODO: Replace me with correct function
from os.path import join, isdir # TODO: Replace me with correct function

def dfsFiles(wd):
    """
    Fill me in with algorithm provided

    TODO: Complete the function based off the pseudocode
    """
    wdLst = getDirs(wd)
    while len(wdLst) != 0:
        x = wdLst[0]
        wdLst.remove(x)
        print(x)
        newLst = getDirs(x)
        if len(newLst) != 0:
            for i in newLst:
                wdLst.insert(0, i)
                



def getDirs(wd):
    """
    Returns a list of directories to be traversed

    TODO: Fix the 2 different TODO s in this function
    """
    resultList = []
    for f in listdir(wd): # TODO: Find function from OS that will complete this function
        if isdir(join(wd, f)): # TODO: Find this function in the os.path directory 
            
            resultList.append(join(wd, f))
    return resultList


if __name__ == "__main__":
    dfsFiles(input("working directory >>> ")) # TODO: Replace this we a SINGLE command line argument 

# I ran the dfssearch.py file in my computer's terminal:
# python dfssearch.py Test
# And it worked, but it's not working here in VSC.


