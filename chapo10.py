# lists

# Python HAS NO support for arrays --> use lists

# a list is a sequence (is ordered)

l = [40, 20, 30, 60]

print(l)

# list don't have to have the elements of the same type

ll = ["kko", 23.0, 22]
print(ll)

# nested lists? yes

lll = [l, ll, 12]
print(lll)

# list with no elements: empty list

empty_list = []
print(empty_list)


# lists are immutable: you can alter their content

cheeses = ['Burduf', 'Edam', 'Gouda']
print(cheeses)
print(type(cheeses))
print(id(cheeses))

print(cheeses[0])
cheeses[0] = "Cheddar"
print(cheeses[0])
print(cheeses)
print(type(cheeses))
print(id(cheeses))  # sane id

'''
['Burduf', 'Edam', 'Gouda']
<class 'list'>
4347983176
Burduf
Cheddar
['Cheddar', 'Edam', 'Gouda']
<class 'list'>
4347983176
'''

# the in operator works also on lists

print("Cheddar" in cheeses) # True
print("Burduf" in cheeses)   # False


# traversing a list

# the most common: for reading
for cheese in cheeses:
    print(cheese)


# what if you want to update some of the elements of the lists
# you need the indices

print("How many cheeeses: ", len(cheeses))

print(range(3))  # range(0, 3)
print(list(range(3)))  # [0, 1, 2]

# so it's safe to use range of len
for i in range(len(cheeses)):
    print(i)
    print(cheeses[i])
    if cheeses[i] == 'Edam':
        cheeses[i] = "Gourmet"

print(cheeses)


len([]) #0


for x in []:
    print("It will never get printed")

# nested lists count as a single element

llust =  ['spam', 1, ['Brie', 'Roquefort', 'Pol le Veq'], [1, 2, 3]]
len(llust) == 4 ### True


# list operations

# concatenate lists ?
a = [1, 2, 3]
b = [4, 5, 6]
print(a + b) # [1, 2, 3, 4, 5, 6]


b = [2, 5, 6]
print(a +b ) # [1, 2, 3, 2, 5, 6]  don't care if the elements are repeating



# list slices

t = ['a', 'b', 'c', 'd', 'e', 'f']
t[:]
t[0: 3] # same crap: [0, 3) or [0, 2]
print(t[0:3]) # ['a', 'b', 'c']

## slice operator can mutate many elements at once
t[1: 3] = ['x', 'y']   # [1, 2] or [1, 3)
print(t)  #




# list methods (void methods)


# add an element to a list

print("before append:", t)
t.append('w')
print("after append:", t)


# extend a list with other list
t1 = ['a', 'b', 'c']
t2 = ['d', 'e']

print("before extend:", t1)
print(t1.extend(t2))  # None
print("after extend:", t1)

#t2 remains the same


# sort arranges the elements from low to high
t = ['d', 'c', 'e', 'b', 'a']
print("before sort", t)
t.sort # that will do nothing
t.sort()
print("after sort", t)
print("void methods", t.sort()) # None


# map, filter and reduce

t = [1, 2, 3]

def sum_all(list):
    total = 0  # accumulator
    for x in list:
        total += x   # augmented assignement statement
    return  total


summy = sum_all(t)
print("sum = ", summy)

# We have already a built-in op for that

# sum is an operation of reduce type : all the elements of a list to a single value
print(sum(t))  # 6

# map operation
def capitalize_all(list):
    res = []
    for elem in list:
        res.append(elem.capitalize())
    return res


print(capitalize_all(['a', 'b']))


# filter: extract a sublist from a list

# deleting from a list

t = ['a', 'b', 'c']

## when you know the index and need the value you delete
print("before delete:", t)
x = t.pop(1)  # pop return the element that was removed for a possible reuse
print("after delete:", t)

## what if you don't provide an index -> it will delete the last element
t = ['a', 'b', 'c']
print("before delete:", t)
x = t.pop()
print("after delete:", t)


## when you know the index and don't need the value you delete: operator del
print("before delete:", t)
del t[1]  #  del will NOT return the element that was removed
print("after delete:", t)


## you know already the element you want to remove (but not the index)

t = ['a', 'b', 'c']
print("before delete:", t)
t.remove('b')
print("after delete:", t)


# what if this element is not distinct ? it removes only the first element
t = ['a', 'b', 'c', 'b']
print("before delete:", t)
t.remove('b')  # return None
print("after delete:", t)


# how to remove many elements ? using slice operator?

t = ['a', 'b', 'c', 'd', 'e', 'f']
print("before delete:", t)
del t[1: 3]
print("after delete:", t)



# lists and strings


## string to list
s = "spam"
lister = list(s)  # don't use 'list' as a variable name
print(lister)


s = 'pining for the fjords'
lister2 = s.split() # by whitespace
print(lister2)

s = "boom-crash-bye"
lister3 = s.split("-")
print(lister3)  # split by -


# list --> string : use join

t = ['pining', 'for', 'the', 'fjords']
delimiter = ' '
s = delimiter.join(t)  # weird syntax : looks like
# the same as

print("<-> ".join(t))  # pining<-> for<-> the<-> fjords


# objects and values
a = "banana"
b = "banana"

print(a == b) # True
print(id(a))
print(id(b))
print(id(a) == id(b))  # True

# 2xchecked if the 2 variables refer to the same object
# is operatpr
print(a is b) # True


# create 2 lists with the same content
a = [1, 2, 3]
b = [1, 2, 3]

print(a is b)  # False
print(a == b)  # True

# we are saying that lists are equivalent. because they have the same elements
# but not identical, because they are not the same object

print(id(a))
print(id(b))

print(id(a) == id(b)) # False


# how to nake aliases (references the same object)

a = [1, 2, 3]
b = a

print(a is b) # True



# reference is the association between variable and object


def delete_head(t):
    del t[0]



letters = ['a', 'b', 'c']

print("before delete head: ", letters)
delete_head(letters)
print("after delete head: ", letters)

# we pass the reference
# t amd letters are aliases to the same object : t is letters




# OPERATIONS THAT MODIFY LISTS AND OPERATIONS THAT CREATES NEW LISTS


#APPEND MODIFY BUT NOT CREATE
t1  =  [1, 2 ]
print("before appending ", t1)
id1 = id(t1)
t1.append(3) # None
print("after appending ", t1)
id2 = id(t1)

print("id1 vs id2 ", id1 == id2)  # True aka the same list



# +  creates new lists

t1  =  [1, 2 ]
print("before appending ", t1)
id1 = id(t1)


t2 = t1 + [3]  # new list
id2 = id(t2)
print("id1 vs id2 ", id1 == id2)  # False



# slice operatpr

t4 = [1, 2, 3]
id1 = id(t4)
t2 = t4[1:]   # different list
print(t2)
id2 = id(t2)
print("id1 vs id2 ", id1 == id2)  # False


# what about forcing

t1 = t[1:]
















