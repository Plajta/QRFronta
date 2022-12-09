from flask import Flask, render_template
import os

# custom import
from database import *

# Define socket host and port
# running on port 5000

app = Flask(__name__)

@app.route("/")
def Response():
    return "Zde nemáš co dělat..."

@app.route("/admin")
def admin_load():
    return render_template("index.html")

if __name__ == "__main__":
    app.run()