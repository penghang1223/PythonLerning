# coding:utf-8

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(len(numbers) - 1)
# print(numbers[9])
# print(id(numbers))
# print('获取列表完整数据：', numbers[:])
# print('另一种获取完整列表的方法：', numbers[0:])
# print('第三种获取列表的方法：', numbers[0:-1])
# print('列表的反序:', numbers[::-1])
# print('列表的反项获取', numbers[-3:-1])
# print('步长获取切片:', numbers[0: 8: 2])
# print('切片生成空列表', numbers[0: 0])
# new_numbers = numbers[: 4]
# print(new_numbers)
# numbers.reverse()
# print('列表的反序', numbers)
#
# numbers[3] = 'code'
# print(numbers)
# numbers[2: 5] = ['a', 'b', 'c']  # 切片修改列表数据
# print(numbers)

item = numbers.pop(4)  # 不填数据默认 弹出最后一个数   填上索引 删除指定位置数据
print(item, numbers, len(numbers))

del numbers[4]  # 删除索引  索引不存在 报错
print(numbers)
try:
    tuple_test = (1, 2, 3)
    del tuple_test[1]  # 元组不可根据索引删除元素    可以删除元组
    print(tuple_test)  # 元组不可修改
except:
    print("Error")
