# coding:utf-8

a = [1, 2, 3]
b = (1, 2, 3)
c = {1, 2, 3}

print(tuple(a), set(c))  # 把列表转成元组 集合

print(type(tuple(a)), type(set(c)))

print(tuple(a) == b)  # true
print(set(a) == c)  # true

print(id(set(a)))
print(id(b))
print(id(tuple(a)))
print("-------------")
print(tuple(a) is b)  #
print(set(a) is c)  #
print(id(a))
print(id(c))

print(list(b), set(b))  # 元组转列表集合
print(list(c), tuple(c))  # 集合转列表元组

print(list(a))

print(str(a), type(str(a)))  # '[1, 2, 3]'
print(str(b), type(str(b)))  # 不可逆
print(str(c), type(str(c)))  # 不可逆

print(list(str(a)))  # 不可逆
print(tuple(str(b)))  # 不可逆
print(set(str(c)))  # 不可逆   函数内部包裹函数  优先执行内部函数

_a = str(a)
_b = list(_a)
print(_b)
