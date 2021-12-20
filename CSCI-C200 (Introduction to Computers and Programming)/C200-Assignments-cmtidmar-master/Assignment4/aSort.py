def pseudoCode_To_Code(num):
    """
    Sorts a given array
    Input: An array A[0..n-1] of orderable elements
    Output: Array a[0..n-1] sorted in nondecreasing order
    """
    for i in range(len(num)):
        for j in range(0, len(num) - i -1):
            if num[j] > num[j+1]:
                num[j], num[j+1] = num[j+1], num[j]
    return num

print(pseudoCode_To_Code([5, 4, 7, 9, 3]))
print(pseudoCode_To_Code([3, 5, 10, 34, 6]))
print(pseudoCode_To_Code([4, 122, 11, 332]))