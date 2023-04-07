# coding:utf-8

name = 'dewei'
# 字符串没有reverse属性

new_name = name[::-1]
print(new_name)

# print(new_name)
# result = new_name.index('wei')  找不到会报错
# print(result)

# result = new_name.find('d')
# print(result)

result = new_name.find('de3')  # 找不到返回-1
print(result)
