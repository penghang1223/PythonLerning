# coding:utf-8

books = []
print(id(books))
books.append('python入门课程')
print(books)
print(id(books))  # 查看内存中的地址

number = 1.1
tuple_test = (1,)
dict_test = {'name': 'dewei'}

books.append(number)
books.append('django')
books.append(1)

print(books)
print(id(books))
