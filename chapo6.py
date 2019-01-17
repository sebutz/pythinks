# fruitful functions

import math

radius = 1.2
radians = 3.4

e = math.exp(1.8)
height = radius * math.sin(radians)

def area(radius):
    a = math.pi * radius ** 2
    return a

# what if we miss return

def area2(radius):
    a = math.pi * radius ** 2


print(area(30))
print(area2(30))  # None

a = 0;b = 0
b = a = 3   # a gets 3 and then b gets a , that is 3
print("a= ", a); print("b = ", b)


# incremental development
import math

x1 = 10; x2 = 13
y1 = 10; y2 = 14
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(distance)


def distancer(x1, x2, y1, y2):
    return 0.0


d = distancer(x1, x2, y1, y2)
print("d = ", d )

# can we redefine a function again? looks like yes
def distancer(x1, x2, y1, y2):
     dx = x2 - x1
     dy = y2 - y1
     dsquared = dx**2 + dy**2
     print("dsquared: ", dsquared)
     return 1.0

dd = distancer(x1, x2, y1, y2)
print("dd= ", dd)


def distancer(x1, x2, y1, y2):
    dx = x2 - x1
    dy = y2 - y1
    dsquared = dx ** 2 + dy ** 2
    print("dsquared: ", dsquared)
    return math.sqrt(dsquared)


ddd = distancer(x1, x2, y1, y2)
print("ddd= ", ddd)



'''
2827.4333882308138
None
a=  3
b =  3
5.0
d =  0.0
dsquared:  25
dd=  1.0
dsquared:  25
ddd=  5.0
'''



# more recursion


def factorial(n):
    if n == 0:
        return 1

print(factorial(3))


def factorial(n):
    if n == 0:
        return 1
    else:
        recurse = factorial(n -1)
        result = n * recurse
        return result

# what happens if n = 1.5

# factorial(1.5) RuntimeError: Maximum recursion depth exceeded
# solution: verify  the type using the built-in function
# isinstance
def factorial(n):
    if not isinstance(n, int):
        print("Factorial is defined only for the integers")
        return None
    elif n < 0:
        print("Factorial is not defined for negative numbers")
        return  None
    elif n == 0:
        return 1
    else:
        recurse = factorial(n -1)
        result = n * recurse
        return result

factorial(1.5)
factorial(-300)


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) * fibonacci(n - 2)