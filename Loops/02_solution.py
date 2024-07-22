#Sum of Even Numbers
#Calculate the sum of even numbers up to a given number n.

n = int(input("Enter the count of numbers:"))
sum_even = 0
for i in range(1,n+1):
    if i % 2 == 0:
        sum_even += 1
print("Sum of even numbers from 1 upto n is:",sum_even)