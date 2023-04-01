my_dict = {"防守打法": 33,
           "b": '撒打发',
           "导出的": "dasd"
           }

# key 不可重复
# value 可以重复


print(my_dict)

my_dict2 = {}
my_dict3 = dict()

print(type(my_dict2))
print(type(my_dict3))

# 字典嵌套


stu_score_dict = {
    "小明": {
        "语文": 100,
        "数学": 99,
        "英语": 88
    },
    "小红": {
        "语文": 100,
        "数学": 99,
        "英语": 88
    },
    "小华": {
        "语文": 100,
        "数学": 99,
        "英语": 88
    }

}

# shift alt 鼠标滚轮

# alt j
# 同一个词

print(stu_score_dict)
scor=stu_score_dict["小明"]["语文"]
print(scor)

stu_score_dict["小明"]["语文"] = 1000
print(stu_score_dict)