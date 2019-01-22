# gathering keyword args, the SCATTER operator **
'''
function that gathers all its arguments in a tuple
you can call this function with any number of positional arguments(arguments that don't have keywords)
'''
def printall(* args):
    print(args)

printall(1, 23, "adsad")


# as we were saying, if the arguments are named...
# DOES NOT WORK


# printall(1, 324, third="adasd")   unexpected keyword argument


# to gather keyword arguments, you have to use ** operator (SCATTER operator

def printall2(* args, **kwargs):
    print(args, kwargs)

printall2(1, 324, third ="adasd") # (1, 324) {'third': 'adasd'}



# other use

d = dict(x = 1, y = 2)
print(d)

from collections import  namedtuple

Point = namedtuple('Point', ['x', 'y']); p = Point(2, 3)
print(p)

# passing a dictionary  to constructor
pp = Point(**d)  # using scatter operator
print(pp)

