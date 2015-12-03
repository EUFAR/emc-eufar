# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fillwindow.ui'
#
# Created: Tue Jun 16 09:11:44 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import os

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
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icons/warning_icon2.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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
        self.fw_label_2.setPixmap(QtGui.QPixmap(_fromUtf8("icons/warning_icon2.png")))
        self.fw_label_2.setScaledContents(True)
        self.fw_label_2.setObjectName(_fromUtf8("fw_label_2"))
        self.verticalLayout_2.addWidget(self.fw_label_2)
        spacerItem = QtGui.QSpacerItem(20, 18, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        spacerItem1 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.fw_label_1 = QtGui.QLabel(fillWindow)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("font/DroidSansFallbackFull.ttf"))
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
        self.fw_detailButton.setMinimumSize(QtCore.QSize(138, 27))
        self.fw_detailButton.setMaximumSize(QtCore.QSize(138, 27))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("font/DroidSansFallbackFull.ttf"))
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.fw_detailButton.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("icons/preferences_icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.fw_detailButton.setIcon(icon1)
        self.fw_detailButton.setIconSize(QtCore.QSize(25, 25))
        self.fw_detailButton.setObjectName(_fromUtf8("fw_detailButton"))
        self.horizontalLayout_2.addWidget(self.fw_detailButton)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.fw_cancelButton = QtGui.QPushButton(fillWindow)
        self.fw_cancelButton.setMinimumSize(QtCore.QSize(107, 27))
        self.fw_cancelButton.setMaximumSize(QtCore.QSize(107, 27))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("icons/cancel_icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.fw_cancelButton.setIcon(icon2)
        self.fw_cancelButton.setIconSize(QtCore.QSize(25, 25))
        self.fw_cancelButton.setObjectName(_fromUtf8("fw_cancelButton"))
        self.horizontalLayout_2.addWidget(self.fw_cancelButton)
        if os.name == "nt":
            spacerItem5 = QtGui.QSpacerItem(50, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        else:
            spacerItem5 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.fw_okButton = QtGui.QPushButton(fillWindow)
        self.fw_okButton.setMinimumSize(QtCore.QSize(93, 27))
        self.fw_okButton.setMaximumSize(QtCore.QSize(93, 27))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("font/DroidSansFallbackFull.ttf"))
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.fw_okButton.setFont(font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("icons/save_icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.fw_okButton.setIcon(icon3)
        self.fw_okButton.setIconSize(QtCore.QSize(25, 25))
        self.fw_okButton.setObjectName(_fromUtf8("fw_okButton"))
        self.horizontalLayout_2.addWidget(self.fw_okButton)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        spacerItem7 = QtGui.QSpacerItem(20, 13, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout_3.addItem(spacerItem7)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.verticalLayout_3.addLayout(self.verticalLayout)
        if os.name == "nt":
            fillWindow.resize(500, 250)
            fillWindow.setMinimumSize(QtCore.QSize(500, 250))
            fillWindow.setMaximumSize(QtCore.QSize(500, 250))
            self.fw_label_1.setMinimumSize(QtCore.QSize(390, 170))
            self.fw_label_1.setMaximumSize(QtCore.QSize(390, 170))
        else:
            fillWindow.resize(450, 220)
            fillWindow.setMinimumSize(QtCore.QSize(450, 220))
            fillWindow.setMaximumSize(QtCore.QSize(452, 220))
            self.fw_label_1.setMinimumSize(QtCore.QSize(341, 140))
            self.fw_label_1.setMaximumSize(QtCore.QSize(341, 140))
        self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 1, 1)

        self.retranslateUi(fillWindow)
        QtCore.QMetaObject.connectSlotsByName(fillWindow)

    def retranslateUi(self, fillWindow):
        fillWindow.setWindowTitle(_translate("fillWindow", "Warning", None))
        self.fw_label_1.setText(_translate("fillWindow", "<html><head/><body><p align=\"justify\">All mandatory fields have not been filled in, or have been incorrectly filled in. You can save your file if you want to complete/correct it later. All fields which have not been completely filled in are indicated in <span style=\" font-weight:600; color:#c80000;\">red</span>, and in <span style=\" font-weight:600; color:#0000c8;\">blue</span> for those incorrectly filled in (see Details to have a complete list). <span style=\" font-weight:600;\">Do not use an incomplete/incorrect xml file for storage and/or sql queries.</span></p></body></html>", None))
        self.fw_detailButton.setText(_translate("fillWindow", "Show details", None))
        self.fw_cancelButton.setText(_translate("fillWindow", "Cancel", None))
        self.fw_okButton.setText(_translate("fillWindow", "Save", None))

