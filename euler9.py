import math

def euler9():
    """There exists exactly one Pythagorean triplet for which a + b + c = 1000.
    Find the product abc."""
    
    
    for a in range(1,1000):
        for b in range(1,1000):
            if a+b+math.sqrt(a**2+b**2) == 1000:
                aa=a
                bb=b
                c = math.sqrt(a**2+b**2)
                if c % 1 == 0:

                    return int(aa*bb*c)