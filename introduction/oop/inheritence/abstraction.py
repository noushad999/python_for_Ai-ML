#abstraction hocche kono complex system er unnecessary details gulo k hide kora, jate user ra sudhu relevant information gulo te focus korte pare. abstraction er maddhome amra code k aro simple, organized, and maintainable korte pari. abstraction k amra class er maddhome implement korte pari, jekhane amra sudhu important attributes and methods gulo define kori, ebong internal implementation details gulo k hide kori.
#for example, dhoren amra ekta vehicle class baniyechi, jekhane amra sudhu vehicle er important attributes and methods gulo define korechi, jemon start_engine, stop_engine, ebong drive. user ra sudhu ei methods gulo use kore vehicle k operate korte pare, kintu tader kache engine er internal implementation details gulo hide thake.
#so what is happening here!
#abstraction er maddhome amra complex system gulo k simple and understandable korte pari. 
#etar fole user ra sudhu relevant information gulo te focus korte pare, ebong unnecessary details gulo theke bachte pare. abstraction er fole amra better code organization, reusability, and maintainability pete pari.

from abc import ABC, abstractmethod

class Vehicle(ABC):
  @abstractmethod
  def start(self):
    pass #no implementation
  
class Car(Vehicle):
  def start(self):
    return "Car engine started"

class Bike(Vehicle):
  def start(self):
    return "Bike engine started"
  
car=Car()
bike=Bike()

print(car.start())  # Output: Car engine started
print(bike.start())  # Output: Bike engine started