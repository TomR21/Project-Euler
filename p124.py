# PROBLEM 124
# Returns product of all distinct prime factors
def prime_factors(n):
    x = n
    i = 2
    product = 1
    last_prime = 0
    while n > i:
        if x % i == 0:
            if i != last_prime:
                last_prime = i
                product *= i
            x = x / i
        else:
            i += 1

    return product


nums = {}
for n in range(1, 100_001):
    product = prime_factors(n)
    
    # If n is prime and larger than 4000, do not add to dict 
    if product == 1 and n > 3000:
        continue
    elif product == 1 and n <= 3000:
        rad = n
    else:
        rad = product
        if rad > 3_000:
            continue
    nums[n] = rad

sorted_dict = sorted(nums.items(), key=lambda x: (x[1], x[0]))
print(list(sorted_dict)[9999])

# As there will be a lot of products that are below 10.000, we only add rad values below 3.000, as any rad values above the 10.000th spot are irrelevant. 
# Furthermore, any prime above 3000 will also have a rad value too high to change the rankings below the 10.000th spot.
