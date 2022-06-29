# pip install tensorflow==1.2
# pip install numpy==1.14.2
# pip install tflearn
# pip install windows-curses
# pip install nltk
# nltk.download('punkt')
# pip install firebase-admin
# pip install json
# pip install keyboard


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
import speech_recognition as sr
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import time

translator = Translator()

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

from nltk.stem.lancaster import LancasterStemmer

stemmer = LancasterStemmer()

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


def window():
    class Ui_MainWindow(object):
        def setupUi(self, MainWindow):
            MainWindow.setObjectName("Language Select")
            MainWindow.resize(466, 299)
            self.centralwidget = QtWidgets.QWidget(MainWindow)

            # Radio button for english
            self.radioButton_english = QtWidgets.QRadioButton(self.centralwidget)
            self.radioButton_english.setGeometry(QtCore.QRect(30, 40, 95, 20))
            self.radioButton_english.toggled.connect(self.englishSelected)

            # Radio button for french
            self.radioButton_french = QtWidgets.QRadioButton(self.centralwidget)
            self.radioButton_french.setGeometry(QtCore.QRect(30, 70, 95, 20))
            self.radioButton_french.toggled.connect(self.frenchSelected)

            # Radio button for german
            self.german = QtWidgets.QRadioButton(self.centralwidget)
            self.german.setGeometry(QtCore.QRect(30, 100, 95, 20))
            self.german.toggled.connect(self.germanSelected)

            # Radio button for spanish
            self.spanish = QtWidgets.QRadioButton(self.centralwidget)
            self.spanish.setGeometry(QtCore.QRect(30, 130, 95, 20))
            self.spanish.toggled.connect(self.spanishSelected)

            # Radio button for japanese
            self.japanese = QtWidgets.QRadioButton(self.centralwidget)
            self.japanese.setGeometry(QtCore.QRect(30, 160, 95, 20))
            self.japanese.toggled.connect(self.japaneseSelected)

            # Radio button for chinese
            self.chinese = QtWidgets.QRadioButton(self.centralwidget)
            self.chinese.setGeometry(QtCore.QRect(30, 190, 95, 20))
            self.chinese.toggled.connect(self.chineseSelected)

            # Radio button for russian
            self.russian = QtWidgets.QRadioButton(self.centralwidget)
            self.russian.setGeometry(QtCore.QRect(30, 220, 95, 20))
            self.russian.toggled.connect(self.russianSelected)

            self.label = QtWidgets.QLabel(self.centralwidget)
            self.label.setGeometry(QtCore.QRect(170, 10, 211, 20))
            MainWindow.setCentralWidget(self.centralwidget)

            self.retranslateUi(MainWindow)
            QtCore.QMetaObject.connectSlotsByName(MainWindow)

        def englishSelected(self, selected):
            if selected:
                lang = 'en'
                MainWindow.close()
                recreatedChat(lang)

        def frenchSelected(self, selected):
            if selected:
                lang = 'fr'
                MainWindow.close()
                recreatedChat(lang)

        def germanSelected(self, selected):
            if selected:
                lang = 'de'
                MainWindow.close()
                recreatedChat(lang)

        def spanishSelected(self, selected):
            if selected:
                lang = 'es'
                MainWindow.close()
                recreatedChat(lang)

        def japaneseSelected(self, selected):
            if selected:
                lang = 'ja'
                MainWindow.close()
                recreatedChat(lang)

        def chineseSelected(self, selected):
            if selected:
                lang = 'zh-CN'
                MainWindow.close()
                recreatedChat(lang)

        def russianSelected(self, selected):
            if selected:
                lang = 'ru'
                MainWindow.close()
                recreatedChat(lang)

        def retranslateUi(self, MainWindow):
            _translate = QtCore.QCoreApplication.translate

            MainWindow.setWindowTitle(_translate("MainWindow", "Language Select"))
            self.radioButton_english.setText(_translate("MainWindow", "English"))
            self.label.setText(_translate("MainWindow", "Select your language:"))
            self.radioButton_french.setText(_translate("MainWindow", "French"))
            self.german.setText(_translate("MainWindow", "German"))
            self.spanish.setText(_translate("MainWindow", "Spanish"))
            self.japanese.setText(_translate("MainWindow", "Japanese"))
            self.chinese.setText(_translate("MainWindow", "Chinese"))
            self.russian.setText(_translate("MainWindow", "Russian"))

    if __name__ == "__main__":
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())


def recreatedChat(language):
    print("Got into AI")
    # ref2 = ''

    # Read input from DB
    # ref = db.reference('My input/input')
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Speak')

        audio = r.listen(source)
        r.adjust_for_ambient_noise(source)
        text = r.recognize_google(audio, language=language)
        ref = text
        print(ref)


        # if ref2 != ref:
        trans_text = translator.translate(ref)
        inp = trans_text.text

        # if inp.lower() == "quit":
        #     break

        results = model.predict([bag_of_words(inp, words)])
        results_index = numpy.argmax(results)
        tag = labels[results_index]

        for tg in data["intents"]:
            if tg['tag'] == tag:
                responses = tg['response']

        upload_response = random.choice(responses)
        print(upload_response)



        # displayer(microphone,AI_response,language)

        # Upload data to DB
        ref1 = db.reference('AI output')
        ref1.update({
            'output': upload_response
        })

        # ref2 = inp
        displayer(ref, upload_response, language)


def displayer(deeeww, ai_respinse, lange):
    class displayer(object):
        print("recieve: {}".format(deeeww))
        print("ai response= {}".format(ai_respinse))
        print("language: {}".format(lange))

        def clicker(self):
            # recreatedChat(lange)
            print("win")

        def setupUi(self, MainWindow2):
            MainWindow2.setObjectName("MainWindow")
            MainWindow2.resize(466, 299)
            self.centralwidget = QtWidgets.QWidget(MainWindow2)

            self.butt = QtWidgets.QPushButton(MainWindow2)
            self.butt.setText("Give Command")
            self.butt.clicked.connect(self.clicker)

            self.label1 = QtWidgets.QLabel(self.centralwidget)
            self.label1.setGeometry(QtCore.QRect(170, 90, 211, 20))
            MainWindow2.setCentralWidget(self.centralwidget)

            self.label2 = QtWidgets.QLabel(self.centralwidget)
            self.label2.setGeometry(QtCore.QRect(170, 120, 211, 20))
            MainWindow2.setCentralWidget(self.centralwidget)

            self.retranslateUi(MainWindow2)
            QtCore.QMetaObject.connectSlotsByName(MainWindow2)

        def retranslateUi(self, MainWindow2):
            _translate = QtCore.QCoreApplication.translate
            MainWindow2.setWindowTitle(_translate("MainWindow", "Response"))
            self.label1.setText(_translate("MainWindow", deeeww))
            self.label2.setText(_translate("MainWindow", ai_respinse))

    if __name__ == "__main__":
        app = QtWidgets.QApplication(sys.argv)
        MainWindow2 = QtWidgets.QMainWindow()
        ui1 = displayer()
        ui1.setupUi(MainWindow2)
        MainWindow2.show()
        time.sleep(10)
        sys.exit(app.exec_())


window()
