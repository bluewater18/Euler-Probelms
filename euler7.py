from functions import findPrimes

def euler7(primeI):
    """finds the primeI'th prime number"""
    #need to make a tighter bound on primes
    #could create a new helper function that creates a list of the first x primes
    primes = findPrimes(primeI*100)
    #print(len(primes))
    return primes[primeI-1]