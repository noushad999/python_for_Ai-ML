class character:
  def __init__(self, name, health, attack):
    self.name = name
    self.health = health
    self.attack = attack
    self.blood= blood
  
  def attack_enemy(self):
    print(f"{self.name} attacks with power {self.attack} blood {self.blood}")

worrior = character("Aragorn", 100, 50,red)
mage = character("Gandalf", 80, 70,white)

worrior.attack_enemy()
mage.attack_enemy()


#code explanation:
#1.a class named character is defined with an __init__ method to initialize the attributes name, health, and attack.
#2.an attack_enemy method is defined within the class to print the attack action of the character
#3.two instances of the character class are created: worrior and mage, each with their own attributes.
#4.the attack_enemy method is called for both instances to demonstrate their behavior.
#output:
#Aragorn attacks with power 50
#Gandalf attacks with power 70