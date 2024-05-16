# 转译
print('\n')  # 输出空行
print(r'\n')  # 输出 \n

# 多个变量赋值
a, b, c = 1, 2, "runoob"

# Python3 中有六个标准的数据类型：
# Dictionary（字典）
# Python3 的六个标准数据类型中：
# 不可变数据（3 个）：Number（数字）、String（字符串）、Tuple（元组）；
# 可变数据（3 个）：List（列表）、Dictionary（字典）、Set（集合）。

# Number（数字）
s = 1 + 1
print(type(s))
print(isinstance(s, list))
print(True == 0)

# String（字符串）
print("字符串" + str("1234")[1:3])

# List（列表）
list1 = ['abcd', 786, 2.23, 'runoob', 70.2]
print(list1[1:3])
print(list("11442"))

# Tuple（元组）
tuple1 = ('abcd', 786, 2.23, 'runoob', 70.2)
print(tuple1[1:4])
print(tuple("1122"))

# Set（集合）
print(set("1234324"))

print({x: x**2 for x in (2, 4, 6)})