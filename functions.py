##FILE CONTAINING USEFULL FUNCTIONS
import math

def findPrimes(y):
    """finds all the primes up to y
    Uses Sieve of Eratosthenes"""
    A = []
    primes= []
    for a in range(y):
        A.append(True)
    for i in range(2, int(math.sqrt(y))):
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



def fib(x,fibdic):
    """Recursively finds fibonacci numbers
    Helper for euler 2"""
    if x in fibdic.keys():
        return fibdic.get(x)
    else:
        fibdic[x] = fib(x-1, fibdic)+fib(x-2,fibdic)
        return fibdic.get(x)
    
    
def isPali(y):
    """returns true if y is a palindrome"""
    tempstr = str(y)
    
    if tempstr == tempstr[::-1]:
        return True
    else:
        return False
    
    
def primeFactorsUpto(x):
    """returns the primefactors for values upto x"""
    for a in range(1,x):
        allFactors.append(primeFact(a))
        
        
    
def primeFact(y):
    """returns the primefactors of y"""
    factors = []
    temp = y
    primes = findPrimes(y)
    primes.append(y)
    while y != 1:
        for p in primes:
            if y % p == 0:
                y = y/p
                factors.append(p)
    return factors 



def findDiv(num):
    """returns sorted list of divisors of num"""
    divs = []
    for x in range(1,int(math.sqrt(num+1))):
        #print(x)
        if num%x == 0:
            divs.append(x)
            divs.append(int(num/x))
    return sorted(divs)


def factorial(a):
    """returns the product of the factorial sequence up to a'th index"""
    if a <= 1:
        return 1
    else:
        return a* factorial(a-1)