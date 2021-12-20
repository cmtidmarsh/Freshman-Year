from rectangle import Rectangle

def intersects(Rectangle, lst):
    """
    Return a tuple of the rectangles that intersect rectangle
    """
    returnLst = []
    for item in lst:
        if Rectangle != item:
            if Rectangle.isintersection(item):
                returnLst.append(item)
    return returnLst




r1 = Rectangle((2, 2,), (6, 6), color = "Red")
r2 =  Rectangle((5, 5), (9, 13), "Green", move = (-1, -1))
r3 = Rectangle((11, 7), (25, 9), move = (1, 1))
r4 = Rectangle((2, 19), (25, 20), "Blue")

lstOfRect = [r1, r2, r3, r4]

print(lstOfRect)
for r in lstOfRect:
    print(r)

for r in lstOfRect:
    print(r, intersects(r, lstOfRect))

for i in range(len(lstOfRect)):
    r = lstOfRect[i]
    print(r)
    r.move()
    print(r)
    print()

for r in lstOfRect:
    print(r, intersects(r, lstOfRect))
