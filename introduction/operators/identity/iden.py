"to compare the memory location of two objects"

"""
is-when both objects point to the same memory location
is not-when both objects point to different memory locations
"""

a=[1,2,3]
b=a
c=[1,2,3]

print(a is b)      #True
print(a is c)      #False