import time,math
class Car():

	def __init__(self,make,model,year):
		self.make=make	
		self.model=model
		self.year=year
		self.odometer_reading=0
	   
	def set_Descriptive_Name(self):
		long_name=self.make.title()+' '+self.model+' '+str(self.year)
		return(long_name.title())
   
	def read_Odometer(self):
	 	print("The odometer reading of the car is "+str(self.odometer_reading))   
	
	def getCarId(self):
		millseconds=time.time()*1000
		carId=str(math.ceil(millseconds/2016))+self.make+self.model
		if self.year<=2016:
			return(carId)
		else:
			return("1000")
			
class Battery():
	def __init__(self,wattage=100,size=10):
		self.wattage=wattage
		self.size=size
	def desc_battery(self):
		print("The size of battery is "+str(self.size))
		
class EletricCar(Car):
	def __init__(self,make,model,year,country):
		super().__init__(make,model,year)
		self.country=country
		self.battery=Battery()
	def read_Odometer(self):
		print("Electric car has Odometer reading of "+str(self.odometer_reading))
	
	
my_car=Car("Audi","A5",2016)	
#my_car.read_Odometer()   
#print(my_car.set_Descriptive_Name())
#print(my_car.getCarId())

my_tesla=EletricCar("tesla","12X",2017,"USA")
#print(my_tesla.set_Descriptive_Name()+"is made in "+my_tesla.country)
#my_tesla.read_Odometer()
