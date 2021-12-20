def warpFactor(flt):
    numfloat = float(int(flt))
    if numfloat >= 0 and numfloat <1:
        print("Sublight (Warp Factor 0)")
    elif numfloat >=1 and numfloat < 10:
        print("Warp Factor 1")
    elif numfloat >= 10 and numfloat < 39:
        print("Warp Factor 2")
    elif numfloat >= 39 and numfloat < 102:
        print("Warp Factor 3")
    elif numfloat >= 102 and numfloat < 214:
        print("Warp Factor 4")
    elif numfloat >= 214 and numfloat < 392:
        print("Warp Factor 5")
    elif numfloat >= 392 and numfloat < 656:
        print("Warp Factor 6")
    elif numfloat >= 656 and numfloat < 1024:
        print("Warp Factor 7")
    elif numfloat >= 1024 and numfloat < 1516:
        print("Warp Factor 8")
    else:
        print("Warp Factor 9")

print(warpFactor(1588))
print(warpFactor(.867))
print(warpFactor(41.0))
print(warpFactor(12.5))
