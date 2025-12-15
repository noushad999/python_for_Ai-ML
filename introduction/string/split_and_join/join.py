#join() method ekta iterable er moddhe thaka string gulo ke specific separator er basis e join kore ekta single string return kore.

str="a,b,c"
s=str.split(",")
print("after spliting",s)

#join
result=",".join(s)
print("after joining",result)