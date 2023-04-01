# # 读取
# import time
# # 打开
# # 要用斜杠  不能反斜杠
# f = open("E:/PythonLerning/heima/20230321/test.txt", "r", encoding="UTF-8")
# # 读写
# print (type(f))
# # 关闭
# # print(f.read(10))
# # 连续调用两次read   下一次从上一次结尾接着读取  类似指针
# # print(f.readlines())  读取全部行 封装到列表中
# f1 = f.readline()
# # 类型时字符串
# f2 = f.readline()
# f3 = f.readline()
# # 一次读取一行
# print(f1)
# print(f2)
# print(f3)
#
# print(type(f1))
# # f.close()
# time.sleep(1111)


# with open("E:/PythonLerning/heima/20230321/test.txt", "r", encoding="UTF-8") as f:
#     # 自动关闭文件
#     for line in f:
#         # 一次得到一行文本数据
#         print(line)
# with open("E:/PythonLerning/heima/20230321/test.txt", "r", encoding="UTF-8") as f:
#  content=f.read()
#  count = content.count("f")
# print(count)
count = 0
with open("E:/PythonLerning/heima/20230321/test.txt", "r", encoding="UTF-8") as f:
    for line in f:
        line=line.strip()
        words = line.split(" ")
        for word in words:
            if word == "f":
                print("加一")
                count +=1
    print(line)
    print(words)
    print(f"出现{count}")





