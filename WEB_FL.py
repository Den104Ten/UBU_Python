from flask import Flask, redirect, url_for, render_template, request
from flask_sqlalchemy import SQLAlchemy
import sqlite3

conn = sqlite3.connect('users.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS users
             (username TEXT, password TEXT, email TEXT)''')

conn.commit()
conn.close()


class MyApp(Flask):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


app = MyApp(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)


def check_user(username, email):
    user = User.query.filter_by(username=username, email=email).first()
    if user:
        return True
    else:
        return False

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']

        new_user = User(username=username, password=password, email=email)
        if check_user(username, email):
            return render_template('register_incorrect.html')
        else:
            db.session.add(new_user)
            db.session.commit()

        return render_template('login.html')

    return render_template('register.html')


@app.route("/register_incorrect", methods=["GET", "POST"])
def register_incorrect():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']

        new_user = User(username=username, password=password, email=email)
        if check_user(username, email):
            return render_template('register_incorrect.html')
        else:
            db.session.add(new_user)
            db.session.commit()

        return render_template('login.html')

    return render_template('register.html')



@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username, password=password).first()

        if user:
            return render_template("home_page.html")
        else:
            return render_template("login_incorrect.html")

    return render_template('login.html')



@app.route("/login_incorrect", methods=["GET", "POST"])
def login_incorrect():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']

        conn = sqlite3.connect("users.db")
        c = conn.cursor()

        c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        user = c.fetchone()

        conn.close()

        if user:
            return render_template("home_page.html")  # после логина переправка на home
        else:
            return render_template("login_incorrect.html")  # если неправильно введены данные, то обратно

    return render_template('login_incorrect.html')



if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)


