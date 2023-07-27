from flask import Flask, redirect, url_for, render_template, request
from flask_sqlalchemy import SQLAlchemy
import sqlite3

app = Flask(__name__)

conn = sqlite3.connect('users.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS users
             (username TEXT, password TEXT, email TEXT)''')

conn.commit()
conn.close()


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']

        conn = sqlite3.connect("users.db")
        c = conn.cursor()

        c.execute("INSERT INTO users (username, password, email) VALUES (?, ?, ?)", (username, password, email))

        conn.commit()
        conn.close()

        return render_template('login.html')

    return render_template('register.html')


@app.route("/login", methods=["GET", "POST"])
def login():
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

    return render_template('login.html')

if __name__ == "__main__":
    app.run(debug=True)


