def budgetSummary(categoryFileLocation, expenseFileLocation):
    """
    Given the file locations for category and expense, call the method
    readCategory(categoryFileLocation)
    and 
    readExpenses(expenseFileLocation)

    From here:
    Imagine that you wish to track your monthly expenses by category.  For example, housing might include rent, and the various utilities.  You have categorized all of the important expenses in a dictionary of the form 
    {expense : category, ...}. Each month your bank gives you a list of all your expenses in the form of [ (expense, amount),...], where expense could appear more than once in the list. 
    Write a function that returns a dictionary of the form { category : total, ... }. Have a special category `miscellaneous' for any expense that does not appear in your mapping.  
    Do not include categories for which there are no corresponding expenses
    """

    categoryDict = readCategory(categoryFileLocation)
    expenseList = readExpenses(expenseFileLocation)
    expenses = {}

    # TODO: Complete based off the comment description

    return 

def readCategory(location):
    """
    Reading the file from the location, where the first column is the 
    *expense*, the other column is the *category*, which is separated by " ABC ".

    Hint: Use split method on a string (look at python documentation)
    """
    result = {}
    # TODO: Read the values and separate the values and get a dictionary back

    categories = open(location, "r") # Open the file
    data = categories.readlines()
    for line in data:                
        item, category = line.split("ABC")      # Split the file at ABC

    result = categories              # Set result to location with the split.
    categories.close()
    return result                    # Return the result

readCategory(location)

def readExpenses(location):
    """
    Reading the file from the location, where the first column is 
    the *expense*, second column is the *amount*, separated by a ",".

    Return a list of tuples while reading the file.  
    """
    result = []

    # TODO: Do the work
    with open(location, 'r') as expenses:
        data = expense.readlines()
        for line in data:
            (item, expense) = ### NOT DONE SECOND ATTEMPT


    ### FIRST ATTEMPT
    location = open("expenses.txt", "r") #Open the expense file and have Python read it.
    location.read()
    expense = "" # String = expense
    amount = [0] # Start with the amount at 0
    for element in location:
        amount += 1
        result = expense[element] + amount[0]
        result = (expense, amount)
        location.close()
        return result


