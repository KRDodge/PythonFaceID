import FaceIDPython.DetectFaceID as Detector
import FaceIDPython.LearnFaceID as Learner
import FaceIDPython.RecognizeFaceID as Recognizer

import os
import cv2
import sys
import numpy as np
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5 import QtGui
from PyQt5.QtCore import *

form_class = uic.loadUiType("MainView.ui")[0]

class GetImage:
    def CutImage(path):
        img_array = np.fromfile(path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        height, width, channels = img.shape
        if(width > 1250):
            resize = 1250 / width
            img = cv2.resize(img, dsize=None, fx=resize, fy=resize)
        if(height > 800):
            resize = 800 / height
            img = cv2.resize(img, dsize=None, fx=resize, fy=resize)
        return img

class MainView(QWidget, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.FileDialogButton.clicked.connect(self.FileDialogButton_clicked)
        self.LearnButton.clicked.connect(self.LearnButton_clicked)
        self.DetectButton.clicked.connect(self.DetectButton_clicked)
        self.TestButton.clicked.connect(self.TestButton_clicked)


    def FileDialogButton_clicked(self):
        file = QFileDialog.getOpenFileName(
            self,
            "Select 7z or image files to open",
            os.getcwd(),
            "files (*.7z *.png *.bmp *.jpg)")[0]
        if(file == ''):
            print('No Path')
            return

        self.FilePathLineEdit.setText(file)
        img = GetImage.CutImage(file)
        img = Detector.DetectFaceID.imageShower(img)
        h,w,c = img.shape
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        qImg = QtGui.QImage(img.data, w, h, w * c, QtGui.QImage.Format_RGB888)
        pixmap = QtGui.QPixmap.fromImage(qImg)
        self.ImageLabel.setPixmap(pixmap)


    def LearnButton_clicked(self):
        id = self.IDLineEdit.text()
        if(id == ''):
            print('No Path or ID')
            return

        Learner.LearnFaceID.learnImage(id)


    def TestButton_clicked(self):
        id = self.IDLineEdit.text()
        file = self.FilePathLineEdit.text()
        if (file == '' or id == ''):
            print('No Path or ID')
            return

        yml = "ymldata/" + str(id) + '.yml'
        if os.path.isfile(yml) == False:
            print('false')
            return

        img = GetImage.CutImage(file)
        img, result = Recognizer.RecognizeFaceID.recognizeFaceByImage(img,id)

        print(result)

        h, w, c = img.shape
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        qImg = QtGui.QImage(img.data, w, h, w * c, QtGui.QImage.Format_RGB888)
        pixmap = QtGui.QPixmap.fromImage(qImg)
        self.ImageLabel.setPixmap(pixmap)


    def DetectButton_clicked(self):
        file = self.FilePathLineEdit.text()
        id = self.IDLineEdit.text()
        if (file == '' or id == ''):
            print('No Path or ID')
            return

        img = GetImage.CutImage(file)
        img = Detector.DetectFaceID.imageDetctor(img, id)

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    window = MainView()
    window.show()
    app.exec_()

