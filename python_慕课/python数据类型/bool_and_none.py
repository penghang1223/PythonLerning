# coding:utf-8

test = None
a = 0
b = 1
c = 0.0
d = 0.1
e = ''
f = 'None'
g = None
test = True

if __name__ == '__main__':  # 入口函数  不被其他文件调用
    print(bool(a))
    print(bool(b))
    print(bool(c))
    print(bool(d))
    print(bool(e))
    print(bool(f))
    print(bool(g))
    print(test)
    print(type(test))
    print(type(None))
