"""
with statement in python:
the with statement in python is used for resource management and exception handling. it is commonly used for file handling to ensure that a file is properly opened and closed after its suite finishes, even if an exception is raised.
the syntax of the with statement is as follows:
with expression as variable:
    with-block (statements)
example of using with statement for file handling:
with open("example.txt", "r") as file:
    content = file.read()
    print(content)
#output:
Hello, World!

while using the with statement, the file is automatically closed after the block of code is executed, even if an error occurs within the block. this helps to prevent resource leaks and makes the code cleaner and more readable.
#example of using with statement for file handling:
with open('D:/python_for_Ai-ML/introduction/fhandling/file.txt', 'r') as file:
    content = file.read()
    print(content)
#output:
Hello, World!

"""
with open('D:/python_for_Ai-ML/introduction/fhandling/data.txt','w') as file:
    content=input("enter some data to write into the file:")
    file.write(content)
print("data written successfully")
  
  