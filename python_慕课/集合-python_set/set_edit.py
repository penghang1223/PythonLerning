# coding:utf-8

a_list = ['python', 'django', 'django', 'flask']

a_set = set()  # 用set定义一个空集合

a_set.add(a_list[0])  # 根据索引将列表内的值添加进集合
a_set.add(a_list[1])
a_set.add(a_list[2])
a_set.add(a_list[-1])
print(a_set)
print("----------------")

a_set.add(True)
a_set.add(None)
print(a_set)  # 集合去重  原先有true不会再次生成

print("----------------")

a_tuple = ('a', 'b', 'c')
a_set.update(a_tuple)  # 把元组加到集合
print(a_set)
a_set.update('python')  # 把字符串加到集合
print(a_set)

a_set.remove('python')  # 删除指定元素
print(a_set)

# a_set.clear()  # 清除集合
# print(a_set)

# a_set.remove('flask')  # 移除不存在的元素 会报错
# print(a_set)

del a_set
print(a_set)
