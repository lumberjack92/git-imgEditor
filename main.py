from PyQt5.QtWidgets import QApplication, QDialog, QFileDialog, QMessageBox
from PyQt5 import QtGui, QtCore
import sys, interface
import cv2
import numpy as np

class Login(QDialog, interface.LoginWindow):
    imgPath = None
    image = None
    webImg = False
    loadImg = False

    def __init__(self):
        super(Login, self).__init__()
        self.autorization(self)
        self.btn_ok_add_1.clicked.connect(self.getFileName)
        self.btn_ok_add_2.clicked.connect(self.webCamImg)
        self.btn_ok_add_3.clicked.connect(self.lookBChannel)
        self.btn_ok_add_4.clicked.connect(self.lookGChannel)
        self.btn_ok_add_5.clicked.connect(self.lookRChannel)
        self.btn_ok_add_6.clicked.connect(self.blurImg)
        self.btn_ok_add_7.clicked.connect(self.grayImg)
        self.btn_ok_add_8.clicked.connect(self.rectangleImg)

    def getFileName(self):
        filename = None
        filename, _ = QFileDialog.getOpenFileName(self,
                             "Выбрать файл",
                             ".",
                             "JPEG Files(*.jpeg);;PNG Files(*.png)")
        self.webImg = False
        self.loadImg = True
        if filename != "":
            self.imgPath = filename
            self.image = cv2.imread(self.imgPath)
            self.selectImg(self.imgPath)

    def selectImg(self, img):
        self.pix = QtGui.QPixmap(img)
        self.pix = self.pix.scaled(self.label_img.size(), QtCore.Qt.KeepAspectRatio)
        self.label_img.setPixmap(self.pix)
        self.label_img.setAlignment(QtCore.Qt.AlignCenter)
        self.label_img.setMinimumSize(100, 100)
        self.unlockBtn()

    def unlockBtn(self):
        self.btn_ok_add_3.setEnabled(True)
        self.btn_ok_add_4.setEnabled(True)
        self.btn_ok_add_5.setEnabled(True)
        self.btn_ok_add_6.setEnabled(True)
        self.btn_ok_add_7.setEnabled(True)
        self.btn_ok_add_8.setEnabled(True)

    def setImg(self, img):
        height = img.shape[0]
        width = img.shape[1]
        if width > height :
            self.desired_width = 900
            self.aspect_ratio = self.desired_width / img.shape[1]
            self.height = int(self.aspect_ratio * img.shape[0])
            self.resized_image = cv2.resize(img, (self.desired_width, self.height))
        else:
            self.desired_height = 600
            self.aspect_ratio = self.desired_height / img.shape[0]
            self.width = int(self.aspect_ratio * img.shape[1])
            self.resized_image = cv2.resize(img, (self.width, self.desired_height))
        height = self.resized_image.shape[0]
        width = self.resized_image.shape[1]
        bytesPerLine = 3 * width
        cv2.cvtColor(self.resized_image, cv2.COLOR_BGR2RGB, self.resized_image)                                        
        self.QImg = QtGui.QImage(self.resized_image.data, width, height, bytesPerLine, QtGui.QImage.Format_RGB888)
        self.label_img.setPixmap(QtGui.QPixmap.fromImage(self.QImg))

    def lookBChannel(self):
        b, g, r = cv2.split(self.image)
        k = np.zeros_like(b)
        b = cv2.merge([b,k,k])
        self.setImg(b)
    
    def lookGChannel(self):
        b, g, r = cv2.split(self.image)
        k = np.zeros_like(b)
        g = cv2.merge([k,g,k])
        self.setImg(g)
    
    def lookRChannel(self):
        b, g, r = cv2.split(self.image)
        k = np.zeros_like(b)
        r = cv2.merge([k,k,r])
        self.setImg(r)
        
    def blurImg(self):
        valBlur = self.slider.value()
        if valBlur % 2 == 1:
            blurImg = cv2.medianBlur(self.image, valBlur)
        else:
            valBlur -= 1
            blurImg = cv2.medianBlur(self.image, valBlur)
        self.setImg(blurImg)

    def grayImg(self):
        gray_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        color_image = cv2.cvtColor(gray_image, cv2.COLOR_GRAY2RGB)
        self.setImg(color_image)
    
    def rectangleImg(self):
        cornerOneHor = self.input_1.text()
        cornerOneVert = self.input_2.text()
        cornerTwoHor = self.input_3.text()
        cornerTwoVert = self.input_4.text()
        height = self.image.shape[0]
        width = self.image.shape[1]
        try:
            if (int(cornerOneHor) <= width) and (int(cornerTwoHor) <= width)\
                and (int(cornerOneVert) <= height) and (int(cornerTwoVert) <= height):
                cv2.rectangle(self.image,(int(cornerOneHor),int(cornerOneVert)),(int(cornerTwoHor),int(cornerTwoVert)),(255,0,0),5)
                self.setImg(self.image)
            else:
                self.error_rectangle_val()
        except:
            self.error_rectangle()

    def error_rectangle(self):
        error_window = QMessageBox()
        self.error_window(error_window)
        error_window.setWindowTitle("Внимание!")
        error_window.setText("Введите корректные данные!")
        error_window.exec_()

    def error_rectangle_val(self):
        error_window = QMessageBox()
        self.error_window(error_window)
        error_window.setWindowTitle("Внимание!")
        error_window.setText("Данные больше изображения!")
        error_window.exec_()

    def webCamImg(self):
        cap = cv2.VideoCapture(0)
        while True:
            _, frame = cap.read()
            cv2.imshow('Enter S - save photo', frame)
            if cv2.waitKey(1) & 0xFF == ord('s'):
                _, self.imgPath = cap.read()
                self.image = self.imgPath
                self.setImg(self.imgPath)
                self.webImg = True
                self.loadImg = False
                self.unlockBtn()
                break
        cap.release()
        cv2.destroyAllWindows()

def login():
    app = QApplication(sys.argv)
    login = Login()
    login.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    login()