# Problem 2
f1 = 1
f2 = 2
sum = 0
while f1 < 4000000:
    new1 = f1+f2
    f1 = f2
    f2 = new1

    if f1 % 2 == 0:  # check if f1 is even
       sum += f1

print(sum)
