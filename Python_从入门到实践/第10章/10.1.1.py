# 1
# 新建变量 单独接收  不建议使用
# with open("pi_digits.txt","r",encoding="UTF-8"):
#     file_test = open("pi_digits.txt")  # 繁琐
#     contents = file_test.read()
#     print(contents)
# # 2
#  起别名   最好使用这个
# with open("pi_digits.txt","r",encoding="UTF") as test_file:
#   contents = test_file.read()
#   print(contents)

# 3
# 需要单独关闭文件  麻烦
# f = open("pi_digits.txt","r",encoding="UTF")
# contents = f.read()
# print(contents)
# f.close()

# 4
#
# f = open("pi_digits.txt","r",encoding="UTF")
# contents = f.read()
# print(contents.strip()) # 删除字符串末尾空白


# 逐行读取
# 提前定义所需要读取文件的名字   将文件名称赋值给filename
# filename = 'pi_digits.txt'
#
# with open(filename) as file_obiection:
#     for line in file_obiection:
#         print(line)


# filename = 'pi_digits.txt'
#
# with open(filename) as file_obiection:
#     for line in file_obiection:
#         line = line.strip() # 将去除空格后的文件重新赋值给line
#         print(line)

filename = 'pi_digits.txt'

with open(filename) as file_obiection:
    lines = file_obiection.readlines()
for line in lines:
        line = line.strip() # 将去除空格后的文件重新赋值给line
        print(line)
print(type(line))