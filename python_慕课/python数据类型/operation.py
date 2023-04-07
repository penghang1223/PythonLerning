# coding:utf-8

a = 1
b = 2
c = 3

d = a + b + c
d += c
print(d)  # 9

d -= a
print(d)  # 8

d *= b  # d = d * b
print(d)  # 16

# a /= b
# print(a)

a //= b
print(a)

c %= 3
print(c)

f = 10
f **= 2
print(f)

list_01 = [1, 2, 3]
print(list_01 * 2)
tuple_01 = (1, 2, 3)
print(tuple_01 * 2)  # 列表只可以和数字做乘法
print(tuple_01)  # 元组也可以乘

dict_01 = {'name': 'dewei'}  # 字典不支持*乘法

gb = 1
b = gb * 1024 * 1024 * 1024
print(b)
