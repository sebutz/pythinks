# any and all

# built-in function
# takes a sequence of boolean values and return True if any of the values are True


print(any([False, True, False]))  # True

print(any([False, True, "kkk"]))  # True


# not very useful : we can use  "in"  operator

# word avoids forbidden if there are not any forbidden letters in word
def avoids(word, forbidden):
    return not any(letter in forbidden for letter in word)

# using any with generators is efficient (don't have to traverse to whole sequence)


# all


print(all([False, True, False]))
print(all([True, True, "kkk"]))  # True