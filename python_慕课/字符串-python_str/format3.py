# coding:utf-8

info_n = ('my name \nis %s\n' % 'dewei')  # 换行
print(info_n)

info_t = 'my name \tis dewei'  # 横向制表
print(info_t)

info_v = 'my name \vis dewei'  # 纵向制表
print(info_v)

info_a = 'my name \ais dewei'  # 响铃
print(info_a)

info_b = 'my name is dewei\b'  # 删除前一个字符
print(info_b)

info_r = 'my name is dewei\r'  # 删除前面一行
print(1, info_r, info_b)

info_f = 'my name is dewei\f'  # 翻页
print('f', info_f)

print('my name is \'dewei\'')  # 需要转义的字符前加反斜杠
print("my name is \"Dewei\"")

print('my name is \\ dewei')

print(r'my name is \\ dewei\n')  # 将当前的转义字符无效化
