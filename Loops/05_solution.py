#Find the First Non-repeated character
#Given a string, find the first non-repeated character 
string = "teeterabcabcd"
for char in string:
    print(char)
    if string.count(char) == 1:
        print("Char is: ",char)
        break