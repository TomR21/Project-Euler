# PROBLEM 116
import math

total = 0
for n in range(2, 5):
    for x in range(1, int(50/n)+1):
        total += math.comb(50 - (n-1)*x, x)
        print(total)

# We can construct an array of 50 zeroes to represent all the grey tiles. Each red bar takes up two slots, and hence we can remove 
# 2 consecutive zeroes for a 1. This looks like this: [0, 0, 1, 0, 0, ...]. So we can find all possible combinations of placing 1 bar
# by calculating 49 choose 1. We can continue this process for multiple red bars, and this can also be applied to x bars of length n by 
# removing (n-1)*x from 50 and then calculating (this number choose x).   
