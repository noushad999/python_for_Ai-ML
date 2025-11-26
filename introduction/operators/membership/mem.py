"""
membership operators are used to test whether a value or variable is present in a sequence (such as a string, list, tuple, set, or dictionary).
"""

"""
in operator return true if we find the specified value in the sequence

not in operator return true if we do not find the specified value in the sequence

we cant use membership operators with numbers like int or float

etc
a=12345
print(1 in a) #error
"""

fruit=["apple","banana","cherry"]
print("banana"in fruit) #true
print("apple" not in fruit) #true