'''
从可迭代的对象中分解元素
'''
from collections import deque
a = ('acme', 11, 22, (1, 2, 3))

name, *_, (*_, num) = a
print(name)
print(num)



