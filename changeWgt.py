# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'changeWgt.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(388, 175)
        Form.setStyleSheet("QWidget#Form\n"
"{\n"
"background-image: url(:/register/resource/picture/changeWgt_background.jpg);\n"
"}")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(140, 120, 91, 31))
        self.pushButton.setStyleSheet("QPushButton{\n"
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
        self.pushButton.setObjectName("pushButton")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(20, 50, 361, 41))
        self.widget.setObjectName("widget")
        self.formLayout = QtWidgets.QFormLayout(self.widget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit.setStyleSheet("font: 11pt \"楷体\";")
        self.lineEdit.setClearButtonEnabled(True)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setStyleSheet("font: 18pt \"隶书\";")
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)

        self.retranslateUi(Form)
        self.pushButton.clicked.connect(Form.changeIt)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "确定修改"))
        self.label.setText(_translate("Form", "将此项修改为："))
import images_rc
