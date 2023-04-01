# alien = {'key': 'value'}
# # 字典['key]
# print(alien['key'])

# 访问字典中的值
# alien_0 = {'color': 'green', 'points': '5'}
# print(['color'])
# print(['points'])
# new_point = alien_0['points']
# print(f'you just earned {new_point} points ')

# 添加键值对
# alien_0 = {'color': 'green', 'points': '5'}
# alien_0['x_positions'] = 0
# alien_0['y_positions'] = 25
# print(alien_0)
#
# # 修改字典中的值
# alien_0['x_positions'] = 5
# print(alien_0)

# 删除键值对
# alien_0 = {'color': 'green', 'points': '5'}
# del alien_0['color']
# print(alien_0)

# 使用get访问值  当key没有对应的值时可以添加默认值  且不会报错
# alien_0 = {'color': 'green', 'speed':'slow'}
# point_value = alien_0.get('points','没有')
# print(point_value)

user_0 = {
    'username': '彭予安',
    'first': '予',
    'last': '安'
}
# 遍历所有键值对
# for key, value in user_0.items():
#     print(f'key: {key}')
#     print(f'value:{value}')
#     # 遍历字典中所有的键
# for k in user_0.keys():
#     print(f'key:{k}')
# 使获取的值排序
# for k in sorted(user_0.keys()):
#     print(f'排序输出:{k}')