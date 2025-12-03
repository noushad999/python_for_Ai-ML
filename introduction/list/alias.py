# list_1=[1,2,3]
# list_2=list_1
# print(f'Before modification list_1: {list_1}, list_2: {list_2}')

# list_2[0]=100
# print(list_1,list_2)

#ekhane dekha jacche je list_1 ero value change hoye gese karon list_2 holo list_1 er alias ba onno nam. Tai jodi amra list_2 ke modify kori tahole list_1 o modify hoye jabe.er jonno amra copy() method use korte pari.

list_1=[1,2,3]
list_2=list_1.copy()
list_2[0]=100
print(list_1,list_2)