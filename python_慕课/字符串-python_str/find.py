# coding:utf-8

info = 'python is a good code'

result = info.find('a')
print(result)
result = info.find('ok')
print(result)

result = info.index('a')
print(result)

# find 找不到元素返回-1
# index找不到报错


try:
    result = info.index('ok')
    print(result)
except:
    print("没有这个元素")
