def euler2(x,y=50):
    """find the sum of even valued fibonacci terms up to x or up to fib number y"""
    fibdic={0:1,1:1}
    fib(y,fibdic)
    fibs = list(fibdic.values())
    sum = 0
    for a in fibs:
        if a > x:
            return sum
        elif a%2 == 0:
            sum+= a


def fib(x,fibdic):
    """Recursively finds fibonacci numbers
    Helper for euler 2"""
    if x in fibdic.keys():
        return fibdic.get(x)
    else:
        fibdic[x] = fib(x-1, fibdic)+fib(x-2,fibdic)
        return fibdic.get(x)