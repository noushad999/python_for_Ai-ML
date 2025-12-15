"""
if condition:
    #code block to be executed if condition is true
else:
    #code block to be executed if condition is false
elif:when we have multiple conditions to check
"""

age=int(input("Enter your age : "))

if(age>=18 and age<100): 
    print("You are eligible to vote")

elif(age<=0 ):
  print("Invalid age")
elif(age>=101):
  print("grter than 100")
else:
    print("You are not eligible to vote")