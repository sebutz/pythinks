# chapter1

# first program
print("Think tank")

# arithmetic ops
adding = 12 + 13; print(adding)
mult = 12 * 2; print(mult)
power = 12 ** 3  # 12 * 12 * 12
print(power)

substr = 11 - 123;print(substr)

# what if
print(12 - - 2) # interpreted as +
print(12 ++ 2) # ignoring one +


divide = 123 / 23 ; print(divide)
divisor = 123 // 23 ; print(divisor)  # floor division operator
remains = 123 % 23 ; print(remains) # 123 = 23 * 5 + 8   # modulus operator


# tools
# find out the type (in Python everything is a type)
print(type(123))
print(type("Hello world"))

# weird stuff: don't assume
bigInt = 1, 000, 000 # Python is interpreting (1, 0, 0)
print(type(bigInt)) # <class 'tuple'>
print(bigInt)  # (1, 0, 0)

