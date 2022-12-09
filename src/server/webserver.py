from flask import Flask, render_template, request, url_for, flash, redirect
import yaml

# custom import
from database import *

# Define socket host and port
# running on port 5000

app = Flask(__name__)

with open("credentials.yml", "r") as stream:
        try:
            data = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)

@app.route("/")
def Response():
    return "Zde nemáš co dělat..."

@app.route("/admin")
def admin_load():
    return render_template("login.html")

@app.route("/login", methods = ['POST'])
def login():
    
    username = request.form['username']
    password = request.form["password"]
    
    if username == data["username"] and password == data["password"]:
        return render_template("index.html")
    else:
        return "Nepovedlo se :(, špatné jméno nebo heslo"


if __name__ == "__main__":
    app.run()