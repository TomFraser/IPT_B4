from flask import Flask, render_template, request, session, redirect, url_for
import sqlite3
from functools import wraps
import smtplib
from email.mime.text import MIMEText

c = sqlite3.connect('database.db', check_same_thread=False)
database = c.cursor()
app = Flask(__name__)
app.config["SECRET_KEY"] = "a_hidden_key"

def getUserInfo(email, password):
    return {"name": "Steven Lau", "email":"slau2@bbc.qld.edu.au", "userImg":"images/Stv.jpeg"}

def loggedIn():
    return "userEmail" in session

def findStaffInfo():
    name = database.execute("SELECT name FROM staff WHERE email = ?", (session["userEmail"],)).fetchone()[0]
    userImage = "https://schoolbox.bbc.qld.edu.au/portrait.php?userId=" + str(database.execute("SELECT schoolboxstaffId FROM staff WHERE email = ?", (session["userEmail"],)).fetchone()[0]) + "&size=profile"
    return {"name":name, "userImg":userImage}

def loginRequired(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if loggedIn():
            return f(*args, **kwargs)
        else:
            return redirect("/login")

    return wrap

@app.route('/', methods=['GET', 'POST'])
def redirectToSplash():
    return redirect("/login")

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
            day = request.form["date"]
            session['day'] = day
            period = request.form["period"]
            room = request.form["room"]
            query = database.execute("SELECT room,period,teacherID,class FROM ROOMTIMETABLE where day = ? AND room = ? AND period = ?", (day,room,period)).fetchone()
            if query:
                currentChoice = {"room": query[0],"period": query[1], "class": query[3], "teacher": query[2]}
            else:
                currentChoice = {"room":room, "period":period, "class":"No Class", "teacher":"No Teacher"}
            session["roomChoice"] = currentChoice
            return render_template("landingPage.html", staffUser=findStaffInfo(), roomDetails=currentChoice)
        elif requestType == "Create Change":
            return redirect('/create')
        elif requestType == "view":
            return redirect('/view')
        elif requestType == "create":
            return redirect('/home')
    elif request.method == "GET":
        roomDeets = {"room":"", "period":"-", "class":"-", "teacher":"-"}
        return render_template("landingPage.html", staffUser=findStaffInfo(), roomDetails=roomDeets)

@app.route('/view', methods=['GET', 'POST'])
@loginRequired
def viewChanges():
    if request.method == "POST":
        buttonRequest = request.form['button']
        if buttonRequest == "view":
            return redirect("/view")
        elif buttonRequest == "create":
            return redirect("/home")
        elif buttonRequest == "logout":
            session.pop("userEmail", None)
            return redirect("/login")
    elif request.method == "GET":
        databaseCollection = database.execute("SELECT room, day, startPeriod, endPeriod, reason FROM CHANGES WHERE changedTeacherID = ?", (findStaffInfo()['name'],)).fetchall()
        databaseCollection1 = database.execute("SELECT room, day, startPeriod, endPeriod, reason, changedTeacherID FROM CHANGES WHERE teacherID = ?", (findStaffInfo()['name'],)).fetchall()
        return render_template('view.html', yourChanges=databaseCollection, changes=databaseCollection1, staffUser=findStaffInfo())

@app.route('/create', methods=['GET', 'POST'])
def createChagnes():
    if request.method == "POST":
        buttonRequest = request.form['button']
        if buttonRequest == "Request Change":
            date = request.form['changeDate']
            endPeriod = request.form['endPeriod']
            reason = request.form['reason']
            teacherList = database.execute("SELECT teacherID FROM ROOMTIMETABLE WHERE day = ? AND period BETWEEN ? AND ? AND room = ?", (session['day'], session['roomChoice']['period'], endPeriod, session['roomChoice']['room'])).fetchall()
            teacherList = sorted(set(teacherList))
            session['teacherList'] = teacherList
            session['reason'] = reason
            databaseInput = [session['roomChoice']['room'],date,session['roomChoice']['period'], endPeriod, findStaffInfo()['name'], reason, session['roomChoice']['teacher']]
            database.execute("INSERT INTO CHANGES VALUES (?, ?, ?, ?, ?, ?, ?)", (databaseInput),)
            c.commit()
            return render_template("finalReq.html", date=date, roomInfo=session['roomChoice'], end=endPeriod, staffUser=findStaffInfo(), teachers=teacherList, changeReaon=reason)
        elif buttonRequest == "Submit":
            #Send Teachers Emails
            #This isnt done as we use actual staff emails so sending them email while testing the database would be annoying. However, a slice of code simply needs to be inserted to send the emails.
            return redirect("/view")
        elif buttonRequest == 'view':
            return redirect("/view")
        elif buttonRequest == 'create':
            return redirect('/home')
    elif request.method == "GET":
        return render_template("changes.html", staffUser=findStaffInfo(), roomDetails=session["roomChoice"])

if __name__ == "__main__":
    app.run(debug=True)
