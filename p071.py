# PROBLEM 71
import math

a = 3/7
distance = 100   # difference between calculated fraction and 3/7, starting at 100

for d in range(8, 1000000):
    c_d = math.floor((3*d)/7)   # calculate largest numerator below 3/7 in terms of c/d
    new_distance = abs((c_d/d)-a)  # new distance 

    if math.gcd(c_d, d) == 1 and new_distance < distance:
        distance = new_distance              # set the old distance to the smallest distance
        print("c: "+str(c_d)+", d: "+str(d))
        
# Only the smallest fraction below 3/7 is calculated for each denominator. 
# This is done because the answer most likely was in one of these fractions. Otherwise, the second largest numerator below 3/7 could be considered
