"""
Docstring for handling.file
file handling in python:
file handling is an important aspect of programming that allows us to read from and write to files on our computer.
in python, we can handle files using built-in functions and methods. 

2 primary files types:
1.text files: these files contain plain text and can be easily read and edited using text editors. examples include .txt, .csv, .html files.
2.binary files: these files contain data in a format that is not human-readable. examples include .jpg, .png, .exe files. 
file operations:
1.opening a file: we can open a file using the open() function, which takes the file name and mode (read, write, append) as arguments.
2.reading from a file: we can read the contents of a file using methods like read(), readline(), and readlines().
3.writing to a file: we can write data to a file using methods like write() and writelines().
4.closing a file: it is important to close a file after we are done with it using the close() method to free up system resources. 
example of file handling in python:
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
This is a file handling example in Python.
"""


"""
all modes and explanations:
'r' - read mode (default): opens the file for reading.
'w' - write mode: opens the file for writing (creates a new file or truncates an existing file).
'a' - append mode: opens the file for appending (creates a new file if it does not exist).
'b' - binary mode: opens the file in binary mode (used for non-text files). 

'x' - exclusive creation: creates a new file and opens it for writing. raises an error if the file already exists.
't' - text mode (default): opens the file in text mode (used for text files).
'+' - read and write mode: opens the file for both reading and writing.
'r+' - read and write mode: opens the file for both reading and writing. the file pointer is placed at the beginning of the file.
'w+' - write and read mode: opens the file for both writing and reading. creates a new file or truncates an existing file.
'a+' - append and read mode: opens the file for both appending and reading. creates a new file if it does not exist.
'x+' - exclusive creation and read/write mode: creates a new file and opens it for both reading and writing. raises an error if the file already exists.


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

"""

