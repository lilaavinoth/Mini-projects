import pyrebase

config = {
    "apiKey": "AIzaSyBXU8YW9Uc46pnnBtbpMVfoMfCNwHHwIu0",
    "authDomain": "safety-78287.firebaseapp.com",
    "databaseURL": "https://safety-78287-default-rtdb.firebaseio.com",
    "projectId": "safety-78287",
    "storageBucket": "safety-78287.appspot.com",
    "messagingSenderId": "252983743713",
    "appId": "1:252983743713:web:2b02d951846f7e55c8d3a0",
    "measurementId": "G-MYXBVTGW69"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

def changedetec(value):
    print("changed")

def stream_handler(message):
    # print(message["event"])  # put
    # print(message["path"])  # /-K7yGTTEp7O549EzTYtI
    print(message["data"])  # {'title': 'Pyrebase', "body": "etc..."}
    changedetec(message["data"])


# output = db.child("AI output").stream(stream_handler)
inputfromphone = db.child("My input").child("input").stream(stream_handler)