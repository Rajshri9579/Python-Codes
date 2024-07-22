age = int(input("Enter the age:"))
day = input("Enter the day:")
price = 12 if age >= 18 else 8
if day == "Wednesday":
    price = price - 2
print(price)