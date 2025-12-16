"""
nested try-except blocks:
1.a try-except block that is placed inside another try or except block.
2.allows for more granular error handling in complex scenarios.
3.enables handling of different exceptions at different levels of the code.
example:
try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    try:
        result = num1 / num2
        print(f"The result is: {result}")
    except ZeroDivisionError:
        print("Error! Division by zero is not allowed.")
except ValueError:
    print("Invalid input! Please enter numeric values.")
#what is happening here!
#1.the outer try block contains code that may raise a ValueError.   
#2.if a ValueError occurs (e.g., if the user inputs a non-numeric value), the outer except block handles it and prints an error message.
#3.the inner try block contains code that may raise a ZeroDivisionError.
#4.if a ZeroDivisionError occurs (e.g., if the user tries to divide by zero), the inner except block handles it and prints an error message.
"""
try:
    num1=int(input("enter a number: "))
    num2=int(input("enter another number: "))
    try:
        result= num1/num2
        print(f"result is: {result}")
    except ZeroDivisionError:
        print("error! division by zero is not allowed.")
except ValueError:
    print("error! please enter a valid number.")