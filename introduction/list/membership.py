"""
in operator use kore check kora hoy kono element list er moddhe ache kina.

not in operator use kore check kora hoy kono element list er moddhe nai kina.
"""

lst_1=[1,2,3,4,5]
check=int(input("Enter a number to check: "))
# if check in lst_1:
#   print("found")
# else:
#   print("not found")

#similarly using not in operator
if check not in lst_1:
  print("not found")
else:
  print("found")
