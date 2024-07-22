#Function with *args
#Write a function that takes variable number of arguments and returns their sum

def summ_all(*args):
    return sum(args)

print(summ_all(1,25,8))
print(summ_all(1,2,3,4,5,6,7,8,9))
print(summ_all(98,1))

#We can write any word on the place of args but writing args considered as a good practice. And * also plays an important role.