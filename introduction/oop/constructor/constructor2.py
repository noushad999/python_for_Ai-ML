# example with __init__ method
class Car:
  def __init__(self,brand,color):
    self.brand=brand
    self.color=color
    
car1=Car("Toyota","Red") #values automatically set during object creation but without  __init__ method we have to call separate method to set values
print(f"car1 brand is {car1.brand} and color is {car1.color}")


"""
syntax:
class ClassName:
    def __init__(self, parameter1, parameter2, ...):
        self.attribute1 = parameter1
        self.attribute2 = parameter2
        ...
example:
class Character:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack
character1 = Character("Aragorn", 100, 50)
character2 = Character("Gandalf", 80, 70) 
"""