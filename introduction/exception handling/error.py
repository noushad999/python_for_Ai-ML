"""
Docstring for oop.inheritence.error

1.what are errors!
in programming, errors are issues or problems in the code that prevent it from running correctly. they can occur for various reasons, such as syntax mistakes, logical flaws, or unexpected conditions during execution.
there are several types of errors in programming, including:
1.syntax/compile time errors: these occur when the code violates the rules of the programming language, such as missing parentheses or incorrect indentation.
2.runtime errors: these happen during the execution of the program, such as division by zero or accessing an undefined variable.
3.logical errors: these are mistakes in the program's logic that lead to incorrect results, even though the code runs without crashing.

2.handling errors in python
python provides several mechanisms to handle errors gracefully, allowing programmers to manage exceptions and maintain the flow of the program. some common techniques include:
1.try-except blocks: these allow you to catch and handle exceptions that may occur during the execution of a block of code.
2.finally block: this block is executed after the try-except blocks, regardless of whether an exception occurred or not. it is often used for cleanup actions.
3.raise statement: this is used to manually raise exceptions when certain conditions are met in the code.
4.custom exceptions: programmers can define their own exception classes to handle specific error conditions in a more meaningful way. 
3.example of error handling in python
try: 
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = num1 / num2
    print(f"The result is: {result}")
except ValueError:
    print("Invalid input! Please enter numeric values.")
except ZeroDivisionError:
    print("Error! Division by zero is not allowed.")
finally:
    print("Execution completed.")
#what is happening here!
#1.the try block contains code that may potentially raise exceptions. 
#2.if a ValueError occurs (e.g., if the user inputs a non-numeric value), the corresponding except block handles it and prints an error message.
#3.if a ZeroDivisionError occurs (e.g., if the user tries to divide by zero), the corresponding except block handles it and prints an error message.
#4.the finally block is executed at the end, regardless of whether an exception occurred or not.

"""
"""
errors in software is called bugs.
and removing+fixing bugs is called debugging.

for example:
1.syntax error:
print("hello world"
#here the closing parenthesis is missing, which will raise a syntax error.  
2.runtime error:
a = 10
b = 0
result = a / b
#here dividing by zero will raise a runtime error.
3.logical error:
def calculate_area(radius):
    return 3.14 * radius * radius
area = calculate_area(5)
print(f"Area of the circle is: {area}")
#here if we mistakenly use 3.14 instead of math.pi, it will lead to a logical error in the area calculation.
#so what is happening here!
#1.syntax errors are detected by the interpreter before the code is executed, preventing the program from running.
#2.runtime errors occur during the execution of the program and can cause it to crash if not handled properly.
#3.logical errors do not raise exceptions but lead to incorrect results, requiring careful debugging to identify and fix the issue. 

"""
"""
what is exception!
an exception is an event that occurs during the execution of a program that disrupts the normal flow of instructions. it is a way for a program to signal that an error or unexpected condition has occurred.
examples of exceptions in python:
1.zero division error:
a = 10
b = 0
result = a / b  # raises ZeroDivisionError
2.index error:
my_list = [1, 2, 3]
print(my_list[5])  # raises IndexError
3.key error:
my_dict = {"name": "Alice", "age": 25}
print(my_dict["gender"])  # raises KeyError
4.type error:   
num = "10"
result = num + 5  # raises TypeError    
#so what is happening here!
#1.exceptions are raised when the program encounters an error condition that it cannot handle.
#2.each of the examples above demonstrates a different type of exception that can occur in python.
#3.when an exception is raised, the program's normal flow is interrupted, and if not handled, it will terminate with an error message.
#4.to handle exceptions and maintain the program's flow, we can use try-except blocks as demonstrated in the previous example.

exception->
1.start while program execution
2.warning sign that something is wrong
3.catch and handle the issue



"""
'''
exception handling?
1.a mechanism to handle runtime errors in a controlled manner, allowing the program to continue executing or fail gracefully.
2.provides a way to catch and respond to exceptions that may occur during program execution.
3.helps in maintaining the normal flow of the program even when unexpected errors occur.
example of exception handling in python:
try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = num1 / num2
    print(f"The result is: {result}")
except ValueError:
    print("Invalid input! Please enter numeric values.")
except ZeroDivisionError:
    print("Error! Division by zero is not allowed.")   
finally:
    print("Execution completed.")
#what is happening here!
#1.the try block contains code that may potentially raise exceptions.   
#2.if a ValueError occurs (e.g., if the user inputs a non-numeric value), the corresponding except block handles it and prints an error message.
#3.if a ZeroDivisionError occurs (e.g., if the user tries to divide by zero), the corresponding except block handles it and prints an error message.
#4.the finally block is executed at the end, regardless of whether an exception occurred or not.
benefits of exception handling:
1.error management: allows programmers to handle errors gracefully without crashing the program.
2.code clarity: separates error-handling code from regular code, making it easier to read and maintain.
3.debugging aid: provides useful information about the nature of errors, aiding in debugging and troubleshooting.
4.resource management: ensures that resources (like file handles or network connections) are properly released, even in the event of an error.


'''


"""
try block:
1.a block of code that is used to wrap code that may potentially raise exceptions.
2.allows programmers to test a block of code for errors.
3.if an exception occurs within the try block, the control is transferred to the corresponding except block.

try-code error
except block:
1.a block of code that is used to handle exceptions raised in the try block.
2.specifies the type of exception it can handle.
3.allows programmers to define custom error-handling logic for specific exceptions.
example:
try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = num1 / num2
    print(f"The result is: {result}")
except ValueError:
    print("Invalid input! Please enter numeric values.")
except ZeroDivisionError:
    print("Error! Division by zero is not allowed.")
#what is happening here!
#1.the try block contains code that may potentially raise exceptions.
#2.if a ValueError occurs (e.g., if the user inputs a non-numeric value), the corresponding except block handles it and prints an error message.
#3.if a ZeroDivisionError occurs (e.g., if the user tries to divide by zero), the corresponding except block handles it and prints an error message.
#4.this allows the program to continue executing without crashing, providing a better user experience.

"""
try:
    num=int(input("enter a number: "))
    result=10/num
    print(f"result is: {result}")
except ZeroDivisionError:
    print("error! division by zero is not allowed.")

except ValueError:
    print("error! please enter a valid number.")
    
except TypeError:
    print("error! invalid input type.")

finally:
    print("execution completed.")
#what is happening here!
#1.the try block contains code that may potentially raise exceptions.
#2.if a ZeroDivisionError occurs (e.g., if the user inputs zero), the corresponding except block handles it and prints an error message.
#3.if a TypeError occurs (e.g., if the user inputs a non-numeric value), the corresponding except block handles it and prints an error message.
#4.the finally block is executed at the end, regardless of whether an exception occurred or not.

#finally block:
"""
1.a block of code that is used to define cleanup actions that must be executed under all circumstances
2.it is placed after the try and except blocks
3.the code inside the finally block is executed regardless of whether an exception occurred or not.
example:
try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = num1 / num2
    print(f"The result is: {result}")
except ValueError:
    print("Invalid input! Please enter numeric values.")
except ZeroDivisionError:
    print("Error! Division by zero is not allowed.")
finally:
    print("Execution completed.")
#what is happening here!
#1.the try block contains code that may potentially raise exceptions.
#2.if a ValueError occurs (e.g., if the user inputs a non-numeric value), the corresponding except block handles it and prints an error message.
#3.if a ZeroDivisionError occurs (e.g., if the user tries to divide by zero), the corresponding except block handles it and prints an error message.
#4.the finally block is executed at the end, regardless of whether an exception occurred or not.    
"""

