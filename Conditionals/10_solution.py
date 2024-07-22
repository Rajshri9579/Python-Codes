pet_species = "Cat"
age_of_pet = int(input("Enter the age of your cat:"))

if pet_species == "Cat":
    if age_of_pet < 5:
       food_type = "Junior cat food"
    elif age_of_pet >=5:
        food_type = "Senior cat food" 

print(food_type," you should feed to your cat")