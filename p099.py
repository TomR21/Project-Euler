# PROBLEM 99
import math

# Separate the base and exponent and put them together in a list
with open("p099_base_exp.txt") as file:
    list1 = []
    for line in file:
        string = str(line.rstrip('\n'))
        index = string.find(',')
        base = string[:index]
        exp = string[index + 1:]

        list1.append([int(base), int(exp)])

highest = 0
n = 0         # Line number
for x in list1: 
    n += 1
    extra = math.log(x[0], 2)  # Convert the base to base 2, and keep the extra exponent to obtain the new exponent (exponent * extra)
    
    # Now we only have to check if the new exponent is bigger than the previous highest exponent
    if extra * x[1] > highest:
        highest = extra * x[1]
        high_n = n

print(high_n)

# This works because we convert all bases to base 2, and hence we only have to look at which exponent is bigger
