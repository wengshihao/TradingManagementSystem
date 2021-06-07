# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TopenSPandCPWgt.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(834, 847)
        Form.setStyleSheet("QWidget#Form\n"
"{\n"
"border-image: url(:/TmainWgt/resource/picture/TopenSPandCPWgt_background.jpg);\n"
"}")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(30, 20, 168, 30))
        self.label_3.setStyleSheet("font: 18pt \"隶书\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(30, 440, 168, 30))
        self.label_4.setStyleSheet("font: 18pt \"隶书\";")
        self.label_4.setObjectName("label_4")
        self.tableView = QtWidgets.QTableView(Form)
        self.tableView.setGeometry(QtCore.QRect(30, 50, 761, 371))
        self.tableView.setStyleSheet("font: 18pt \"楷体\";")
        self.tableView.setObjectName("tableView")
        self.tableView_2 = QtWidgets.QTableView(Form)
        self.tableView_2.setGeometry(QtCore.QRect(30, 480, 761, 321))
        self.tableView_2.setStyleSheet("font: 18pt \"楷体\";")
        self.tableView_2.setObjectName("tableView_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_3.setText(_translate("Form", "商家供应"))
        self.label_4.setText(_translate("Form", "顾客需求"))
import images_rc
