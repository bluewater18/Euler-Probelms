##Could be improved by working downwards and taking the first palindrome in such a way that it is guarenteed to be the largest
##could have a bound on what needs to be tested i.e. 10**x+1 to (10**x+1-sqrt(9.999*10**x))

def euler4(x):
    """Find the largest palindrome made from the product of two x-digit numbers."""
    x_digit_numbers = list(range(10**(x-1), 10**x))
    x_digit_numbers.reverse()
    palis=[]
    for x in x_digit_numbers:
        #print(x)
        for y in x_digit_numbers:
            temp = x*y
            if isPali(temp):
                palis.append(temp)
    return max(palis)


def isPali(y):
    """returns true if the y is a palindrome"""
    tempstr = str(y)
    
    if tempstr == tempstr[::-1]:
        return True
    else:
        return False