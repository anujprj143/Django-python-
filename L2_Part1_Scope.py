
# Nested Statements and Scope 


#A Variable names have a "scope", which determines the visibility of that variable name to other parts of our code.



x = 25

def printer():
    x = 50
    return x

print(x)
print(printer())


#Guess the output of print x? 25 or 50? Or what about this:

print(x)
print(printer())
print(x)


