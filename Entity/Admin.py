from Entity.User import User


class Admin(User):
    def show_info(self):
        dic = {"idcustomer": self.iduser, "username": self.username, "password": self.password}
        print("Admin " + str(dic))
