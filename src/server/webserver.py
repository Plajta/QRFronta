
from flask import Flask, render_template, request, redirect
from flask_socketio import SocketIO, send, emit
import yaml
import json
from engineio.payload import Payload
import time

#encoding
import base64
import uuid

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
Last_Users = None
Count = []
mins = 0

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

@app.route("/front")
def register():
    return render_template("register.html")

@app.route("/user_post", methods = ['POST'])
def user_interface_post():

    username = request.form['username']

    UUID = uuid.uuid1()
    data = base64.b64encode(username.encode("utf-8")).decode("utf-8")
    redisbase.add(UUID, data)

    done = False
    users = redisbase.retrieve_all()
    for elem in users:
        if data in elem:
            done = True
            break
    
    if(done):
        return redirect(f"http://localhost:5000/user/{data}")
    else:
        return "Nepovedlo se! Bohužel jste nebyl zařazen do fronty"

@app.route("/user/<string:data>")
def user_interface(data: str):
    print(data)
    return render_template("user.html")

@app.route("/error")
def error():
    return render_template("error.html")

#
# SocketIO
#

@socketio.on('message')
def handle_message(data):
    global Count

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
        
        #setting timestamp
        for i in range(data_dict["user_len"]):
            try:
                Count[i] += 1
            except Exception as E:
                Count.append(1)

        print(Count)
        Count = Count[:data_dict["user_len"] - 1]

        #getting mean
        inc = 0
        for elem in Count: inc += elem

        if len(Count) == 0: mins = 0
        else: mins = round(inc / len(Count))

        data_dict["time"] = mins

        #sending data
        data_json = json.dumps(data_dict)
        print(data_json)
        
        time.sleep(1)
        socketio.emit("update", data_json)

@socketio.on("request-spec")
def handle_individual_request(data):
    if Abort == False:
        users = redisbase.retrieve_all()

        if users == None:
            socketio.emit("update", "false")
        elif len(users) == 0:
            socketio.emit("update", "false")
        else:
            Found = False
            obj_order = None

            for iter_count, elem in enumerate(users):
                if data["request-data-specific"] in elem:
                    #it exists!
                    Found = True
                    obj_order = iter_count
            
            if not Found:
                socketio.emit("update", "false")
            else:
                #found it!
                data_dict = {
                    "order": obj_order,
                    "timespan": mins
                }

                socketio.emit("update", data_dict)

        

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

@socketio.on("delete-specific")
def remove_specific(data):
    redisbase.delete(data)

if __name__ == "__main__":
    socketio.run(app, host="127.0.0.1", port=5000)

@socketio.on("next")
def call_next():
    redisbase.delete(0)