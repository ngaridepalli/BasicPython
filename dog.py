class Dog():

	def __init__(self,name,age):
		self.name=name
		self.age=age

	def sit(self):
		print(self.name.title(),"sitting")

	def rolling(self):
		print(self.name.title(),"rolling")


my_dog=Dog("wille",6)
print(my_dog.name.title()+" of age "+str(my_dog.age))
newname="doggy"
my_dog.name=newname
print("new name of my dog"+ my_dog.name.title()+" of age "+str(my_dog.age))
my_dog.sit()
my_dog.rolling()




