class MyMessage:

	def __init__(self,message):
		self.message=message
		
 
	def display_message(self):
		print("I'm learning "+self.message+" In this chapter")
		
	def favourit_book(title):
	    #print("My Favourite Book is :"+title)
		return "My Favourite Book is :"+title
		
myMsg=MyMessage("Using Functions")
myMsg.display_message()
#myMsg.favourit_book("Alice in the wonder land")
print(myMsg.favourit_book("Alice in the wonder land"))
