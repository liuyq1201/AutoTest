"""
切片

"""

x = "helloword"
x1 = [1, 2, 3, 4, 5, 6]
a = slice(1, 4)
a.start
print(x1[a])
print(a.start)
print(a.stop)
print(a.step)
s = "helloword"
print(a.indices(len(s)))
for i in range(*a.indices(len(s))):
    print(s[i])
print(*(1, 2, 3))
print((1, 2, 3))
