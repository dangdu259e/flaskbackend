from Services import Connection
import secrets
secret = secrets.token_urlsafe(32)

def insert_user(email, password):
    # connect DB MYSQL
    connection = Connection.ConnectionDB()
    # Query and check
    try:
        with connection.cursor() as cursor:
            # Read a single record
            # cursor.execute('SELECT * FROM accounts WHERE username = %s AND password = %s', (username, password,))
            sql = "INSERT INTO `khachhang` (`username`,`password`) VALUES (%s,%s);"
            cursor.execute(sql, (email, password))
            return 'success'
            connection.commit()
            connection.close()
    finally:
        connection.close()
