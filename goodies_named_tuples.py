# named tuples
# a quicker way to define classes

class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __str__(self):
        return '(%g, %g)' % (self.x, self.y)


'''
more concise way
'''

from collections import  namedtuple

Point2 = namedtuple('Point2', ['x', 'y'])
p = Point2(1, 3)
print(p)
print(p.x, p.y)

# p = Point2() that will fail as there no parameters provided
p = Point()
print(p)