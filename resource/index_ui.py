# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'index.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1271, 955)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.Fathe_widget = QtWidgets.QWidget(Form)
        self.Fathe_widget.setStyleSheet("background-color: rgb(255, 170, 255);")
        self.Fathe_widget.setObjectName("Fathe_widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.Fathe_widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.up_widget = QtWidgets.QWidget(self.Fathe_widget)
        self.up_widget.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.up_widget.setObjectName("up_widget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.up_widget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.up_widget)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.verticalLayout.addWidget(self.up_widget)
        self.middle_widget = QtWidgets.QWidget(self.Fathe_widget)
        self.middle_widget.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.middle_widget.setObjectName("middle_widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.middle_widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget_12 = QtWidgets.QWidget(self.middle_widget)
        self.widget_12.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.widget_12.setObjectName("widget_12")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_12)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_mid_1_1 = QtWidgets.QWidget(self.widget_12)
        self.widget_mid_1_1.setStyleSheet("background-color: rgb(85, 170, 0);")
        self.widget_mid_1_1.setObjectName("widget_mid_1_1")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_mid_1_1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.widget = QtWidgets.QWidget(self.widget_mid_1_1)
        self.widget.setStyleSheet("background-color: rgb(170, 170, 127);")
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.horizontalLayout_4.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(self.widget_mid_1_1)
        self.widget_2.setStyleSheet("background-color: rgb(170, 170, 127);")
        self.widget_2.setObjectName("widget_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.widget_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.lineEdit_a = QtWidgets.QLineEdit(self.widget_2)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.lineEdit_a.setFont(font)
        self.lineEdit_a.setObjectName("lineEdit_a")
        self.gridLayout_4.addWidget(self.lineEdit_a, 0, 0, 1, 1)
        self.horizontalLayout_4.addWidget(self.widget_2)
        self.widget_3 = QtWidgets.QWidget(self.widget_mid_1_1)
        self.widget_3.setStyleSheet("background-color: rgb(170, 170, 127);")
        self.widget_3.setObjectName("widget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.pushButton = QtWidgets.QPushButton(self.widget_3)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_3.addWidget(self.pushButton, 0, 0, 1, 1)
        self.horizontalLayout_4.addWidget(self.widget_3)
        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 4)
        self.horizontalLayout_4.setStretch(2, 1)
        self.verticalLayout_2.addWidget(self.widget_mid_1_1)
        self.widget_mid_1_4 = QtWidgets.QWidget(self.widget_12)
        self.widget_mid_1_4.setStyleSheet("background-color: rgb(85, 170, 0);")
        self.widget_mid_1_4.setObjectName("widget_mid_1_4")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.widget_mid_1_4)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.widget_7 = QtWidgets.QWidget(self.widget_mid_1_4)
        self.widget_7.setStyleSheet("background-color: rgb(170, 255, 127);")
        self.widget_7.setObjectName("widget_7")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.widget_7)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_4 = QtWidgets.QLabel(self.widget_7)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_7.addWidget(self.label_4)
        self.lineEdit_key_a_col = QtWidgets.QLineEdit(self.widget_7)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.lineEdit_key_a_col.setFont(font)
        self.lineEdit_key_a_col.setObjectName("lineEdit_key_a_col")
        self.horizontalLayout_7.addWidget(self.lineEdit_key_a_col)
        self.horizontalLayout_11.addWidget(self.widget_7)
        self.verticalLayout_2.addWidget(self.widget_mid_1_4)
        self.widget_mid_1_5 = QtWidgets.QWidget(self.widget_12)
        self.widget_mid_1_5.setStyleSheet("background-color: rgb(85, 170, 0);")
        self.widget_mid_1_5.setObjectName("widget_mid_1_5")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.widget_mid_1_5)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.widget_8 = QtWidgets.QWidget(self.widget_mid_1_5)
        self.widget_8.setStyleSheet("background-color: rgb(170, 255, 127);")
        self.widget_8.setObjectName("widget_8")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.widget_8)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_5 = QtWidgets.QLabel(self.widget_8)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_8.addWidget(self.label_5)
        self.lineEdit_a_col = QtWidgets.QLineEdit(self.widget_8)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.lineEdit_a_col.setFont(font)
        self.lineEdit_a_col.setObjectName("lineEdit_a_col")
        self.horizontalLayout_8.addWidget(self.lineEdit_a_col)
        self.horizontalLayout_12.addWidget(self.widget_8)
        self.verticalLayout_2.addWidget(self.widget_mid_1_5)
        self.horizontalLayout.addWidget(self.widget_12)
        self.widget_13 = QtWidgets.QWidget(self.middle_widget)
        self.widget_13.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.widget_13.setObjectName("widget_13")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_13)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widget_mid_1_2 = QtWidgets.QWidget(self.widget_13)
        self.widget_mid_1_2.setStyleSheet("background-color: rgb(85, 170, 0);")
        self.widget_mid_1_2.setObjectName("widget_mid_1_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_mid_1_2)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.widget_6 = QtWidgets.QWidget(self.widget_mid_1_2)
        self.widget_6.setStyleSheet("background-color: rgb(170, 170, 127);")
        self.widget_6.setObjectName("widget_6")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.widget_6)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.label_3 = QtWidgets.QLabel(self.widget_6)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_9.addWidget(self.label_3, 0, 0, 1, 1)
        self.horizontalLayout_5.addWidget(self.widget_6)
        self.widget_5 = QtWidgets.QWidget(self.widget_mid_1_2)
        self.widget_5.setStyleSheet("background-color: rgb(170, 170, 127);")
        self.widget_5.setObjectName("widget_5")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.widget_5)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.lineEdit_b = QtWidgets.QLineEdit(self.widget_5)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.lineEdit_b.setFont(font)
        self.lineEdit_b.setObjectName("lineEdit_b")
        self.gridLayout_8.addWidget(self.lineEdit_b, 0, 0, 1, 1)
        self.horizontalLayout_5.addWidget(self.widget_5)
        self.widget_4 = QtWidgets.QWidget(self.widget_mid_1_2)
        self.widget_4.setStyleSheet("background-color: rgb(170, 170, 127);")
        self.widget_4.setObjectName("widget_4")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.widget_4)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.pushButton_3 = QtWidgets.QPushButton(self.widget_4)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_7.addWidget(self.pushButton_3, 0, 0, 1, 1)
        self.horizontalLayout_5.addWidget(self.widget_4)
        self.horizontalLayout_5.setStretch(0, 1)
        self.horizontalLayout_5.setStretch(2, 1)
        self.verticalLayout_3.addWidget(self.widget_mid_1_2)
        self.widget_mid_1_6 = QtWidgets.QWidget(self.widget_13)
        self.widget_mid_1_6.setStyleSheet("background-color: rgb(85, 170, 0);")
        self.widget_mid_1_6.setObjectName("widget_mid_1_6")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.widget_mid_1_6)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.widget_10 = QtWidgets.QWidget(self.widget_mid_1_6)
        self.widget_10.setStyleSheet("background-color: rgb(170, 255, 127);")
        self.widget_10.setObjectName("widget_10")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.widget_10)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_7 = QtWidgets.QLabel(self.widget_10)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_10.addWidget(self.label_7)
        self.lineEdit_key_b_col = QtWidgets.QLineEdit(self.widget_10)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.lineEdit_key_b_col.setFont(font)
        self.lineEdit_key_b_col.setObjectName("lineEdit_key_b_col")
        self.horizontalLayout_10.addWidget(self.lineEdit_key_b_col)
        self.horizontalLayout_13.addWidget(self.widget_10)
        self.verticalLayout_3.addWidget(self.widget_mid_1_6)
        self.widget_mid_1_7 = QtWidgets.QWidget(self.widget_13)
        self.widget_mid_1_7.setStyleSheet("background-color: rgb(85, 170, 0);")
        self.widget_mid_1_7.setObjectName("widget_mid_1_7")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.widget_mid_1_7)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.widget_9 = QtWidgets.QWidget(self.widget_mid_1_7)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.widget_9.setFont(font)
        self.widget_9.setStyleSheet("background-color: rgb(170, 255, 127);")
        self.widget_9.setObjectName("widget_9")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.widget_9)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_6 = QtWidgets.QLabel(self.widget_9)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_9.addWidget(self.label_6)
        self.lineEdit_b_col = QtWidgets.QLineEdit(self.widget_9)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.lineEdit_b_col.setFont(font)
        self.lineEdit_b_col.setObjectName("lineEdit_b_col")
        self.horizontalLayout_9.addWidget(self.lineEdit_b_col)
        self.horizontalLayout_14.addWidget(self.widget_9)
        self.verticalLayout_3.addWidget(self.widget_mid_1_7)
        self.horizontalLayout.addWidget(self.widget_13)
        self.verticalLayout.addWidget(self.middle_widget)
        self.down_widget = QtWidgets.QWidget(self.Fathe_widget)
        self.down_widget.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.down_widget.setObjectName("down_widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.down_widget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.down_widget)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_2.addWidget(self.pushButton_4)
        self.verticalLayout.addWidget(self.down_widget)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 6)
        self.verticalLayout.setStretch(2, 2)
        self.gridLayout.addWidget(self.Fathe_widget, 0, 0, 1, 1)

        self.retranslateUi(Form)
        self.pushButton_4.clicked.connect(Form.run_the_compare)
        self.lineEdit_b_col.textChanged['QString'].connect(Form.get_b_col)
        self.pushButton_3.clicked.connect(Form.select_b_file)
        self.lineEdit_a.textChanged['QString'].connect(Form.get_path_a)
        self.lineEdit_b.textChanged['QString'].connect(Form.get_path_b)
        self.pushButton.clicked.connect(Form.select_a_file)
        self.lineEdit_key_a_col.textChanged['QString'].connect(Form.get_key_a_col)
        self.lineEdit_a_col.textChanged['QString'].connect(Form.get_a_col)
        self.lineEdit_key_b_col.textChanged['QString'].connect(Form.get_key_b_col)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "工具集1.0"))
        self.label_2.setText(_translate("Form", "文件A:"))
        self.pushButton.setText(_translate("Form", "选择"))
        self.label_4.setText(_translate("Form", "A关键字列："))
        self.label_5.setText(_translate("Form", "A对比列:"))
        self.lineEdit_a_col.setPlaceholderText(_translate("Form", "空格隔开的列数"))
        self.label_3.setText(_translate("Form", "文件B:"))
        self.pushButton_3.setText(_translate("Form", "选择"))
        self.label_7.setText(_translate("Form", "B关键字列："))
        self.label_6.setText(_translate("Form", "B对比列:"))
        self.lineEdit_b_col.setPlaceholderText(_translate("Form", "空格隔开的列数"))
        self.pushButton_4.setText(_translate("Form", "执行"))
