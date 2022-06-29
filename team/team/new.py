from threading import Thread

import nltk
import pickle
import numpy
import tflearn
import tensorflow
import random
import json
import os
import firebase_admin
from googletrans import Translator
from firebase_admin import credentials, db
from gtts import gTTS
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import csv

import time
global lang
lang = ""
global PhoneResp
PhoneResp = ""


rrr = ""
print("Please wait while building model")

translator = Translator()

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


class myClassA(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.daemon = True
        self.start()

    def run(self):
        while True:
            sharer()

speedOfVehicle = None
engine_temp = None
tire_pressure = None
lights = None
track_time = None
lat = None
lon =None
ignition =None
odometer = None
direction = None
Gps_status = None
Speed_Wheel_Front_Right =None
Speed_Wheel_Front_Left = None
Vehicle_Speed = None
Speed_Wheel_Rear_Left =None
Speed_Wheel_Rear_Right =None
Longitudinal_Acceleration =None
Transversal_Acceleration = None
Distance_Totalizer = None
Engine_Coolant_Temperature =None
Steering_Wheel_Angle =None
Steering_Wheel_Rotation_Speed =None
Steering_Wheel_Angle_Offset =None
Engine_RPM = None
Mean_Effective_Torque =None
Raw_Sensor = None
Seat_Belt_Driver_Reminder =None
Seat_Belt_Front_Passenger_Reminder =None
Seat_Belt_2nd_Row_Center_Status = None
Seat_Belt_2nd_Row_Right_Status = None
Seat_Belt_2nd_Row_Left_Status = None
Parking_Brake = None
Front_Left_Door_Warning =None
Front_Right_Door_Warning =None
Rear_Right_Door_Warning = None
Boot_Door_Warning = None
Rear_Left_Door_Warning =None
Driver_Door_Locked = None
Fuel_Low = None
Low_Beam = None
High_Beam =None
Warning_Lights =None
ABS_Warning_Request =None
Battery_Warning = None
internalbattvolts =None
VehicleBatteryVoltage =None
waveband =None
programme_type =None
Frequency_of_channel =None
programme_identification =None
stationName =None
source = None
Time_Spent_on_the_Channel =None
Start_time_on_Channel = None
End_time_on_Channel = None
CategoryName = None
AppName = None
State = None
BT_Connectivity_Status =None
Time_BT_is_connected =None
Start_time_for_BT_connectivity =None
End_time_for_BT_connectivity =None
key =None
source_headUnit =None
direction_headUnit =None
CategoryName_headUnit =None
AppName_headUnit =None
ScreenName =None
KeyType =None
Action =None
Theft_Detection=None
Fuel=None
Window=None
Accident= None

class Sharer(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.daemon = True
        self.start()

    def run(self):
        sharer()
def sharer():

    datas = open('carTestData.csv', encoding='utf-8-sig')
    csv_datas = csv.reader(datas)
    data_lines = list(csv_datas)

    time.sleep(2)
    global speedOfVehicle,tire_pressure,lights,engine_temp,tire_pressure,lights,track_time,lat,lon,ignition,odometer
    global direction,Gps_status,Speed_Wheel_Front_Right,Speed_Wheel_Front_Left,Vehicle_Speed,Speed_Wheel_Rear_Left,Speed_Wheel_Rear_Right
    global Longitudinal_Acceleration,Transversal_Acceleration,Distance_Totalizer,Engine_Coolant_Temperature,Steering_Wheel_Angle
    global Steering_Wheel_Rotation_Speed,Steering_Wheel_Angle_Offset,Engine_RPM,Mean_Effective_Torque,Raw_Sensor,Seat_Belt_Driver_Reminder
    global Seat_Belt_Front_Passenger_Reminder,Seat_Belt_2nd_Row_Center_Status,Seat_Belt_2nd_Row_Right_Status,Seat_Belt_2nd_Row_Left_Status
    global Parking_Brake,Front_Left_Door_Warning,Front_Right_Door_Warning,Rear_Right_Door_Warning,Boot_Door_Warning,Rear_Left_Door_Warning
    global Driver_Door_Locked,Fuel_Low,Low_Beam,High_Beam,Warning_Lights,ABS_Warning_Request,Battery_Warning,internalbattvolts,VehicleBatteryVoltage
    global waveband,programme_type,Frequency_of_channel,programme_identification,stationName,source,Time_Spent_on_the_Channel,Start_time_on_Channel
    global End_time_on_Channel,CategoryName,AppName,State,BT_Connectivity_Status,Time_BT_is_connected,Start_time_for_BT_connectivity,End_time_for_BT_connectivity
    global key,source_headUnit,direction_headUnit,CategoryName_headUnit,AppName_headUnit,ScreenName,KeyType,Action,Theft_Detection,Fuel,Window,Accident
    speedOfVehicle = data_lines[1][0]
    engine_temp = data_lines[1][1]
    tire_pressure = data_lines[1][2]
    lights = data_lines[1][3]
    track_time = data_lines[1][4]
    lat = data_lines[1][5]
    lon = data_lines[1][6]
    ignition = data_lines[1][7]
    odometer = data_lines[1][8]
    direction = data_lines[1][9]
    Gps_status = data_lines[1][10]
    Speed_Wheel_Front_Right = data_lines[1][11]
    Speed_Wheel_Front_Left = data_lines[1][12]
    Vehicle_Speed = data_lines[1][13]
    Speed_Wheel_Rear_Left = data_lines[1][14]
    Speed_Wheel_Rear_Right = data_lines[1][15]
    Longitudinal_Acceleration = data_lines[1][16]
    Transversal_Acceleration = data_lines[1][17]
    Distance_Totalizer = data_lines[1][18]
    Engine_Coolant_Temperature = data_lines[1][19]
    Steering_Wheel_Angle = data_lines[1][20]
    Steering_Wheel_Rotation_Speed = data_lines[1][21]
    Steering_Wheel_Angle_Offset = data_lines[1][22]
    Engine_RPM = data_lines[1][23]
    Mean_Effective_Torque = data_lines[1][24]
    Raw_Sensor = data_lines[1][25]
    Seat_Belt_Driver_Reminder = data_lines[1][26]
    Seat_Belt_Front_Passenger_Reminder = data_lines[1][27]
    Seat_Belt_2nd_Row_Center_Status = data_lines[1][28]
    Seat_Belt_2nd_Row_Right_Status = data_lines[1][29]
    Seat_Belt_2nd_Row_Left_Status = data_lines[1][30]
    Parking_Brake = data_lines[1][31]
    Front_Left_Door_Warning = data_lines[1][32]
    Front_Right_Door_Warning = data_lines[1][33]
    Rear_Right_Door_Warning = data_lines[1][34]
    Boot_Door_Warning = data_lines[1][35]
    Rear_Left_Door_Warning = data_lines[1][36]
    Driver_Door_Locked = data_lines[1][37]
    Fuel_Low = data_lines[1][38]
    Low_Beam = data_lines[1][39]
    High_Beam = data_lines[1][40]
    Warning_Lights = data_lines[1][41]
    ABS_Warning_Request = data_lines[1][42]
    Battery_Warning = data_lines[1][43]
    internalbattvolts = data_lines[1][44]
    VehicleBatteryVoltage = data_lines[1][45]
    waveband = data_lines[1][46]
    programme_type = data_lines[1][47]
    Frequency_of_channel = data_lines[1][48]
    programme_identification = data_lines[1][49]
    stationName = data_lines[1][50]
    source = data_lines[1][51]
    Time_Spent_on_the_Channel = data_lines[1][52]
    Start_time_on_Channel = data_lines[1][53]
    End_time_on_Channel = data_lines[1][54]
    CategoryName = data_lines[1][55]
    AppName = data_lines[1][56]
    State = data_lines[1][57]
    BT_Connectivity_Status = data_lines[1][58]
    Time_BT_is_connected = data_lines[1][59]
    Start_time_for_BT_connectivity = data_lines[1][60]
    End_time_for_BT_connectivity = data_lines[1][61]
    key = data_lines[1][62]
    source_headUnit = data_lines[1][63]
    direction_headUnit = data_lines[1][64]
    CategoryName_headUnit = data_lines[1][65]
    AppName_headUnit = data_lines[1][66]
    ScreenName = data_lines[1][67]
    KeyType = data_lines[1][68]
    Action = data_lines[1][69]
    Theft_Detection = data_lines[1][70]
    Fuel = data_lines[1][71]
    Window = data_lines[1][72]
    Accident = data_lines[1][73]
    # connecting dataset to Variables


    uploader = db.reference("Trip Data")
    uploader.update({
        'speedOfVehicle': speedOfVehicle,
        'engine_temp': engine_temp,
        'tire_pressure': tire_pressure,
        'lights': lights,
        'track_time': track_time,
        'lat': lat,
        'lon': lon,
        'ignition': ignition,
        'odometer': odometer,
        'direction': direction,
        'Gps_status': Gps_status,
        'Theft_Detection':Theft_Detection,
        'Fuel':Fuel,
        'Window':Window,
        'Accident':Accident

    })
    uploader = db.reference("CAN Data")
    uploader.update({
        'Speed_Wheel_Front_Right': Speed_Wheel_Front_Right,
        'Speed_Wheel_Front_Left': Speed_Wheel_Front_Left,
        'Vehicle_Speed': Vehicle_Speed,
        'Speed_Wheel_Rear_Left': Speed_Wheel_Rear_Left,
        'Speed_Wheel_Rear_Right': Speed_Wheel_Rear_Right,
        'Longitudinal_Acceleration': Longitudinal_Acceleration,
        'Transversal_Acceleration': Transversal_Acceleration,
        'Distance_Totalizer': Distance_Totalizer,
        'Engine_Coolant_Temperature': Engine_Coolant_Temperature,
        'Steering_Wheel_Angle': Steering_Wheel_Angle,
        'Steering_Wheel_Rotation_Speed': Steering_Wheel_Rotation_Speed,
        'Steering_Wheel_Angle_Offset': Steering_Wheel_Angle_Offset,
        'Engine_RPM': Engine_RPM,
        'Mean_Effective_Torque': Mean_Effective_Torque,
        'Raw_Sensor': Raw_Sensor,
        'Seat_Belt_Driver_Reminder': Seat_Belt_Driver_Reminder,
        'Seat_Belt_Front_Passenger_Reminder': Seat_Belt_Front_Passenger_Reminder,
        'Seat_Belt_2nd_Row_Center_Status': Seat_Belt_2nd_Row_Center_Status,
        'Seat_Belt_2nd_Row_Right_Status': Seat_Belt_2nd_Row_Right_Status,
        'Seat_Belt_2nd_Row_Left_Status': Seat_Belt_2nd_Row_Left_Status,
        'Parking_Brake': Parking_Brake,
        'Front_Left_Door_Warning': Front_Left_Door_Warning,
        'Front_Right_Door_Warning': Front_Right_Door_Warning,
        'Rear_Right_Door_Warning': Rear_Right_Door_Warning,
        'Boot_Door_Warning': Boot_Door_Warning,
        'Rear_Left_Door_Warning': Rear_Left_Door_Warning,
        'Driver_Door_Locked': Driver_Door_Locked,
        'Fuel_Low': Fuel_Low,
        'Low_Beam': Low_Beam,
        'High_Beam': High_Beam,
        'Warning_Lights': Warning_Lights,
        'ABS_Warning_Request': ABS_Warning_Request,
        'Battery_Warning': Battery_Warning,
        'internalbattvolts': internalbattvolts,
        'VehicleBatteryVoltage': VehicleBatteryVoltage,
    })
    uploader = db.reference("Head Unit Data")
    uploader.update({
        'waveband': waveband,
        'programme_type': programme_type,
        'Frequency_of_channel': Frequency_of_channel,
        'programme_identification': programme_identification,
        'stationName': stationName,
        'source': source,
        'Time_Spent_on_the_Channel': Time_Spent_on_the_Channel,
        'Start_time_on_Channel': Start_time_on_Channel,
        'End_time_on_Channel': End_time_on_Channel,
        'CategoryName': CategoryName,
        'AppName': AppName,
        'State': State,
        'BT_Connectivity_Status': BT_Connectivity_Status,
        'Time_BT_is_connected': Time_BT_is_connected,
        'Start_time_for_BT_connectivity': Start_time_for_BT_connectivity,
        'End_time_for_BT_connectivity': End_time_for_BT_connectivity,
        'key': key,
        'source_headUnit': source_headUnit,
        'direction_headUnit': direction_headUnit,
        'CategoryName_headUnit': CategoryName_headUnit,
        'AppName_headUnit': AppName_headUnit,
        'ScreenName': ScreenName,
        'KeyType': KeyType,
        'Action': Action,
    })


from nltk.stem.lancaster import LancasterStemmer

stemmer = LancasterStemmer()

cardata = open("car_data.json", 'r')
honda = cardata.read()
honda_data = json.loads(honda)

with open("voice data.json") as file:
    data = json.load(file)

try:
    with open("data.pickle", "rb") as f:
        words, labels, training, output = pickle.load(f)
except:
    words = []
    labels = []
    docs_x = []
    docs_y = []
    continuation = []

    for intent in data["intents"]:
        for pattern in intent["patterns"]:
            wrds = nltk.word_tokenize(pattern)
            words.extend(wrds)
            docs_x.append(wrds)
            docs_y.append(intent["tag"])

        if intent["tag"] not in labels:
            labels.append(intent["tag"])

    words = [stemmer.stem(w.lower()) for w in words if w != "?"]
    words = sorted(list(set(words)))

    labels = sorted(labels)

    training = []
    output = []

    out_empty = [0 for _ in range(len(labels))]

    for x, doc in enumerate(docs_x):
        bag = []

        wrds = [stemmer.stem(w.lower()) for w in doc]

        for w in words:
            if w in wrds:
                bag.append(1)
            else:
                bag.append(0)

        output_row = out_empty[:]
        output_row[labels.index(docs_y[x])] = 1

        training.append(bag)
        output.append(output_row)

    training = numpy.array(training)
    output = numpy.array(output)

    with open("../data.pickle", "wb") as f:
        pickle.dump((words, labels, training, output), f)

tensorflow.reset_default_graph()

net = tflearn.input_data(shape=[None, len(training[0])])
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, len(output[0]), activation="softmax")
net = tflearn.regression(net)

model = tflearn.DNN(net)

if os.path.exists("../model.tflearn.meta"):
    model.load("model.tflearn")
else:
    model.fit(training, output, n_epoch=1000, batch_size=8, show_metric=True)
    model.save("model.tflearn")


    def bag_of_words(s, words):
        bag = [0 for _ in range(len(words))]

        s_words = nltk.word_tokenize(s)
        s_words = [stemmer.stem(word.lower()) for word in s_words]

        for se in s_words:
            for i, w in enumerate(words):
                if w == se:
                    bag[i] = 1

        return numpy.array(bag)

cred = credentials.Certificate('firebase-json.json')

firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://my-ai-81afb.firebaseio.com/'
})


