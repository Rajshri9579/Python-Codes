#Default parameter value
#write a function that greets a user. if no nsme is provided, it should greet with a default name.

def greet(name = "User"):
    return "Hello, " + name + " !"

print(greet("Chai"))
print(greet())