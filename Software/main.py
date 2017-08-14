from flask import Flask, render_template, request, session, redirect, url_for
import sqlite3

app = Flask(__name__)

@app.route('/')
def splash():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
