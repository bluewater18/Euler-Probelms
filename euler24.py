import itertools
##TODO make a recursive function to create all factorials
##     make a function that converts a number to the 
    
def euler24(x,y):
    """returns the x'th ordered lexographical permutation of digits up to y"""
    digits = []
    for a in range(y+1):
        digits.append(a)
    perms = list(itertools.permutations(digits))
   
    #print(perms[x-1])
    returnStr = ''
    for x in perms[x-1]:
        returnStr += str(x)
    return int(returnStr)


def perms(x):
    """returns all permutations of list x recursively"""
    #print('test')
    if len(x) == 1:
        return str(x[0])
    else:
        return str(x[0]) + perms(x[1:])
    
    
    
    

