from flask import Flask, render_template, request
from flask_socketio import SocketIO, send, emit
import yaml
import json
from engineio.payload import Payload
import time

# custom import
from database import RedisBase

# Define socket host and port
# running on port 5000

app = Flask(__name__)

socketio = SocketIO(app, cors_allowed_origins="*")
redisbase = RedisBase()

#this is not secure
Payload.max_decode_packets = 100
Abort = False

with open("credentials.yml", "r") as stream:
        try:
            data = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)

#
# Function definitions
#
def DB_Check(socketio, optional = True):
    users_check = redisbase.retrieve_all()
    if len(users_check) == 0 and optional:
        socketio.emit("is_successful", "true")
    else:
        socketio.emit("is_successful", "false")


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
    print('received message: ' + data["data"])

    if data["data"] == "request-data" and Abort == False:
        users = redisbase.retrieve_all()

        if users == None:
            data_dict = {
                "user_len": 0,
                "user_data": []
            }
        elif len(users) == 0:
            data_dict = {
                "user_len": len(users),
                "user_data": []
            }
        else:
            data_dict = {
                "user_len": len(users),
                "user_data": users
            }

        data_json = json.dumps(data_dict)
        print(data_json)
        
        time.sleep(1)
        socketio.emit("update", data_json)

@socketio.on("create-new")
def create_new(data):
    redisbase.delete_all()
    DB_Check(socketio)

@socketio.on("remove-all") #its basically the same
def remove_all(data):
    redisbase.delete_all()
    DB_Check(socketio)

@socketio.on("abort")
def abort(data):
    redisbase.delete_all()
    Abort = True #to stop website from refreshing

    DB_Check(socketio, Abort)

if __name__ == "__main__":
    socketio.run(app, host="127.0.0.1", port=5000)