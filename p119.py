# PROBLEM 119

val_list = []
for n in range(2, 100):         # range long enough to produce a list of 33 items, so answer is most likely in there
    for x in range(2, 10):     
        val = n**x
        if sum([int(x) for x in str(val)]) == n:         # check if the sum is equal to the base 
            val_list.append(val)

val_list.sort()              # list needs to be sorted as it is not entirely in order
print(val_list[29])

# we calculate for n between 2 and 100 all powers of 2 till 10. If the sum of the digits of this value is equal to n,
# we have found one of the numbers we are looking for. 
