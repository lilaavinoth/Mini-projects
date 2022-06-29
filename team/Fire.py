import pyrebase
from firebasedata import LiveData

config = {
    "apiKey": "AIzaSyA51f_cnFfxwZ__5PEPWmSbevRZTv63kGI",
    "authDomain": "realtime-listener-675c6.firebaseapp.com",
    "projectId": "realtime-listener-675c6",
    "storageBucket": "realtime-listener-675c6.appspot.com",
    "messagingSenderId": "564143348171",
    "databaseURL": "https://realtime-listener-675c6-default-rtdb.firebaseio.com/",
    "appId": "1:564143348171:web:004fc2616757d43fe43e4e",
    "measurementId": "G-L2LE9N8HJE"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()
# db.child("users").child("Morty")
data = {"name": "Mortimer 'Morty' Smith","value":"vinoth's brain"}
db.child("users").push(data)


def stream_handler(message):
  # print(message["event"])  # put
  # print(message["path"])  # /-K7yGTTEp7O549EzTYtI
  print(message["data"])  # {'title': 'Pyrebase', "body": "etc..."}


my_stream = db.child("users").stream(stream_handler)
