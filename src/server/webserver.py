from flask import Flask, render_template, request
from flask_socketio import SocketIO
import yaml

# custom import
from database import *

# Define socket host and port
# running on port 5000

app = Flask(__name__)

socketio = SocketIO(app, cors_allowed_origins="*")

with open("credentials.yml", "r") as stream:
        try:
            data = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)

#
# Standart Flask
#

@app.route("/admin")
def Response():
    return render_template("login.html")

@app.route("/login", methods = ['POST'])
def login():
    
    username = request.form['username']
    password = request.form["password"]
    
    if username == data["username"] and password == data["password"]:
        return render_template("index.html")
    else:
        return "Nepovedlo se :(, špatné jméno nebo heslo"

#
# SocketIO
#

@socketio.on('message')
def handle_message(data):
    print('received message: ' + data)

if __name__ == "__main__":
    socketio.run(app)