import math    
    
def euler21(x):
    """sum of all the amicable numbers under x"""
    amicableList = []
    for a in range(x):
        temp = amicable(a)
        if temp != None:
            amicableList.append(temp) 
    #return amicableList
    return sum(amicableList)


def amicable(x):
    xDivs = getDivisors(x) 
    y = sum(xDivs)
    yDivs = getDivisors(y)
    ySum = sum(yDivs)
    if ySum == x and y!=x:
        return x
    



def getDivisors(x):
    divisors = [1]
    for a in range(2, int(math.sqrt(x)+1)):
        if x%a == 0:
            #print('appending: ' +str(a))
            if a != int(x/a):
                divisors.append(a)
                divisors.append(int(x/a))
            else:
                divisors.append(a)
    return divisors
