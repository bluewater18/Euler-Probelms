
def euler15(x,y,dicto = {}):
    """Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down    How many such routes are there through a x*y grid"""
    if (x,y) in dicto.keys():
        return dicto.get((x,y))
    elif y == 0:
        return 1
    elif x == y:
        dicto[(x,y)] = 2*euler15(x,y-1,dicto)
        return dicto.get((x,y))

    else:
        dicto[(x,y)] = euler15(x,y-1,dicto) + euler15(x-1,y,dicto)
        return dicto.get((x,y))
    