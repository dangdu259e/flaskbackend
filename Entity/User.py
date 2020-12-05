class User:
    def __init__(self, iduser, username, password):
        self.iduser = iduser
        self.username = username
        self.password = password

    def show_info(self):
        tup = {"idcustomer": self.iduser, "username": self.username, "password": self.password}
        print(str(tup))

    def show_info_name(self):
        tup = {"idcustomer": self.iduser, "username": self.username, "password": self.password}
        print("User " + str(tup))
