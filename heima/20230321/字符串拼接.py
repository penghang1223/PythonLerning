# 加号字符串拼接


name = '交换机暗示健康'

student = "小明"
print(name,student)
# 逗号会转义成空格


print(name+student)
# 加号字符串拼接


# print(f"name +studen" ,name,student)



# %s 占位符

name = 'fd'
print("hfhfias dioahj fdhasujfhka: %s" % name)

class_num = 478
phone_num = 1312312
avg_salary = "100w"

message = "%s班级的手机号是%s,平均工资%s" %(class_num,phone_num,avg_salary)
print(message.strip())


# %s
# 将内容转换为字符串 放入占位位置
# %d
# 将你内容转换成整数
#
# %f
# 将内容转换为浮点型
flo_002 = 32.13213
int_002= 21
str_002 = "dasdsad"
message = "浮点数%f,整数是%d,字符串是%s" % (flo_002,int_002,str_002)
print(message)



# 数字精度控制


num = 11
num2 = 11.111
print("宽度为5:%5d" % num)
#打印出來的數字前有三個空格

print("宽度为1:%1d" % num)
# 打印出来的数字前没有空格
# %5d  表示小数点前保留5位
print("宽度为7 小数精度为:%7.4f" % num2)
# 小数点后保留四位
print("不限制宽度 小数精度为:%.6f" % num2)



a = "d达大厦"
b = 12
c = 12.1111

message = f"我是a{a},我是b{b},我是c{c}"
print(message)

# 可以格式化表达式  具有明确结果  充当变量

print("1*1: %d" % 1*1)
print(f"1*3:{1*3}")
