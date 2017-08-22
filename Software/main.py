from flask import Flask, render_template, request, session, redirect, url_for
from general import sendUser
import sqlite3

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def splash():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        if(sendUser(email, password)) == True:
            return redirect("/home")
    elif request.method == 'GET':
        return render_template("login.html")

@app.route('/home', methods=['GET', 'POST'])
def landingPage():
    if request.method == "POST":
        if request.form['sidemenuButton'] == 'logout':
            return redirect("/")
    elif request.method == "GET":
        return render_template("landingPage.html")


if __name__ == "__main__":
    app.run(debug=True)
