from flask import Blueprint, render_template, request

auth = Blueprint('auth', __name__)

@auth.route('/register', methods = ['GET', 'POST'])
def register():
    data = request.form
    print(data)
    return render_template("auth/register.html")

@auth.route('/login', methods = ['GET', 'POST'])
def login():
    data = request.form
    print(data)
    return render_template("auth/login.html", text="Testing")

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"