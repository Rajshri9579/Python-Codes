#Recursive Function
#Create a recursive function to calculate the factorial of a number.

def factorial(m):
    if m == 0:
        return 1
    else:
        return m * factorial(m-1)

print(factorial(7))