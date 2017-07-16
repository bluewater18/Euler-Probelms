def euler6(x):
    """Find the difference between the sum of the squares of the first x natural numbers and the square of the sum"""
    sumSqr = 0
    iSum = 0
    
    for i in range(1,x+1):
        
        sumSqr += i**2
        iSum += i
    iSum = iSum**2
    
    
    return iSum - sumSqr
    