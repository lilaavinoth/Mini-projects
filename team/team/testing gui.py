import sys
from PyQt5 import QtCore, QtGui, QtWidgets
global lang

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

        def frenchSelected(self, selected):
            if selected:
                lang = 'fr'

        def germanSelected(self, selected):
            if selected:
                lang = 'de'

        def spanishSelected(self, selected):
            if selected:
                lang = 'es'

        def japaneseSelected(self, selected):
            if selected:
                lang = 'ja'

        def chineseSelected(self, selected):
            if selected:
                lang = 'zh-CN'

        def russianSelected(self, selected):
            if selected:
                lang = 'ru'


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


        # Driver Code


    if __name__ == "__main__":
        app = QtWidgets.QApplication(sys.argv)

        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())

window()