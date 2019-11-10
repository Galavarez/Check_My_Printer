# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(497, 244)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/img/printer.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 301, 201))
        self.groupBox.setObjectName("groupBox")
        self.listWidget_2 = QtWidgets.QListWidget(self.groupBox)
        self.listWidget_2.setGeometry(QtCore.QRect(10, 20, 281, 171))
        self.listWidget_2.setObjectName("listWidget_2")
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(320, 10, 161, 201))
        self.groupBox_2.setObjectName("groupBox_2")
        self.button_nozzle_check = QtWidgets.QPushButton(self.groupBox_2)
        self.button_nozzle_check.setGeometry(QtCore.QRect(10, 20, 141, 51))
        self.button_nozzle_check.setObjectName("button_nozzle_check")
        self.button_head_cleaning_normal = QtWidgets.QPushButton(self.groupBox_2)
        self.button_head_cleaning_normal.setGeometry(QtCore.QRect(10, 80, 141, 51))
        self.button_head_cleaning_normal.setObjectName("button_head_cleaning_normal")
        self.button_head_cleaning_deep = QtWidgets.QPushButton(self.groupBox_2)
        self.button_head_cleaning_deep.setGeometry(QtCore.QRect(10, 140, 141, 51))
        self.button_head_cleaning_deep.setObjectName("button_head_cleaning_deep")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 220, 471, 16))
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Check my printer"))
        self.groupBox.setTitle(_translate("Form", "Список принтеров"))
        self.groupBox_2.setTitle(_translate("Form", "Действие над принтером"))
        self.button_nozzle_check.setText(_translate("Form", "Проверка дюз"))
        self.button_head_cleaning_normal.setText(_translate("Form", "Прочистка печатающей\n"
"головки (обычная)"))
        self.button_head_cleaning_deep.setText(_translate("Form", "Прочистка печатающей\n"
"головки (глубокая)"))
        self.label.setText(_translate("Form", "* Программа работает только с принтерами|мфу Canon и Epson"))
import res_rc
