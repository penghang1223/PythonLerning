# coding:utf-8

info = '    my name is dewei    '
new_info = info.strip()  # 去掉指定字符  不填默认去掉空格
print('.' + new_info + '.')

info_01 = 'my name is dewei'
new_info_01 = info_01.strip(info_01)
print(new_info_01)
print(len(new_info_01))

new_str = 'abcde'
print(new_str.lstrip('a'))  # 只去开头
print(new_str.rstrip('e'))  # 只去尾

new_info_01 = "hello  hello helloh"
new_info_01 = new_info_01.strip("h")  # 去除指定字符串
print(new_info_01)
