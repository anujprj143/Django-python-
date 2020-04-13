######################
####--FUNCTIONS--#####
######################


#
# So what is a function?
#
# Formally, a function is a useful device that groups together a set of statements
# so they can be run more than once. They can also let us specify parameters that
# can serve as inputs to the functions.
#
# On a more fundamental level, functions allow us to not have to repeatedly write
# the same code again and again.
#
# Functions will be one of most basic levels of reusing code in Python, and it will
# also allow us to start thinking of program design
#

######################
# def Statements
######################


# Syntax has the following form:

def my_func(param1='default'):
    """
    Docstring goes here.
    """
    print(param1)

# Function begins with def then a space followed by the name of the function.
 #we wouldn't want to call a function the same name as a
# built-in function in Python (such as len).
#
# Next come a pair of parenthesis with a number of arguments separated by a comma.
# These arguments are the inputs for your function. You'll be able to use these
# inputs in your function and reference them. After this you put a colon.
#
# Now here is the important step, we must indent to begin the code inside our
# function correctly.
#
# Next we'll see the doc-string, this is where we write a basic description of
# the function. Using iPython and iPython Notebooks, we'll be able to read these
# doc-strings by pressing Shift+Tab after a function name. Doc strings are not
# necessary for simple functions, but its good practice to put them in so you or
# other people can easily understand the code written.
#


#
# ######################
# Example 1
# ######################

# A simple print 'hello' function

def hello():
    print("hello")

hello()

# ######################
# Example 2
# ######################

# We can expand on this by using the return keyword, that way we can actually return
# a result and save it for future use, instead of just displaying it.

def giveMeHello():
    return "hello"

result = giveMeHello()
print(result)

# Common mistake:
print(giveMeHello)
# give the error because the parenthesis is absent here after the function.

# ######################
# Example 3
# ######################
#
#  a function that returns tells you whether a number is even or not

def evenCheck(num):
    print("I'm checking to see if {} is even!".format(num))

    # Experienced way: (Don't need an if statement)
    print(num%2 == 0)

evenCheck(41)

# ######################
# Example 4
# ######################
#
# a function that will greet you!
#

def helloYou(name="Default Name"):
    return("Hello, "+name)

# Try this with and without a name
result = helloYou()
print(result)

# ######################
# Example 5
# ######################
#
# a function that will add two numbers together, only if they are even!
#

def addEvenOnly(num1,num2):
    """
    INPUT: Two numbers
    OUTPUT: False if both numbers are not even,
    the sum if both numbers ar even
    """
    if (num1 % 2!=0) or (num2 % 2 != 0):
        return False
    else:
        return num1+num2

x = addEvenOnly(1,2)
y = addEvenOnly(2,2)
print(x)
print(y)

# ######################
# Lambda Expressions
# ######################

# We won't always need a full blown function, often we just want to use
#  a function only once, in some of these cases, it makes more sense to use a
# lambda expression, also known as an anonymous function. example:

def timesTwo(num):
    return num*2

# Lambda expression
lambda num: num*2

# syntax is
# lambda input parameter : return_value

# To really understand the use case for this, we need to introduce a function
# that accepts other functions as input parameters, in this case, we will use filter:
#
my_list = [1,2,3,4,5,6,7,8,9,10]

def evenBool(num):
    return num%2 == 0
# function returns true if even and false otherwise

evens = filter(evenBool,my_list)
print(list(evens))

# Now with Lambda!
evens = filter(lambda num: num%2==0,my_list)
print(list(evens))



# ######################
# Methods
# ######################

# Methods are almost like functions that are built into the object. Some Methods
# return something, others just affect the object in place.

st = 'hello my name is Sam'
st.lower()
st.upper()
st.split()

tweet = 'Go Sports! #Sports'
tweet.split('#')
tweet.split('#')[1]

d = {'k1':1,'k2':2}
d.keys()
d.items()

lst = [1,2,3]
x = lst.pop()

# in Operator (not a method, just something useful)
# It returns true in case if the number is present is list, false otherwise
'x' in [1,2,3]

print('x' in ['x','y','z'])
