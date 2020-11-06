def palindrome(n):       # returns if int n is a palindrome or not
    if n == int(str(n)[::-1]):
        return True
    else:
        return False

list1 = []
for n in range(1, 7070):       # upper end is found by solving 10^8 = 2x^2 - 2x + 1 (where x is a positive int) and taking previous value
    i = n                     # for each starting value n, increment i up until the sum gets above 10^8
    asum = i**2               # asum is calculated once before loop to ensure numbers only get added to list that are a combination of two squares
    i += 1
    while asum < 100000000:
        asum += i**2
        if palindrome(asum) and asum < 100000000:
            list1.append(asum)
        i += 1
        
new = set(list1)   # remove duplicates
print(sum(new))
