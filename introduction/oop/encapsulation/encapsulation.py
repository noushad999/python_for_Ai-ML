
"""
Docstring for oop.encapsulation.encapsulation

encapsulation is one of the fundamental principles of object-oriented programming (oop). it refers to the bundling of data (attributes) and methods (functions) that operate on that data into a single unit called a class. encapsulation helps to restrict direct access to some of an object's components, which can prevent the accidental modification of data and promote modularity and maintainability in code.
benefits of encapsulation:
1.data hiding: encapsulation allows for restricting access to certain attributes and methods, protecting the internal state of an object from unintended interference and misuse.
2.modularity: by encapsulating related data and behavior within a class, code becomes more organized and easier to manage.
3.maintainability: changes to the internal implementation of a class can be made without affecting the external code that uses the class, as long as the public interface remains unchanged.
4.reusability: encapsulated classes can be reused across different parts of a program or in different projects without exposing their internal workings.
example of encapsulation in python:
class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number  # private attribute
        self.__balance = balance  # private attribute
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
    def get_balance(self):
        return self.__balance
account = BankAccount("123456789", 1000)
account.deposit(500)
account.withdraw(200) 
print(account.get_balance())  # Output: 1300
in this example, the BankAccount class encapsulates the account number and balance as private attributes (prefixed with __). the methods deposit, withdraw, and get_balance provide controlled access to these attributes, ensuring that the internal state of the BankAccount object is protected from direct external modification.

shoja banglay:
encapsulation holo kono object er  internal details k hide kora and etar direct access k restricted kora. etar maddhome amra data k safe rakhte pari and code k aro organized and maintainable korte pari.
etake amra private attributes and methods er maddhome implement korte pari, jeta class er bahire theke access kora jay na. etar fole amra object er internal state k accidental modification theke protect korte pari.
etar fole amra better code organization, data protection, and easier maintenance pete pari.
er fole data modification er somoy unexpected behavior theke bachte pari, karon sudhu class er methods er maddhomei data access kora jay.

for example amra jodi phone class baniye thaki, tahole amra phone er internal components gulo k private rakhte pari, jate user ra sudhu phone er public methods gulo diyei phone k use korte pare, internal components gulo k direct access korte na pare. etar fole phone er internal state safe thake and unexpected behavior theke bacha jay.


"""

class bank_account:
  def __init__(self,acc_no,balance):
    self.acc_no=acc_no
    self.__balance=balance #private attribute .karon amra chaichi na user ra direct access korte pare.er jonno amra balance er age __ use korechi.
    
  def deposit(self,amount):
      self.__balance+=amount
      print(f"deposited amount: {amount} ,new balance: {self.__balance}") #private attribute access korar jonno amra method use korechi.ar amra ekhane f string use korechi.f string hocche string formatting er ekta notun upay.jekhane amra string er moddhe direct variable er value use korte pari.
      
  def get_balance(self):
        return self.__balance #controlled access to private attribute

account=bank_account("123456789",1000)
account.deposit(2000)
print(account.get_balance())

#behind the scene:
#1.a class named bank_account is defined with a constructor __init__ that initializes the account number and balance attributes.
#2.the balance attribute is made private by prefixing it with double underscores (__), restricting direct access from outside the class.
#3.a method deposit is defined to add an amount to the balance and print the new balance using an f string for formatting.
#4.a method get_balance is defined to provide controlled access to the private balance attribute.
#5.an instance of the bank_account class is created with an account number and initial balance.
#6.the deposit method is called to add money to the account, and the new balance is printed.
#7.the get_balance method is called to retrieve and print the current balance.


#jodi amra print(account.__balance) try kori tahole error dibe.karon amra chaichi na user ra direct access korte pare.etai amra private attribute k direct access korte dibo na.


"""
    kokhon f string use korbo!
    jokhon amra string er moddhe variable er value use korte chai tokhon amra f string use korbo.
    f string er age f use korte hoy.
    f string er moddhe variable er value use korar jonno amra curly braces {} use korte hoy.  

"""