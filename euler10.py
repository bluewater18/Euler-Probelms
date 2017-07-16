from functions import findPrimes
def euler10(x):
    """Find the sum of all the primes below x."""
    primes = findPrimes(x)
    return(sum(primes))