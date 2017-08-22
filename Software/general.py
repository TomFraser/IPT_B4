from flask import Flask, render_template, request, session, redirect, url_for
debug = False
def sendUser(email, password):
    if debug:
        print(email)
        print(password)
        print("Sending User Data to BBC")
    #Send user info to BBC
    return True
