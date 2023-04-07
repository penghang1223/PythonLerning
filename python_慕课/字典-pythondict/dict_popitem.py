# # coding:utf-8
#
students = {'dewei': '到', 'xiaomu': '在', 'xiaoyun': '在呢', 'xiaogao': '在'}
print('xiaogao 在吗')
xiaogao = students.popitem()  # 弹出的最后一个字典值 以元组存储
print('{} 喊 {}'.format(xiaogao[0], xiaogao[1]))
print(type(xiaogao))
print('xiaoyun 在吗')
print("----------------------")

xiaoyun = students.popitem()
print('{} 喊 {}'.format(xiaoyun[0], xiaoyun[1]))

print('xiaomu 在吗')
print("----------------------")

xiaomu = students.popitem()
print('{} 喊 {}'.format(xiaomu[0], xiaomu[1]))
print('dewei在吗')
print("----------------------")

dewei = students.popitem()
print('{} 喊 {}'.format(dewei[0], dewei[1]))
print(students)
students.popitem()
#
# tuple_01 = ("aaa", "bbb", "ccc", "ddd", "eee", "fff", "ggg", "hhh", "iii")
# print(tuple_01[1])  # 元组支持索引
