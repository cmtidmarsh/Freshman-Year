from sorting import quick_sort, merge_sort, bubble_sort, insertion_sort
from random import sample
from time import time
import matplotlib.pyplot as plt


def generateList(size) -> list:
    """
    Generates a list of random numbers. 
    https://docs.python.org/3/library/random.html#random.sample
    """
    return sample(range(100000000), size)


def timeToSort(function, listToSort: list) -> float:
    """
    Given a sorting function, sort the list. Return the time it takes to sort 
    """
    start = time()
    function(listToSort)
    end = time()
    return end - start


def main():
    """
    To make a copy of the list, you can do the following:
    >>> var = [1, 2, 3]
    >>> varCopy = var.copy() # This will make a copy of the list

    You will need to make a copy because if you sort the list before another 
    algorithm, it would run quicker on a list already sorted 
    """
    functions = {
        "Quick Sort": quick_sort,
        "Merge Sort": merge_sort,
        "Bubble Sort": bubble_sort,
        "Insertion Sort": insertion_sort,
        "Tim Sort": sorted
    }
    sortingTimes = {
        "Quick Sort": [],
        "Merge Sort": [],
        "Bubble Sort": [],
        "Insertion Sort": [],
        "Tim Sort": []
    }

    # TODO: Create size list
    # sizelst = [2000, 4000, 6000, 8000, 10000]
    sizelst = list(range(0, 10000, 2000))

    # TODO: For each potential size of the list:
    #           - Generate a list of that size
    #           - For each function that sorts:
    #               - Make a copy of the list to sort
    #               - Sort the list and store the time to sort in the 
    #                   in the appropriate place in the appropriate 
    #                   dictionary

    for i in sizelst:
        x = generateList(i)
        for j in functions.keys():
            k = x.copy()
            m = timeToSort(functions[j], k)
            sortingTimes[j].append([m])





                



    # TODO: Plot the functions to look similar to the graph
    plt.title("Run Times of Sorting Functions")
    plt.xlabel("List Size")
    plt.ylabel("Time2Run")
    plt.plot([i for i in sizelst], [j for j in sortingTimes["Quick Sort"]], 'b-', label = "Quick Sort")
    plt.plot([i for i in sizelst], [j for j in sortingTimes["Merge Sort"]], 'y-', label = "Merge Sort")
    plt.plot([i for i in sizelst], [j for j in sortingTimes["Bubble Sort"]], 'g-', label = "Bubble Sort")
    plt.plot([i for i in sizelst], [j for j in sortingTimes["Insertion Sort"]], 'r-', label = "Insertion Sort")
    plt.plot([i for i in sizelst], [j for j in sortingTimes["Tim Sort"]], 'm-', label = "Tim Sort")
    plt.legend()
    plt.show()

    """
    TODO: Describe the runtime of each algorithm. 

    According the graph, Bubble Sort has the most efficient runtime out of all of the sorts, 
    while Insertition Sort has the second most efficient time. Then everything else is below.
    """


if __name__ == "__main__":
    main()
