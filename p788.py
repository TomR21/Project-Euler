# PROBLEM 788
import math

# Start with D(2)
d_prev = 18
n = 3
while n < 2023:
    d_new = d_prev + 9
    i = 1    
    while i < n/2:
        d_new += math.comb(n, i)*pow(9, i)*10   # possible combinations
        d_new -= math.comb(n-1, i-1)*pow(9, i)  # remove for non-zero common index
        d_new -= math.comb(n-1, i)*pow(9, i)    # remove for zero common index
        i += 1

    n += 1
    d_prev = d_new

print(d_prev % 1_000_000_007)

# Each number of length n has to contain at least > n/2 same digits. The other digits can be whatever else, as long as they are not the same as the 
# most common digits, as these are counted elsewhere. So for n=5, we have some number aaxax, where the a is the common digit and x can be whatever. 
# The digit a has 10 possibilities (0-9) and x has 9 possibilites (0-9 excluding a). By starting with zero x's, we have 9 options (11111, ..., 99999). 
# Then additional x are added, counted by the variable i. Taking combinations gives the total possibilities, multiplied by 9 to the power i for 
# each possibility. x being equal to zero at the start of the number is accounted by for the second combination, while the last combination accounts for 
# the most common digit being zero, but removing all numbers where the first digit is zero. 
