# PROBLEM 74

def factorial(n):   # Returns the value of the factorial of number n
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

total = 0
for start in range(1, 10**6):
    value_list = [start]
    new_val = start
    count = 1
    while True:                # cycles until a value in value_list has been repeated 
        new_val = sum([factorial(int(x)) for x in str(new_val)])   
        if new_val in value_list:
            if count == 60:
                total += 1
                print("+1 at start: "+str(start))
            break
        value_list.append(new_val)
        count += 1

print(total)
