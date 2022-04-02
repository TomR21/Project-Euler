# PROBLEM 387
from math import sqrt, ceil

def is_prime(n):
    for x in range(2, ceil(sqrt(n))+1):
        if n % x == 0:
            return False

    return True

# Create all RTH between 10 and 100
harshads = []
for x in range(10, 100):
    x_list = [int(i) for i in list(str(x))]
    if x % sum(x_list) == 0:
        harshads.append(x_list)

# Main loop
count = 181  # Sum of strong, right truncatable Harshad primes between 1 and 99
harshads_old = [h[:] for h in harshads]
for k in range(3, 15):
    harshads_new = []

    # Loop over old harshad numbers
    for h in harshads_old:
      
        # Check if old harshad number is prime
        is_prev_prime = is_prime(int("".join(map(str, h))) / sum(h))

        # Loop for each new integer to be added at the end of old harshad number
        for x in range(10):
            newnum = int("".join(map(str, h + [x])))
            sums = sum(h) + x

            # Check if new number satisfies prime conditions, if so count it and dont add it to new harshad list
            if is_prev_prime:
                if is_prime(newnum):
                    count += newnum
                    continue

            # Check if new number is harshad
            if newnum % sums == 0:
                harshads_new.append(h + [x])

    # Copy new harshad numbers to use in next loop
    harshads_old = [h[:] for h in harshads_new]

print(count)


# The program starts off with making a list of all harshad numbers between 10 and 99. As all future numbers to be added to count need to have one of these 
# harshad numbers as their origin, we use these original numbers to check for new harshad numbers. This is done by taking the old number and adding 0 to 9
# at the end. In case the old harshad number divided by its digit sum is prime, aswell as the new number being prime, then it is added to the count and
# can no longer be a harshad number. This is because the new number is prime and hence dividing it by its digit sum will not be equal to an integer.
