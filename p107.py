# PROBLEM 107
import numpy as np

m = np.zeros(shape=(40, 40))

with open("p107_network.txt", 'r+') as f:
    for index, line in enumerate(f):
        newline = line.replace('-', '100000')
        m[index, :] = newline.split(",")

total = 523664 / 2

# Add 100000 to all lower triangular values
e = np.tril(np.ones(shape=(40, 40))) * 100000
m = m + e

# Obtain all values from the matrix and sort them. 
lowest_vals = m.flatten()
lowest_vals.sort()   

# Main loop
paths = []
prev_val = 0
index = 0
count = 0
for val in lowest_vals:
    if val > 99000:
        break

    if prev_val == val:
        index += 1
    else:
        index = 0
        prev_val = val

    res = np.argwhere(m == val)
    x, y = res[index, 0] + 1, res[index, 1] + 1

    # Scanning if duplicates exist
    next = False
    both = 0
    for list in paths:
        if x in list and y in list:
            next = True

        if x in list:
            both += 1

        if y in list:
            both += 1

    if next:
        continue

    # Merge two list containing x and y
    paths_copy = paths[:]
    if both == 2:
        for l in paths_copy:
            if x in l:
                x_list = l
                paths.remove(l)
            if y in l:
                y_list = l
                paths.remove(l)

        paths.append(x_list + y_list)

    # Adding Phase
    add = True
    update_count = False
    for i, list in enumerate(paths):
        if x in list or y in list:
            list.append(x)
            list.append(y)
            paths[i] = list
            add = False
            update_count = True

    if add:
        paths.append([x, y])
        update_count = True

    if update_count:
        count += val

print(total - count)

# Solution was found using Kruskal's Algorithm. Most of the code in the loop is for identifying if the new edge makes the new graph cyclic or not.
