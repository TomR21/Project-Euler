# PROBLEM 26

def cycle_length(digit_list, start_index):
    """ Returns the length of recurring cycle in a list of digits, starting at some index """
    index = 0
    start_value = digit_list[start_index]
    cycle_list = [start_value]

    # Loop either ends when the index has reached the end of the list or when a cycle has been found
    while True:
        index += 1
        if index == len(digit_list):
            return 0
        if digit_list[index] == start_value:
            n = len(cycle_list)
            if cycle_list == digit_list[index:index+n] == digit_list[index+n:index+2*n]:
                return n
            cycle_list.append(digit_list[index])
        else:
            cycle_list.append(digit_list[index])

def long_division(k, n):
    """ Returns up to the nth decimal value for 1/k """
    num = 10
    denom = k
    digits = []
    for _ in range(n):
        digit = num // denom
        num = (num - digit*denom)*10
        digits.append(digit)

    return digits

longest_cycle = 0
for k in range(2, 1000):
    digit_list = long_division(k, 5000)
    max_cycle = 0

    # Try for different starting places, as some start later (e.g. 1/6 = 0.1(6))
    for i in range(4):
        length = cycle_length(digit_list, i)
        if length > max_cycle:
            max_cycle = length

    if max_cycle > longest_cycle:
        print(k)
        longest_cycle = max_cycle
        
# Program works by first finding the 5000 decimal values, then searching for a recurring pattern using cycle_length. This is done for different starting places,
# and if one of them has a recurring cycle longer than the current longest the denominator value is printed out. 
