# sets
'''
set-like operations, including addition, subtraction, union and intersection
'''

# behaves like a a collection of dictionary keys with no values


s = {2, 3, 3}
print(s)  # {2, 3}

# set substraction is available as a method called difference
def subtract(d1, d2):
    return set(d1) - set(d2)


d1 = {1, 4, 7, 8}
d2 = {2, 5, 7, 9}

print(subtract(d1, d2))  # {8, 1, 4}

'''
Stupid logic and function 
when an element appears for the first time is added to the dictionary
If the same element appears again, the function returns True
'''
def has_duplicates(t):
    d = {}
    for x in t:
        if x in d:
            return True
        d[x] = True
    return False


# rewriting it with sets

def has_duplicates(t):
    return len(set(t)) < len(t)  # that's cooler


d = {23, 434, 545, 33}  # {33, 434, 23, 545}
print(d)

# print(d[1]) # TypeError: 'set' object does not support indexing

print(d.pop())  # 33
print(d) # {434, 23, 545}

d.add(23)
print(d)

d.add("23")
print(d) # {434, 23, '23', 545}

print(d.pop())  # 434
print(d) # {23, '23', 545}

