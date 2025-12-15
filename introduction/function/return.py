#return statement is used to exit a function and go back to the place where it was called. It can also return a value to the caller.

def get_full_name(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name  # returning the full name to the caller

name=get_full_name("noushad", "ramim")
print("Full Name:", name)

#return function use korar shomoy function k ekta variable e assign kora hoy tarpor oi variable print kora hoy.karon return function value return kore.


"""
1.function naming should be meaningful and descriptive.
2.length of function name should be reasonable.
3.use lowercase letters and underscores to separate words in function names.
4.avoid global variables inside functions.

"""