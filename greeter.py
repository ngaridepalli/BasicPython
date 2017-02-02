import car
#from car import *
#from car import Car
def greet_user():

	print("Hello!")
greet_user()

mycar=car.Car('Ford','GX',2015)
print(mycar.set_Descriptive_Name())
myelecar=car.EletricCar('Tesla','XX','2056','USA')
print(myelecar.set_Descriptive_Name())