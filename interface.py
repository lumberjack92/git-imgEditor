from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QSlider

class LoginWindow(object):
    def autorization(self, Dialog):
        self.btnActive = False
        Dialog.setWindowTitle("Редактор изображений")
        Dialog.setWindowIcon(QtGui.QIcon('ico_med.png'))
        Dialog.setObjectName("Dialog")
        Dialog.setFixedSize(1200, 700)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_img = QtWidgets.QLabel(Dialog)
        self.label_img.setGeometry(QtCore.QRect(40, 20, 900, 600))
        self.label_img.setStyleSheet("background-color: rgb(255,255,255);")
        self.label_Title_Img = QtWidgets.QLabel(Dialog)
        self.label_Title_Img.setGeometry(QtCore.QRect(980, 20, 200, 30))
        self.label_Title_Img.setText("Загрузка изображений")
        self.label_Title_Img.setAlignment(QtCore.Qt.AlignCenter)
        self.btn_ok_add_1 = QtWidgets.QPushButton(Dialog)
        self.btn_ok_add_1.setGeometry(QtCore.QRect(980, 50, 200, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_ok_add_1.setFont(font)
        self.btn_ok_add_1.setText("Загрузить изображение")
        self.btn_ok_add_1.setObjectName("btn_ok_add_1")
        self.btn_ok_add_2 = QtWidgets.QPushButton(Dialog)
        self.btn_ok_add_2.setGeometry(QtCore.QRect(980, 80, 200, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_ok_add_2.setFont(font)
        self.btn_ok_add_2.setText("Сделать фото с веб-камеры")
        self.btn_ok_add_2.setObjectName("btn_ok_add_2")
        self.label_Title_operation = QtWidgets.QLabel(Dialog)
        self.label_Title_operation.setGeometry(QtCore.QRect(980, 110, 200, 30))
        self.label_Title_operation.setText("Операции с изображением")
        self.label_Title_operation.setAlignment(QtCore.Qt.AlignCenter)
        self.btn_ok_add_3 = QtWidgets.QPushButton(Dialog)
        self.btn_ok_add_3.setGeometry(QtCore.QRect(980, 140, 200, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_ok_add_3.setEnabled(False)
        self.btn_ok_add_3.setFont(font)
        self.btn_ok_add_3.setText("Изображение в синем канале")
        self.btn_ok_add_3.setObjectName("btn_ok_add_3")
        self.btn_ok_add_4 = QtWidgets.QPushButton(Dialog)
        self.btn_ok_add_4.setGeometry(QtCore.QRect(980, 170, 200, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_ok_add_4.setEnabled(False)
        self.btn_ok_add_4.setFont(font)
        self.btn_ok_add_4.setText("Изображение в зеленом канале")
        self.btn_ok_add_4.setObjectName("btn_ok_add_4")
        self.btn_ok_add_5 = QtWidgets.QPushButton(Dialog)
        self.btn_ok_add_5.setGeometry(QtCore.QRect(980, 200, 200, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_ok_add_5.setEnabled(False)
        self.btn_ok_add_5.setFont(font)
        self.btn_ok_add_5.setText("Изображение в красном канале")
        self.btn_ok_add_5.setObjectName("btn_ok_add_5")
        self.btn_ok_add_6 = QtWidgets.QPushButton(Dialog)
        self.btn_ok_add_6.setGeometry(QtCore.QRect(980, 230, 200, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_ok_add_6.setEnabled(False)
        self.btn_ok_add_6.setText('Блюр изображения:')
        self.btn_ok_add_6.setFont(font)
        self.btn_ok_add_6.setObjectName("btn_ok_add_4")

        self.slider = QSlider(Dialog) 
        self.slider.setGeometry(QtCore.QRect(980, 265, 200, 20)) 
        self.slider.setOrientation(QtCore.Qt.Horizontal)
        self.slider.setTickPosition(QSlider.TicksAbove)
        self.slider.setTickInterval(2)
        self.slider.setRange(3, 55)
        self.slider.setValue(3)
        self.slider.setSingleStep(2)
        self.slider.valueChanged[int].connect(self.changeValue)

        self.btn_ok_add_7 = QtWidgets.QPushButton(Dialog)
        self.btn_ok_add_7.setGeometry(QtCore.QRect(980, 290, 200, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_ok_add_7.setEnabled(False)
        self.btn_ok_add_7.setFont(font)
        self.btn_ok_add_7.setText("Изображение в оттенках серого")
        self.btn_ok_add_7.setObjectName("btn_ok_add_4")
        self.btn_ok_add_8 = QtWidgets.QPushButton(Dialog)
        self.btn_ok_add_8.setGeometry(QtCore.QRect(980, 320, 200, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_ok_add_8.setEnabled(False)
        self.btn_ok_add_8.setFont(font)
        self.btn_ok_add_8.setText("Синий прямоугольника")
        self.btn_ok_add_8.setObjectName("btn_ok_add_4")

        self.label_Title_rectangle = QtWidgets.QLabel(Dialog)
        self.label_Title_rectangle.setGeometry(QtCore.QRect(980, 350, 200, 30))
        self.label_Title_rectangle.setText("Координаты прямоугольника (px)")
        self.label_Title_rectangle.setAlignment(QtCore.Qt.AlignCenter)

        self.label_rectangle_left_up = QtWidgets.QLabel(Dialog)
        self.label_rectangle_left_up.setGeometry(QtCore.QRect(980, 365, 200, 30))
        self.label_rectangle_left_up.setText("Первая вершина")
        self.label_rectangle_left_up.setAlignment(QtCore.Qt.AlignCenter)

        self.label_rectangle_left_up_hor = QtWidgets.QLabel(Dialog)
        self.label_rectangle_left_up_hor.setGeometry(QtCore.QRect(980, 380, 90, 30))
        self.label_rectangle_left_up_hor.setText("По горизонтали")
        self.label_rectangle_left_up_hor.setAlignment(QtCore.Qt.AlignCenter)

        self.input_1 = QtWidgets.QLineEdit(Dialog)
        self.input_1.setGeometry(QtCore.QRect(980, 410, 90, 20))

        self.label_rectangle_left_up_vert = QtWidgets.QLabel(Dialog)
        self.label_rectangle_left_up_vert.setGeometry(QtCore.QRect(1090, 380, 90, 30))
        self.label_rectangle_left_up_vert.setText("По вертикали")
        self.label_rectangle_left_up_vert.setAlignment(QtCore.Qt.AlignCenter)

        self.input_2 = QtWidgets.QLineEdit(Dialog)
        self.input_2.setGeometry(QtCore.QRect(1090, 410, 90, 20))

        self.label_rectangle_right_bottom = QtWidgets.QLabel(Dialog)
        self.label_rectangle_right_bottom.setGeometry(QtCore.QRect(980, 425, 200, 30))
        self.label_rectangle_right_bottom.setText("Противоположная вершина")
        self.label_rectangle_right_bottom.setAlignment(QtCore.Qt.AlignCenter)

        self.label_rectangle_right_bottom_hor = QtWidgets.QLabel(Dialog)
        self.label_rectangle_right_bottom_hor.setGeometry(QtCore.QRect(980, 440, 90, 30))
        self.label_rectangle_right_bottom_hor.setText("По горизонтали")
        self.label_rectangle_right_bottom_hor.setAlignment(QtCore.Qt.AlignCenter)

        self.input_3 = QtWidgets.QLineEdit(Dialog)
        self.input_3.setGeometry(QtCore.QRect(980, 470, 90, 20))

        self.label_rectangle_right_bottom_vert = QtWidgets.QLabel(Dialog)
        self.label_rectangle_right_bottom_vert.setGeometry(QtCore.QRect(1090, 440, 90, 30))
        self.label_rectangle_right_bottom_vert.setText("По вертикали")
        self.label_rectangle_right_bottom_vert.setAlignment(QtCore.Qt.AlignCenter)

        self.input_4 = QtWidgets.QLineEdit(Dialog)
        self.input_4.setGeometry(QtCore.QRect(1090, 470, 90, 20))

    def changeValue(self, value):
        self.btn_ok_add_6.setText(f'Блюр изображения: {value}')

    def error_window(self, Error):
        Error.setWindowTitle("Ошибка")
        Error.setObjectName("error_window")