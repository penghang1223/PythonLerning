# 集合差集
# set1 = {1,2,3}
# set2 = {2,3,4}
# # 调用方法  difference_update
# set1.difference_update(set2)
# print(set1)
# # 集合合并
# set1 = {1,2,3}
# set2 = {2,3,4}
# # 合并方法   union
# set3 = set1.union(set2)
# print(set3)


# 定义一个列表
my_list = ["大萨达","大叔大婶大","大萨达撒所大所撒大所","大大地块","打算到两个","愈发地"]
# 定义一个空的集合  用来接收列表里的值
my_set = set()
for i in my_list:
    my_set.add(i)
print(my_set)



