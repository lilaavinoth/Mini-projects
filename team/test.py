from PyQt5.QtWidgets import QApplication, QFileDialog
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.Qt import QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow
import time
import sys


app = QApplication([])
player = QMediaPlayer()
wgt_video = QVideoWidget()
wgt_video.show()
player.setVideoOutput(wgt_video)
player.setMedia(QMediaContent(QUrl.fromLocalFile('honda intro.avi')))
player.play()
time.sleep(5)
player.stop()
app.startingUp()