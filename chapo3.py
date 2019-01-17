# functions

x = 42

# function call
type(x)

print(type(type)) # class type

# name of the function: type
#  expression in parentheses: argument

# function takes an argument and returns a result (returned value)

# function to convert values from one type to another

y = str(x)

print(type(x))
print(type(y))

# not everything can be converted

z = "aaa"

# int(z) # ValueError


t = int(2.99)
print(type(t))
print(int(t)) # gets only the integer part


# math functions
import math

print(math)

radians = 0.7
height = math.sin(radians)

print(height)
print(math.pi)

print(math.sqrt(2))


# composition of functions
print("composition of functions")
degrees = 45
x = math.sin(45/360.0 * 2 * math.pi)
print(x)

y = math.exp(math.log10(x))
print(y)


# adding new functions
def print_lyrics():  # header of the function
    print("verse 1")  # the body
    print("verse 2")  # the body


print_lyrics() # <class 'NoneType'>  aka this function does not return a value

print(type(print_lyrics()))

# but what is a function? does it have a type?
print(type(print_lyrics)) # <class 'function'>


# use a function inside of another function

def sin_crap(x):
    return math.sin(x);


print(sin_crap(90))


def some_f():
    y = some_g(3) # 3 is here the argument
    return y + 2


def some_g(x): # parameter
    return x + 7


# even some_g() is defined later in the file,
# the interpreter knows to pick it up
print(some_f())


def some_h(i):
    kk = some_g(i)
    return kk ** 2


# the argument is first evaluated before is sent to some_h
some_h(math.sin(some_f()))


# scope
# kk is not visible outside of the some_h(i) in the body where it was defined
# print(kk)

# same for the parameters in header
# print(i)

