# PROBLEM 73
import math

total = 3        # 3 values between 1/3 and 1/2 below d=9
for d in range(9, 12001):
    c_low = math.ceil(d/3)   # calculate lowest numerator above 1/3 in terms of c/d
    c_high = math.floor(d/2) # highest numerator below 1/2

    for numerator in range(c_low, c_high+1):    # range of all numerators for fraction 1/d
        if math.gcd(numerator, d) == 1:
            total += 1

print(total)
