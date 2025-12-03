a=[1,2,3]
b=[3,4,5]

#set function to find common elements

s1=set(a)
s2=set(b)

s3=s1.intersection(s2)
print(list(s3))