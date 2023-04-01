'''练习题'''

# 1、输出最后一个字符的长度
# 定义一个变量存储输入的字符串
# input_str = input()
# # 再定一个变量接收输入的值
# word = input_str.strip().split(' ')
# print(len(word[-1]))
# input_str = input()
# word = input_str.strip().split(' ')
# print(len(word[-1]))


a = "my name is zhangkang"
b = "my\nname\nis\nzhangkang"
c = "my\tname\tis\tzhangkang"

a = a.split()
b = b.split()
c = c.split()

print(a)
print(b)

d = "my,name,is,zhangkang"
e = "my;name;is;zhangkang"
f = "my-name-is-zhangkang"

d = d.split(",")
e = e.split(";")
f = f.split("-")

print(d)
print(e)

a = "zhangkang"
b1 = a.split(",", 1)
b2 = a.split(",", 2)
b8 = a.split(",", 8)
b9 = a.split(",", 9)

print(b1)
print(b2)
print(b8)
