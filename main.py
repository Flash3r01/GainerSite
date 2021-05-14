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

@app.route('/projects')
def projects():
    return render_template("projects.html", title="Projects")

@app.route('/games')
def games():
    return render_template("games.html", title="Featured Games")

@app.route('/links')
def links():
    return render_template("links.html", title="Links")

@app.route('/about')
def about():
    return render_template("about.html", title="About")

if __name__ == "__main__":
    app.run(host="0.0.0.0")
