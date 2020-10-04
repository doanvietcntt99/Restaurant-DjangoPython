import pymysql.cursors
def ConnectDatabase(SQLConsole):
    connection = pymysql.connect(host='127.0.0.1',
                                 user='root',
                                 password='123456',
                                 db='pythonwebtasteit',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    print("Kết nối thành công!")
    try:

        with connection.cursor() as cursor:
            sql = SQLConsole
            cursor.execute(sql)
            return cursor       
    finally:
        # Đóng kết nối 
        connection.close()
KQ = ConnectDatabase("Select * From Admin_Login")
print()
for row in KQ:
    print(row)