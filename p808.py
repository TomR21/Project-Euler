# PROBLEM 808
import bisect

def primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in range(3, int(n**0.5)+1, 2):
        if sieve[i]:
            sieve[i*i::2*i] = [False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3, n, 2) if sieve[i]]


prime_square_list = [p*p for p in primes(100_000_000)]

total = 0
count = 0
for p in prime_square_list:     # Loop over each square prime
    p_rev = int(str(p)[::-1])
    if p_rev != p:        # check if it is not a palindrome
        index = bisect.bisect(prime_square_list, p_rev)   # find index of closest number to reverse number in sorted squared primes list
        if prime_square_list[index-1] == p_rev:     # if it exists, add it
            total += p
            count += 1

    if count == 50:
        break

print(total)
