from Services import Connection
import secrets
secret = secrets.token_urlsafe(32)

def check_Login(email, password):
    # connect DB MYSQL
    connection = Connection.ConnectionDB()
    # Query and check
    try:
        with connection.cursor() as cursor:
            # Read a single record
            # cursor.execute('SELECT * FROM accounts WHERE username = %s AND password = %s', (username, password,))
            sql = "SELECT * FROM admin WHERE username = %s AND password = %s"
            cursor.execute(sql, (email, password))
            data = cursor.fetchall()
            if (len(data) > 0):
                return 'success'
                # return url_for('/get/homepage', methods=['GET'])
            else:
                return 'Invalid'
            connection.commit()
            connection.close()
    finally:
        connection.close()

