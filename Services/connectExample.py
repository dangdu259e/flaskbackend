import pymysql.cursors
import json

# Kết nối vào database.
from flask import jsonify
def runn():
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='1234',
                                 db='mydb',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)

    print("connect successful!!")

    try:

        with connection.cursor() as cursor:

            # SQL
            sql = "SELECT * FROM khachhang"

            # Thực thi câu lệnh truy vấn (Execute Query).
            cursor.execute(sql)

            print("cursor.description: ", cursor.description)

            print()

            for row in cursor:
                dic = row #từ điển
                #bóc từ từ điên thành object
                #chuyển object thành jsonify là xong
                print(dic)
            #     print(jsonify(dic))
            #     print(type(dic))
            # some JSON:


    finally:
        # Đóng kết nối (Close connection).
        connection.close()