from flask import Flask
from flask.helpers import send_from_directory

app = Flask(__name__)

@app.route('/hello')
def hello():
    return "Hello Internet!"

@app.route('/')
def index():
    return send_from_directory("static", "index.html")