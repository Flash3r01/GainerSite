from flask import Flask, render_template
from flask.helpers import send_from_directory

app = Flask(__name__)

@app.route('/hello')
def hello():
    return "Hello Internet!"

@app.route('/static')
def staticPage():
    return send_from_directory("static", "html/static.html")

@app.route('/')
def index():
    return render_template("index.html", title="Home")