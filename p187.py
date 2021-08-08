# PROBLEM 187
import bisect

# Sieve method of finding primes
def primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in range(3, int(n**0.5)+1, 2):
        if sieve[i]:
            sieve[i*i::2*i] = [False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3, n, 2) if sieve[i]]


prime_list = primes(51*10**6)  # list of all primes up to 51.000.000 (51 instead of 50 to prevent index error)
index = 0
sum = 0

for p1 in prime_list:
    # Find the first value in prime_list where the product p1*rem exceeds 10**8
    rem = (10**8) / p1
    last_index = bisect.bisect_left(prime_list, rem)    

    # As all products are unique, we can simply add all possible combinations to the total
    sum += len(prime_list[index:last_index])
    index += 1             # Increase starting index to avoid duplicate combinations (i.e. 2*5 and 5*2)

print(sum)
