import pymysql

con = pymysql.connect(host='localhost', port=3306, database='hrs', charset='utf8', user='root', password='123456')
no = int(input('编号：'))
name = input('名字：')
loc = input('所在地：')

try:
    with con.cursor() as cursor:
        result = cursor.execute('insert into tb_dept values (%s, %s, %s)', (no, name, loc))
    if result == 1:
        print('添加成功')
    con.commit()
finally:
    con.close()