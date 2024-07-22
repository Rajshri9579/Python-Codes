#Validate Input
#Keep asking the user for input until they enter a number b/w 1 nd 0

number = int(input("Enter the input:"))
while True:
    if 1 <= number <= 10:
        print("Thanks")
        break
    else:
        print("Invalid number, please try again.....")
        exit()