def bag_of_words(s, words):
    bag = [0 for _ in range(len(words))]

    s_words = nltk.word_tokenize(s)
    s_words = [stemmer.stem(word.lower()) for word in s_words]

    for se in s_words:
        for i, w in enumerate(words):
            if w == se:
                bag[i] = 1

    return numpy.array(bag)


dataset = open('carTestData.csv', encoding='utf-8-sig')
csv_data = csv.reader(dataset)
data_lines = list(csv_data)


class myClassC(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.daemon = True
        self.start()

    def run(self):
        messagereader()
def messagereader():
    ref2a = ''
    msgrefresh = db.reference("Realtime")
    msgrefresh.update({
        'Message': "",
        'Sender': ""
    })
    while True:
        nameofperson = db.reference('Realtime/Sender')
        messagerecieved = db.reference('Realtime/Message')
        aa = nameofperson.get()
        bb = messagerecieved.get()
        if bb != ref2a:
            replysound(aa + ", sent you a message," + bb)
            time.sleep(3)
            ref2a = bb

class myClassg(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.daemon = True
        self.start()

    def run(self):
        windowOpenDetection()

def windowOpenDetection():
    time.sleep(6)
    while True:
        fd = data_lines[1][7]
        fds = int(Window)
        if (fd == 0) and (fds == 1):
            spect = db.reference("Special_window")
            spect.update({
                'AlertWindow': "1"
            })
            time.sleep(100)

class accident(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.daemon = True
        self.start()

    def run(self):
        accidente()

def accidente():
    time.sleep(6)
    while True:
        fd = int(Accident)

        if fd == 1:
            acc = db.reference("Special_Accident")
            acc.update({
                'AlertWindow': "1"
            })
            time.sleep(100)




class myClassD(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.daemon = True
        self.start()

    def run(self):
        smsmessagereader()

def smsmessagereader():
    ref2b = ''
    msgrefresh = db.reference("SMS")
    msgrefresh.update({
        'SMS Message': "",
        'SMS Sender': ""
    })
    while True:
        nameofperson = db.reference('SMS/SMS Sender')
        messagerecieved = db.reference('SMS/SMS Message')
        aa = nameofperson.get()
        bb = messagerecieved.get()
        if bb != ref2b:
            replysound('You recieved an SMS, ' + bb)
            time.sleep(2)
            ref2b = bb

class myClassF(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.daemon = True
        self.start()
    def run(self):
        fuel()

def fuel():
    time.sleep(5)
    while True:
        fd = int(data_lines[1][71])
        if fd <= 5:
            replysound("Your car is running out of fuel. Please refuel as soon as possible")
            time.sleep(100)

class enginecoolang(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.daemon = True
        self.start()
    def run(self):
        enginecool()

def enginecool():
    time.sleep(5)
    while True:
        fd = int(data_lines[1][19])
        if fd >= 195:
            replysound("Your car's engine coolant temperature is too high. Please switch off the car for a while")
            time.sleep(100)

class battwarn(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.daemon = True
        self.start()
    def run(self):
        battwarnin()

def battwarnin():
    time.sleep(5)
    while True:
        fd = data_lines[1][43]
        if fd == 1:
            replysound("Your car battery is low. Please Take necessary Action")
            time.sleep(1000)

def BootDoorWarnign():
    time.sleep(5)
    while True:
        fd = data_lines[1][35]
        fdds= data_lines[1][7]
        if fd == 1 and fdds == 1:
            replysound("Your car Boot is open. Please close it")
            time.sleep(1000)
        elif fd == 1 and fdds == 0:
            spect = db.reference("Special")
            spect.update({
                'BootAlert': "1"
            })
            time.sleep(100)

class Sidedooropende(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.daemon = True
        self.start()
    def run(self):
        Sidedooropendet()

def Sidedooropendet():
    time.sleep(6)
    while True:
        time.sleep(6)
        fd = data_lines[1][7]
        fld = data_lines[1][32]
        frd = data_lines[1][33]
        rld = data_lines[1][36]
        rrd = data_lines[1][34]
        time.sleep(1)
        if (fd == 0) and (fld == 1):
            spect = db.reference("Special_fldw")
            spect.update({
                'frontleftdoorwarning': "1"
            })
        if (fd == 0) and (frd == 1):
            spect = db.reference("Special_frdw")
            spect.update({
                'frontrightdoorwarning': "1"
            })
        if (fd == 0) and (rld == 1):
            spect = db.reference("Special_rldw")
            spect.update({
                'rearleftdoorwarning': "1"
            })
        if (fd == 0) and (rrd == 1):
            spect = db.reference("Special_rrdw")
            spect.update({
                'rearrightdoorwarning': "1"
            })
        if (fd == 1) and (rrd == 1):
            replysound("Rear Right Door is not Closed Properly. Please close it")
        if (fd == 1) and (rld == 1):
            replysound("Rear Left Door is not Closed Properly. Please close it")
        if (fd == 1) and (frd == 1):
            replysound("Front Right Door is not Closed Properly. Please close it")
        if (fd == 1) and (fld == 1):
            replysound("Front Left Door is not Closed Properly. Please close it")


class seatbelt(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.daemon = True
        self.start()
    def run(self):
        seatb()

def seatb():
    time.sleep(5)
    while True:
        time.sleep(5)
        sbdr = data_lines[1][26]
        sbpr = data_lines[1][27]
        sb2rl = data_lines[1][30]
        sb2rr = data_lines[1][29]
        sb2rc = data_lines[1][28]
        ig = data_lines[1][7]
        if ig == 1 and sbdr == 1:
            replysound("Driver please connect your seatbelt")
        if ig == 1 and sbpr == 1:
            replysound("Front Passenger please connect your seatbelt")
        if ig == 1 and sb2rl == 1:
            replysound("Passenger at the left in second row, please connect your seatbelt")
        if ig == 1 and sb2rr == 1:
            replysound("Passenger at the right in second row, please connect your seatbelt")
        if ig == 1 and sb2rc == 1:
            replysound("Passenger at the center in second row, please connect your seatbelt")


class overspeed(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.daemon = True
        self.start()
    def run(self):
        oversp()

def oversp():
    time.sleep(5)
    while True:
        time.sleep(5)
        sssp = int(data_lines[1][0])
        if sssp >= 150:
            replysound("Please reduce the speed. You are going too fast")

class tirepress(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.daemon = True
        self.start()
    def run(self):
        tirepp()

def tirepp():
    time.sleep(5)
    while True:
        time.sleep(5)
        tprr = int(data_lines[1][2])
        if tprr <= 20:
            replysound("The tire pressure of the car is too low. Please fill up air immediately")



class myClassE(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.daemon = True
        self.start()

    def run(self):
        Phonereader(self)

def Phonereader(self):
    ref2c = ''
    phonereader = db.reference("My input")
    phonereader.update({
        'input': ""
    })
    while True:
        phonedata = db.reference('My input/input')
        language = db.reference('My input/lang')
        aa = phonedata.get()
        langbd = language.get()
        global PhoneResp
        if aa != ref2c:
            if langbd == "en":
                txt = recreatedChat(aa)
                PhoneResp = txt
                # self.result.emit(txt)
            else:
                txt = Exclude_English(aa, lang)
                PhoneResp = txt
                # self.result.emit(txt)
            # self.tedd.emit(PhoneResp)
            ref2c = aa


def AC():
    print('ac from switch case')


def vol_inc():
    print('volume increase from switch case')
    currentVolume = honda_data['volume']
    print(currentVolume + 5)


def vol_dec():
    print('volume decrease from switch case')


def lightson():
    try:
        data_lines[1][3] = 1
        writer = csv.writer(open('carTestData.csv', 'w', newline=''))
        writer.writerows(data_lines)
        replysound(rrr)
    except:
        print("please close the Excel file to update the value")


def speed():
    final = rrr + " " + speedOfVehicle
    replysound(final)


def enginetemp():
    fin = rrr + " " + engine_temp
    replysound(fin)

def lightsoff():
    try:
        data_lines[1][3] = 0
        writer = csv.writer(open('carTestData.csv', 'w', newline=''))
        writer.writerows(data_lines)
        replysound(rrr)
    except:
        print("please close the Excel file to update the value")

def fuellevel():
    try:
        fe = data_lines[1][71]
        replysound(rrr + fe)
    except:
        print("please close the Excel file to update the value")

def highbeam():
    try:
        data_lines[1][40] = 1
        data_lines[1][39] = 0
        writer = csv.writer(open('carTestData.csv', 'w', newline=''))
        writer.writerows(data_lines)
        replysound(rrr)
    except:
        print("please close the Excel file to update the value")

def lowbeam():
    try:
        data_lines[1][40] = 0
        data_lines[1][39] = 1
        writer = csv.writer(open('carTestData.csv', 'w', newline=''))
        writer.writerows(data_lines)
        replysound(rrr)
    except:
        print("please close the Excel file to update the value")

def parkingbreakon():
    try:
        data_lines[1][31] = 1
        writer = csv.writer(open('carTestData.csv', 'w', newline=''))
        writer.writerows(data_lines)
        replysound(rrr)
    except:
        print("please close the Excel file to update the value")

def parkingbreakoff():
    try:
        data_lines[1][31] = 0
        writer = csv.writer(open('carTestData.csv', 'w', newline=''))
        writer.writerows(data_lines)
        replysound(rrr)
    except:
        print("please close the Excel file to update the value")

def warninglightson():
    try:
        data_lines[1][41] = 1
        writer = csv.writer(open('carTestData.csv', 'w', newline=''))
        writer.writerows(data_lines)
        replysound(rrr)
    except:
        print("please close the Excel file to update the value")

def warninglightsoff():
    try:
        data_lines[1][41] = 0
        writer = csv.writer(open('carTestData.csv', 'w', newline=''))
        writer.writerows(data_lines)
        replysound(rrr)
    except:
        print("please close the Excel file to update the value")

def ignitionon():
    try:
        data_lines[1][7] = 1
        writer = csv.writer(open('carTestData.csv', 'w', newline=''))
        writer.writerows(data_lines)
        replysound(rrr)
    except:
        print("please close the Excel file to update the value")

def ignitionoff():
    try:
        data_lines[1][7] = 0
        writer = csv.writer(open('carTestData.csv', 'w', newline=''))
        writer.writerows(data_lines)
        replysound(rrr)
    except:
        print("please close the Excel file to update the value")

def windowshut():
    try:
        data_lines[1][72] = 0
        writer = csv.writer(open('carTestData.csv', 'w', newline=''))
        writer.writerows(data_lines)
        replysound(rrr)
    except:
        print("please close the Excel file to update the value")

def tirepresstell():
    try:
        pee = data_lines[1][2]
        replysound(rrr + pee)
    except:
        print("please close the Excel file to update the value")

def bluetoo():
    try:
        data_lines[1][58] = 1
        writer = csv.writer(open('carTestData.csv', 'w', newline=''))
        writer.writerows(data_lines)
        replysound(rrr)
    except:
        print("please close the Excel file to update the value")

def bluetoooff():
    try:
        data_lines[1][58] = 0
        writer = csv.writer(open('carTestData.csv', 'w', newline=''))
        writer.writerows(data_lines)
        replysound(rrr)
    except:
        print("please close the Excel file to update the value")

def fm():
    try:
        data_lines[1][46] = "FM"
        writer = csv.writer(open('carTestData.csv', 'w', newline=''))
        writer.writerows(data_lines)
        replysound(rrr)
    except:
        print("please close the Excel file to update the value")

def am():
    try:
        data_lines[1][46] = "AM"
        writer = csv.writer(open('carTestData.csv', 'w', newline=''))
        writer.writerows(data_lines)
        replysound(rrr)
    except:
        print("please close the Excel file to update the value")
def wb():
    try:
        data_lines[1][46] = "WB"
        writer = csv.writer(open('carTestData.csv', 'w', newline=''))
        writer.writerows(data_lines)
        replysound(rrr)
    except:
        print("please close the Excel file to update the value")

def news():
    try:
        data_lines[1][47] = "NEWS"
        writer = csv.writer(open('carTestData.csv', 'w', newline=''))
        writer.writerows(data_lines)
        replysound(rrr)
    except:
        print("please close the Excel file to update the value")
def public():
    try:
        data_lines[1][47] = "Public"
        writer = csv.writer(open('carTestData.csv', 'w', newline=''))
        writer.writerows(data_lines)
        replysound(rrr)
    except:
        print("please close the Excel file to update the value")

def whether():
    try:
        data_lines[1][47] = "Whether"
        writer = csv.writer(open('carTestData.csv', 'w', newline=''))
        writer.writerows(data_lines)
        replysound(rrr)
    except:
        print("please close the Excel file to update the value")

def emergency():
    try:
        data_lines[1][47] = "Emergency"
        writer = csv.writer(open('carTestData.csv', 'w', newline=''))
        writer.writerows(data_lines)
        replysound(rrr)
    except:
        print("please close the Excel file to update the value")

switch_case = {
    1: AC,
    2: vol_inc,
    3: vol_dec,
    4: lightson,
    5: speed,
    6: enginetemp,
    7: lightsoff,
    8: fuellevel,
    9: highbeam,
    10: lowbeam,
    11: parkingbreakon,
    12: parkingbreakoff,
    13: warninglightson,
    14: warninglightsoff,
    15: ignitionon,
    16: ignitionoff,
    17: windowshut,
    18: tirepresstell,
    19: bluetoo,
    20: bluetoooff,
    21: fm,
    22: am,
    23: wb,
    24: news,
    26: public,
    27: whether,
    28: emergency,
}

res = ""
def replysound(voice):
    print(voice)
    speak = gTTS(text=voice, lang='en', slow=False, lang_check=True)
    filename = "speaker.mp3"
    speak.save(filename)
    os.system("start  " + filename)
    # playsound.playsound(filename)
    global res
    res = str(voice)


    # displayer(microphone,AI_response,language)

    # Upload data to DB
    ref1 = db.reference('AI output')
    ref1.update({
        'output': voice
    })

    # ref2 = inp
    # displayer(ref, upload_response, language)

    return res


def recreatedChat(user_command):
    print("Got into AI")
    # ref2 = ''

    global rrr

    # Read input from DB
    # ref = db.reference('My input/input')

    results = model.predict([bag_of_words(user_command, words)])
    results_index = numpy.argmax(results)
    tag = labels[results_index]

    for tg in data["intents"]:
        if tg['tag'] == tag:
            responses = tg['response']
            domain = tag

    upload_response = random.choice(responses)
    print(upload_response)
    # replysound(upload_response,tag)
    rrr = upload_response

    switch_case[tag]()


def Exclude_English(user_command, lang):
    print("Got into translation section")
    # ref2 = ''

    # Read input from DB
    # ref = db.reference('My input/input')
    print(lang)
    trans_text = translator.translate(user_command, dest='en', src=lang)
    inp = trans_text.text

    results = model.predict([bag_of_words(inp, words)])
    results_index = numpy.argmax(results)
    tag = labels[results_index]

    for tg in data["intents"]:
        if tg['tag'] == tag:
            responses = tg['response']
            domain = tag

    upload_response = random.choice(responses)
    print(upload_response)
    global rrr
    rrr = upload_response
    switch_case[tag]()

class myClassB(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.daemon = True
        self.start()
    def run(self):
        gui()

def gui():
    class VoiceWorker(QtCore.QObject):
        textChanged = QtCore.pyqtSignal(str)
        result = QtCore.pyqtSignal(str)
        tedd = QtCore.pyqtSignal(str)

        @QtCore.pyqtSlot()
        def task(self):
            print(lang)
            import speech_recognition as sr
            r = sr.Recognizer()
            m = sr.Microphone()
            print("Speak")
            with m as source:
                audio = r.listen(source)
                print("recognizing")
                try:
                    value = r.recognize_google(audio, language=lang)

                    self.textChanged.emit(value)
                    print("You said: {}".format(value))

                    if lang == "en":
                        txt = recreatedChat(value)
                        self.result.emit(txt)
                    else:
                        txt = Exclude_English(value, lang)
                        self.result.emit(txt)

                    global res
                    self.tedd.emit(res)


                    # print(txt)
                except sr.UnknownValueError:
                    print("Oops")

    app = QtWidgets.QApplication(sys.argv)
    worker = VoiceWorker()
    thread = QtCore.QThread()
    thread.start()
    worker.moveToThread(thread)

    window = QtWidgets.QWidget()
    window.setGeometry(200, 200, 350, 400)
    window.setWindowTitle("DORIS Simulator")

    def retranslateUi(MainWindow):
        _translate = QtCore.QCoreApplication.translate
        english.setText(_translate("MainWindow", "English"))
        label.setText(_translate("MainWindow", "Select your language:"))
        french.setText(_translate("MainWindow", "French"))
        german.setText(_translate("MainWindow", "German"))
        spanish.setText(_translate("MainWindow", "Spanish"))
        japanese.setText(_translate("MainWindow", "Japanese"))
        chinese.setText(_translate("MainWindow", "Chinese"))
        russian.setText(_translate("MainWindow", "Russian"))
        arabic.setText(_translate("MainWindow", "Arabic"))
        hindi.setText(_translate("MainWindow", "Hindi"))
        malayalam.setText(_translate("MainWindow", "Malayalam"))
        marathi.setText(_translate("MainWindow", "Marathi"))
        tamil.setText(_translate("MainWindow", "Tamil"))
        telugu.setText(_translate("MainWindow", "Telugu"))
        urdu.setText(_translate("MainWindow", "Urdu"))
        bengali.setText(_translate("MainWindow", "Bengali"))
        gujarathi.setText(_translate("MainWindow", "Gujarati"))
        amharic.setText(_translate("MainWindow", "Amharic"))
        basque.setText(_translate("MainWindow", "Basque"))
        portuguese.setText(_translate("MainWindow", "Portuguese"))
        bulgarian.setText(_translate("MainWindow", "Bulgarian"))
        catalan.setText(_translate("MainWindow", "Catalan"))
        cherokee.setText(_translate("MainWindow", "Cherokee"))
        croatian.setText(_translate("MainWindow", "Croatian"))
        czech.setText(_translate("MainWindow", "Czech"))
        danish.setText(_translate("MainWindow", "Danish"))
        dutch.setText(_translate("MainWindow", "Dutch"))
        estonian.setText(_translate("MainWindow", "Estonian"))
        filipino.setText(_translate("MainWindow", "Filipino"))
        finnish.setText(_translate("MainWindow", "Finnish"))
        greek.setText(_translate("MainWindow", "Greek"))
        hebrew.setText(_translate("MainWindow", "Herbrew"))
        hungarian.setText(_translate("MainWindow", "Hungarian"))
        icelandic.setText(_translate("MainWindow", "Icelandic"))
        italian.setText(_translate("MainWindow", "Italian"))
        korean.setText(_translate("MainWindow", "Korean"))
        latvian.setText(_translate("MainWindow", "Latvian"))
        lithuanian.setText(_translate("MainWindow", "Lithuanian"))
        malay.setText(_translate("MainWindow", "Malay"))
        norwegian.setText(_translate("MainWindow", "Norwegian"))
        polish.setText(_translate("MainWindow", "Polish"))
        romanian.setText(_translate("MainWindow", "Romanian"))
        serbian.setText(_translate("MainWindow", "Serbian"))
        slovak.setText(_translate("MainWindow", "Slovak"))
        slovenian.setText(_translate("MainWindow", "Slovenian"))
        swahili.setText(_translate("MainWindow", "Swahili"))
        swedish.setText(_translate("MainWindow", "Swedish"))
        turkish.setText(_translate("MainWindow", "Turkish"))
        ukrainian.setText(_translate("MainWindow", "Ukrainian"))
        vietnamese.setText(_translate("MainWindow", "Vietnamese"))
        welsh.setText(_translate("MainWindow", "Welsh"))
        kannada.setText(_translate("MainWindow", "Kannada"))
        thai.setText(_translate("MainWindow", "Thai"))
        indonesian.setText(_translate("MainWindow", "Indonesian"))



    def englishL(selected):
        if selected:
            global lang
            lang = 'en'

    english = QtWidgets.QRadioButton(window)
    english.setGeometry(QtCore.QRect(85, 80, 95, 20))
    english.toggled.connect(englishL)

    def frenchL(selected):
        if selected:
            global lang
            lang = 'fr'

    french = QtWidgets.QRadioButton(window)
    french.setGeometry(QtCore.QRect(85, 110, 95, 20))
    french.toggled.connect(frenchL)

    def bulgarianL(selected):
        if selected:
            global lang
            lang = "bg"

    bulgarian = QtWidgets.QRadioButton(window)
    bulgarian.setGeometry(QtCore.QRect(85, 140, 95, 20))
    bulgarian.toggled.connect(bulgarianL)


    def spanishL(selected):
        if selected:
            global lang
            lang = 'es'

    spanish = QtWidgets.QRadioButton(window)
    spanish.setGeometry(QtCore.QRect(85, 170, 95, 20))
    spanish.toggled.connect(spanishL)

    def japaneseL(selected):
        if selected:
            global lang
            lang = "ja"

    japanese = QtWidgets.QRadioButton(window)
    japanese.setGeometry(QtCore.QRect(185, 80, 95, 20))
    japanese.toggled.connect(japaneseL)

    def chineseL(selected):
        if selected:
            global lang
            lang = 'zh-CN'

    chinese = QtWidgets.QRadioButton(window)
    chinese.setGeometry(QtCore.QRect(185, 110, 95, 20))
    chinese.toggled.connect(chineseL)

    def russianL(selected):
        if selected:
            global lang
            lang = 'ru'

    russian = QtWidgets.QRadioButton(window)
    russian.setGeometry(QtCore.QRect(185, 140, 95, 20))
    russian.toggled.connect(russianL)

    def arabicL(selected):
        if selected:
            global lang
            lang = "ar"

    arabic = QtWidgets.QRadioButton(window)
    arabic.setGeometry(QtCore.QRect(185, 170, 95, 20))
    arabic.toggled.connect(arabicL)

    def hindiL(selected):
        if selected:
            global lang
            lang = "hi"

    hindi = QtWidgets.QRadioButton(window)
    hindi.setGeometry(QtCore.QRect(285, 80, 95, 20))
    hindi.toggled.connect(hindiL)

    def malayalamL(selected):
        if selected:
            global lang
            lang = "ml"

    malayalam = QtWidgets.QRadioButton(window)
    malayalam.setGeometry(QtCore.QRect(285, 110, 95, 20))
    malayalam.toggled.connect(malayalamL)

    def marathiL(selected):
        if selected:
            global lang
            lang = "mr"

    marathi = QtWidgets.QRadioButton(window)
    marathi.setGeometry(QtCore.QRect(285, 140, 95, 20))
    marathi.toggled.connect(marathiL)

    def tamilL(selected):
        if selected:
            global lang
            lang = "ta"

    tamil = QtWidgets.QRadioButton(window)
    tamil.setGeometry(QtCore.QRect(285, 170, 95, 20))
    tamil.toggled.connect(tamilL)

    def teluguL(selected):
        if selected:
            global lang
            lang = "te"

    telugu = QtWidgets.QRadioButton(window)
    telugu.setGeometry(QtCore.QRect(385, 80, 95, 20))
    telugu.toggled.connect(teluguL)

    def urduL(selected):
        if selected:
            global lang
            lang = "ur"

    urdu = QtWidgets.QRadioButton(window)
    urdu.setGeometry(QtCore.QRect(385, 110, 95, 20))
    urdu.toggled.connect(urduL)

    def bengaliL(selected):
        if selected:
            global lang
            lang = "bn"

    bengali = QtWidgets.QRadioButton(window)
    bengali.setGeometry(QtCore.QRect(385, 140, 95, 20))
    bengali.toggled.connect(bengaliL)

    def gujaratiL(selected):
        if selected:
            global lang
            lang = "gu"

    gujarathi = QtWidgets.QRadioButton(window)
    gujarathi.setGeometry(QtCore.QRect(385, 170, 95, 20))
    gujarathi.toggled.connect(gujaratiL)

    def amharicL(selected):
        if selected:
            global lang
            lang = "am"

    amharic = QtWidgets.QRadioButton(window)
    amharic.setGeometry(QtCore.QRect(485, 80, 95, 20))
    amharic.toggled.connect(amharicL)

    def basqueL(selected):
        if selected:
            global lang
            lang = "eu"

    basque = QtWidgets.QRadioButton(window)
    basque.setGeometry(QtCore.QRect(485, 110, 95, 20))
    basque.toggled.connect(basqueL)

    def portugueseL(selected):
        if selected:
            global lang
            lang = "pt-PT"

    portuguese = QtWidgets.QRadioButton(window)
    portuguese.setGeometry(QtCore.QRect(485, 140, 95, 20))
    portuguese.toggled.connect(portugueseL)

    def germanL(selected):
        if selected:
            global lang
            lang = 'de'

    german = QtWidgets.QRadioButton(window)
    german.setGeometry(QtCore.QRect(485, 170, 95, 20))
    german.toggled.connect(germanL)

    def catalanL(selected):
        if selected:
            global lang
            lang = "ca"

    catalan = QtWidgets.QRadioButton(window)
    catalan.setGeometry(QtCore.QRect(585, 80, 95, 20))
    catalan.toggled.connect(catalanL)

    def cherokeeL(selected):
        if selected:
            global lang
            lang = "chr"

    cherokee = QtWidgets.QRadioButton(window)
    cherokee.setGeometry(QtCore.QRect(585, 110, 95, 20))
    cherokee.toggled.connect(cherokeeL)

    def croatianL(selected):
        if selected:
            global lang
            lang = "hr"

    croatian = QtWidgets.QRadioButton(window)
    croatian.setGeometry(QtCore.QRect(585, 140, 95, 20))
    croatian.toggled.connect(croatianL)

    def czechL(selected):
        if selected:
            global lang
            lang = "cs"

    czech = QtWidgets.QRadioButton(window)
    czech.setGeometry(QtCore.QRect(585, 170, 95, 20))
    czech.toggled.connect(czechL)

    def danishL(selected):
        if selected:
            global lang
            lang = "da"

    danish = QtWidgets.QRadioButton(window)
    danish.setGeometry(QtCore.QRect(685, 80, 95, 20))
    danish.toggled.connect(danishL)

    def dutchL(selected):
        if selected:
            global lang
            lang = "nl"

    dutch = QtWidgets.QRadioButton(window)
    dutch.setGeometry(QtCore.QRect(685, 110, 95, 20))
    dutch.toggled.connect(dutchL)

    def estonianL(selected):
        if selected:
            global lang
            lang = "et"

    estonian = QtWidgets.QRadioButton(window)
    estonian.setGeometry(QtCore.QRect(685, 140, 95, 20))
    estonian.toggled.connect(estonianL)

    def filipinoL(selected):
        if selected:
            global lang
            lang = "fil"

    filipino = QtWidgets.QRadioButton(window)
    filipino.setGeometry(QtCore.QRect(685, 170, 95, 20))
    filipino.toggled.connect(filipinoL)

    def finnishL(selected):
        if selected:
            global lang
            lang = "fi"

    finnish = QtWidgets.QRadioButton(window)
    finnish.setGeometry(QtCore.QRect(785, 80, 95, 20))
    finnish.toggled.connect(finnishL)

    def greekL(selected):
        if selected:
            global lang
            lang = "el"

    greek = QtWidgets.QRadioButton(window)
    greek.setGeometry(QtCore.QRect(785, 110, 95, 20))
    greek.toggled.connect(greekL)

    def hebrewL(selected):
        if selected:
            global lang
            lang = "iw"

    hebrew = QtWidgets.QRadioButton(window)
    hebrew.setGeometry(QtCore.QRect(785, 140, 95, 20))
    hebrew.toggled.connect(hebrewL)

    def hungarianL(selected):
        if selected:
            global lang
            lang = "hu"

    hungarian = QtWidgets.QRadioButton(window)
    hungarian.setGeometry(QtCore.QRect(785, 170, 95, 20))
    hungarian.toggled.connect(hungarianL)

    def icelandicL(selected):
        if selected:
            global lang
            lang = "is"

    icelandic = QtWidgets.QRadioButton(window)
    icelandic.setGeometry(QtCore.QRect(885, 80, 95, 20))
    icelandic.toggled.connect(icelandicL)

    def indonesianL(selected):
        if selected:
            global lang
            lang = "id"

    indonesian = QtWidgets.QRadioButton(window)
    indonesian.setGeometry(QtCore.QRect(885, 110, 95, 20))
    indonesian.toggled.connect(indonesianL)

    def italianL(selected):
        if selected:
            global lang
            lang = "it"

    italian = QtWidgets.QRadioButton(window)
    italian.setGeometry(QtCore.QRect(885, 140, 95, 20))
    italian.toggled.connect(italianL)

    def koreanL(selected):
        if selected:
            global lang
            lang = "ko"

    korean = QtWidgets.QRadioButton(window)
    korean.setGeometry(QtCore.QRect(885, 170, 95, 20))
    korean.toggled.connect(koreanL)

    def latvianL(selected):
        if selected:
            global lang
            lang = "lv"

    latvian = QtWidgets.QRadioButton(window)
    latvian.setGeometry(QtCore.QRect(985, 80, 95, 20))
    latvian.toggled.connect(latvianL)

    def lithuanianL(selected):
        if selected:
            global lang
            lang = "lt"

    lithuanian = QtWidgets.QRadioButton(window)
    lithuanian.setGeometry(QtCore.QRect(985, 110, 95, 20))
    lithuanian.toggled.connect(lithuanianL)

    def malayL(selected):
        if selected:
            global lang
            lang = "ms"

    malay = QtWidgets.QRadioButton(window)
    malay.setGeometry(QtCore.QRect(985, 140, 95, 20))
    malay.toggled.connect(malayL)

    def norwegianL(selected):
        if selected:
            global lang
            lang = "no"

    norwegian = QtWidgets.QRadioButton(window)
    norwegian.setGeometry(QtCore.QRect(985, 170, 95, 20))
    norwegian.toggled.connect(norwegianL)

    def polishL(selected):
        if selected:
            global lang
            lang = "pl"

    polish = QtWidgets.QRadioButton(window)
    polish.setGeometry(QtCore.QRect(1085, 80, 95, 20))
    polish.toggled.connect(polishL)

    def romanianL(selected):
        if selected:
            global lang
            lang = "ro"

    romanian = QtWidgets.QRadioButton(window)
    romanian.setGeometry(QtCore.QRect(1085, 110, 95, 20))
    romanian.toggled.connect(romanianL)

    def serbianL(selected):
        if selected:
            global lang
            lang = "sr"

    serbian = QtWidgets.QRadioButton(window)
    serbian.setGeometry(QtCore.QRect(1085, 140, 95, 20))
    serbian.toggled.connect(serbianL)

    def slovakL(selected):
        if selected:
            global lang
            lang = "sk"

    slovak = QtWidgets.QRadioButton(window)
    slovak.setGeometry(QtCore.QRect(1085, 170, 95, 20))
    slovak.toggled.connect(slovakL)

    def slovenianL(selected):
        if selected:
            global lang
            lang = "sl"

    slovenian = QtWidgets.QRadioButton(window)
    slovenian.setGeometry(QtCore.QRect(1185, 80, 95, 20))
    slovenian.toggled.connect(slovenianL)

    def swahiliL(selected):
        if selected:
            global lang
            lang = "sw"

    swahili = QtWidgets.QRadioButton(window)
    swahili.setGeometry(QtCore.QRect(1185, 110, 95, 20))
    swahili.toggled.connect(swahiliL)

    def swedishL(selected):
        if selected:
            global lang
            lang = "sv"

    swedish = QtWidgets.QRadioButton(window)
    swedish.setGeometry(QtCore.QRect(1185, 140, 95, 20))
    swedish.toggled.connect(swedishL)

    def thaiL(selected):
        if selected:
            global lang
            lang = "th"

    thai = QtWidgets.QRadioButton(window)
    thai.setGeometry(QtCore.QRect(1185, 170, 95, 20))
    thai.toggled.connect(thaiL)

    def turkishL(selected):
        if selected:
            global lang
            lang = "tr"

    turkish = QtWidgets.QRadioButton(window)
    turkish.setGeometry(QtCore.QRect(1285, 80, 95, 20))
    turkish.toggled.connect(turkishL)

    def ukrainianL(selected):
        if selected:
            global lang
            lang = "uk"

    ukrainian = QtWidgets.QRadioButton(window)
    ukrainian.setGeometry(QtCore.QRect(1285, 110, 95, 20))
    ukrainian.toggled.connect(ukrainianL)

    def vietnameseL(selected):
        if selected:
            global lang
            lang = "vi"

    vietnamese = QtWidgets.QRadioButton(window)
    vietnamese.setGeometry(QtCore.QRect(1285, 140, 95, 20))
    vietnamese.toggled.connect(vietnameseL)

    def welshL(selected):
        if selected:
            global lang
            lang = "cy"

    welsh = QtWidgets.QRadioButton(window)
    welsh.setGeometry(QtCore.QRect(1285, 170, 95, 20))
    welsh.toggled.connect(welshL)

    def kannadaL(selected):
        if selected:
            global lang
            lang = "kn"

    kannada = QtWidgets.QRadioButton(window)
    kannada.setGeometry(QtCore.QRect(1385, 170, 95, 20))
    kannada.toggled.connect(kannadaL)

    label = QtWidgets.QLabel(window)
    label.setGeometry(QtCore.QRect(50, 50, 211, 20))

    title_label = QtWidgets.QLabel(window)
    title_label.setText("DORIS AI")
    title_label.move(135, 10)
    title_label.setFont(QtGui.QFont("SansSerif", 15))

    programs_says = QtWidgets.QLabel(window)
    programs_says.setText("Command:")
    programs_says.move(50, 200)

    your_text = QtWidgets.QLabel(window)
    worker.textChanged.connect(your_text.setText)
    your_text.move(110, 200)
    your_text.resize(200, 30)
    your_text.setWordWrap(True)

    programs_Response = QtWidgets.QLabel(window)
    programs_Response.setText("Response:")
    programs_Response.move(50, 250)

    response_ = QtWidgets.QLabel(window)
    worker.tedd.connect(response_.setText)
    response_.move(110, 250)
    response_.resize(200, 30)
    response_.setWordWrap(True)

    start_button = QtWidgets.QPushButton("Start")
    close_button = QtWidgets.QPushButton("Close")

    v_box = QtWidgets.QVBoxLayout()
    v_box.addStretch()
    v_box.addWidget(start_button)
    v_box.addWidget(close_button)
    window.setLayout(v_box)
    start_button.clicked.connect(worker.task)
    close_button.clicked.connect(QtCore.QCoreApplication.instance().quit)
    retranslateUi(window)
    QtCore.QMetaObject.connectSlotsByName(window)
    window.show()
    sys.exit(app.exec())



Sharer()
myClassA()
myClassB()
myClassC()
enginecoolang()
overspeed()
seatbelt()
accident()
myClassD()
myClassE()
myClassF()
battwarn()
myClassg()
tirepress()
Sidedooropende()
BootDoorWarnign()

while True:
    pass

input()
