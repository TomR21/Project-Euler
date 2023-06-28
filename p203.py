# PROBLEM 203
import math

def primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in range(3, int(n**0.5)+1, 2):
        if sieve[i]:
            sieve[i*i::2*i] = [False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3, n, 2) if sieve[i]]

# Highest possible prime is the sqrt of the highest number, given by (50 choose 25)
prime_bound = math.floor(math.sqrt(math.comb(50, 25)))
prime_list = primes(prime_bound)
squares = [x*x for x in prime_list]

# Create a set to store all distinct numbers in, add all numbers to this set
distinct_nums = {1}
for n in range(1, 51):
    for k in range(0, math.ceil(n/2)+1):
        distinct_nums.add(math.comb(n, k))

# Add up all distinct numbers and subtract the numbers which are divisible by a square prime
count = sum(distinct_nums)
for num in distinct_nums:
    for square in squares:
        if num % square == 0:
            count -= num
            break

print(count)
