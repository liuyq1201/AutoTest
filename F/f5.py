"""
列表中出现元素的最多次数

"""
from collections import Counter

x = [1, 2, 3, 45, 1, 2, 3, 451, 2, 3, 451, 2, 3, 451, 2, 3, 451, 2, 3, 451, 2, 3, 451, 2, 2, 45]
c = Counter(x)
print(c.most_common(2))
