"""
append mode in python:
the append mode in python is used to open a file for adding new data at the end of the file without deleting the existing data.
if the file does not exist, it creates a new file.
the syntax for opening a file in append mode is as follows:
file = open("filename", "a")
example of using append mode:
#opening a file in append mode
file = open("example.txt", "a")
#appending data to the file
file.write("This is an appended line.\n")
file.write("Appending another line.")
#closing the file
file.close()  
#opening the file in read mode to verify the appended data
file = open("example.txt", "r")
#reading the contents of the file
content = file.read()
print(content)
#closing the file
file.close()
#output:
Hello, World!

"""
with open('D:/python_for_Ai-ML/introduction/fhandling/data2.txt','a') as file:
  
 content=input("enter some data to append into the file:")
 file.write(content)
print("data appended successfully")