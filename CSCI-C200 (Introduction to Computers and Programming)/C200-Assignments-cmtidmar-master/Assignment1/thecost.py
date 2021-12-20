
colorPages = input("What is the number of pages in color? >>>")
numColorPages = int(colorPages)

bwPages = input("What is the number of page in b&w? >>>")
numBWPages = int(bwPages)

theCost = (0.25 * numColorPages) + (0.04 * numBWPages)

print("The cost is " + str(theCost))
