
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


# In simple terms, the idea of scope can be described by 3 general rules:
#
# 1. Name assignments will create or change local names by default.
# 2. Name references search (at most) four scopes, these are:
#     * local
#     * enclosing functions
#     * global
#     * built-in
# 3. Names declared in global and nonlocal statements map assigned names to
# enclosing module and function scopes.
#
#
# The statement in #2 above can be defined by the LEGB rule.
#
# **LEGB Rule.**
#
# L: Local — Names assigned in any way within a function (def or lambda)),
# and not declared global in that function.
#
# E: Enclosing function locals — Name in the local scope of any and all
# enclosing functions (def or lambda), from inner to outer.
#
# G: Global (module) — Names assigned at the top-level of a module file, or
# declared global in a def within the file.
#
# B: Built-in (Python) — Names preassigned in the built-in names module :
# open,range,SyntaxError,...



#Local

# x is local here:
f = lambda x:x**2


# Enclosing function locals
#
# This occurs when we have a function inside a function (nested functions)
#

name = 'This is a global name'

def greet():
    # Enclosing function
    name = 'Sammy'

    def hello():
        print('Hello '+name)

    hello()

greet()




# Global
print name


# Built-in
# These are the built-in function names in Python (can't overwrite these!)

len


# Local Variables

# When you declare variables inside a function definition, they are not related
# in any way to other variables with the same names used outside the function -
# i.e. variable names are local to the function. This is called the scope of the
# variable. All variables have the scope of the block they are declared in
# starting from the point of definition of the name.
#
# Example:

x = 50

def func(x):
    print('x is', x)
    x = 2
    print('Changed local x to', x)

func(x)
print('x is still', x)


################################
# The Global Statement
################################

# If we want to assign a value to a name defined at the top level of the program
# (i.e. not inside any kind of scope such as functions or classes), then we have
# to tell Python that the name is not local, but it is global. We do this using
# the global statement. It is impossible to assign a value to a variable defined
# outside a function without the global statement.
#
# We can use the values of such variables defined outside the function
# (assuming there is no variable with the same name within the function).
 #Using the global statement makes it amply clear that the variable is defined
# in an outermost block.
#
# Example:

x = 50

def func():
    global x
    print('This function is now using the global x!')
    print('Because of global x is: ', x)
    x = 2
    print('Ran func(), changed global x to', x)

print('Before calling func(), x is: ', x)
func()
print('Value of x (outside of func()) is: ', x)


# The global statement is used to declare that x is a global variable - hence,
# when we assign a value to x inside the function, that change is reflected
# when we use the value of x in the main block.
#
# We can specify more than one global variable using the same global statement
# e.g. global x, y, z.

###############################
# Conclusion
###############################

# One last mention is that
#we can use the globals() and locals() functions to check what are our current
# local and global variables.


