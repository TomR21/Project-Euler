import math

def primes(n):           # sieve method to obtain a list of primes
    sieve = [True] * n
    for i in range(3, int(n**0.5)+1, 2):
        if sieve[i]:
            sieve[i*i::2*i] = [False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3, n, 2) if sieve[i]]
    
primelist = primes(100)

highest_phi = [0, 0]            #[n, n/phi]
n = 1
for prime in primelist:     
    n *= prime                      # for each iteration, multiplicate by a prime

    if n > 10**6:
        break

    phi = 1                   # we start with phi=1 as 1 is always included
    for i in range(2, n):
        if math.gcd(i, n) == 1:   # check if they have dont a common divisor
            phi += 1
            
    val = n/phi 
    if val > highest_phi[1]:   # check if found value is greater than previous one
        highest_phi[0] = n
        highest_phi[1] = val

print(highest_phi)

# Answer: 510510
# We multiplicate the primes, because the only thing that determines whether a number is relatively prime is if its a prime itself. For example, 2 is a prime, 
and hence the number probably includes a 2. But as 4 is not prime and a multiple of 4, we can move on to 3, then to 5, 7, ...
