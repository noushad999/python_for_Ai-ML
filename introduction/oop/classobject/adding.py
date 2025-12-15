class car:
  def set_details(self,brand,color):
    self.brand=brand
    self.color=color
    
  def show_details(self):
    print(f"car brand is {self.brand} and color is {self.color}")
car1=car()
car1.set_details("Toyota","Red")
car1.show_details()

car2=car()
car2.set_details("Honda","Blue")
car2.show_details()


#code explanation:
#1.a class named car is defined with two methods: set_details and show_details.
#2.the set_details method initializes the attributes brand and color of the car object.
#3.the show_details method prints the brand and color of the car object.
#4.two instances of the car class are created: car1 and car2, each with their own attributes.
#5.the show_details method is called for both instances to display their details.
#output:
#car brand is Toyota and color is Red
#car brand is Honda and color is Blue

#so what is happening here!
#when we create an object of the class car, we can use the methods defined in the class to set and get the attributes of that object.
#the self parameter in the methods refers to the instance of the class itself, allowing us to access and modify the object's attributes.

#so what is self here!
#self is a reference to the current instance of the class. it is used to access variables and methods associated with the current object.
#when we define methods in a class, we need to include self as the first parameter to indicate that the method belongs to the instance of the class.
#when we call a method on an object, python automatically passes the object as the first argument
#for example:
#car1.show_details() is equivalent to car.show_details(car1)
