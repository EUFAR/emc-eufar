# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'apiwindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_apiWindow(object):
    def setupUi(self, apiWindow):
        apiWindow.setObjectName("apiWindow")
        apiWindow.resize(700, 400)
        apiWindow.setMinimumSize(QtCore.QSize(700, 400))
        apiWindow.setMaximumSize(QtCore.QSize(700, 400))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        apiWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/info_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        apiWindow.setWindowIcon(icon)
        apiWindow.setStyleSheet("QWidget {\n"
"    background-color: rgb(230,230,230);\n"
"}")
        self.gridLayout = QtWidgets.QGridLayout(apiWindow)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.iw_label_2 = QtWidgets.QLabel(apiWindow)
        self.iw_label_2.setMinimumSize(QtCore.QSize(50, 50))
        self.iw_label_2.setMaximumSize(QtCore.QSize(50, 50))
        self.iw_label_2.setText("")
        self.iw_label_2.setPixmap(QtGui.QPixmap("icons/info_popup_icon.svg"))
        self.iw_label_2.setScaledContents(True)
        self.iw_label_2.setObjectName("iw_label_2")
        self.verticalLayout.addWidget(self.iw_label_2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.iw_label_1 = QtWidgets.QLabel(apiWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.iw_label_1.sizePolicy().hasHeightForWidth())
        self.iw_label_1.setSizePolicy(sizePolicy)
        self.iw_label_1.setMinimumSize(QtCore.QSize(400, 120))
        self.iw_label_1.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.iw_label_1.setFont(font)
        self.iw_label_1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.iw_label_1.setFrameShadow(QtWidgets.QFrame.Plain)
        self.iw_label_1.setLineWidth(0)
        self.iw_label_1.setMidLineWidth(0)
        self.iw_label_1.setTextFormat(QtCore.Qt.AutoText)
        self.iw_label_1.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignTop)
        self.iw_label_1.setWordWrap(True)
        self.iw_label_1.setObjectName("iw_label_1")
        self.verticalLayout_2.addWidget(self.iw_label_1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 17, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.checkBox = QtWidgets.QCheckBox(apiWindow)
        self.checkBox.setMinimumSize(QtCore.QSize(0, 20))
        self.checkBox.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setItalic(True)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.checkBox.setFont(font)
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout.addWidget(self.checkBox)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        spacerItem4 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_3.addItem(spacerItem4)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem5 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.iw_okButton = QtWidgets.QToolButton(apiWindow)
        self.iw_okButton.setMinimumSize(QtCore.QSize(90, 27))
        self.iw_okButton.setMaximumSize(QtCore.QSize(90, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.iw_okButton.setFont(font)
        self.iw_okButton.setStyleSheet("QToolButton {\n"
"    border: 1px solid #acacac;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                    stop:0 #f0f0f0, stop:1 #e5e5e5);\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"    border: 1px solid #7eb4ea;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                    stop:0 #ecf4fc, stop:1 #dcecfc);\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"    border: 1px solid #579de5;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                    stop:0 #daecfc, stop:1 #c4e0fc);\n"
"}")
        self.iw_okButton.setObjectName("iw_okButton")
        self.horizontalLayout_2.addWidget(self.iw_okButton)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 1, 1)

        self.retranslateUi(apiWindow)
        QtCore.QMetaObject.connectSlotsByName(apiWindow)

    def retranslateUi(self, apiWindow):
        _translate = QtCore.QCoreApplication.translate
        apiWindow.setWindowTitle(_translate("apiWindow", "Information on EUFAR API"))
        self.iw_label_1.setText(_translate("apiWindow", "<html><head/><body><p align=\"justify\">Since version 1.3.0, EMC is now directly connected to the EUFAR database through an API. It will load automatically project data, aicraft data, operator data and instrument data. The list of aircraft and instrument in EMC is now automatically updated from the EUFAR database. </p><p align=\"justify\">The <span style=\" font-weight:600;\">Project acronym TextBox</span> has been replaced by a <span style=\" font-weight:600;\">SuggestBox</span>. Just write the first letters of a project acronym, and EMC will list you all projects including those letters. Then just select a project in the list, and the relevant fields will be automatically filled in.</p><p align=\"justify\">Because of the structure of the EUFAR database, in EMC, only the following fields will be automatically filled in: Project title, Project acronym, Project abstract, Aircraft and Operator.</p></body></html>"))
        self.checkBox.setText(_translate("apiWindow", "continue displaying the API information window at startup"))
        self.iw_okButton.setText(_translate("apiWindow", "Ok"))

