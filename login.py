# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setEnabled(True)
        Form.resize(600, 500)
        Form.setMinimumSize(QtCore.QSize(600, 500))
        Form.setMaximumSize(QtCore.QSize(600, 500))
        Form.setStyleSheet("QWidget#Form\n"
"{\n"
"border-image: url(:/login/resource/picture/login_background.jpg);\n"
"}")
        self.loginBtn = QtWidgets.QPushButton(Form)
        self.loginBtn.setEnabled(True)
        self.loginBtn.setGeometry(QtCore.QRect(150, 370, 281, 51))
        self.loginBtn.setStyleSheet("QPushButton\n"
"{\n"
"background-color:rgb(85, 255, 255);\n"
"font: 16pt \"楷体\";\n"
"border-radius:20px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"background-color:rgb(255, 170, 127);\n"
"}")
        self.loginBtn.setObjectName("loginBtn")
        self.supplierLogRiobtn = QtWidgets.QRadioButton(Form)
        self.supplierLogRiobtn.setGeometry(QtCore.QRect(200, 310, 81, 16))
        self.supplierLogRiobtn.setStyleSheet("font: 15pt \"楷体\";")
        self.supplierLogRiobtn.setChecked(True)
        self.supplierLogRiobtn.setObjectName("supplierLogRiobtn")
        self.tradersLogRiobtn = QtWidgets.QRadioButton(Form)
        self.tradersLogRiobtn.setGeometry(QtCore.QRect(400, 310, 85, 16))
        self.tradersLogRiobtn.setStyleSheet("font: 15pt \"楷体\";")
        self.tradersLogRiobtn.setObjectName("tradersLogRiobtn")
        self.customerLogRiobtn = QtWidgets.QRadioButton(Form)
        self.customerLogRiobtn.setGeometry(QtCore.QRect(310, 310, 71, 16))
        self.customerLogRiobtn.setStyleSheet("font: 15pt \"楷体\";")
        self.customerLogRiobtn.setObjectName("customerLogRiobtn")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(80, 300, 99, 35))
        self.label.setStyleSheet("color:rgb(0, 0, 0);\n"
"font: 16pt \"楷体\";")
        self.label.setObjectName("label")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(110, 140, 321, 131))
        self.layoutWidget.setObjectName("layoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setVerticalSpacing(40)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setStyleSheet("color:rgb(0, 0, 0);\n"
"font: 16pt \"楷体\";")
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setStyleSheet("color:rgb(0, 0, 0);\n"
"font: 16pt \"楷体\";")
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.accountLogComBox = QtWidgets.QComboBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.accountLogComBox.sizePolicy().hasHeightForWidth())
        self.accountLogComBox.setSizePolicy(sizePolicy)
        self.accountLogComBox.setMinimumSize(QtCore.QSize(0, 35))
        self.accountLogComBox.setStyleSheet("font: 11pt \"楷体\";\n"
"\n"
"")
        self.accountLogComBox.setEditable(True)
        self.accountLogComBox.setObjectName("accountLogComBox")
        self.accountLogComBox.addItem("")
        self.accountLogComBox.addItem("")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.accountLogComBox)
        self.passwordLogLedit = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.passwordLogLedit.sizePolicy().hasHeightForWidth())
        self.passwordLogLedit.setSizePolicy(sizePolicy)
        self.passwordLogLedit.setMinimumSize(QtCore.QSize(0, 35))
        self.passwordLogLedit.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.passwordLogLedit.setStyleSheet("font: 11pt \"楷体\";")
        self.passwordLogLedit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordLogLedit.setClearButtonEnabled(True)
        self.passwordLogLedit.setObjectName("passwordLogLedit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.passwordLogLedit)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(130, 40, 361, 35))
        self.label_4.setStyleSheet("color:rgb(0, 0, 0);\n"
"font: 26pt \"隶书\";")
        self.label_4.setObjectName("label_4")
        self.gotoRegisterBtn = QtWidgets.QPushButton(Form)
        self.gotoRegisterBtn.setGeometry(QtCore.QRect(510, 430, 71, 41))
        self.gotoRegisterBtn.setStyleSheet("QPushButton\n"
"{\n"
"background-color:rgb(229, 229, 229);\n"
"font: 16pt \"楷体\";\n"
"border-radius:20px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"background-color:rgb(170, 255, 255);\n"
"}")
        self.gotoRegisterBtn.setObjectName("gotoRegisterBtn")

        self.retranslateUi(Form)
        self.loginBtn.clicked.connect(Form.loginToMainpane)
        self.gotoRegisterBtn.clicked.connect(Form.show_register_pane)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.loginBtn.setText(_translate("Form", "登录"))
        self.supplierLogRiobtn.setText(_translate("Form", "供应商"))
        self.tradersLogRiobtn.setText(_translate("Form", "交易员"))
        self.customerLogRiobtn.setText(_translate("Form", "顾客"))
        self.label.setText(_translate("Form", "登录身份："))
        self.label_2.setText(_translate("Form", "账   号："))
        self.label_3.setText(_translate("Form", "密   码："))
        self.accountLogComBox.setItemText(0, _translate("Form", "S0001"))
        self.accountLogComBox.setItemText(1, _translate("Form", "C0001"))
        self.label_4.setText(_translate("Form", "零件交易管理子系统"))
        self.gotoRegisterBtn.setText(_translate("Form", "注册"))
import images_rc
