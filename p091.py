# PROBLEM 91

# Pythagoras works only if one of the angles is 90 degrees. Therefore check if one of these relations hold to find if there is 90 degree angle
# Note a, b, c are the lengths of A (OP), B (OQ) and C (PQ)
def find_ans(a,b,c):
    if a + b == c:
        return True
    elif a + c == b:
        return True
    elif b + c == a:
        return True
    else:
        return False


count = 0
N = 50

# Loop over all points in the lattice
for x1 in range(0,N+1):
    for y1 in range(0, N+1):
        for x2 in range(0,N+1):
            for y2 in range(0,N+1):
                if x1 == y1 == 0:
                    continue

                if x2 == y2 == 0:
                    continue

                if x1 == x2 and y1 == y2:
                    continue

                a_sqr = x1**2 + y1**2
                b_sqr = x2**2 + y2**2
                c_sqr = (x1 - x2)**2 + (y1 - y2)**2

                if find_ans(a_sqr, b_sqr, c_sqr):
                    count += 1

print(count/2)
