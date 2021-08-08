# PROBLEM 92

count = 0
for i in range(1, 10000000):
    a = [int(x) for x in str(i)]  # Make a list of all seperate integers in the number

    while a != [1] or a != [8, 9]:
        num = 0
        for z in a:
            num += z**2
        a = [int(x) for x in str(num)]

        if a == [1]:
            break
        if a == [8, 9]:
            count += 1
            break
            
print(count)
