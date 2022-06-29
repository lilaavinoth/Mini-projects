import csv
import time
import firebase_admin
from firebase_admin import credentials,db
from Sharer import *


cred = credentials.Certificate('firebase-json.json')

firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://my-ai-81afb.firebaseio.com/'
})