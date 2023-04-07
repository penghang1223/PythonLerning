# coding:utf-8

info = 'this is a string example!!'

result = info.startswith('this')
print(result)

result = info.startswith('this is a string example!!')  # 判断开头字符
print(result)

print(bool(info == 'this is a string example!!'))

result = info.endswith('this is a string example!!')  # 判断结尾字符
print('result:', result)
