import sqlite3

c = sqlite3.connect('database.db', check_same_thread=False)
database = c.cursor()

def setupDB():

    database.execute('''CREATE TABLE STUDENT (
    studentID INTEGER PRIMARY KEY,
    email TEXT NOT NULL UNIQUE,
    firstName TEXT NOT NULL,
    lastName TEXT NOT NULL
    )''')

    database.execute('''CREATE TABLE STAFF (
    staffID INTEGER PRIMARY KEY,
    email TEXT NOT NULL UNIQUE,
    firstName TEXT NOT NULL,
    lastName TEXT NOT NULL
    )''')

    database.execute('''CREATE TABLE ROOM (
    roomID TEXT PRIMARY KEY,
    block TEXT NOT NULL,
    subject TEXT,
    FOREIGN KEY (subject) REFERENCES COURSE(courseID)
    )''')

    database.execute('''CREATE TABLE COURSE (
    courseID INTEGER NOT NULL PRIMARY KEY,
    room TEXT NOT NULL,
    name TEXT NOT NULL,
    teacher INTEGER NOT NULL,
    FOREIGN KEY (room) REFERENCES ROOM(roomID),
    FOREIGN KEY (teacher) REFERENCES STAFF(staffID)
    )''')

    database.execute('''CREATE TABLE STUDENT-COURSE (
        
    )''')

setupDB()
