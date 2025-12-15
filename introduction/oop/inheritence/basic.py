class Animal:
  def speak(self):
    return "Animal speaks"

class Dog(Animal):
  def bark(self):
    return "Dog barks"
  
dog=Dog()
dog.speak()
dog.bark()

