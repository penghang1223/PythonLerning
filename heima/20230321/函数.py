# 定义函数  形参
# 调用函数 实参
# """ """

#
# def check(a, b, c):
#     print(f"体温:{a},身高{b},体重{c}")
#     if a > 31:
#         print(f"你快挂了,体温{a}")
#     else:
#         print(f"你快挂了,体温{a}")
#
#
# check(11, 122, 34)
#
# # return 将结果返回调用者
# a = check(11, 22, 33)
# print(a)
#
#
# def add(z, x):
#     result = z + x
#     return result
#
#
# # 将result的值返回给r
#
# # 函数返回值通过变量接收
# r = add(1, 2)
# print(r)
#
# # 多行注释
#
# """
# """
# # 全局变量 先声明再赋值
#

#
# # 关键字参数
# def user_info(name, age, phone):
#     print(f"名字{name},年龄{age},手机号{phone}")
#
#
# # 位置参数
# user_info("小明", 18, 1221212)
#
# # 关键字参数  不按顺序
# user_info(name="John", age=18, phone="321123")
# user_info(phone="321123", name="John", age=18)
# # 位置关键字混用  位置参数要在前面
# user_info("John", age=18, phone="321123")
#
#
# # 缺省参数
# # 传递参数设置默认值
# # 默认参数必须写在最后 age
# def user_info(name, phone, age="18"):
#     print(f"名字{name},年龄{age},手机号{phone}")
#
#
# user_info("消防", 12, )
#
#
# # 不定长参数
# # 可变参数
#
#
# # 参数不限
# # 位置不定长
# def user_info(*args):
#     # 所有参数被args收集  然后合并为一个元组
#     print(args)
#
#
# user_info("tom", 12, 13, 13, "哈哈")
# user_info("dsad")
#
#
# # 关键字不定长
# # 所有的键值会被args接收  已字典形式存储  传参要按照字典格式传
# def user_info(**args):
#     print(args)
#
#
# user_info(name="ton", age="12")


# 函数接收函数默认运行程序为 pytest
# 所有以test开头的字符串 函数都会被解释为测试用例


def est_func(computer):
    result = computer(1, 2)
    print(result)


def computer(x, y):
    return x + y


est_func(computer)


# 匿名函数

# lambda 只使用一次

def ttest_func(computer):
    result = (1, 2)
    print(result)


ttest_func(lambda x, y: x + y)
# 使用格式    lambda  传入参数 : 函数体