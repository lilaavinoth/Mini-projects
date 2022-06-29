print("Car Interface Activated")
import sys
import Car_AI
from PyQt5 import QtCore, QtGui, QtWidgets, Qt

import speech_recognition as sr


class VoiceWorker(QtCore.QObject):
    textChanged = QtCore.pyqtSignal(str)


    @QtCore.pyqtSlot()
    def task(self):

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
                Car_AI.recreatedChat(value)

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
title_label.move(135,10)
title_label.setFont(QtGui.QFont("SansSerif", 15))

you_said = QtWidgets.QLabel(window)
you_said.move(25,100)

programs_says = QtWidgets.QLabel(window)
programs_says.setText("Command:")
programs_says.move(50,150)

your_text = QtWidgets.QLabel(window)
worker.textChanged.connect(your_text.setText)
your_text.move(110,150)
your_text.resize(200,30)
your_text.setWordWrap(True)

programs_Response = QtWidgets.QLabel(window)
programs_Response.setText("Response:")
programs_Response.move(50,200)

response_ =  QtWidgets.QLabel(window)
worker.textChanged.connect(response_.setText)

response_.move(110,200)
response_.resize(200,30)
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
window.show()
sys.exit(app.exec())

gui