
# num_to_roman = {1: "I", 
#                 4: "IV",
#                 5: "V",
#                 9: "IX",
#                 10: "X",
#                 40: "XL",
#                 50: "L",
#                 90: "XC",
#                 100: "C"}


num_to_roman = [(100, 'C'), 
                (90, 'XC'),
                (50, 'L'),
                (40, 'XL'),
                (10, 'X'),
                (9, 'IX'),
                (5, 'V'),
                (4, 'IV'),
                (1, 'I')]


def int_to_roman(nums):

    result = ""
    while nums > 0:
        print(nums)
        for integer, roman in num_to_roman:
            while nums >= integer:
                result = result + roman
                nums = nums - integer
    return result

if __name__ == "__main__":
    for i in range(1, 100):
        calling = int_to_roman(i)
        print(calling, sep='')

