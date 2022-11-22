# PROBLEM 100
small = 5
same = 7
big = 10

n = 1
while True:
    new_small = small + same
    new_same = big + same
    new_big = 2 * new_small

    if n % 2 == 0:
        if new_big*small+1 > 10**12:
            print(new_same*small+1)
            print(new_big*small+1)
            break
    else:
        if new_big*small > 10**12:
            print(new_same*small)
            print(new_big * small)
            break

    small = new_small
    same = new_same
    big = new_big

    n += 1

# Each fraction of b/n * (b-1)/(n-1) = 1/2 is only valid when a/b * c/d when either a == d with b = 2c or b == c with d = 2a where a, b, c, d 
# are all integers. Let us denote a, d as same numbers when a == d, and b/c as big/small respectively when b = 2c.   
# It turns out that the new 2 numbers that are the same are the addition of the previous largest number and previous same number. 
# The new smallest number is the previous same number + previous small number. This can be done in a loop to until we have the first value of b above 10^12
