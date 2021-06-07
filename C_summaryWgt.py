# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C_summaryWgt.ui'
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
"border-image: url(:/CmainWdt/resource/picture/CsummaryWgt_background.jpg);\n"
"}")
        self.tableView = QtWidgets.QTableView(Form)
        self.tableView.setGeometry(QtCore.QRect(190, 80, 491, 221))
        self.tableView.setStyleSheet("font: 16pt \"隶书\";")
        self.tableView.setObjectName("tableView")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(40, 330, 168, 30))
        self.label_4.setStyleSheet("font: 18pt \"隶书\";")
        self.label_4.setObjectName("label_4")
        self.tableView_2 = QtWidgets.QTableView(Form)
        self.tableView_2.setGeometry(QtCore.QRect(190, 330, 491, 192))
        self.tableView_2.setStyleSheet("font: 16pt \"隶书\";")
        self.tableView_2.setObjectName("tableView_2")
        self.tableView_3 = QtWidgets.QTableView(Form)
        self.tableView_3.setGeometry(QtCore.QRect(190, 560, 491, 192))
        self.tableView_3.setStyleSheet("font: 16pt \"隶书\";")
        self.tableView_3.setObjectName("tableView_3")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(40, 30, 168, 30))
        self.label.setStyleSheet("font: 18pt \"隶书\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(200, 30, 168, 30))
        self.label_2.setStyleSheet("font: 18pt \"隶书\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(40, 80, 168, 30))
        self.label_3.setStyleSheet("font: 18pt \"隶书\";")
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(30, 550, 168, 30))
        self.label_5.setStyleSheet("font: 18pt \"隶书\";")
        self.label_5.setObjectName("label_5")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_4.setText(_translate("Form", "拒绝的订单："))
        self.label.setText(_translate("Form", "目前支出总额："))
        self.label_2.setText(_translate("Form", "1348元"))
        self.label_3.setText(_translate("Form", "成交订单："))
        self.label_5.setText(_translate("Form", "被拒绝的订单："))
import images_rc
