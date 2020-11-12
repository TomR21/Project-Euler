# Problem 57

a1, a2 = 3, 7
b1, b2 = 2, 5    # Starting values

count = 0
for _ in range(3, 1001):
    anew = a1 + 2*a2         # calculate new numerator (a) and denominator (b)
    bnew = b1 + 2*b2

    if len(str(anew)) > len(str(bnew)):
        count += 1

    a1 = a2
    a2 = anew
    b1 = b2
    b2 = bnew

print(count)
