# PROBLEM 58
import math


def is_prime(n):
    if n % 2 == 0:
        return False
    for i in range(3, math.ceil(n**0.5)+1):
        if n % i == 0:
            return False
    return True


primes = 3
total = 5
ratio = primes/total

value = 9
inc = 4
while ratio >= 0.1:                     # until the ratio is below 0.1, for each loop get the 4 values and add the primes to the primes counter
    for i in range(4):
        value += inc
        if is_prime(value):
            primes += 1
        total += 1

    ratio = primes/total
    inc += 2                           # increment each value, goes up for each new 2 row/columns added

print(inc-1)               # inc - 1 as the inc gets incremented by 2 when we have found the found, but the total length is inc + 1
