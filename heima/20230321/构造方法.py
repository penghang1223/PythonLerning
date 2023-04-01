class Student():
    #定义类 首字母大写
    name = None
    age = None
    phone = None
    #类属性  自动  传给 init


    # 定义方法
    def __init__(self, name, age, phone):
        #self 调用方法内的变量
         self.name = name
         self.age = age
         self.phone = phone
         print(f"Student创建了一个队象")
stu = Student("小明",12,"312312")
print(stu.name)
print(stu.age)
print(stu.phone)