# PROBLEM 102
import math
import csv


def contains_origin(alist):
    """ Returns True if the triangle contains the origin, False when not """
    # Calculate triangle area using Hedon's Formula 
    Ax, Ay, Bx, By, Cx, Cy = alist
    ac = math.sqrt((Ax - Cx) ** 2 + (Ay - Cy) ** 2)
    ab = math.sqrt((Ax - Bx) ** 2 + (Ay - By) ** 2)
    bc = math.sqrt((Cx - Bx)**2 + (Cy - By)**2)
    s = (ac+ab+bc)/2

    area1 = math.sqrt(s*(s-ab)*(s-bc)*(s-ac))

    # Calculate area of three triangles, all with O(irigin) as one of the three points
    d1 = math.sqrt(Ax ** 2 + Ay ** 2)
    d2 = math.sqrt(Bx ** 2 + By ** 2)
    d3 = math.sqrt(Cx**2 + Cy**2)

    s1 = (d1+d2+ab)/2
    area_ab = math.sqrt(s1*(s1-d1)*(s1-d2)*(s1-ab))

    s2 = (d1+d3+ac)/2
    area_ac = math.sqrt(s2*(s2-d1)*(s2-d3)*(s2-ac))

    s3 = (d2+d3+bc)/2
    area_bc = math.sqrt(s3*(s3-d2)*(s3-d3)*(s3-bc))
    area2 = area_ab + area_ac + area_bc

    # Check if the area1 and area2 are roughly similar (uncertainty arises from floating point errors) 
    # If they are similar, the origin must be within the triangle.
    if area2 - area1 > 0.1:
        return False
    else:
        return True


with open('p102_triangles.txt', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

count = 0
for list in data:
    coords_list = [int(x) for x in list]
    if contains_origin(coords_list):
        count += 1

print(count)
