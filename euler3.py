import math


def euler3(x):
    """largest prime factor of the number x"""
    if x > 10**5:
        print('large')
        primes = findPrimes(int(math.sqrt(x)))
    else:
        primes = findPrimes(x)
    primes.reverse()
    maxa =0
    for prime in primes:
        if x % prime ==0:
            if prime > maxa:
                maxa = prime
    if maxa > 1:
        return maxa
    else:
        return "this number is a prime"
            
    
    
def findPrimes(y):
    """finds all the primes up to y
    Uses Sieve of Eratosthenes"""
    A = []
    primes= []
    for a in range(y):
        A.append(True)
    for i in range(2, int(math.sqrt(y))):
        print(i)
        if A[i] == True:
            j =[]
            count = 0

            while True:
                temp = i*i+i*count
                count+=1
                
                if temp >= y:
                    
                    break
                else:
                    j.append(temp)
                
            for b in j:


                A[b] = False
            
           
    for k in range(2,len(A)):
        if A[k] == True:
            primes.append(k)
    return primes