# 创建一个dog类
class Dog:
    def __init__(self, name, age):
        """
        初始化属性
        """
        self.name = name
        self.age = age

    def sit(self):
        print(f"蹲下{self.name}")

    def roll_over(self):
        print(f"打滚{self.name}")


my_dog = Dog("小七", 7)
# my_dog 是对象   为对象的属性赋值
your_dog = Dog("丽丽", 9)

print(f"名字{my_dog.name}")
print(f"年龄{my_dog.age}")
print(f"年龄{your_dog.name}")
print(f"年龄{your_dog.age}")
