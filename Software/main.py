from flask import Flask, render_template, request, session, redirect, url_for
from general import sendUser
import sqlite3

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def splash():
    email = request.form["email"]
    password = request.form["password"]
    sendUser(email, password)
    return render_template("login.html")

@app.route('/home', methods=['GET', 'POST'])
def landingPage():


if __name__ == "__main__":
    app.run(debug=True)
