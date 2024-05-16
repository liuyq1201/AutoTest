"""
字典推导式
"""

d = {
    'a': 1,
    'b': 8,
    'd': 3,
    'd': 16,
    'e': 4,
}
r = {key: value for key, value in d.items() if value > 5}
print(r)
print(dict((key, value) for key, value in d.items() if value > 5))
