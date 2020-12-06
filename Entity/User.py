from werkzeug.security import generate_password_hash, check_password_hash

class User:
    def __init__(self, iduser, username, password):
        self.iduser = iduser
        self.username = username
        self.password = password

    def show_info(self):
        dic = {"iduser": self.iduser, "username": self.username, "password": self.password}
        print(str(dic))

    def show_info_name(self):
        dic = {"iduser": self.iduser, "username": self.username, "password": self.password}
        print("User " + str(dic))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)