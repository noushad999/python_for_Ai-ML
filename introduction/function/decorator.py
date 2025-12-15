"""
1.Decorators are a way to modify or enhance the behavior of functions or methods without changing their actual code.
2.Decorators are defined using the "@" symbol followed by the decorator function name above the function to be decorated.


example:
we are ordering a burger in a restaurant. we can add extra toppings or sauces to the burger without changing the original recipe of the burger. similarly, decorators allow us to add extra functionality to a function without modifying its code.

burger - function
extra toppings/sauces - extra features or functionality 

tar mane decorator holo function er behaviour k modify or enhance korar ekta way, jeta function er original code k change na kore extra functionality add kore.

"""

def my_decorator(func):
  def wrapper():
    print("Something is happening before the function is called.")
    func()
    print("Something is happening after the function is called.")
    
  return wrapper

@my_decorator
def say_hello():
  print("hello")
  
say_hello()

#code explanation:
#1.my_decorator function takes another function func as an argument.
#2.inside my_decorator, a nested function wrapper is defined, which adds extra functionality
#3.the wrapper function prints a message before and after calling the original function func.
#4.the my_decorator function returns the wrapper function.
#5.the @my_decorator syntax is used to apply the decorator to the say_hello
#6.when say_hello() is called, it actually calls the wrapper function, which adds the extra behavior defined in the decorator.
#output:
#Something is happening before the function is called.
#hello
#Something is happening after the function is called.
