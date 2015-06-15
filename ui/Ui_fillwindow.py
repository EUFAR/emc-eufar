# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fillwindow.ui'
#
# Created: Wed Mar 18 08:33:32 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_fillWindow(object):
    def setupUi(self, fillWindow):
        fillWindow.setObjectName(_fromUtf8("fillWindow"))
        fillWindow.resize(450, 200)
        fillWindow.setMinimumSize(QtCore.QSize(450, 200))
        fillWindow.setMaximumSize(QtCore.QSize(450, 200))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(self.progPath + "/icons/warning_icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        fillWindow.setWindowIcon(icon)
        self.gridLayout = QtGui.QGridLayout(fillWindow)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.fw_label_2 = QtGui.QLabel(fillWindow)
        self.fw_label_2.setMinimumSize(QtCore.QSize(55, 55))
        self.fw_label_2.setMaximumSize(QtCore.QSize(55, 55))
        self.fw_label_2.setText(_fromUtf8(""))
        self.fw_label_2.setPixmap(QtGui.QPixmap(_fromUtf8(self.progPath + "/icons/warning_icon.png")))
        self.fw_label_2.setScaledContents(True)
        self.fw_label_2.setObjectName(_fromUtf8("fw_label_2"))
        self.verticalLayout_2.addWidget(self.fw_label_2)
        spacerItem = QtGui.QSpacerItem(20, 18, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        spacerItem1 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.fw_label_1 = QtGui.QLabel(fillWindow)
        self.fw_label_1.setMinimumSize(QtCore.QSize(341, 120))
        self.fw_label_1.setMaximumSize(QtCore.QSize(341, 120))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8(self.progPath + "/font/DroidSansFallbackFull.ttf"))
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.fw_label_1.setFont(font)
        self.fw_label_1.setWordWrap(True)
        self.fw_label_1.setObjectName(_fromUtf8("fw_label_1"))
        self.horizontalLayout.addWidget(self.fw_label_1)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        spacerItem2 = QtGui.QSpacerItem(20, 13, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout_3.addItem(spacerItem2)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.fw_detailButton = QtGui.QPushButton(fillWindow)
        self.fw_detailButton.setMinimumSize(QtCore.QSize(93, 27))
        self.fw_detailButton.setMaximumSize(QtCore.QSize(93, 27))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8(self.progPath + "/font/DroidSansFallbackFull.ttf"))
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.fw_detailButton.setFont(font)
        self.fw_detailButton.setObjectName(_fromUtf8("fw_detailButton"))
        self.horizontalLayout_2.addWidget(self.fw_detailButton)
        spacerItem4 = QtGui.QSpacerItem(120, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.fw_okButton = QtGui.QPushButton(fillWindow)
        self.fw_okButton.setMinimumSize(QtCore.QSize(93, 27))
        self.fw_okButton.setMaximumSize(QtCore.QSize(93, 27))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8(self.progPath + "/font/DroidSansFallbackFull.ttf"))
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.fw_okButton.setFont(font)
        self.fw_okButton.setObjectName(_fromUtf8("fw_okButton"))
        self.horizontalLayout_2.addWidget(self.fw_okButton)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        spacerItem6 = QtGui.QSpacerItem(20, 13, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout_3.addItem(spacerItem6)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 1, 1)

        self.retranslateUi(fillWindow)
        QtCore.QMetaObject.connectSlotsByName(fillWindow)

    def retranslateUi(self, fillWindow):
        fillWindow.setWindowTitle(_translate("fillWindow", "Warning", None))
        self.fw_label_1.setText(_translate("fillWindow", "<html><head/><body><p align=\"justify\">All mandatory fields have not been filled in, or have been incorrectly filled in. You can save your file if you want to complete/correct it later. All fields which have not been completely filled in are indicated in <span style=\" font-weight:600; color:#c80000;\">red</span>, and in <span style=\" font-weight:600; color:#0000c8;\">blue</span> for those incorrectly filled in (see Details to have a complete list). <span style=\" font-weight:600;\">Do not use an incomplete/incorrect xml file for storage and/or sql queries.</span></p></body></html>", None))
        self.fw_detailButton.setText(_translate("fillWindow", "Show details", None))
        self.fw_okButton.setText(_translate("fillWindow", "OK", None))

