
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


