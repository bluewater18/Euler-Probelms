import math
"""Could maybe increase speed by removing numbers as they are found"""
    
def euler23():
    """Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers"""
    sums = []
    abundantNums = findAbundantNums()
    for x in abundantNums:
        #print(x)
        for y in abundantNums:
            #print(y)
            if x+y<28123:
                sums.append(int(x+y))
    #for x in range(1,28123):
        #print(x)
        #for y in abundantNums:
            #if x-y in abundantNums:
                #break
            #else:
                #sums.append(x)
    nums = range(1,28123)
    nums = set(nums)
    nonSums = nums - set(sums)
    
    #for x in range(1,28123):
        #for y in set(sums):
            #if x == y:
                #break
            #else:
                #nonSums.append(x)
    #print(nonSums)
    return sum(nonSums)
                
                
    

def getDivisors(x):
    divisors = [1]
    #print('****')
    #print(int(math.sqrt(x+1)))
    for a in range(2, int(math.sqrt(x)+1)):
        #print(a)
        #print(x%a)
        if x%a == 0:
            #print('appending: ' +str(a))
            if a != int(x/a):
                divisors.append(a)
                divisors.append(int(x/a))
            else:
                divisors.append(a)
    return divisors
            
def findAbundantNums():
    abundantNums = []
    for x in range(1,28123):
        divisors = getDivisors(x)
        if sum(divisors) > x:
            abundantNums.append(x)  
    return abundantNums
