start=int(input("Enter starting value: "))

stop=int(input("Enter stopping value: "))

skip=int(input("Enter skip value: "))

for i in range(start,stop):
  if i==skip:
    continue
  print(i)