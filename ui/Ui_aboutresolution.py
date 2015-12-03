# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'aboutwindow.ui'
#
# Created: Fri Feb 13 13:26:14 2015
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

class Ui_aboutResolution(object):
    def setupUi(self, aboutResolution):
        aboutResolution.setObjectName(_fromUtf8("aboutResolution"))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(aboutResolution.sizePolicy().hasHeightForWidth())
        aboutResolution.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("font/DroidSansFallbackFull.ttf"))
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        aboutResolution.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icons/xml_icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        aboutResolution.setWindowIcon(icon)
        self.gridLayout = QtGui.QGridLayout(aboutResolution)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.aw_label_2 = QtGui.QLabel(aboutResolution)
        self.aw_label_2.setMinimumSize(QtCore.QSize(55, 55))
        self.aw_label_2.setMaximumSize(QtCore.QSize(55, 55))
        self.aw_label_2.setText(_fromUtf8(""))
        self.aw_label_2.setPixmap(QtGui.QPixmap(_fromUtf8("icons/warning_icon.png")))
        self.aw_label_2.setScaledContents(True)
        self.aw_label_2.setObjectName(_fromUtf8("aw_label_2"))
        self.verticalLayout.addWidget(self.aw_label_2)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout)
        spacerItem1 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.aw_label_1 = QtGui.QLabel(aboutResolution)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.aw_label_1.sizePolicy().hasHeightForWidth())
        self.aw_label_1.setSizePolicy(sizePolicy)

        font = QtGui.QFont()
        font.setFamily(_fromUtf8("font/DroidSansFallbackFull.ttf"))
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.aw_label_1.setFont(font)
        self.aw_label_1.setFrameShape(QtGui.QFrame.NoFrame)
        self.aw_label_1.setFrameShadow(QtGui.QFrame.Plain)
        self.aw_label_1.setLineWidth(1)
        self.aw_label_1.setMidLineWidth(0)
        self.aw_label_1.setTextFormat(QtCore.Qt.AutoText)
        self.aw_label_1.setScaledContents(False)
        self.aw_label_1.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignTop)
        self.aw_label_1.setWordWrap(True)
        self.aw_label_1.setObjectName(_fromUtf8("aw_label_1"))

        aboutResolution.resize(390, 220)
        aboutResolution.setMinimumSize(QtCore.QSize(390, 170))
        aboutResolution.setMaximumSize(QtCore.QSize(390, 170))
        self.aw_label_1.setMinimumSize(QtCore.QSize(290, 140))
        self.aw_label_1.setMaximumSize(QtCore.QSize(290, 140))
        
        self.horizontalLayout.addWidget(self.aw_label_1)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        spacerItem2 = QtGui.QSpacerItem(20, 10, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem2)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.aw_okButton = QtGui.QPushButton(aboutResolution)
        self.aw_okButton.setMinimumSize(QtCore.QSize(93, 27))
        self.aw_okButton.setMaximumSize(QtCore.QSize(93, 27))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("font/DroidSansFallbackFull.ttf"))
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.aw_okButton.setFont(font)
        self.aw_okButton.setObjectName(_fromUtf8("aw_okButton"))
        self.horizontalLayout_2.addWidget(self.aw_okButton)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)

        self.retranslateUi(aboutResolution)
        QtCore.QMetaObject.connectSlotsByName(aboutResolution)

    def retranslateUi(self, aboutResolution):
        aboutResolution.setWindowTitle(_translate("aboutResolution", "Warning", None))
        self.aw_label_1.setText(_translate("aboutResolution", "<html><head/><body><p><br/></p></body></html>", None))
        self.aw_okButton.setText(_translate("aboutResolution", "OK", None))

