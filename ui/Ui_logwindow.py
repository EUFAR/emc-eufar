# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'logwindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Changelog(object):
    def setupUi(self, Changelog):
        Changelog.setObjectName("Changelog")
        Changelog.resize(600, 450)
        font = QtGui.QFont()
        font.setFamily("font/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        Changelog.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/changelog_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Changelog.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(Changelog)
        self.gridLayout.setObjectName("gridLayout")
        self.log_txBrower = QtWidgets.QTextBrowser(Changelog)
        font = QtGui.QFont()
        font.setFamily("font/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.log_txBrower.setFont(font)
        self.log_txBrower.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.log_txBrower.setObjectName("log_txBrower")
        self.gridLayout.addWidget(self.log_txBrower, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.lg_okButton = QtWidgets.QPushButton(Changelog)
        self.lg_okButton.setMinimumSize(QtCore.QSize(50, 27))
        self.lg_okButton.setMaximumSize(QtCore.QSize(50, 27))
        font = QtGui.QFont()
        font.setFamily("font/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.lg_okButton.setFont(font)
        self.lg_okButton.setObjectName("lg_okButton")
        self.horizontalLayout.addWidget(self.lg_okButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        self.retranslateUi(Changelog)
        QtCore.QMetaObject.connectSlotsByName(Changelog)

    def retranslateUi(self, Changelog):
        _translate = QtCore.QCoreApplication.translate
        Changelog.setWindowTitle(_translate("Changelog", "Changelog"))
        self.log_txBrower.setDocumentTitle(_translate("Changelog", "Changelog"))
        self.lg_okButton.setText(_translate("Changelog", "Ok"))

