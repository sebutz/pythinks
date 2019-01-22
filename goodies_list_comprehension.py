# list comprehension

# harder to debug (you can't put a print statement inside the loop)

def capitalize_all(t):
    res = []
    for s in t:
        res.append(s.capitalize())
    return res


s = "adfdaf  Aafdaf  aFasfadf"
print(s)
print(capitalize_all(s))


# shorter
def capitalize_all2(t):
    return [s.capitalize() for s in t]  # list comprehension

print(capitalize_all2(s))


# some interpretation:
'''
[...]  we have [] i.e. constructing a new list, 
for s in t  i.e.  we are traversing a list 
'''



# use list comprehension for filtering

def only_upper(t):
    return [s for s in t  if s.isupper()]

s = "adfdaf  Aafdaf  aFasfadf"
print(only_upper(s))