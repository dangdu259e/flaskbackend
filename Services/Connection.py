import pymysql.cursors


# Hàm trả về một connection.
def ConnectionDB():
    # Bạn có thể thay đổi các thông số kết nối.
    connection = pymysql.connect(host='192.168.5.129',
                                 user='root',
                                 password='1234',
                                 db='simplehr',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    return connection
