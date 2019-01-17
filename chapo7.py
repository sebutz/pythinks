# iteration : run a block of code repeatedly

# reassignment : it's legal

x = 'aaa'
x = 2


# updating variables but depending on old value

x = x + 1
print(x)


# while

def countdown(n):
    while n > 0:
        print(n)
        n = n -1

    print("kBoom")


countdown(5)
countdown(0)

# break

while True:
    line = input(">>> ")
    if line.upper() == 'DONE':
        break # out of the loop
    print(line)

print('KBoom Boom!')

# Newton method for square root

a = 4
x = 3
y = (x + a / x ) /2
y
print("y =", y)


# repeating the process  to get a better estimation
x = y
y = (x + a/x) / 2
y
print("y = ", y)

# and so on
# when y = x, we stop. We don't know the iterations

while True:
    print(x)
    y = (x + a / x) / 2
    if y == x:
        break
    x = y

# it's dangerous to test float equality
# use built-in function abss to compute the absolute value(the magnitude)

epsilon = 0.0000001 # error allowed
while True:
    print(x)
    y = (x + a / x) / 2
    if abs(y -x) < epsilon:
        break
    x = y












