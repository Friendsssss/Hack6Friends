"""
Routes and views for the flask application.
"""
import os
from datetime import datetime
from flask import render_template
from Hack import app

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )
@app.route('/Run_Script')
def run_script():
    #coding: utf-8
    print(os.getcwd())
    tt = open("test2.txt", "r")
    txt = tt.read()

    z = txt.find(". .")
    print("last", z)
    word = "ковид"
    a = txt.find(word)
    print("word", a)
    b = txt.find(".", 0, txt.find(word))
    for b1 in range(0, z):
        b1 = txt.find(".", b1, txt.find(word))
        if b1>-1:
            b = b1
    print("start", b)
    c = txt.find(". ", a+1, z+2)
    print("end", c)

    f = open("test.txt", "w")

    for i in range(b+2, c+1):
        f.write(txt[i])
    f.close()
    f = open("test.txt", "r")
    print(f.read())



