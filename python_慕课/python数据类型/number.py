# coding:utf-8

name = 'dewei'
age = 33
weight = 66.7

# 用于判断当前模块是否是主程序入口。
# 如果当前模块是主程序入口，则执行if语句块中的代码；
# 如果当前模块是被其他模块导入的，则不执行if语句块中的代码。
# if 下的代码被其他模块导入不会被执行
if __name__ == '__main__':
    print(name)
    print(age)
    print(weight)
    print(type(age))
    print(type(weight))
    print(type(3.14))
    print(type(50))

    # float(x)
    # 将x转换到一个浮点数
    #
    # complex(real[, imag]) 创建一个复数
    #
    # str(x)
    # 将对象x转换为字符串
    #
    # repr(x)
    # 将对象x转换为表达式字符串
    #
    # eval(str)
    # 用来计算在字符串中的有效Python表达式, 并返回一个对象
    #
    # tuple(s)
    # 将序列s转换为一个元组
    #
    # list(s)
    # 将序列s转换为一个列表
    #
    # chr(x)
    # 将一个整数转换为一个字符
    #
    # unichr(x)
    # 将一个整数转换为Unicode字符
    #
    # ord(x)
    # 将一个字符转换为它的整数值
    #
    # hex(x)
    # 将一个整数转换为一个十六进制字符串
    #
    # oct(x)
    # 将一个整数转换为一个八进制字符串
