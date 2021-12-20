string1 = "{0} - {1}" # TODO: Complete this string to use format
string2 = "{0:>10}" # TODO: Complete this string to use format
string3 = "00{0:.2f}" # TODO: Complete this string to use format
string4 = "Does {0} == {1} ? -> {2}" # TODO: Complete this string to use format
string5 = "{:~^10s}" # TODO: Complete this string to use format


# NOTE: Do not modify anything below this line
# Added this so we can test the strings on our own, to ensure no 
# manual entry of tests
if __name__ == "__main__":
    strings = [string1, string2, string3, string4, string5]

    resultStrings = [
        ["10 - 11", "12 - 13", "1 - 1", "4 - 4", "5 - 5"], # Results for string1
        ["      Star", "      Trek", "       TNG", " Hello   !"], # Results for string2
        ["002.00", "003.14", "000.00", "000.70", "005.00"], # Results for string3
        ["Does 1 == 2 ? -> False", "Does 2 == 2 ? -> True", "Does A == B ? -> yes"], # Results for string4
        ["~~~C200~~~", "~~~WOW~~~~", "~~~~Oh~~~~", "~~~wOw~~~~"] # Results for string5
    ]

    args1 = [
        [10, 11], [12, 13], [1, 1], [4, 4], [5, 5]
    ] # Arguments for string1

    args2 = [
        ["Star"], ["Trek"], ["TNG"], ["Hello   !"]
    ] # Arguments for string2

    args3 = [
        [2], [3.1415926], [.0000001], [.7], [5]
    ] # Arguments for string3

    args4 = [
        [1, 2, False], [2, 2, True], ["A", "B", "yes"]
    ] # Arguments for string4

    args5 = [
        ["C200"], ["WOW"], ["Oh"], ["wOw"]
    ] # Arguments for string5

    args = [args1, args2, args3, args4, args5]

    for i in range(len(args)):
        print("String {} Tests".format(i + 1))
        print()
        currentArgs = args[i]
        curString = strings[i]
        resultString = resultStrings[i]
        for j in range(len(currentArgs)):
            yourString = curString.format(*currentArgs[j]) # What is this line? 
            # https://docs.python.org/3/tutorial/controlflow.html#unpacking-argument-lists 
            # We will learn more about this in the semester but just allows you to provide the arguments without 
            # the programmer doing it themselves
            corrString = resultString[j]
            print(" Your String   : '" + yourString + "'\n Correct String: '" +  corrString + "'\nMatches : " + str(yourString == corrString))
            print()

