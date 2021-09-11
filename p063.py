# PROBLEM 63
sum = 0
for n in range(1, 100):
    for a in range(1, 10):
        y = a**n
        list = [int(x) for x in str(y)]
        if len(list) == n:
            sum += 1

print(sum)
