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

@app.route('/Features')
def features():
    """Renders the features page."""
    return render_template(
        'features.html',
        title='Features',
        year=datetime.now().year,
        message='Your features page.'
    )

@app.route('/Index')
def index():
    """Renders the index page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
        message='Your home page.'
    )

@app.route('/Worldwide')
def pricing():
    """Renders the worldwide page."""
    return render_template(
        'worldwide.html',
        title='Pricing',
        year=datetime.now().year,
        message='Your pricing page.'
    )

@app.route('/Atwork')
def atwork():
    """Renders the atwork page."""
    return render_template(
        'atwork.html',
        title='At work',
        year=datetime.now().year,
        message='Your at work page.'
    )

@app.route('/Shops')
def shops():
    """Renders the shops page."""
    return render_template(
        'shops.html',
        title='Shops',
        year=datetime.now().year,
        message='Your shops page.'
    )

@app.route('/Inbg')
def inbg():
    """Renders the inbg page."""
    return render_template(
        'inbg.html',
        title='In bg',
        year=datetime.now().year,
        message='Your in bg page.'
    )

@app.route('/Search')
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
    return render_template(
        'index2.html'
    )

