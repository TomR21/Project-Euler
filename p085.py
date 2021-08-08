# PROBLEM 85

distance = 2*10**6
lowest_distance = 2*10**7      # lowest difference between amount of rect and distance
for x in range(3, 100):
    for y in range(60, 150):   # y values picked after some testing, values below 60 gave too low values of total rect
        total = 0              # total rectangles for x and y
        for i in range(1, x+1):              # i, j are coordinates of rect 
            for j in range(1, y+1):
                total += (x-i+1)*(y-j+1)   # add additional rect for each i, j 

        newdistance = abs(distance - total)
        if newdistance < lowest_distance:
            lowest_distance = newdistance
            print(str(total) + " at x:" + str(x) + " and y:" + str(y)+" with area:"+str(x*y))
            
# each area x by y can have rectangles (i, j) of i=1, 2, ..., x and j=1, 2, ..., y
# the amount of rect that fit within the area are the remaining x for each y, or ((x+1)-i)*((y+1)-1) for the total amount of rectangles,
# where the +1 comes from the fact that the initial rectangle itself also needs to be counted 
