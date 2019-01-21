# dictionaries

# in list indices have integers, in dictionaries they can be almost any type
# mapping  a set of indices(keys) and a set of values
# key-value pair (item)

# empty dictionary
d = dict()
print(d)

eng2sp = {'one': 'uno', 'two': 'dos', 'three': 'tres'}
print(eng2sp['one'])

# adding to dictionary
eng2sp['four'] = "quatro"
print(eng2sp)

# the order of the items is not the same (is not guaranteed)

# what if the key is not in dictionary
# print(eng2sp['five'])
# KeyError: 'five'

# you can have all the info
print(eng2sp.keys())
print(eng2sp.values())
print(eng2sp.items())
'''
dict_keys(['one', 'two', 'four', 'three'])
dict_values(['uno', 'dos', 'quatro', 'tres'])
dict_items([('one', 'uno'), ('two', 'dos'), ('four', 'quatro'), ('three', 'tres')])
'''

# testing the appartenance of a key
print("uno" in eng2sp)  # False, because "uno" is not a key
print("one" in eng2sp)  # True, "one" is key, equivalent with searching in keys (this is used in looping !!!)
print("one" in eng2sp.keys())  # True

# we can search also in values

print("uno" in eng2sp.values())  # True


# dictionary as a set of counters
def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d


h = histogram("brontosaurus")
print(h)
'''
{'r': 2, 's': 2, 'b': 1, 't': 1, 'o': 2, 'a': 1, 'n': 1, 'u': 2}
'''

# get with default value
# if the key appears in dictionary, return the corresponding value, otherwise return the default value
# something like a get-or-else, but without saving in the dictionary that default value

h = histogram('a')
print(h)

print(h.get("a", "kkk"))
print(h.get('b', 'kkk'))

print(h)


# loops

def print_hist(h):
    for c in h:
        print(c, h[c])


h = histogram('parrot')
print_hist(h)

'''
r 2
t 1
a 1
o 1
p 1
'''


# reverse look up, there is no simple syntax
def reverse_lookup(di, v):
    for k in di:
        if di[k] == v:
            return k

    raise ValueError  # raise statement causes an exception


h = histogram('parrot')
print(h)
k = reverse_lookup(h, 2)
print(k)


# k = reverse_lookup(h, 3)
# print(k)  # ValueError

# lists can appear as values in a dictionary
# inverting a dictionary


def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]  # the list from the key
        else:
            inverse[val].append(key)  # adding to that key
    return inverse


hist = histogram('parrot')
print(hist)
inverse = invert_dict(hist)
print(inverse)
'''
{'p': 1, 'a': 1, 'o': 1, 'r': 2, 't': 1}
{1: ['p', 'a', 'o', 't'], 2: ['r']}
'''

# dictionary is implemented using a hashtable and that means the keys have to be hashable
# hash: a function that takes a value of any kind and returns an integer
# dictionaries use these integers, called hash values to store and look up key-value pairs

# system works fine if the keys are immutable
# mutable types (like lists) aren't  hashable --> the simplest way to get this limitation is to use tuples


# memoized version of fibonacci

known = {0: 0, 1: 1}


def fibonacci(n):
    if n in known:
        return known[n]

    res = fibonacci(n - 1) + fibonacci(n - 2)
    known[n] = res
    return res


# global variables
# known is created outside the function, so it belongs to the special
# frame called __main__

# variables from __main__ are sometimes called global because they can be
# accessed from any function.
# local variables dissapear when their function ends, global variables persist
# from one function call to the next

# it's common use global variables will be flags(boolean variables that indicate, "flag"
# whether a condition is true)


verbose = True


def example1():
    if verbose:
        print("Running example1")


# example of shadowing (and bad programming)
been_called = False


def example2():
    been_called = True  # here been_called it's a local variable which is shadowing the global one


example2()
print(been_called)  # still False


# ok, but how can we reassign global variable inside the function

def example3():
    global been_called  # don't create a local variable, I will use the global one
    been_called = True


example3()
print(been_called)  # True

count = 0


def example4():
    global count
    count = count + 1  # wrong


known = {0: 0, 1: 1}


def example5():
    global known
    known = dict()


# long integers

n = fibonacci(50)
print(n)  # in Python3 all the longs are gone, there are only ints



