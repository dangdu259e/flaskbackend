from Entity.User import User


class Customer(User):
    def show_info(self):
        tup = {"idcustomer": self.iduser, "username": self.username, "password": self.password}
        print("Customer " + str(tup))
