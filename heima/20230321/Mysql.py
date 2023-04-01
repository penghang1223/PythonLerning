import pymysql
conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='981223'
)
cursor = conn.cursor() # 获取到游标对象?
conn.select_db("bilibili")
cursor.execute("select * from danmu")  # 成员方法 获取游标对象
result:  tuple = cursor.fetchall()  #成员方法 fetchall 获取查询结果  封装到元组内
for i in result:
    print(i)

# print(conn.get_server_info())
conn.close()
