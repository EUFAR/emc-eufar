# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'inspirewindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_inspireWindow(object):
    def setupUi(self, inspireWindow):
        inspireWindow.setObjectName("inspireWindow")
        inspireWindow.resize(800, 720)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(inspireWindow.sizePolicy().hasHeightForWidth())
        inspireWindow.setSizePolicy(sizePolicy)
        inspireWindow.setMinimumSize(QtCore.QSize(800, 720))
        inspireWindow.setMaximumSize(QtCore.QSize(800, 720))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        inspireWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/inspire_popup_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        inspireWindow.setWindowIcon(icon)
        inspireWindow.setStyleSheet("QWidget {\n"
"    background-color: rgb(230,230,230);\n"
"}")
        self.gridLayout = QtWidgets.QGridLayout(inspireWindow)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.aw_label_2 = QtWidgets.QLabel(inspireWindow)
        self.aw_label_2.setMinimumSize(QtCore.QSize(50, 50))
        self.aw_label_2.setMaximumSize(QtCore.QSize(50, 50))
        self.aw_label_2.setText("")
        self.aw_label_2.setPixmap(QtGui.QPixmap("icons/inspire_popup_icon.svg"))
        self.aw_label_2.setScaledContents(True)
        self.aw_label_2.setObjectName("aw_label_2")
        self.verticalLayout.addWidget(self.aw_label_2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.aw_label_1 = QtWidgets.QLabel(inspireWindow)
        self.aw_label_1.setMinimumSize(QtCore.QSize(690, 400))
        self.aw_label_1.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.aw_label_1.setFont(font)
        self.aw_label_1.setWordWrap(True)
        self.aw_label_1.setObjectName("aw_label_1")
        self.horizontalLayout.addWidget(self.aw_label_1)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        spacerItem2 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.aw_okButton = QtWidgets.QToolButton(inspireWindow)
        self.aw_okButton.setMinimumSize(QtCore.QSize(93, 27))
        self.aw_okButton.setMaximumSize(QtCore.QSize(93, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.aw_okButton.setFont(font)
        self.aw_okButton.setStyleSheet("QToolButton {\n"
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
        self.aw_okButton.setObjectName("aw_okButton")
        self.horizontalLayout_2.addWidget(self.aw_okButton)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)

        self.retranslateUi(inspireWindow)
        QtCore.QMetaObject.connectSlotsByName(inspireWindow)

    def retranslateUi(self, inspireWindow):
        _translate = QtCore.QCoreApplication.translate
        inspireWindow.setWindowTitle(_translate("inspireWindow", "About EUFAR Metadata Creator"))
        self.aw_label_1.setText(_translate("inspireWindow", "<html><head/><body><p align=\"justify\">INSPIRE is \'a European Union initiative to establish an infrastructure for spatial information in Europe that is geared to help to make spatial or geographical information more accessible and interoperable for a wide range of purposes supporting sustainable development.\'</p><p align=\"justify\">The INSPIRE directive lays down a general framework for a Spatial Data Infrastructure (SDI) for the purposes of European Community environmental policies and policies or activities which may have an impact on the environment. The INSPIRE Directive entered into force on 15 May 2007.</p><p align=\"justify\">INSPIRE is based on the infrastructures for spatial information established and operated by the member states of the European Union. The directive addresses 34 spatial data themes needed for environmental applications. To ensure that the spatial data infrastructures of the member states are compatible and usable in a community and transboundary context, the INSPIRE Directive requires that additional legislation or common Implementing Rules (IR) are adopted for a number of specific areas (metadata, interoperability of spatial data sets and services, network services, data and service sharing, monitoring and reporting). These are published either as Commission Regulations or as Decisions.</p><p align=\"justify\">The Commission is assisted in the process of adopting such rules by a regulatory committee, INSPIRE Committee, composed of representatives of the member states and chaired by a representative of the Commission (this is known as the Comitology procedure).</p><p align=\"justify\">Wikipedia - Infrastructure for Spatial Information in the European Community (<a href=\"https://en.wikipedia.org/wiki/Infrastructure_for_Spatial_Information_in_the_European_Community\"><span style=\" text-decoration: underline; color:#0000ff;\">https://en.wikipedia.org/wiki/Infrastructure_for_Spatial_Information_in_the_Eu ropean_Community</span></a>)</p><p>Link to the INSPIRE regulation: <a href=\"http://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri\"><span style=\" text-decoration: underline; color:#0000ff;\">http://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:32008R1205&amp;from=EN</span></a></p><p align=\"justify\">Link to the INSPIRE website: <a href=\"http://inspire.ec.europa.eu/index.cfm\"><span style=\" text-decoration: underline; color:#0000ff;\">http://inspire.ec.europa.eu/index.cfm</span></a></p></body></html>"))
        self.aw_okButton.setText(_translate("inspireWindow", "Ok"))

