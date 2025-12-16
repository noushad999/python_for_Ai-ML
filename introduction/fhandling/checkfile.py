"""
to find whether a file exists or not:
we can use the os.path module in python to check if a file exists or not.
example:
import os
file_path = 'path/to/your/file.txt'
if os.path.exists(file_path):
    print("File exists")
else:
    print("File does not exist")
    
"""
import os

if os.path.exists('D:/python_for_Ai-ML/introduction/fhandling/data2.txt'):
    print("File exists")
else:
    print("File does not exist")