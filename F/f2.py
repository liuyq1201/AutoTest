"""

两个字典寻找相同的

"""
x = {
    "a": 1,
    "b": 2,
    "c": 4,

}
x1 = {
    "a": 1,
    "b": 3,
    "d": 4,
}

print(x.keys() & x1.keys())
print(x.keys() - x1.keys())
print(x.items() & x1.items())
print(x.keys() - {'c', 'd'})

'''
&符号在Python中既可以执行通常的按位与运算，也可以执行set集合里面的交集运算
|：并集；也可以表示数字运算中的按位或运算
-：差集
^：对称差集
'''



