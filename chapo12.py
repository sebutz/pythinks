# tuples

# tuples is a sequence of values
# the values can be any type, and they are indexed by integers,
# so, in that respect, tuples are like lists
# the difference is that the tuples are immutable

t = 'a', 'b', 'c'

print(t)  # ('a', 'b', 'c')

# although is not necessary, this is the common way to write tuples:
t = ('a', 'b', 'c')

print(t)


# tuple of 1
# this is not a tuple
t1 = ('a')
print(type(t1))  # <class 'str'>

t1 = ('a', )
print(type(t1))  # <class 'tuple'>

# empty tuple

t0 = tuple()
print(type(t0))  # <class 'tuple'>

# most list operators work also with tuples

t = ('a', 'b', 'c')
print(t[0])
print(t[1:3])

# ok, but how is immutable?

# t[0] = 'e'  # TypeError: 'tuple' object does not support item assignment
print(t)



