import pymysql

no = int(input('输入要删除的编号：'))

con  = pymysql.connect(host='localhost', port=3306, database='hrs', charset='utf8', user='root', password='123456', autocommit=True)

try:
    with con.cursor() as cursor:
        result = cursor.execute('delete from tb_dept where dno=%s', (no))
    if result == 1:
        print('删除成功')
finally:
    con.close()
