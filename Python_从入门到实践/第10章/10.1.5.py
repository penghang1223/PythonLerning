filename = 'pi_digits.txt'
with open(filename) as file_obiection:
    lines = file_obiection.readlines()  # readlines(num)  num表示读取多少个值


pi_string = ''

for line in lines:
        # line = line.strip() # 将去除空格后的文件重新赋值给line
        # print(line)
       pi_string = line.strip() + pi_string
        # for循环遍历 把line的值 加到pi_string 列表内

    
print(pi_string)