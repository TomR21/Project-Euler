# PROBLEM 25

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

n = 20
print(factorial(2*n) / (factorial(n)**2))

# If you let 0 denote going right and 1 going down, then there are 2n choose n ways to arrange the zeros in an array. 
# The ones will then be at the remaing spots 
