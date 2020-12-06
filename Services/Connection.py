import pymysql.cursors


# Hàm trả về một connection.
def ConnectionDB():
    # Bạn có thể thay đổi các thông số kết nối.
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='1234',
                                 db='mydb',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    return connection
