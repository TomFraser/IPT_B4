from flask import Flask, render_template, request, session, redirect, url_for
import sqlite3
from functools import wraps

c = sqlite3.connect('staff.db', check_same_thread=False)
database = c.cursor()

app = Flask(__name__)
app.config["SECRET_KEY"] = "a_hidden_key"

def getUserInfo(email, password):
    return {"name": "Steven Lau", "email":"slau2@bbc.qld.edu.au", "userImg":"images/Stv.jpeg"}

def loggedIn():
    return "userEmail" in session

def loginRequired(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if loggedIn():
            return f(*args, **kwargs)
        else:
            return redirect("/login")

    return wrap

@app.route('/login', methods=['GET', 'POST'])
def splash():
    session.pop("userEmail", None)
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        emailQuery = database.execute("SELECT email FROM staff WHERE email = ? ", (email,))
        emailQuery = emailQuery.fetchone()
        passwordQuery = database.execute("SELECT password FROM staff WHERE password = ? AND email = ?", (password,email))
        passwordQuery = passwordQuery.fetchone()
        if emailQuery:
            if passwordQuery:
                session["userEmail"] = email
                return redirect("/home")
            else:
                return redirect("/login")
        else:
            return redirect("/login")
    elif request.method == 'GET':

        return render_template("login.html")

@app.route('/home', methods=['GET', 'POST'])
@loginRequired
def landingPage():
    if request.method == "POST":
        requestType = request.form['button']
        if requestType == 'logout':
            session.pop("userEmail", None)
            return redirect("/login")
        elif requestType == "Search":
            date = request.form["date"]
            period = request.form["period"]
            room = request.form["room"]
            name = database.execute("SELECT name FROM staff WHERE email = ?", (session["userEmail"],)).fetchone()[0]
            userImage = "https://schoolbox.bbc.qld.edu.au/portrait.php?userId=" + str(database.execute("SELECT schoolboxstaffId FROM staff WHERE email = ?", (session["userEmail"],)).fetchone()[0]) + "&size=profile"
            staffMember = {"name":name, "userImg":userImage}
            # query = database.execute("SELECT room, subjectID, teacher FROM subject WHERE room = ? AND period = ? AND day = ?", room, period, date).fetchone()[0]
            roomDeets = {"room": room,"period": period, "class": "IPT1201", "teacher": "Ron Plumlee"}
            return render_template("landingPage.html", staffUser=staffMember, roomDetails=roomDeets)

    elif request.method == "GET":
        name = database.execute("SELECT name FROM staff WHERE email = ?", (session["userEmail"],)).fetchone()[0]
        userImage = "https://schoolbox.bbc.qld.edu.au/portrait.php?userId=" + str(database.execute("SELECT schoolboxstaffId FROM staff WHERE email = ?", (session["userEmail"],)).fetchone()[0]) + "&size=profile"
        staffMember = {"name":name, "userImg":userImage}
        roomDeets = {"room":"", "period":"-", "class":"-", "teacher":"-"}
        return render_template("landingPage.html", staffUser=staffMember, roomDetails=roomDeets)

@app.route('/view', methods=['GET', 'POST'])
@loginRequired
def viewChanges():
    return "VIEW!"

@app.route('/create', methods=['GET', 'POST'])
def createChagnes():
    return "CREATE!"

if __name__ == "__main__":
    app.run(debug=True)
