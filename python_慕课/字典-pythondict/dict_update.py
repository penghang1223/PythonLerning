# coding:utf-8

user = {'username': 'dewei', 'age': 33}
xiaomu = {'username': '小慕', 'age': 10, 'top': 175, 'sex': '男'}
user.update(xiaomu)  # 把xiaomu内的元素更新到user  旧的被覆盖  新的添加进去
print(user)

value = user.setdefault('username', 'xiaoyun')  # 有username则输出 username 没有则按 xiaoyun 默认值输出
value = user.setdefault('birthday', '2020-1-1')
print(user, value)

# user['top'] = 174
#
# print(user)
# user['username'] = '小慕'F
# print(user)
# user['top'] = 175
# user['age'] = 10
# print(user)
