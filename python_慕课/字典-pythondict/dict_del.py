# coding:utf-8

projects = {
    'ipad': {'name': 'ipad', 'price': 2200, 'desc': '平板电脑'},
    'iphone': {'name': 'iphone', 'price': 3000, 'desc': '智能手机'},
    'pc': {'name': 'pc', 'price': 5000, 'desc': '台式电脑'},
    'mac': {'name': 'mac', 'price': 8000, 'desc': '平板电脑'}
}

# new_pro = projects.clear()  清楚所有的key value
# print(new_pro)
print(projects.keys())

print('一个中学生购买了{}, 价格是{}'.format(projects['pc']['name'], projects['pc']['price']))
projects.pop('pc')  # 删除key  包括对应的value
print(projects.keys())

result = projects.pop('mac')
print('一个程序员购买了{}, 它的价格是{}'.format(result['name'], result.get('price')))
print(projects.keys())

print('{} 和 {} 都被卖出了， 他们一共花费了{}元'.format(
    projects['ipad']['name'], projects['iphone']['name'],
    projects['ipad']['price'] + projects['iphone']['price']
))

projects.clear()
print(projects.keys())

del projects  # 删除字典
print(projects)
