import pyrebase
from firebasedata import LiveData

config = {
    "apiKey": "AIzaSyA-8GaJ1AbBO3pTVEh0Q4Y57wyniEAINz0",
    "authDomain": "my-ai-81afb.firebaseapp.com",
    "databaseURL": "https://my-ai-81afb.firebaseio.com",
    "projectId": "my-ai-81afb",
    "storageBucket": "my-ai-81afb.appspot.com",
    "databaseURL" "https://my-ai-81afb.firebaseio.com/"
    "messagingSenderId": "309184166422",
    "appId": "1:309184166422:web:f1ebbb1da7aaddb61f1337",
    "measurementId": "G-7PEFMR0Y5Z"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

# db.child("users").child("Morty")
# data = {"name": "Mortimer 'Morty' Smith","value":"vinoth's brain"}
# db.child("users").push(data)

def changedetec(value):
    print("changed")

def stream_handler(message):
    # print(message["event"])  # put
    # print(message["path"])  # /-K7yGTTEp7O549EzTYtI
    print(message["data"])  # {'title': 'Pyrebase', "body": "etc..."}
    changedetec(message["data"])


# output = db.child("AI output").stream(stream_handler)
inputfromphone = db.child("My input").child("input").stream(stream_handler)
