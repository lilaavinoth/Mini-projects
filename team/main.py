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

global vinoth

import sys
from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from PyQt5.QtWidgets import QMessageBox


def recreatedChat(voice_input):
    print("Got into AI")
    ref2 = ''
    while True:
        # Read input from DB
        # ref = db.reference('My input/input')
        # with sr.Microphone() as source:
        #     print('Speak')
        #     audio = r.listen(source)
        #     # r.adjust_for_ambient_noise(source)
        #     text = r.recognize_google(audio)
        #     ref = text
        #     print(ref)
        ref = voice_input

        ref1 = ref

        if ref2 != voice_input:
            translator = Translator()
            trans_text = translator.translate(ref1)
            inp = trans_text.text

            # inp = ref
            if inp.lower() == "quit":
                break

            results = model.predict([bag_of_words(inp, words)])
            results_index = numpy.argmax(results)
            tag = labels[results_index]

            for tg in data["intents"]:
                if tg['tag'] == tag:
                    responses = tg['response']

            upload_response = random.choice(responses)
            print(upload_response)
            res = str(upload_response)
            # update_label(res)

            # Upload data to DB
            ref = db.reference('AI output')
            ref.update({
                'output': upload_response
            })

        ref2 = voice_input

        print("AI code ended")
        return res


def gui():
    txt = ''
    txtt = ''

    class VoiceWorker(QtCore.QObject):
        textChanged = QtCore.pyqtSignal(str)

        @QtCore.pyqtSlot()
        def task(self):
            import speech_recognition as sr
            r = sr.Recognizer()
            m = sr.Microphone()

            print("Speak")
            with m as source:
                audio = r.listen(source)
                print("recognizing")
                try:
                    value = r.recognize_google(audio)
                    self.textChanged.emit(value)
                    print("You said: {}".format(value))
                    res = recreatedChat(value)
                    msg = QMessageBox()
                    msg.setWindowTitle("Response")
                    msg.setText(res)
                    x = msg.exec_()
                except sr.UnknownValueError:
                    print("Oops")

    app = QtWidgets.QApplication(sys.argv)

    worker = VoiceWorker()
    thread = QtCore.QThread()
    thread.start()
    worker.moveToThread(thread)

    window = QtWidgets.QWidget()
    window.setGeometry(200, 200, 350, 400)
    window.setWindowTitle("Assistant")

    title_label = QtWidgets.QLabel(window)
    title_label.setText("Assistant")
    title_label.move(135, 10)
    title_label.setFont(QtGui.QFont("SansSerif", 15))

    you_said = QtWidgets.QLabel(window)
    you_said.move(25, 100)

    programs_says = QtWidgets.QLabel(window)
    programs_says.setText("Command:")
    programs_says.move(50, 150)

    your_text = QtWidgets.QLabel(window)
    worker.textChanged.connect(your_text.setText)
    your_text.move(110, 150)
    your_text.resize(200, 30)
    your_text.setWordWrap(True)

    # programs_Response = QtWidgets.QLabel(window)
    # programs_Response.setText("Response:")
    # programs_Response.move(50, 200)

    # response_ = QtWidgets.QLabel(window)
    # response_.setText(txt)
    # response_.move(110, 200)
    # response_.resize(200, 30)
    # response_.setWordWrap(True)

    start_button = QtWidgets.QPushButton("Start")
    close_button = QtWidgets.QPushButton("Close")

    v_box = QtWidgets.QVBoxLayout()
    v_box.addStretch()
    v_box.addWidget(start_button)
    v_box.addWidget(close_button)
    window.setLayout(v_box)

    start_button.clicked.connect(worker.task)
    close_button.clicked.connect(QtCore.QCoreApplication.instance().quit)
    window.show()
    sys.exit(app.exec())


os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

translator = Translator()
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


# recreatedChat()
gui()
