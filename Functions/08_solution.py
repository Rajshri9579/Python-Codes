#Function with **kwargs.
#Create a function that accepts any number of keyword arguments and prints them i the format key: value.


def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}:{value}")


print_kwargs(name="Shaktiman", power="Lazer")
print_kwargs(name="Shaktiman", power="Lazer", enemy="Dr.Jackaal")