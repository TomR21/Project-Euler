# PROBLEM 816
import numpy as np
from decimal import Decimal

s_new1 = 290797
s_new2 = (s_new1**2) % 50515093

points = [(s_new1, s_new2)]
N = 2_000_000
for _ in range(N-1):
    s_new1 = (s_new2**2) % 50515093
    s_new2 = (s_new1**2) % 50515093
    points.append([s_new1, s_new2])

points = np.array(points)
ind = np.lexsort((points[:, 0], points[:, 1]))

p_sort = points[ind]
distances = []
for i in range(len(p_sort)):
    for j in range(i+1, len(p_sort)):
        if p_sort[j, 1] - p_sort[i, 1] > 300:
            break
        if np.abs(p_sort[j, 0] - p_sort[i, 0]) < 300:
            x_diff = int(p_sort[j, 0]) - int(p_sort[i, 0])
            y_diff = int(p_sort[j, 1]) - int(p_sort[i, 1])
            d = Decimal(x_diff**2 + y_diff**2).sqrt()
            distances.append(d)

print(min(distances))

# Algorithm works by first calculating 2 million random points, then sorting one axis (x-axis) and transport the corresponding other elements in the other 
# row (y-axis) aswell. Now only check the closest points (x_diff < 300) and see if the other values (y_diff) also differ less than 300. If so, add distance
# to list and print out minimum distance
