import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot


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
        ui = displayer()
        ui.setupUi(MainWindow2)
        MainWindow2.show()
        sys.exit(app.exec_())


displayer("enciende el aire acondicionado","Air conditioner turned on","es")