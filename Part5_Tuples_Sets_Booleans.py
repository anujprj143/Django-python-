## Tuples, Sets, and Booleans ####
##################################
#
# Python tuples are very similar to lists, however, unlike lists they are
# immutable meaning they can not be changed. You would use tuples to present
# things that shouldn't be changed, such as days of the week, or dates on a calendar.
#
# Here we will get a brief overview of the following:
#
#     1.) Constructing Tuples
#     2.) Basic Tuple Methods
#     3.) Immutability
#     4.) When to Use Tuples.
#
# Now see how to use tuples based on what we've learned
# about lists. We can treat them very similarly with the major distinction being
# that tuples are immutable.
#
############################
#### Constructing Tuples ###
############################
#
# The construction of a tuples use () with elements separated by commas. For example:

#creating a tuple with mixed types
t = (1,2,3)

# Checking len just like a list
len(t)

# Can also mix object types
t = ('one',2)

# Show
t

# Using indexing just like we did in lists
t[0]

# Slicing just like a list
t[-1]

############################
### Basic Tuple Methods ####
############################

# Tuples have built-in methods, but not as many as lists do.


# Use .index to enter a value and return the index
t.index('one')

# Use .count to count the number of times a value appears
t.count('one')

####################
### Immutability ###
####################

# It can't be stressed enough that tuples are immutable.
# To drive that point home:

t[0]= 'change'
# we get error as : TypeError: 'tuple' object does not support item assignment


# Because of this immutability, tuples can't grow.
# Once a tuple is made we can not add to it.

t.append('nope')
#AttributeError: 'tuple' object has no attribute 'append'


############################
### When to use Tuples #####
############################

# we may be wondering, "Why bother using tuples when they have fewer available
# methods?" To be honest, tuples are not used as often as lists in programming,
# but are used when immutability is necessary. If in our program we are passing
#  around an object and need to make sure it does not get changed, then tuple
# become our solution. It provides a convenient source of data integrity.
#
#
# have an understanding of their immutability.
#

########################################################
########################################################
############## SETS AND BOOLEANS #######################
########################################################
########################################################
#
# There are two other object types in Python that we should know. Sets and Booleans.
#
############
### Sets ###
############

# Sets are an unordered collection of *unique* elements. We can construct them
# by using the set() function.

x = set()

#adding to sets with the add() method
x.add(1)

#Showing
x


# Note the curly brackets. This does not indicate a dictionary! Although you can
# draw analogies as a set being a dictionary with only keys.
#
# a set has only unique entries. So what happens when we try to add
# something that is already in a set?

# Adding a different element
x.add(2)

#Showing
x

# Trying to add the same element
x.add(1)

#Showing
x


#how it won't place another 1 there. That's because a set is only
# concerned with unique elements! We can cast a list with multiple repeat
# elements to a set to get the unique elements.

# Creating a list with repeats
l = [1,1,2,2,3,4,5,6,1,1]

# Cast as set to get unique values
set(l)

##########################
######## Booleans ########
##########################
# Python comes with Booleans (with predefined True and False displays that are
# basically just the integers 1 and 0). It also has a placeholder object called
# None.

# Setting object to be a boolean
a = True

#Showing
a


# We also use comparison operators to create booleans.

# Output is boolean
1 > 2


# We also use None as a placeholder for an object that we don't want to reassign yet:

# None placeholder
b = None
