"""
open() function in python:
the open() function is a built-in function in python that is used to open a file and return a file object.
it takes two arguments: the file name (or path) and the mode in which the file is to be opened.
the mode can be:
'r' - read mode (default): opens the file for reading.
'w' - write mode: opens the file for writing (creates a new file or truncates an existing file).
'a' - append mode: opens the file for appending (creates a new file if it does not exist).
'b' - binary mode: opens the file in binary mode (used for non-text files).
example of using open() function:
#opening a file in write mode
file = open("example.txt", "w")
#writing to the file
file.write("Hello, World!\n")
file.write("This is a file handling example in Python.")
#closing the file 
file.close()
#opening the file in read mode  
file = open("example.txt", "r")
#reading the contents of the file
content = file.read()
print(content)
#closing the file
file.close()
#output:
Hello, World!

syntax:
file = open("filename", "mode")

"""
file = open('D:/python_for_Ai-ML/introduction/fhandling/file.txt', 'r')
content = file.read()
print(content)
file.close()

