# coding:utf-8

int_data = 12  # 整形
float_data = 3.14  # 浮点型

str_int_data = str(int_data)  # 转成字符串
str_float_data = str(float_data)  # 转成字符串
print(str_int_data, str_float_data, type(str_int_data), type(str_float_data))
print("-----------------")

zero_number = 0
_number = -1

str_zero_number = str(zero_number)  # 转成字符串
str_number = str(_number)  # 转成字符串
print(str_zero_number, str_number, type(str_zero_number), type(str_number))

# 字符串转数字

str_float = '3.14'  # 字符串
str_int = 123456

real_float = float(str_float)  # 字符串转成浮点
real_int = int(str_int)  # 字符串转成int

print(real_float, real_int, type(real_float), type(real_int))

mix_str = '123'
mix_str1 = '123a'  # 必须是纯数字
print(float(mix_str))
print(float(mix_str1))  # 报错
print("-----------------")

float_data_str = '3.14'
test_int = int(float_data_str)  # 不符合int类型数据
print(test_int)  # 会报错
test_data = float(float_data_str)
print(test_data, type(test_data))
print("-----------------")

int_data_str = '123'
test_data = float(int_data_str)
print(test_data, type(test_data))
