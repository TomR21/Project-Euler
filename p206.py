# Problem 206

for x in range(10**9, 10**10):   # Upper and lower limit for the integers
    ans = str(x**2)
    if ans[0] == "1" and ans[2] == "2" and ans[4] == "3" and ans[6] == "4" and ans[8] == "5":
        if ans[10] == "6" and ans[12] == "7" and ans[14] == "8" and ans[16] == "9":
            print(x)
            
