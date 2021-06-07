# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cfmTradeWgt.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        Form.setStyleSheet("QWidget#Form\n"
"{\n"
"border-image: url(:/register/resource/picture/changeWgt_background.jpg);\n"
"}")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(60, 20, 261, 61))
        self.label_2.setStyleSheet("font: 18pt \"隶书\";")
        self.label_2.setObjectName("label_2")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(60, 90, 271, 141))
        self.textEdit.setStyleSheet("font: 12pt \"楷体\";")
        self.textEdit.setObjectName("textEdit")
        self.cfmTradeBtn = QtWidgets.QPushButton(Form)
        self.cfmTradeBtn.setGeometry(QtCore.QRect(60, 240, 91, 31))
        self.cfmTradeBtn.setStyleSheet("QPushButton{\n"
"    \n"
"    background-color: rgb(245, 255, 48);\n"
"border:1px solid #717171;\n"
"border-radius:10px;\n"
"font: 13pt \"楷体\";\n"
"background-color: qconicalgradient(cx:0.5,cy:0.522909, angle:179.9, stop:0.494318 rgba(238, 233, 220, 255), stop:0.5 rgba(236, 236, 236, 255));\n"
"\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    background-color: qlineargradient(spread:pad, x1:0.909, y1:0.864, x2:0.926, y2:0, stop:0.448864 rgba(255, 239, 88, 250), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"}\n"
"\n"
"")
        self.cfmTradeBtn.setObjectName("cfmTradeBtn")
        self.refuseTradeBtn = QtWidgets.QPushButton(Form)
        self.refuseTradeBtn.setGeometry(QtCore.QRect(220, 240, 91, 31))
        self.refuseTradeBtn.setStyleSheet("QPushButton{\n"
"    \n"
"    background-color: rgb(245, 255, 48);\n"
"border:1px solid #717171;\n"
"border-radius:10px;\n"
"font: 13pt \"楷体\";\n"
"background-color: qconicalgradient(cx:0.5,cy:0.522909, angle:179.9, stop:0.494318 rgba(238, 233, 220, 255), stop:0.5 rgba(236, 236, 236, 255));\n"
"\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    background-color: qlineargradient(spread:pad, x1:0.909, y1:0.864, x2:0.926, y2:0, stop:0.448864 rgba(255, 239, 88, 250), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"}\n"
"\n"
"")
        self.refuseTradeBtn.setObjectName("refuseTradeBtn")

        self.retranslateUi(Form)
        self.cfmTradeBtn.clicked.connect(Form.cfmThisTrade)
        self.refuseTradeBtn.clicked.connect(Form.refuseThisTrade)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "是否同意此条交易建议?\n"
"（若不同意请给出原因）"))
        self.cfmTradeBtn.setText(_translate("Form", "同意交易"))
        self.refuseTradeBtn.setText(_translate("Form", "拒绝交易"))
import images_rc
