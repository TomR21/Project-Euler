# PROBLEM 9

for a in range(1, 333):      
    for b in range(a+1, 1000 - 2*a - 1):
        c = 1000 - b - a
        if c < 1:           # Prevent negative c values from counting
            break
        if a**2 + b**2 == c**2:
            print(a*b*c)
            break

# As a < b < c, a can at most approximately be a value of 1000/3 = 333.33
# The upper range of b is 1000 - 2*a - 1, as we have to subtract both a and c, where c is atleast a + 2
