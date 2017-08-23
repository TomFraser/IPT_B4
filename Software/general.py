from flask import Flask, render_template, request, session, redirect, url_for

def getUserInfo(email, password):
    return {"name": "Steven Lau", "email":"slau2@bbc.qld.edu.au", "userImg":"images/Stv.jpeg"}

def loggedIn():
    return "userEmail" in session
