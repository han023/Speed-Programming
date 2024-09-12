# https://www.hackerrank.com/challenges/leonardo-and-prime/problem?isFullScreen=true

# Leonardo loves primes and created  queries where each query takes the form of an integer, n. 
# For each n, count the maximum number of distinct prime factors of any number in the inclusive range [1,n].

def primeCount(n):
    factor = 0
    prime=2
    isPrime=True
    prod=1
    while (True):
        for i in range(2, prime):
            if prime % i == 0:
                isPrime = False
        if isPrime:
            prod = prod * prime
            factor +=1
            if prod > n:
                factor -= 1
                break
        prime+=1
        isPrime = True
    return (factor)


