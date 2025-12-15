num1=float(input("enter number 1:"))
num2=float(input("enter number 2:"))

choice=input("enter operation (+,-,*,/):")


if choice=='+':
  print("addition:",num1+num2)

elif choice=='-':
  print("subtraction:",num1-num2)

elif choice=='*':
  print("multiplication:",num1*num2)
  
elif choice=='/':
  if num2!=0:
    print("division:",num1/num2)
  else:
    print("Error: Division by zero is not allowed.")
else:
  print("Invalid operation")