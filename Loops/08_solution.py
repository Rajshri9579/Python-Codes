#Prime Number Checker...
#Check if number is prime

number = int(input("Enter any number:"))
is_prime = True
if number > 1:
    for i in range(2,number+1):
        if (number % i) == 0:
            is_prime = False
            break
print(is_prime)
