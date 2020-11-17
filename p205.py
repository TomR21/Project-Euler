# Problem 205
slist = [[1, 2, 3, 4, 5, 6], [],[],[],[],[]]
for throws in range(5):                     # for each throw calculate all possible values (including duplicates) and add them to second list inside slist
    for n in range(1, 7): 
        for x in slist[throws]:
            slist[throws+1].append(x+n)

flist = [[1, 2, 3, 4],[],[],[],[],[],[],[],[]]
for throws in range(8):                    # same as previous one, except with 4 sided die
    for n in range(1, 5):
        for x in flist[throws]:
            flist[throws+1].append(x+n)

ctotal = len(slist[-1])
clist = [[x,0] for x in range(6, 37)]          # list containing die value and empty spot for occurances of that value
for x in slist[-1]:                            # calculate degeneracy of value
    clist[x-6][1] += 1

ptotal = len(flist[-1])                       # same as previous 
plist = [[x,0] for x in range(9, 37)]
for x in flist[-1]:
    plist[x-9][1] += 1


winchance = 0      
for p in plist:                             # for each die value, check if you win, and add those values to total wins
    wins = 0
    for c in clist:
        if p[0] > c[0]:
            wins += c[1]

    winchance += p[1]*(wins/ctotal)       # this is P(9) for first iteration: chance of winning when throwing that specific p

print(winchance/ptotal)

# Total Probability is defined as (n_9/n_total)*P(9) + (n_10/n_total)*P(10) + .... + (n_36/n_total)*P(36)
