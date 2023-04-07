# # coding:utf-8
#
# a = 'abc'
# print(a.split())  # 去除空格变成列表
#
# b = 'a,b,cd'
# print(b.split(','))
#
# c = 'a|b|c|d'
# print(c.split('|', 1))  # 只切割一次
#
# d = 'a|b|c|d'
# print(d.split('|', 2))  # 只切割两次
#
# # f = ''
# # print(f.split(''))  split('')不能传空
#
# test = ['a', 'b', 'c']
# test_str = '|'.join(test)  # join前面需要插入的分割对象
# print(test_str)
#
# test2 = ['c', 'a', 'b']
# print('|'.join(test2))
#
# test3 = [1, 2, 3]
# print('|'.join(test3))  # 数字类型不能插入    有一个数都不行  字典 元组都不允许插入
# 只有字符串类型的列表可以使用join


# sort_str = 'a b d f i p q c'
# sort_list = sort_str.split(' ')  # 看第十六行
# print(sort_list)
# sort_list.sort()
# print(sort_list)
# sort_str = ' '.join(sort_list)
# print(sort_str)
#


sort_str_new = 'abdfipqc'
print(sort_str_new)

res = sorted(sort_str_new)  # 内置函数 sorted
print(res)
print(''.join(res))
