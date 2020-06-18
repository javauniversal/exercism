import math
from itertools import takewhile

def nth_prime(order):
    if order <= 0:
        raise ValueError("caller logic error")
    
    primes = []

    for candidate in range(2, 1_000_000):
        if prime(candidate, primes):
            primes.append(candidate)

        if len(primes) >= order:
            return primes[order - 1]


def prime(candidate, knwon_primes):
    skip_after = math.floor(math.sqrt(candidate))
    return all(candidate % prime != 0 for prime in knwon_primes[:skip_after])