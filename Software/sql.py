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
    staffID INTEGER NOT NULL PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    schoolboxstaffID TEXT NOT NULL
    )''')

    database.execute('''CREATE TABLE ROOMTIMETABLE(
    room TEXT NOT NULL,
    roomID TEXT PRIMARY KEY,
    day TEXT NOT NULL,
    period INTEGER NOT NULL,
    class TEXT NOT NULL,
    teacher TEXT NOT NULL,
    teacherID TEXT NOT NULL,
    FOREIGN KEY (class) REFERENCES COURSE(courseID)
    FOREIGN KEY (teacher) REFERENCES COURSE(teacher)
    FOREIGN KEY (teacherID) REFERENCES STAFF(name)
    )''')

    database.execute('''CREATE TABLE COURSE (
    courseID INTEGER NOT NULL PRIMARY KEY,
    room TEXT NOT NULL,
    name TEXT NOT NULL,
    teacher INTEGER NOT NULL,
    FOREIGN KEY (room) REFERENCES ROOM(roomID),
    FOREIGN KEY (teacher) REFERENCES STAFF(staffID)
    )''')

setupDB()
