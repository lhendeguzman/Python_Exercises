# Challenge - Classes Exercise

# Add a method to the Car class called age
# that returns how old the car is (2019 - year)

# *Be sure to return the age, not print it

class Car:

    def __init__(self, model="", year=0, maker=""):
        self.model = model
        self.year = year
        self.maker = maker

    def age(self):
    	x = 2019 - self.year
    	return x

wigo = Car("Wigo", 2014, "Toyota")
print(wigo.age())

fortuner = Car("Fortuner", 2011, "Toyota")
print(fortuner.age())