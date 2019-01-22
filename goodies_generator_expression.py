# generator expression
'''
similar to list comprehension
with parantheses instead of square brackets
'''


g = (x**2 for x in range(5))   # <generator object <genexpr> at 0x10328e780>
print(g)  # <generator object <genexpr> at 0x10328e780>


# know to iterate through a sequence of values
# unlike list comprehension it does not compute the values all at once
# it waits to be asked

print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
# print(next(g))  # StopIteration  exception i.e. you reach to the end of sequence, there is no next

# reload
g = (x**2 for x in range(5))
for val in g:
    print(val)


# the generator object keeps track of there it is in sequence
# once the generator is exhausted, it continues to raise StopIteration



# where generators are used?
# in function like sum,max, min
print(sum(x**2 for x in range(5)))