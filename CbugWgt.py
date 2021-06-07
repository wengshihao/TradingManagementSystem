# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CbugWgt.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(350, 473)
        Form.setMinimumSize(QtCore.QSize(350, 473))
        Form.setMaximumSize(QtCore.QSize(350, 473))
        Form.setStyleSheet("QWidget#Form\n"
"{\n"
"border-image: url(:/CmainWdt/resource/picture/CbuyWgt_background.jpg);\n"
"}")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 60, 137, 281))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setStyleSheet("font: 18pt \"隶书\";")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setStyleSheet("font: 18pt \"隶书\";")
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setStyleSheet("font: 18pt \"隶书\";")
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setStyleSheet("font: 18pt \"隶书\";")
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setStyleSheet("font: 18pt \"隶书\";")
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.returnBtn = QtWidgets.QPushButton(Form)
        self.returnBtn.setGeometry(QtCore.QRect(120, 380, 121, 51))
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
"    background-color: qlineargradient(spread:pad, x1:0.909, y1:0.864, x2:0.926, y2:0, stop:0.448864 rgba(85, 239, 88, 250), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"}\n"
"\n"
"")
        self.returnBtn.setObjectName("returnBtn")
        self.layoutWidget_2 = QtWidgets.QWidget(Form)
        self.layoutWidget_2.setGeometry(QtCore.QRect(160, 60, 161, 281))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(20)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.SsupplyWgt_SnoLedit_2 = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.SsupplyWgt_SnoLedit_2.setEnabled(False)
        self.SsupplyWgt_SnoLedit_2.setMinimumSize(QtCore.QSize(0, 30))
        self.SsupplyWgt_SnoLedit_2.setStyleSheet("font: 11pt \"楷体\";")
        self.SsupplyWgt_SnoLedit_2.setText("")
        self.SsupplyWgt_SnoLedit_2.setClearButtonEnabled(False)
        self.SsupplyWgt_SnoLedit_2.setObjectName("SsupplyWgt_SnoLedit_2")
        self.verticalLayout_3.addWidget(self.SsupplyWgt_SnoLedit_2)
        self.SsupplyWgt_PnoLedit_2 = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.SsupplyWgt_PnoLedit_2.setEnabled(False)
        self.SsupplyWgt_PnoLedit_2.setMinimumSize(QtCore.QSize(0, 30))
        self.SsupplyWgt_PnoLedit_2.setStyleSheet("font: 11pt \"楷体\";")
        self.SsupplyWgt_PnoLedit_2.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.SsupplyWgt_PnoLedit_2.setClearButtonEnabled(False)
        self.SsupplyWgt_PnoLedit_2.setObjectName("SsupplyWgt_PnoLedit_2")
        self.verticalLayout_3.addWidget(self.SsupplyWgt_PnoLedit_2)
        self.SsupplyWgt_NumLedit_2 = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.SsupplyWgt_NumLedit_2.setMinimumSize(QtCore.QSize(0, 30))
        self.SsupplyWgt_NumLedit_2.setStyleSheet("font: 11pt \"楷体\";")
        self.SsupplyWgt_NumLedit_2.setClearButtonEnabled(True)
        self.SsupplyWgt_NumLedit_2.setObjectName("SsupplyWgt_NumLedit_2")
        self.verticalLayout_3.addWidget(self.SsupplyWgt_NumLedit_2)
        self.SsupplyWgt_PriceLedit_2 = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.SsupplyWgt_PriceLedit_2.setMinimumSize(QtCore.QSize(0, 30))
        self.SsupplyWgt_PriceLedit_2.setStyleSheet("font: 11pt \"楷体\";")
        self.SsupplyWgt_PriceLedit_2.setClearButtonEnabled(True)
        self.SsupplyWgt_PriceLedit_2.setObjectName("SsupplyWgt_PriceLedit_2")
        self.verticalLayout_3.addWidget(self.SsupplyWgt_PriceLedit_2)
        self.SsupplyWgt_NameLedit_2 = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.SsupplyWgt_NameLedit_2.setMinimumSize(QtCore.QSize(0, 30))
        self.SsupplyWgt_NameLedit_2.setStyleSheet("font: 11pt \"楷体\";")
        self.SsupplyWgt_NameLedit_2.setClearButtonEnabled(True)
        self.SsupplyWgt_NameLedit_2.setObjectName("SsupplyWgt_NameLedit_2")
        self.verticalLayout_3.addWidget(self.SsupplyWgt_NameLedit_2)

        self.retranslateUi(Form)
        self.returnBtn.clicked.connect(Form.cfmBuy)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "顾 客 号："))
        self.label_2.setText(_translate("Form", "零 件 号："))
        self.label_3.setText(_translate("Form", "求购数量："))
        self.label_4.setText(_translate("Form", "单    价:"))
        self.label_5.setText(_translate("Form", "顾客签名："))
        self.returnBtn.setText(_translate("Form", "确认"))
import images_rc
