import math

threesum, fivesum, tsum = 0, 0, 0

for a in range(1, int(1000/5)):  # Sum of all 3 below 1000
    fivesum += 5*a
for b in range(1, math.ceil(1000/3)):  # Sum of all 5 below 1000
    threesum += 3*b
for c in range(1, math.ceil(1000/15)): # Sum of all duplicates (multiples of 15) below 1000
    tsum -= c*15

print(tsum + fivesum + threesum)