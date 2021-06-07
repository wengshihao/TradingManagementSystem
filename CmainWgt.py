# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CmainWgt.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(600, 600)
        Form.setMinimumSize(QtCore.QSize(600, 600))
        Form.setSizeIncrement(QtCore.QSize(600, 600))
        Form.setStyleSheet("QWidget#Form\n"
"{\n"
"border-image: url(:/CmainWdt/resource/picture/CmainWgt_background.jpg);\n"
"}")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(160, 70, 289, 441))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(30)
        self.verticalLayout.setObjectName("verticalLayout")
        self.SseePartsBtn = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SseePartsBtn.sizePolicy().hasHeightForWidth())
        self.SseePartsBtn.setSizePolicy(sizePolicy)
        self.SseePartsBtn.setStyleSheet("QPushButton{\n"
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
"    background-color: qlineargradient(spread:pad, x1:0.909, y1:0.864, x2:0.926, y2:0, stop:0.448864 rgba(159, 239, 88, 250), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"}\n"
"\n"
"")
        self.SseePartsBtn.setObjectName("SseePartsBtn")
        self.verticalLayout.addWidget(self.SseePartsBtn)
        self.SsuppyPartsBtn = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SsuppyPartsBtn.sizePolicy().hasHeightForWidth())
        self.SsuppyPartsBtn.setSizePolicy(sizePolicy)
        self.SsuppyPartsBtn.setStyleSheet("QPushButton{\n"
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
"    background-color: qlineargradient(spread:pad, x1:0.909, y1:0.864, x2:0.926, y2:0, stop:0.448864 rgba(159, 239, 88, 250), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"}\n"
"\n"
"")
        self.SsuppyPartsBtn.setObjectName("SsuppyPartsBtn")
        self.verticalLayout.addWidget(self.SsuppyPartsBtn)
        self.ScfmTradeBtn = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ScfmTradeBtn.sizePolicy().hasHeightForWidth())
        self.ScfmTradeBtn.setSizePolicy(sizePolicy)
        self.ScfmTradeBtn.setStyleSheet("QPushButton{\n"
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
"    background-color: qlineargradient(spread:pad, x1:0.909, y1:0.864, x2:0.926, y2:0, stop:0.448864 rgba(159, 239, 88, 250), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"}\n"
"\n"
"")
        self.ScfmTradeBtn.setObjectName("ScfmTradeBtn")
        self.verticalLayout.addWidget(self.ScfmTradeBtn)
        self.psummaryBtn = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.psummaryBtn.sizePolicy().hasHeightForWidth())
        self.psummaryBtn.setSizePolicy(sizePolicy)
        self.psummaryBtn.setStyleSheet("QPushButton{\n"
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
"    background-color: qlineargradient(spread:pad, x1:0.909, y1:0.864, x2:0.926, y2:0, stop:0.448864 rgba(255, 239, 88, 250), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"}\n"
"\n"
"")
        self.psummaryBtn.setObjectName("psummaryBtn")
        self.verticalLayout.addWidget(self.psummaryBtn)
        self.SresultTradeBtn = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SresultTradeBtn.sizePolicy().hasHeightForWidth())
        self.SresultTradeBtn.setSizePolicy(sizePolicy)
        self.SresultTradeBtn.setStyleSheet("QPushButton{\n"
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
"    background-color: qlineargradient(spread:pad, x1:0.909, y1:0.864, x2:0.926, y2:0, stop:0.448864 rgba(159, 239, 88, 250), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"}\n"
"\n"
"")
        self.SresultTradeBtn.setObjectName("SresultTradeBtn")
        self.verticalLayout.addWidget(self.SresultTradeBtn)
        self.SlogoutBtn = QtWidgets.QPushButton(Form)
        self.SlogoutBtn.setGeometry(QtCore.QRect(510, 560, 75, 23))
        self.SlogoutBtn.setStyleSheet("QPushButton{\n"
"    \n"
"    background-color: rgb(245, 255, 48);\n"
"border:1px solid #717171;\n"
"border-radius:5px;\n"
"font: 15pt \"楷体\";\n"
"background-color: qconicalgradient(cx:0.5,cy:0.522909, angle:179.9, stop:0.494318 rgba(238, 233, 220, 255), stop:0.5 rgba(236, 236, 236, 255));\n"
"\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    background-color: qlineargradient(spread:pad, x1:0.909, y1:0.864, x2:0.926, y2:0, stop:0.448864 rgba(159, 239, 88, 250), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"}\n"
"\n"
"")
        self.SlogoutBtn.setObjectName("SlogoutBtn")

        self.retranslateUi(Form)
        self.SseePartsBtn.clicked.connect(Form.CopenP)
        self.SsuppyPartsBtn.clicked.connect(Form.CopenCP)
        self.ScfmTradeBtn.clicked.connect(Form.CopenSCP)
        self.SresultTradeBtn.clicked.connect(Form.CopenSummary)
        self.SlogoutBtn.clicked.connect(Form.Clogout)
        self.psummaryBtn.clicked.connect(Form.CsummaryP)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.SseePartsBtn.setText(_translate("Form", "求购零件"))
        self.SsuppyPartsBtn.setText(_translate("Form", "修改求购"))
        self.ScfmTradeBtn.setText(_translate("Form", "确认交易"))
        self.psummaryBtn.setText(_translate("Form", "零件/供应商统计"))
        self.SresultTradeBtn.setText(_translate("Form", "交易统计"))
        self.SlogoutBtn.setText(_translate("Form", "注销"))
import images_rc
