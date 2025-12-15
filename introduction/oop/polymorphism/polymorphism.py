
"""
Docstring for oop.polymorphism.polymorphism

polymorphism means same name but different forms.
in oop, polymorphism allows methods to do different things based on the object it is acting upon, even though they share the same name.
for example, consider a method called "attack" that is defined in multiple classes like "Warrior" and "Mage". when we call the "attack" method on a Warrior object, it performs a physical attack, while calling it on a Mage object performs a magical attack. this is polymorphism in action.
polymorphism provides several benefits in oop:
1.flexibility: polymorphism allows for writing more flexible and generic code that can work with different object types.
2.extensibility: new classes can be added with their own implementations of existing methods without modifying existing code.
3.simplified code: polymorphism can lead to cleaner and more understandable code by reducing the need for complex conditional statements to handle different object types.
example of polymorphism in python:
class Animal:
    def sound(self):
        pass
class Dog(Animal):
    def sound(self):
        return "Woof"
class Cat(Animal):
    def sound(self):
        return "Meow" 
def make_sound(animal):
    print(animal.sound())
dog = Dog()
cat = Cat()
make_sound(dog)  # Output: Woof
make_sound(cat)  # Output: Meow
in this example, the make_sound function demonstrates polymorphism by accepting any object of type Animal and calling its sound method, which behaves differently based on the actual object type (Dog or Cat).

another example for better understanding:
run
person can learn which means a person is running
car run on pertrol or diesel which means car is running
computer program is running which means computer is running
here run is same name but different forms

so what is happening here!
we have a common interface (the run action) that behaves differently based on the object type (person, car, computer). this is the essence of polymorphism in oop.

"""
# print(len("python"))
# print(len([1,2,3]))
# print(len({"name":"alice","age":25}))
#what is meant here!
#the len function is used to determine the length of different data types: a string, a list, and a dictionary.
#even though we are using the same function name len, it behaves differently based on the type of object it is called upon.
#this is an example of polymorphism, where the same function name can operate on different data types and produce appropriate results for each type.
#another example of polymorphism with classes
class bird:
  def sound(self):
    return "birds make sound"
  
class crow(bird):
    def sound(self):
      return "crow caws"
class sparrow(bird):
    def sound(self):
      return "sparrow chirps"

bird1=crow()
bird2=sparrow()

print(bird1.sound() ) #output: crow caws
print(bird2.sound() ) #output: sparrow chirps

#what is happening here!
#we have a base class Bird with a method sound. two subclasses, crow and sparrow, override the sound method to provide their specific implementations.
#when we call the sound method on instances of crow and sparrow, we get different outputs based on the actual object type, demonstrating polymorphism.
#benefits of polymorphism in this example:
#1.code reusability: we can use the same method name sound for different bird types without needing to create separate method names for each bird.
#2.extensibility: we can easily add new bird types with their own sound implementations without modifying existing code.
#3.simplified code: we can treat different bird types uniformly through the Bird interface, making the code cleaner and easier to understand.
