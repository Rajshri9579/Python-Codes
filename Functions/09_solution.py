#Generate function with yield
#Write a generator function that yields even numbers up to a specified limit.

def even_generator(limit):
    for i in range(2,limit+1,2):
        yield i
        
for num in even_generator(34):
    print(num)


#When we use keyword return it only iterates single value and then loop stops, that's why keyword yield comes into the picture becoz yield also returns value  but keeps that function in memory as well as keeps its state as it is in memory and finalllyyyy code runs.......