#list comprehension use kora hoy list er moddhe loop chalate and notun list create korte

#syntax:
#new_list=[expression for item in iterable if condition==True]

#expression: kon value new list e add korte chai
#item: current item jeta iterable theke neya hocche
#iterable: kon object er moddhe loop chalate chai (list, string, tuple, set, dictionary)
#condition: optional, jodi kono specific condition er upor base kore new list create korte chai

#without comprehension
"""
squares=[]
for i in range(1,11):
  squares.append(i**2)
print(squares)

"""

#with comprehension
square=[i**2 for i in range(1,11)]
print(square)

#jodi even number er square chai
even_square=[i**2 for i in range(1,11) if i%2==0]
print(even_square)