# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TgiveTadeWgt.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(350, 473)
        Form.setStyleSheet("QWidget#Form\n"
"{\n"
"border-image: url(:/TmainWgt/resource/picture/TgiceTadeWgt_background.jpg);\n"
"}")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(160, 30, 161, 332))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(20)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.T_tnoLedit = QtWidgets.QLineEdit(self.layoutWidget)
        self.T_tnoLedit.setEnabled(False)
        self.T_tnoLedit.setMinimumSize(QtCore.QSize(0, 30))
        self.T_tnoLedit.setStyleSheet("font: 11pt \"楷体\";")
        self.T_tnoLedit.setText("")
        self.T_tnoLedit.setClearButtonEnabled(False)
        self.T_tnoLedit.setObjectName("T_tnoLedit")
        self.verticalLayout_2.addWidget(self.T_tnoLedit)
        self.T_scpnoLedit = QtWidgets.QLineEdit(self.layoutWidget)
        self.T_scpnoLedit.setEnabled(True)
        self.T_scpnoLedit.setMinimumSize(QtCore.QSize(0, 30))
        self.T_scpnoLedit.setStyleSheet("font: 11pt \"楷体\";")
        self.T_scpnoLedit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.T_scpnoLedit.setClearButtonEnabled(True)
        self.T_scpnoLedit.setObjectName("T_scpnoLedit")
        self.verticalLayout_2.addWidget(self.T_scpnoLedit)
        self.T_snoLedit = QtWidgets.QLineEdit(self.layoutWidget)
        self.T_snoLedit.setMinimumSize(QtCore.QSize(0, 30))
        self.T_snoLedit.setStyleSheet("font: 11pt \"楷体\";")
        self.T_snoLedit.setClearButtonEnabled(True)
        self.T_snoLedit.setObjectName("T_snoLedit")
        self.verticalLayout_2.addWidget(self.T_snoLedit)
        self.T_cnoLedit = QtWidgets.QLineEdit(self.layoutWidget)
        self.T_cnoLedit.setMinimumSize(QtCore.QSize(0, 30))
        self.T_cnoLedit.setStyleSheet("font: 11pt \"楷体\";")
        self.T_cnoLedit.setClearButtonEnabled(True)
        self.T_cnoLedit.setObjectName("T_cnoLedit")
        self.verticalLayout_2.addWidget(self.T_cnoLedit)
        self.T_pnoLedit = QtWidgets.QLineEdit(self.layoutWidget)
        self.T_pnoLedit.setMinimumSize(QtCore.QSize(0, 30))
        self.T_pnoLedit.setStyleSheet("font: 11pt \"楷体\";")
        self.T_pnoLedit.setClearButtonEnabled(True)
        self.T_pnoLedit.setObjectName("T_pnoLedit")
        self.verticalLayout_2.addWidget(self.T_pnoLedit)
        self.T_numLedit = QtWidgets.QLineEdit(self.layoutWidget)
        self.T_numLedit.setMinimumSize(QtCore.QSize(0, 30))
        self.T_numLedit.setStyleSheet("font: 11pt \"楷体\";")
        self.T_numLedit.setClearButtonEnabled(True)
        self.T_numLedit.setObjectName("T_numLedit")
        self.verticalLayout_2.addWidget(self.T_numLedit)
        self.T_priceLedit = QtWidgets.QLineEdit(self.layoutWidget)
        self.T_priceLedit.setMinimumSize(QtCore.QSize(0, 30))
        self.T_priceLedit.setStyleSheet("font: 11pt \"楷体\";")
        self.T_priceLedit.setClearButtonEnabled(True)
        self.T_priceLedit.setObjectName("T_priceLedit")
        self.verticalLayout_2.addWidget(self.T_priceLedit)
        self.layoutWidget_2 = QtWidgets.QWidget(Form)
        self.layoutWidget_2.setGeometry(QtCore.QRect(40, 30, 137, 331))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget_2)
        self.label.setStyleSheet("font: 18pt \"隶书\";")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_2.setStyleSheet("font: 18pt \"隶书\";")
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_3.setStyleSheet("font: 18pt \"隶书\";")
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_4.setStyleSheet("font: 18pt \"隶书\";")
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_5.setStyleSheet("font: 18pt \"隶书\";")
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_6.setStyleSheet("font: 18pt \"隶书\";")
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_7.setStyleSheet("font: 18pt \"隶书\";")
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.returnBtn = QtWidgets.QPushButton(Form)
        self.returnBtn.setGeometry(QtCore.QRect(100, 390, 161, 51))
        self.returnBtn.setStyleSheet("QPushButton{\n"
"    \n"
"    background-color: rgb(245, 255, 48);\n"
"border:1px solid #717171;\n"
"border-radius:25px;\n"
"font: 28pt \"楷体\";\n"
"background-color: qconicalgradient(cx:0.5,cy:0.522909, angle:179.9, stop:0.494318 rgba(238, 233, 220, 255), stop:0.5 rgba(236, 236, 236, 255));\n"
"\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    background-color: qlineargradient(spread:pad, x1:0.909, y1:0.864, x2:0.926, y2:0, stop:0.448864 rgba(255, 85, 155, 250), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"}\n"
"\n"
"")
        self.returnBtn.setObjectName("returnBtn")

        self.retranslateUi(Form)
        self.returnBtn.clicked.connect(Form.TcfmGiveTrade)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "交易员号："))
        self.label_2.setText(_translate("Form", "订 单 号："))
        self.label_3.setText(_translate("Form", "供应商号："))
        self.label_4.setText(_translate("Form", "顾 客 号:"))
        self.label_5.setText(_translate("Form", "零 件 号："))
        self.label_6.setText(_translate("Form", "交易数量："))
        self.label_7.setText(_translate("Form", "成交单价："))
        self.returnBtn.setText(_translate("Form", "提出订单"))
import images_rc
