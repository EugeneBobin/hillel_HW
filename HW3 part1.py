#a)
a = 3
b = 4
c = a
a = b
b = c
print(a, b)

#b)
a = 3
b = 4
a, b = b, a
print(a, b)

#c)
a = 3
b = 4
a = a + b
b = a - b
a = a - b
print(a, b)
