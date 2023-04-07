# coding:utf-8

info = 'python是一个非常有魅力的语言'

result = '魅力' in info
print(result)

result = '语言' not in info
print(result)

info2 = 'python is a good code'

print(max(info2))
print('.', min(info2), '.')  # 空格是最小的字符串

info3 = '天气好 要多锻炼身体。'
info4 = '多锻炼身体 身体换变得更好'

new_str = info3 + info4 + '!'  # 加号字符串拼接
print(new_str)
print(len(new_str))
length = len(new_str)
print(type(length))
