# PROBLEM 87
import Functions as func

def primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in range(3, int(n**0.5)+1, 2):
        if sieve[i]:
            sieve[i*i::2*i] = [False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3, n, 2) if sieve[i]]

# for each power, calc all values as a look up table
p_squared = [x**2 for x in primes(7071)]    # 7071 is (5*10**7 - 2**3 - 2**4)**(1/2)
p_cubed = [x**3 for x in primes(369)]       # same as previous but with 1/3 power
p_quad = [x**4 for x in primes(85)]

limit = 5*10**7
numbers = set()               # use a set to prevent certain integers to appear multiple times
for p1 in p_squared:
    for p2 in p_cubed:
        if (p1 + p2) > limit:
            break
        for p3 in p_quad:
            ans = p1 + p2 + p3
            if ans >= limit:
                break
            
            numbers.add(ans)

print(len(numbers))
