# Problem 101
import numpy as np

def f(n):
    ans = 1 - n + n**2 - n**3 + n**4 - n**5 + n**6 - n**7 + n**8 - n**9 + n**10
    return ans


generator_list = [f(x) for x in range(1, 12)]
bop_count = 1

# Loop for each polynomial of order x
for x in range(2, 11):
    b = generator_list[0:x]
    A = []
    
    # Fill the matrix with the polynomial eqs
    for i in range(1, x+1):
        A_sublist = [i**n for n in range(0, x)]
        A.append(A_sublist)

    # Use matrix algebra to obtain coefficients
    coefs = np.linalg.solve(A, b)

    # calculate the bop value and add it to the bop_count
    n = len(coefs) + 1
    res_list = [round(coefs[x])*n**x for x in range(len(coefs))]
    res = sum(res_list)

    bop_count += res

print(bop_count)
