from Entity import User

idcustomer = 1
username = "dangtrungdu"
password = "du1234"

customer = User.User(idcustomer, username, password)
customer.show_info_name()