# PROBLEM 123

def primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in range(3, int(n**0.5)+1, 2):
        if sieve[i]:
            sieve[i*i::2*i] = [False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3, n, 2) if sieve[i]]
    
primes = primes(1000000)
limit = 10**10

for p, n in zip(primes[20000:], range(20001, len(primes)-1)):
    val = (p - 1)**n + (p+1)**n
    remainder = val % (p*p)             # calculate remainder using % operator

    if remainder > limit:
        print(str(remainder)+" found for n: "+str(n)+" and p: "+str(p))
        break

    if n == 25000:                  # calculate remainder for n in batches of 5000, to close down on the value of n
        print("end reached, for p: "+str(p))
        break


# 10**9   n: 7037  p: 71059
# 10001595590 found for n: 21035 and p: 237737

#         n: 9999  p: 104723
#         n: 15000 p: 163847
#         n: 20000 p: 224737
