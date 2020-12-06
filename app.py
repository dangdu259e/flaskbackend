from flask import Flask, render_template, request
from Services import connectExample
from Services import Connection

app = Flask(__name__)


@app.route('/get')
def hello_world():
    return connectExample.runn()


@app.route("/")
def welcome():
    return render_template('welcome.html')
@app.route('/login')
def login():
    return render_template('index.html')

# @app.route('/save-post', methods=['POST', 'GET'])
# def signUp():
#     if request.method == 'POST':
#         id= 3
#         email = request.form['exampleInputEmail1']
#         password = request.form['exampleInputPassword1']
#         try:
#
#             with connection.cursor() as cursor:
#                 # Read a single record
#                 sql = "INSERT INTO khachhang (idkhachhang,username,password) VALUES (%s, %s, %s)"
#                 cursor.execute(sql, (id, email, password))
#                 connection.commit()
#         finally:
#             connection.close()
#             return "Saved successfully."
#     else:
#         return "error"
@app.route('/save-post', methods=['POST', 'GET'])
def signUp():
    # connect DB MYSQL
    connection = Connection.ConnectionDB()

    # request form and get data in form
    if request.method == 'POST':
        email = request.form['exampleInputEmail1']
        password = request.form['exampleInputPassword1']
        # Query and check
        try:
            with connection.cursor() as cursor:
                # Read a single record
                # cursor.execute('SELECT * FROM accounts WHERE username = %s AND password = %s', (username, password,))
                sql = "SELECT * FROM admin WHERE username = %s AND password = %s"
                cursor.execute(sql, (email, password))
                data = cursor.fetchall()
                if (len(data) > 0):
                    return render_template('home.html')
                else:
                    return render_template('error.html.html')
                connection.commit()
                connection.close()
        # Close connect
        finally:
            connection.close()
    else:
        return "error"


app.route('/login/<username>/<password>', methods=['POST','GET'])
def loginuser(username, password):
    # connect DB MYSQL
    connection = Connection.ConnectionDB()

    # request form and get data in form
    if request.method == 'POST':
        email = request.form['exampleInputEmail1']
        password = request.form['exampleInputPassword1']
        # Query and check
        try:
            with connection.cursor() as cursor:
                # Read a single record
                # cursor.execute('SELECT * FROM accounts WHERE username = %s AND password = %s', (username, password,))
                sql = "SELECT * FROM admin WHERE username = %s AND password = %s"
                cursor.execute(sql, (email, password))
                data = cursor.fetchall()
                if (len(data) > 0):
                    return render_template('home.html')
                else:
                    return render_template('error.html')
                connection.commit()
                connection.close()
        # Close connect
        finally:
            connection.close()
    else:
        return "error"


if __name__ == '__main__':
    app.run()
