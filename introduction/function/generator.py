
#  yield ব্যবহার করলে function একটি generator হয়ে যায়।
#  return এর মতো value দেয়, কিন্তু function সম্পূর্ণ শেষ হয় না।
#  yield execution pause করে, পরেরবার আবার সেখান থেকেই শুরু হয়।
#  একসাথে সব data তৈরি না করে, প্রয়োজন অনুযায়ী একটার পর একটা value দেয়।
#  এতে memory কম লাগে (Lazy Evaluation)।
#  বড় dataset / file line-by-line পড়তে দারুণ উপকারী।

#yeild function example:

def count_down(num):
  while num > 0:
    yield num #yield means amra
    num -= 1
    
#using generator
for number in count_down(5):
  print(number)
  
#generator basically use kora hoy memory efficient way te data handle korar jonno, jekhane amra ekshathe sob data memory te rakhte chai na, barong proyojon moto data generate kori.jemon upore example e dekhano hoyeche, amra 5 theke 1 porjonto number generate korchi, kintu sobgulo number ekshathe memory te rakhini, protyekta number proyojon moto yield kore niye aschi.amader joto proyojon toto number generate korte pari, ebong memory te kom load pore.

"""
difference between return and yield:
1.return function ekbar e complete hoye jay, ebong function call korar por sei value return kore dey. yield function execution pause kore rakhe, ebong porer bar abar sei jaygay theke start kore.
2.return function sobgulo value ekshathe return kore dey, jokhon yield function proyojon moto ekta ekta kore value return kore dey.
3.return function memory te sobgulo value rakhte pare, jokhon yield function memory efficient way te data handle kore, karon eta proyojon moto value generate kore.

"""
"""
difference between generator and normal function:
1.normal function sobgulo value ekshathe return kore dey, jokhon generator function proyojon moto ekta ekta kore value return kore dey.
2.normal function execution complete hoye jay, jokhon generator function execution pause kore rakhe, ebong porer bar abar sei jaygay theke start kore.
3.generator function memory efficient way te data handle kore, karon eta proyojon moto value generate kore, jokhon normal function memory te sobgulo value rakhte pare.
"""

"""
difference between iterator and generator:
1.iterator holo ekta object jeta upor e loop chalayte pare, ebong tar moddhe next() method thake. generator holo ekta special type er iterator jeta yield statement use kore value generate kore.
2.iterator sobgulo value ekshathe memory te rakhte pare, jokhon generator memory efficient way te data handle kore, karon eta proyojon moto value generate kore.
3.generator function execution pause kore rakhe, ebong porer bar abar sei jaygay theke start kore, jokhon iterator er khetre emon kono feature thake na.

"""


"""
difference between generator and decorator:
1.generator function ekta special type er function jeta yield statement use kore value generate kore, jokhon decorator function arekta function er behavior modify or enhance kore without changing its actual code.
2.generator function memory efficient way te data handle kore, karon eta proyojon moto value generate kore, jokhon decorator function original function er code k change na kore extra functionality add kore.
3.generator function execution pause kore rakhe, ebong porer bar abar sei jaygay theke start kore, jokhon decorator function original function er behavior k modify or enhance kore.
"""