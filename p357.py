# PROBLEM 357
import math
from numba import jit


@jit(nopython=True)          # Increase computational speed by precompiling the count_check function
def count_check(n):
    for d in range(1, int(math.sqrt(n)) + 1):   # As the rem - d pairs are symmetric (30/2 = 15 <=> 30/15 = 2), only divisors up to the square root
        rem = n / d                             # have to be calculated
        if rem == int(rem):   # check for proper divisor
            val = rem + d
            
            # Checks if val is prime, immediately stops when it is not
            for x in range(2, int(math.sqrt(val)) + 1):     
                if val % x == 0:
                    return 0
    return n


sum = 0
for n in range(1, 100_000_001):
    sum += count_check(n)

print(sum)
