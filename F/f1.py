"""
字典计算排序问题

zip 创建 迭代器
"""
from operator import attrgetter
from operator import itemgetter

x = {
    "a": 2,
    "b": 3,
    "c": 4,
    "d": 16,
    "e": 122,
    "f": 19,
}
r = zip(x.values(), x.keys())
print(zip(*r))
# print(min(r))
# r1 = sorted(r, reverse=True)
# print(r1[0][1])

x1 = [1, 2, 3, 4]
x2 = [1, 2, 3, 4]

print(list(zip(x1, x2)))
print(list(zip(*zip(x1, x2))))

x3 = [{"a": "k", "id": 3, "b": "a"}, {"a": "ttt", "id": 4, "b": "b111"}, {"a": "s", "id": 1, "b": "ao"}, {"a": "b", "id": 2, "b": "b11"}]
print(sorted(x3, key=itemgetter('id')))
print(sorted(x3, key=lambda r: (r['id'])))
# print(sorted(x3, key=attrgetter('a')))

x4 = [1, 2, 3, 4, '2', 4, 'a']
def val(y):
    try:
        int(y)
        return True
    except ValueError:
        return False

r=list(filter(val,x4))
print(r)
