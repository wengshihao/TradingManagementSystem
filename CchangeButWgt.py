# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CchangeButWgt.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(790, 798)
        Form.setMinimumSize(QtCore.QSize(0, 0))
        Form.setMaximumSize(QtCore.QSize(777777, 777777))
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 801, 31))
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 18pt \"隶书\";\n"
"color: rgb(255, 85, 0);")
        self.label.setObjectName("label")
        self.tableView = QtWidgets.QTableView(Form)
        self.tableView.setGeometry(QtCore.QRect(0, 30, 791, 771))
        self.tableView.setMinimumSize(QtCore.QSize(0, 0))
        self.tableView.setStyleSheet("font: 22pt \"楷体\";\n"
"border-image: url(:/CmainWdt/resource/picture/CchangeBuyWgt_background.jpg);")
        self.tableView.setObjectName("tableView")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "                      提示：请双击数据进行修改"))
import images_rc
