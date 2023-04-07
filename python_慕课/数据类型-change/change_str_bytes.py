# coding:utf-8

a = 'hello xiaomu'
print(a, type(a))

b = b'hello xiaomu'  # 将字符串以b包裹
print(b, type(b))

print(b.capitalize())  # 字符串首字母大写
print(b.replace(b'xiaomu', b'dewei'))  # 把xiaomu替换dewei
print(b[:3])
print(b.find(b'x'))

print(dir(b))  # 支持的内置函数

c = 'hello 小慕'  # 比特只支持ascii码  含有中文不能加b  进行比特转换
d = c.encode('utf-8')  # 比特转字符串
print(d, type(d))
print(d.decode('utf-8'))  # 字符串转比特
