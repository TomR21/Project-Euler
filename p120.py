# PROBLEM 120

total = 0
for a in range(3, 1001):
    r_max = 0
    for n in range(1, 2000):           # high n is needed to include all possibilites
        ans = (((a-1)**n) + ((a+1)**n)) % (a**2)    # remainder of the function
        if ans > r_max:                     # check that ensures only highest r gets added 
            r_max = ans

    total += r_max

print(total)
