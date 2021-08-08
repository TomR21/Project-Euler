# PROBLEM 112
non_bouncy, bouncy = 9, 0
num = 10

while bouncy / (bouncy + non_bouncy) != 0.99:
    # Make a list of all single integers forming the number
    num_list = list(str(num))
    a = num_list[:]
    a.sort()
    b = num_list[:]
    b.sort(reverse=True)

    # If it is equal to either of the sorted lists, it is non_bouncy as it has the right order
    if num_list == a or num_list == b:
        non_bouncy += 1
    else:
        bouncy += 1
        
    num += 1
    
print(num-1)
