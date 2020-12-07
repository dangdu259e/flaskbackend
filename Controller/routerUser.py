from flask import Flask, render_template, request, redirect, url_for, session
import secrets
from Services import Connection, checkLogin, insertUser

secret = secrets.token_urlsafe(32)
app = Flask(__name__)
conn = Connection.ConnectionDB()


def loginuser():
    email = request.args.get('email', None)
    print(request)
    print(email)
    # password = request.args.get('password', None)
    # result = checkLogin.check_Login(email, password)
    return 'success'

def insertuser():
    # email = request.args.get('email', None)
    # password = request.args.get('password', None)
    email = request.form.get('email')
    password = request.form.get('password')
    result = insertUser.insert_user(email, password)
    return result
