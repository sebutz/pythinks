# counters like set, appears more than once
# behave like dictionaires
# they are multiset (mathematical idea of multiset)

from collections import Counter

count = Counter('parrot')
print(count)  # Counter({'r': 2, 't': 1, 'p': 1, 'o': 1, 'a': 1})

# unlike dictionaires, counters don't raise exception if the element to be accessed does not exist
# instead they return 0

print(count['d'])  # 0

'''
set-like operations, including ad- dition, subtraction, union and intersection
'''