from functions import factorial
def euler20(x):
    """sums the digits given by the factorial of x"""
    fact = factorial(x)
    
    summ=0
    for a in str(fact):
        summ += int(a)
    return summ