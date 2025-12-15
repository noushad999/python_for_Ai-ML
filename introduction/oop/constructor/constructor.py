
"""
__init__()
1.a special method in Python classes, known as a constructor, that is automatically called when an object of the class is created.
2.used to initialize the attributes of the object.
3.allows us to set initial values for the object's properties when it is instantiated.
4.the first parameter is always self, which refers to the instance being created. subsequent parameters can be used to pass values for initializing attributes.
5.it helps in setting up the object with necessary data right at the time of creation, making the code cleaner and more efficient.
example:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age 
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)
in this example, the __init__ method initializes the name and age attributes for each Person object created.
"""
#example without __init__ method
class character:
  def set_details(self, name, health, attack):
    self.name = name
    self.health = health
    self.attack = attack
  
  def attack_enemy(self):
    print(f"{self.name} attacks with power {self.attack}")
worrior = character()
worrior.set_details("Aragorn", 100, 50)
mage = character()
mage.set_details("Gandalf", 80, 70)   
worrior.attack_enemy()
mage.attack_enemy()
#whqt is happening here!
#we have to call the set_details method separately for each object to initialize their attributes.
#this can lead to errors if we forget to call the method or if we pass incorrect values.
#using __init__ method simplifies the object creation process and ensures that the attributes are always initialized correctly.


"""
3 types of constructors in python
1.default constructor: a constructor that does not take any parameters and initializes the object with default values.
2.parameterized constructor: a constructor that takes parameters to initialize the object with specific values.
3.constructor with default values: a constructor that takes parameters with default values, allowing for optional initialization.(self, name="Unknown", age=0)

"""