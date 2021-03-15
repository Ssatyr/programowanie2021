from datetime import datetime
from flask import Flask, render_template, request
import flask
#from . import app
import os, uuid, sys

app = flask.Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/contact/")
def contact():
    return render_template("contact.html")

@app.route('/upload/')
def upload():
   return render_template("upload.html")

@app.route('/instruction/')
def instruction():
   return render_template("instruction.html")

@app.route("/uploader/", methods = ['GET', 'POST'])
def uploader():
    f = request.files['inputFile']

   

    return render_template(
        "uploaded.html",
        fname = f.filename)

@app.route("/hello/")
@app.route("/hello/<name>")
def hello_there(name = None):
    return render_template(
        "hello_there.html",
        name=name,
        date=datetime.now()
    )

@app.route("/api/data")
def get_data():
    return app.send_static_file("data.json")
