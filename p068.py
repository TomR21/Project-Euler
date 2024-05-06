# PROBLEM 68
import itertools

# Since the total value will start with the lowest number on the outside, leave all smallest numbers on the inside of the ring. 
outside = [6,7,8,9,10]
inside = [1,2,3,4,5]

# Function that checks if all rows have the same value 
def check_sum(lst_out, lst_in):
    a1 = lst_out[0]
    a2 = lst_out[1]
    a3 = lst_out[2]
    a4 = lst_out[3]
    a5 = lst_out[4]

    a6 = lst_in[0]
    a7 = lst_in[1]
    a8 = lst_in[2]
    a9 = lst_in[3]
    a10 = lst_in[4]

    sc1 = a1 + a6 + a7
    sc2 = a2 + a7 + a8
    sc3 = a3 + a8 + a9
    sc4 = a4 + a9 + a10
    sc5 = a5 + a10 + a6
    if sc1 == sc2 == sc3 == sc4 == sc5:
        return True
    else:
        return False

# Create a generator of all permutations of the outside values
outside_perms = itertools.permutations(outside)

# for each permutation of the outside values, loop over all permutations of inside values and check if any satisfy check_sum condition
for lst_out in outside_perms:
        inside_perms = itertools.permutations(inside)
        for lst_in in inside_perms:
            if check_sum(lst_out, lst_in):
                print(f"{lst_out}, {lst_in}")

# Turns out that a few do. Find the ones which have the highest possible value on the inside ring (5) immediately following the 6. 
