#reason for using self in python class
#when we define methods in a class, we use the self parameter to refer to the instance of the class.
#it allows us to access the attributes and methods of the class within its own methods.
#instance means object
#without self, python would not know which instance's attributes or methods we are trying to access.
#it is a convention in python to name the first parameter of instance methods as self, but you can technically use any name.
"""
class student:
  def set details(name,age):
    name=name
    age=age
    
student1=student()
student1.set_details("Alice",20)
print(student1.name)  #this will raise an error because name is not defined for student1 object
"""  
#what is happening here!
#when we call student1.set_details("Alice",20), python internally translates it to student.set_details(student1, "Alice", 20)
#but since we did not use self in the method definition, the attributes name and age are not associated with the student1 object.
#to fix this, we need to use self as the first parameter in the method definition.
#here python will think 
class student:
  def set_details(self,name,age):
    self.name=name
    self.age=age
    print(f"student name is {self.name} and age is {self.age}")
student1=student()
student1.set_details("Alice",20) 
print(student1.name)  #this will now work and print "Alice"