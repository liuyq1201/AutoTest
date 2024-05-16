"""
列表去重
"""

x = [1, 2, 3, 32, 2, 3, 3, 4, 6, 5]
x1 = []
x2 = []
d = {}
"""循环 """
for a in x:
    if a not in x1:
        x1.append(a)
print(x1)

[x2.append(i) for i in x if i not in x2]
print(x2)

print(set(x))

print(sorted(list(set(x)), key=x.index))
print(x.index)

x3 = [{"x": 1, "y": 2}, {"x": 1, "y": 3}, {"x": 1, "y": 2}, {"x": 2, "y": 4}]


def t(items, key=None):
    s1 = set()
    for item in items:
        va = item if key is None else key(item)
        if va not in s1:
            yield item
            s1.add(va)


print(list(t(x3, key=lambda d: (d['x'], d['y']))))
# print(list(t(x3, key=lambda d: (d['x']))))

"""









li = [1,2,3]
print(li.index)
#print(li.index)，输出的那一串为函数名（函数在内存中的地址）
#若b也是一个列表，b.sort(key=a.index)， 
#其中key为形参，接收类型必须为函数。
#即列表b中的每个元素都要经过a.index函数做映射（y=f（x）），
#按映射值大小进行排序
#通俗来说进行b.sort(key=a.index)后b会按a列表的顺序排列。
 
输出结果：
<built-in method index of list object at 0x0000026A26484B00>"""
