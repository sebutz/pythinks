# strings

someString = "abcdef"

letter1 = someString[0]
print(letter1)
print(len(someString))

ll = someString[-1]; print(ll)  # -1 or len() - 1
ll = someString[len(someString) -1];print(ll)

ll = someString[-2]; print(ll)

# traversal with for loop
for letter in someString:
    print(letter)


for letter in someString:
    print("[" + letter+ "]")


# string slices : segment of a string
s = "Monty Python"
print(s[0:5])  # it will be in fact [0, 5)
print(s[6:])
print(s[6: len(s)])  # [6, len(s)]

# the same from the beginning

print(s[:3])  # [0,3) or [0, 2]

print(s[0:0])  # empty string : [0, 0) -->cannot be --> empty string
print(s[1:1])  # still empty
print(s[1:2])  # must be o from Monty

print(s[:]) # full string

# string are immutable!!!

greeting = "Hello world"
# greeting[0] = "J"
'''
    greeting[0] = "J"
TypeError: 'str' object does not support item assignment
'''
print(greeting)
print(id(greeting))

# item is the character , object is the string itself

# ok, but we play around with + and strings
# in fact, we create a new string, that's why

greeting = greeting + " !"
print(greeting)
print(id(greeting))

'''
Hello world
4347983920
Hello world !
4347984048
'''

# searching: pattern of computation


def find_first(word, letter):
    '''
    find a character in a string
    :param word:
    :param letter:
    :return: the index if found or -1 if not
    '''
    index = 0
    while index < len(word):
        if word[index] == letter:
            return index
        else:
            index += 1
    return  -1


print(find_first("alabama", 'a'))
print(find_first("alabama", 'b'))


# pattern of computation : counter
word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count += 1

print(count)


# string methods
print(word.upper())

# by default find is starts with the be2ginning of the string
index = word.find('a')
print("index", index)
print(word.find('an'))


# example also of a optional argument: there is a stop index
print(word.find('an', 3))
print(word.find("a", 3, len(word)))

# the in operator : boolean operator,
# takes two strings and return True if the first string is a substring of a second


print("a" in word)
print("seed" in word)


def in_both(word1, word2):
    for letter in word1:
        if letter in word2:
            print(letter)


print(in_both('bananas', 'oranges'))

# string comparison
if word =='banana':
    print("You're a monkey")














