#polymorphism with operator 
print(10+4)
print("hello"+"world")
print([1,2]+[3,4])
#in the above example, the + operator is used to perform addition for integers, concatenation for strings, and merging for lists. this is an example of polymorphism, where the same operator behaves differently based on the data type of the operands.
#another example with multiplication operator
print(5*3)           #integer multiplication  
print("ha"*3)       #string repetition
print([1,2]*2)     #list repetition
#here, the * operator is used for multiplication with integers, repetition with strings, and repetition with lists, demonstrating polymorphism.
#benefits of polymorphism with operators:
#1.code simplicity: we can use the same operator for different data types without needing to define separate functions or methods for each type.
#2.extensibility: new data types can be added that support existing operators, allowing for seamless integration without changing existing code.
#3.readability: using familiar operators makes the code easier to read and understand, as the intent is clear regardless of the data type.
#4.maintainability: changes to operator behavior for a specific data type can be made in one place, improving code maintainability.
#overall, polymorphism with operators enhances the flexibility and usability of code by allowing the same operator to work with different data types in a context-appropriate manner.

