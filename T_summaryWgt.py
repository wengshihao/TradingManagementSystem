# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'T_summaryWgt.ui'
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
"    border-image: url(:/TmainWgt/resource/picture/T_summaryWgt_background.jpg);\n"
"}")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 20, 168, 30))
        self.label.setStyleSheet("font: 18pt \"隶书\";")
        self.label.setObjectName("label")
        self.cfmmoneyQlabel = QtWidgets.QLabel(Form)
        self.cfmmoneyQlabel.setGeometry(QtCore.QRect(180, 20, 168, 30))
        self.cfmmoneyQlabel.setStyleSheet("font: 18pt \"隶书\";")
        self.cfmmoneyQlabel.setObjectName("cfmmoneyQlabel")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(30, 70, 168, 30))
        self.label_3.setStyleSheet("font: 18pt \"隶书\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(10, 300, 211, 30))
        self.label_4.setStyleSheet("font: 18pt \"隶书\";")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(10, 540, 211, 30))
        self.label_5.setStyleSheet("font: 18pt \"隶书\";")
        self.label_5.setObjectName("label_5")
        self.tableView = QtWidgets.QTableView(Form)
        self.tableView.setGeometry(QtCore.QRect(150, 70, 491, 221))
        self.tableView.setStyleSheet("font: 16pt \"隶书\";")
        self.tableView.setObjectName("tableView")
        self.tableView_2 = QtWidgets.QTableView(Form)
        self.tableView_2.setGeometry(QtCore.QRect(150, 340, 491, 192))
        self.tableView_2.setStyleSheet("font: 16pt \"隶书\";")
        self.tableView_2.setObjectName("tableView_2")
        self.tableView_3 = QtWidgets.QTableView(Form)
        self.tableView_3.setGeometry(QtCore.QRect(150, 580, 491, 192))
        self.tableView_3.setStyleSheet("font: 16pt \"隶书\";")
        self.tableView_3.setObjectName("tableView_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "目前成交额："))
        self.cfmmoneyQlabel.setText(_translate("Form", "1348元"))
        self.label_3.setText(_translate("Form", "成交订单："))
        self.label_4.setText(_translate("Form", "供应商拒绝的订单："))
        self.label_5.setText(_translate("Form", "顾客拒绝的订单："))
import images_rc
