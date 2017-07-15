def euler1(x,y,z):
    """Find the sum of all the multiples of x or y below z"""
    multis = []
    for a in range(z):
        if a % x == 0:
            multis.append(a)
        elif a % y == 0:
                    multis.append(a)
    total = 0                
    for x in multis:
        total += x
    return total