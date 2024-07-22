# The following code is witten according to the questions given in questions.md file and execution should be done by removing comment tags whenever need......



class Car:
    total_car = 0
    
    def __init__(self, brand, model):
        self.__brand = brand             #here, in this line before brand __ is added for privacy purpose.
        self.__model = model             #here, in this line before brand __ is added for privacy purpose.
        Car.total_car += 1

    def get_brand(self):
        return self.__brand + " !"       #here, in this line before brand __ is added for privacy purpose.
   
    def full_name(self):
        return f"{self.__brand} {self.__model}"
    
    def fuel_type(self):
        return "Petrol or Diesel"
    
    @staticmethod                        #here, @staticmethod is a decorator which enhances the quality of methods......
    def general_description():
        return "Cars are means of transport"
    
    @property                            #again a new decorator....
    def model(self):
        return self.__model
        

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric Charge" 
    
    
#my_tesla = ElectricCar("Tesla","Model S","85kWh")
#print(isinstance(my_tesla, Car))                    #here, in both the lines isinstance function is used to verity whethe it is true or false..... 
#print(isinstance(my_tesla, ElectricCar))

#print(my_tesla.brand) 
#print(my_tesla.get_brand())
#print(my_tesla.fuel_type())
#print(my_tesla.battery_size)  
#print(my_tesla.model)
#print(my_tesla.full_name())

#Car("TATA", "Safari")
#Car("TATA", "Nexon")
#my_car = Car("TATA", "Safari")
#my_car.model = "City"
#print(safari.brand)
#print(Car.fuel_type())
#print(Car.total_car)
#print(my_car.model())
#print(my_car.model)
#print(Car.general_description())

#my_car = Car("Toyota", "Corolla")
#print(my_car.get_brand())
#print(my_car.brand)
#print(my_car.model)
#print(my_car.full_name())

#my_new_car = Car("TATA","Safari")
#print(my_new_car.model)

#from below last question of inheritance will take place....
class Battery:
    def battery_info(self):
        return "This is battery"


class Engine:
    def engine_info(self):
        return "This is engine"


class ElectricCarTwo(Battery,Engine, Car):
    pass

#my_new_tesla = ElectricCarTwo("Tesla", "Model S")
#print(my_new_tesla.engine_info())
#print(my_new_tesla.battery_info())