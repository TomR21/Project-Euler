# PROBLEM 60

def primes(n):          # Function creating a list of prime numbers up to n using the sieve method 
    sieve = [True] * n
    for i in range(3, int(n**0.5)+1, 2):
        if sieve[i]:
            sieve[i*i::2*i] = [False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3, n, 2) if sieve[i]]
    
plist1 = func.primes(30000)

def is_prime(n):         # returns if int is prime (True) or not (False)
    if n % 2 == 0:
        return False
    for i in range(3, int((n**0.5)+1), 2):
        if n % i == 0:
            return False
    return True

def can_catenate(n, alist):    # returns if an int n can concatenate with int in a list (True) or not (False)
    for con_prime in alist:
        if not (is_prime(int(str(con_prime) + str(n))) and is_prime(int(str(n) + str(con_prime)))):
            return False

    return True           # if looped through, it can concatenate with all and hence we return true


lowest_sum = 100000
for p0, index0 in zip(plist1, range(len(plist1))):
    for p1, index1 in zip(plist1[index0+1:], range(len(plist1[index0+1:]))):    # use index slicing to prevent duplicate calculations, p1 always start higher than p0
        if not (is_prime(int(str(p0) + str(p1))) and is_prime(int(str(p1) + str(p0)))):
            continue

        for p2, index2 in zip(plist1[index1+1:], range(len(plist1[index1+1:]))):
            if not can_catenate(p2, [p0, p1]):
                continue

            for p3, index3 in zip(plist1[index2+1:], range(len(plist1[index2+1:]))):
                if not can_catenate(p3, [p0, p1, p2]):
                    continue

                for p4, index4 in zip(plist1[index3+1:], range(len(plist1[index3+1:]))):
                    count = 0                               # counts all prime concatenations for each iteration, need to be 8 for all concatenations to be prime
                    for con_prime in [p0, p1, p2, p3]:
                        if is_prime(int(str(con_prime) + str(p4))) and is_prime(int(str(p4) + str(con_prime))):
                            count += 2
                        else:
                            break

                    new_sum = p0 + p1 + p2 + p3 + p4
                    if count == 8 and new_sum < lowest_sum:             # only add new sum if lower then previous sum
                        lowest_sum = new_sum
                        print(lowest_sum)
