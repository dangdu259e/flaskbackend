from Entity.User import User
from Services import Connection

class Customer(User):
    def show_info(self):
        dic = {"idcustomer": self.iduser, "username": self.username, "password": self.password}
        print("Customer " + str(dic))

    def insert_user(self, username, password):
        connection = Connection.ConnectionDB()
        try:
            with connection.cursor() as cursor:
                # Create a new record
                sql = "INSERT INTO `khachhang` (`username`, `password`) VALUES (%s, %s)"
                cursor.execute(sql, (username, password))

            # connection is not autocommit by default. So you must commit to save
            # your changes.
            connection.commit()

            with connection.cursor() as cursor:
                # Read a single record
                sql = "SELECT `id`, `password` FROM `khachhang` WHERE `username`=%s"
                cursor.execute(sql, (username,))
                result = cursor.fetchone()
                print(result)
        finally:
            connection.close()
