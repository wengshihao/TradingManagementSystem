# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CopenPWgt.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 900)
        Form.setMinimumSize(QtCore.QSize(800, 900))
        Form.setMaximumSize(QtCore.QSize(800, 900))
        self.tableView = QtWidgets.QTableView(Form)
        self.tableView.setGeometry(QtCore.QRect(0, 40, 801, 871))
        self.tableView.setStyleSheet("font: 22pt \"楷体\";\n"
"border-image: url(:/CmainWdt/resource/picture/CopenPWgt_background.jpg);")
        self.tableView.setSortingEnabled(False)
        self.tableView.setObjectName("tableView")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 801, 41))
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 18pt \"隶书\";\n"
"color: rgb(255, 85, 0);")
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "                     提示：请双击零件进行求购"))
import images_rc
