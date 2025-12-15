"""
string[start:stop:step]
start=0
stop=3,execlusive 3,2
step=1,2,3
"""

text="this is python programming"
#positive slicing
print(text[1:5:1])  #step=1
print(text[1:8:2])  #step=2
print(text[::])

#negative slicing
print(text[::-1])
