import pymysql

con  = pymysql.connect(host='localhost', port=3306, database='hrs', charset='utf8', user='root', password='123456', autocommit=True)

no = int(input('输入需要修改的编号：'))
name = input('输入需要修改的名字：')
loc = input('输入需要修改的所在地：')

try:
    with con.cursor() as curson:
        result = curson.execute('update tb_dept set dname=%s, dloc=%s where dno=%s', (name, loc, no))
    if result == 1:
        print('更新成功')
finally:
    con.close()