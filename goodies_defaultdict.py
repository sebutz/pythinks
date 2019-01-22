# defaultdict

from collections import defaultdict

'''
like a dictionary except that if you access a key that does not exist, 
it can generate a new value on the fly
'''

'''

the argument is the class list 
not list(), which is a  new list
'''
d = defaultdict(list)
print(d)  # defaultdict(<class 'list'>, {})

t = d['new key']
print(d)  # defaultdict(<class 'list'>, {'new key': []})
print(t)  # []

# the new list t is added by default to the dictionary
# if we modify t , the change appears in d

t.append('new value')
print(d)  # defaultdict(<class 'list'>, {'new key': ['new value']})

# good for a dictionary of lists


