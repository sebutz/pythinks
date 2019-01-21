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

t1 = ('a',)
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

# tuple assignment
a = 6;
b = 4
print(a, b)

# swapping 2 values
temp = a
a = b
b = temp
print(a, b)

# this is using a third variable
c = 5;
d = 7

c, d = d, c  # tuple of variables gets a tuple of expressions (c, d) = (d, c)

print(c, d)

# number have to be the same
#  c, d = 1, 2, 3  # ValueError: too many values to unpack

# moreover : the right side can be any kind of sequence (string , list or tuple)

addr = 'monty@python.org'
uname, domain = addr.split('@')  # list of 2 elements

# tuples as return values
# return multiple values at once

# built-in divmod

t = divmod(7, 3)  # returns a tuple
print(t)

quot, rem = divmod(7, 3)
print(quot);
print(rem)


# t must be a sequence
def mmin_max(t):
    return min(t), max(t)


print(mmin_max(t))


# variable length argument tuples


def printAll(*args):
    print(args)



printAll(1, 2.0, "abc")

# a parameter with * GATHERS arguments into a tuple


# the complement of gather is SCATTER
# if you have a sequence of values and you want to pass it to a function
# as multiple arguments, you can use the * operator


t = (7, 3)
# divmod(t)  # TypeError: divmod expected 2 arguments, got 1

# you need to scatter
print(divmod(*t)) # (2, 1)



# list and tuples

# zip is built-in function that "zips" sequence in a tuple of sequences

s  = 'abc'
t = [0, 1, 2]
z = zip(s, t)  # <zip object at 0x1032a4308>  aka list of tuples
# [('a', 0), ('b', 1), ('c', 2)]

print(z)

# zip with not with the same length sequences

# the result has the smallest length from the seq

zip('Anne', 'Elk')
# [('A', 'E'), ('n', 'l'), ('n', 'k')]  # list of tuples


# use tuple assignement for for loop

t = [('a', 0), ('b', 1), ('c', 2)]
for letter, number in t:
    print(number, letter)



# same element in 2 sequences
def has_match(t1, t2):
    for x, y in zip(t1, t2):
        if x == y:
            return True
    return False



# traverse the elements of a sequence and their indices
print(enumerate('abcd'))  # ([0. 'a'], [1, 'b'], [2. 'c'], [3, 'd'])

en = enumerate("abcd")
# print(en[0])  TypeError: 'enumerate' object is not subscriptable

for index, element in enumerate('abcd'):
    print(index, element)




# dictionaries and tuples

d = {'a':0, 'b':1, 'c':2}

print(d.items())
print(type(d.items()))   # list of tuples
'''
dict_items([('b', 1), ('c', 2), ('a', 0)])
<class 'dict_items'>
'''


# use a list of tuples to initialize a dictionary

t = [('a', 0), ('c', 2), ('b', 1)]
d = dict(t)

print(d)  # {'c': 2, 'a': 0, 'b': 1}


# combining zip with dict

d = dict(zip('abx', range(3)))
print(d)


# traversing a dictionary by items (using tuple assignment)

for key, value in d.items():
    print(key, value)

# is common to use tuples as keys in dictionaries (you can't use lists)


# comparing tuples



print((0, 1, 2) < (1, 2, 3))  # True


# DSU
# decorate, sort, undecorate

def sort_by_length(words):
    t = []
    for word in words:
        t.append((len(word), word))

    t.sort(reverse=True)  # sort in descending order

    res = []
    for length, word in t:
         res.append(word)

    return res

print(sort_by_length(["abdcd", 'rfrfrf', 'freigmremg']))


# sequence of sequences











