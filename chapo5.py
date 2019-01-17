# conditionals and recursion

x = 3
print(x == x)

print(type(3 == 3))  # class 'bool'


# logical operators
print(42 and True)  # True

print(not 42 and True)  # False
print(not 42)  # False
print(not False) # True
print(not 42 or 42)  # 42 !!!!!
print(not 42 or not not 42) #  True

# conditional execution

if x > 0:
    pass


if x % 2 == 0:
    print("x is even")  # can be divided to 2 exactly
else:
    print("x is odd")


# chained conditionals

x = 5
y = 4

if x<y:
    print("x is less than y")
elif x > y:
    print("y is less than x")
else:
    print("x is equal with y")


# nested conditionals

if x == y:
    print("x and y are equal")
else:
    if x < y:
        print("x is less than y")
    else:
        print("x is greated than y")


# recursion
# it's legal for a function to call itself

def countdown(n):
    if n <=0:
        print("Blastoff")
    else:
        print("n is now", n)
        countdown(n-1)


countdown(3)


def print_n(s, n):
    print("n is ", n)
    if n <= 0:
        print("exit now")
        return
    print("s is", s)
    print_n(s, n -1)


print_n("aaa", 8)

'''
True
<class 'bool'>
True
False
False
True
42
True
x is odd
y is less than x
x is greated than y
n is now 3
n is now 2
n is now 1
Blastoff
n is  8
s is aaa
n is  7
s is aaa
n is  6
s is aaa
n is  5
s is aaa
n is  4
s is aaa
n is  3
s is aaa
n is  2
s is aaa
n is  1
s is aaa
n is  0
exit now

Process finished with exit code 0

'''

# keyboard input

text = input("Tell me your name, please: ")
print("Hello ", text)

