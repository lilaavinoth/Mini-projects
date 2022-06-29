import sys
import os
import subprocess
import time
from subprocess import *
from PyQt5.QtWidgets import (QLabel, QRadioButton, QPushButton, QVBoxLayout, QApplication, QWidget)


class basicRadiobuttonExample(QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.label = QLabel('Select Interface:')
        self.rbtn1 = QRadioButton('Phone')
        self.rbtn2 = QRadioButton('Car')
        self.label2 = QLabel("")

        self.rbtn1.toggled.connect(self.onClicked)
        self.rbtn2.toggled.connect(self.onClicked)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.rbtn1)
        layout.addWidget(self.rbtn2)
        layout.addWidget(self.label2)

        self.setGeometry(200, 200, 300, 150)

        self.setLayout(layout)
        self.setWindowTitle('PyQt5')

        self.show()

    def onClicked(self):
        radioBtn = self.sender()
        if radioBtn.isChecked():
            # self.label2.setText("You selected " + radioBtn.text())
            if radioBtn.text() == "Phone":
                os.system('python phone.py')
            else:
                # os.system('python car.py' )
                # os.system('python Car_AI.py')

                subprocess.run("python Without_GUI.py & python RealTime.py & python Sharer.py", shell=True)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = basicRadiobuttonExample()
    sys.exit(app.exec())
