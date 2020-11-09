# Problem 65
l = [1]*105       # list filled with >100 ones
l[1] = 2
k = 2
for n in range(1, len(l)-3, 3):   # change every third entry to 2k, starting at pos 1 in the list (4th in actual list)
    l[n] = 2*k
    k += 1

num = 5  # start with calculating 5th fraction (19/7)
a1 = 8
a2 = 11
for i in l:
    anew = a1 + i*a2    # formula to calculate a_(new)th numerator
    
    if num == 100:
        d = [int(x) for x in list(str(anew))]
        print(sum(d))
        break

    a1 = a2
    a2 = anew
    num += 1
    
    # From the sequence given in the problem I saw that every numerator was found by a_n = a_(n-2) + i*a_(n-1), where the i was the value from the
    # continued fraction list
