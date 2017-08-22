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
        requestType = request.form['sidemenuButton']
        if requestType == 'logout':
            return redirect("/")
        elif requestType == 'view':
            return redirect("/view")
        elif requestType == 'create':
            return redirect("/create")
    elif request.method == "GET":
        staffMember = [dict(name="Steven Chi Lau", userImg="images/Stv.jpeg")]
        return render_template("landingPage.html", staffUser=staffMember)

@app.route('/view', methods=['GET', 'POST'])
def viewChanges():
    return "VIEW!"

@app.route('/create', methods=['GET', 'POST'])
def createChagnes():
    return "CREATE!"

if __name__ == "__main__":
    app.run(debug=True)
