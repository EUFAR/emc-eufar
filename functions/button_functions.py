# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QWidget, QToolButton
from PyQt5.QtGui import QCursor
from functions.sql_functions import sql_valueRead
from ui.Ui_infowindow import Ui_infoWindow


try:
    _encoding = QtWidgets.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig)


def infoButton_clicked(self, button):
    query = sql_valueRead(self, 'windowsMessage', 'Button', button)
    if query:
        self.infoWindow = MyInfo(query[0][1])
        self.infoWindow.setMinimumSize(QtCore.QSize(450, self.infoWindow.sizeHint().height()))
        self.infoWindow.setMaximumSize(QtCore.QSize(450, self.infoWindow.sizeHint().height()))
        self.infoWindow.setGeometry(QCursor.pos().x() - 225, QCursor.pos().y() + 50, 450, 
                                    self.infoWindow.sizeHint().height())
    else:
        self.infoWindow = MyInfo("No information entered for this item.")
        self.infoWindow.setMinimumSize(QtCore.QSize(450, 100))
        self.infoWindow.setMaximumSize(QtCore.QSize(450, 100))
        self.infoWindow.setGeometry(QCursor.pos().x() - 225, QCursor.pos().y() + 50, 450, 150)
    self.infoWindow.exec_()


def plusButton_10_clicked(self, aircraft = None, operator = None, manufacturer = None, identification = None, country = None):
    if aircraft == None:
        if self.ai_aircraft_rl1.currentText() != "Make a choice...":
            if self.ai_aircraft_rl1.currentText() == "Other...":
                if (self.ai_manufacturer_ln.text() == "" or self.ai_type_ln.text() == "" or 
                    self.ai_operator_ln.text() == "" or self.ai_country_rl.currentText() == "Make a choice..." or 
                    self.ai_number_ln.text() == ""):
                    return
                else:
                    aircraft = self.ai_type_ln.text()
                    operator = self.ai_operator_ln.text()
                    manufacturer = self.ai_manufacturer_ln.text()
                    identification = self.ai_number_ln.text()
                    country = self.ai_country_rl.currentText()
            else:
                aircraft = str(self.ai_label_8.text())
                operator = str(self.ai_label_9.text())
                manufacturer = str(self.ai_label_7.text())
                identification = str(self.ai_label_11.text())
                country = str(self.ai_label_10.text())
            self.aircraft_list.append([manufacturer, aircraft, operator, country, identification])
            font1 = QtGui.QFont()
            font1.setFamily("font/SourceSansPro-Regular.ttf")
            font1.setPointSize(10)
            font1.setBold(True)
            font1.setUnderline(True)
            font1.setWeight(75)
            font1.setStyleStrategy(QtGui.QFont.PreferAntialias)
            font2 = QtGui.QFont()
            font2.setFamily("font/SourceSansPro-Regular.ttf")
            font2.setPointSize(10)
            font2.setBold(False)
            font2.setWeight(50)
            font2.setStyleStrategy(QtGui.QFont.PreferAntialias)
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("icons/del_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            tmp1 = QtWidgets.QHBoxLayout()
            self.ai_horlay_2.append(tmp1)
            self.ai_horlay_2[self.ai_acft].setObjectName("ai_horlay_2_" + str(self.ai_acft))
            spacer1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
            self.ai_horlay_2[self.ai_acft].addItem(spacer1)
            tmp2 = QtWidgets.QToolButton()
            self.ai_delbut_2.append(tmp2)
            self.ai_delbut_2[self.ai_acft].setMinimumSize(QtCore.QSize(27, 27))
            self.ai_delbut_2[self.ai_acft].setMaximumSize(QtCore.QSize(27, 27))
            self.ai_delbut_2[self.ai_acft].setText("")
            self.ai_delbut_2[self.ai_acft].setIcon(icon)
            self.ai_delbut_2[self.ai_acft].setIconSize(QtCore.QSize(27, 27))
            self.ai_delbut_2[self.ai_acft].setStyleSheet("QToolButton {\n"
            "    border: 1px solid transparent;\n"
            "    background-color: transparent;\n"
            "    width: 27px;\n"
            "    height: 27px;\n"
            "}\n"
            "\n"
            "QToolButton:hover {\n"
            "    border: 1px solid gray;\n"
            "    border-radius: 3px;\n"
            "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
            "}\n"
            "\n"
            "QToolButton:pressed {\n"
            "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
            "}\n"
            "\n"
            "QToolButton:flat {\n"
            "    border: none;\n"
            "}")
            self.ai_delbut_2[self.ai_acft].setAutoRaise(False)
            self.ai_delbut_2[self.ai_acft].setObjectName("ai_delButton_2_" + str(self.ai_acft))
            self.ai_horlay_2[self.ai_acft].addWidget(self.ai_delbut_2[self.ai_acft])
            spacer2 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
            self.ai_horlay_2[self.ai_acft].addItem(spacer2)
            tmp3 = QtWidgets.QLabel()
            self.ai_lab_5.append(tmp3)
            self.ai_lab_5[self.ai_acft].setFont(font1)
            self.ai_lab_5[self.ai_acft].setMinimumSize(QtCore.QSize(90, 30))
            self.ai_lab_5[self.ai_acft].setMaximumSize(QtCore.QSize(90, 30))
            self.ai_lab_5[self.ai_acft].setText("Operator:")
            self.ai_horlay_2[self.ai_acft].addWidget(self.ai_lab_5[self.ai_acft])
            tmp4 = QtWidgets.QLabel()
            self.ai_lab_6.append(tmp4)
            self.ai_lab_6[self.ai_acft].setFont(font2)
            self.ai_lab_6[self.ai_acft].setMinimumSize(QtCore.QSize(250, 30))
            self.ai_lab_6[self.ai_acft].setMaximumSize(QtCore.QSize(16777215, 30))
            self.ai_lab_6[self.ai_acft].setText(operator)
            self.ai_horlay_2[self.ai_acft].addWidget(self.ai_lab_6[self.ai_acft])
            spacer3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
            self.ai_horlay_2[self.ai_acft].addItem(spacer3)
            tmp5 = QtWidgets.QLabel()
            self.ai_lab_7.append(tmp5)
            self.ai_lab_7[self.ai_acft].setFont(font1)
            self.ai_lab_7[self.ai_acft].setMinimumSize(QtCore.QSize(60, 30))
            self.ai_lab_7[self.ai_acft].setMaximumSize(QtCore.QSize(60, 30))
            self.ai_lab_7[self.ai_acft].setText("Type:")
            self.ai_horlay_2[self.ai_acft].addWidget(self.ai_lab_7[self.ai_acft])
            tmp6 = QtWidgets.QLabel()
            self.ai_lab_8.append(tmp6)
            self.ai_lab_8[self.ai_acft].setFont(font2)
            self.ai_lab_8[self.ai_acft].setMinimumSize(QtCore.QSize(200, 30))
            self.ai_lab_8[self.ai_acft].setMaximumSize(QtCore.QSize(16777215, 30))
            self.ai_lab_8[self.ai_acft].setText(aircraft)
            self.ai_horlay_2[self.ai_acft].addWidget(self.ai_lab_8[self.ai_acft])
            spacer4 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.ai_horlay_2[self.ai_acft].addItem(spacer4)
            self.ai_delbut_2[self.ai_acft].clicked.connect(lambda: self.button_clicked())
            self.verticalLayout_21.addLayout(self.ai_horlay_2[self.ai_acft])
            self.ai_acft += 1
            self.modified = True
            self.make_window_title() 
    else:
        self.aircraft_list.append([manufacturer, aircraft, operator, country, identification])
        font1 = QtGui.QFont()
        font1.setFamily("font/SourceSansPro-Regular.ttf")
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setUnderline(True)
        font1.setWeight(75)
        font1.setStyleStrategy(QtGui.QFont.PreferAntialias)
        font2 = QtGui.QFont()
        font2.setFamily("font/SourceSansPro-Regular.ttf")
        font2.setPointSize(10)
        font2.setBold(False)
        font2.setWeight(50)
        font2.setStyleStrategy(QtGui.QFont.PreferAntialias)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/del_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        tmp1 = QtWidgets.QHBoxLayout()
        self.ai_horlay_2.append(tmp1)
        self.ai_horlay_2[self.ai_acft].setObjectName("ai_horlay_2_" + str(self.ai_acft))
        spacer1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.ai_horlay_2[self.ai_acft].addItem(spacer1)
        tmp2 = QtWidgets.QToolButton()
        self.ai_delbut_2.append(tmp2)
        self.ai_delbut_2[self.ai_acft].setMinimumSize(QtCore.QSize(27, 27))
        self.ai_delbut_2[self.ai_acft].setMaximumSize(QtCore.QSize(27, 27))
        self.ai_delbut_2[self.ai_acft].setText("")
        self.ai_delbut_2[self.ai_acft].setIcon(icon)
        self.ai_delbut_2[self.ai_acft].setIconSize(QtCore.QSize(27, 27))
        self.ai_delbut_2[self.ai_acft].setStyleSheet("QToolButton {\n"
        "    border: 1px solid transparent;\n"
        "    background-color: transparent;\n"
        "    width: 27px;\n"
        "    height: 27px;\n"
        "}\n"
        "\n"
        "QToolButton:hover {\n"
        "    border: 1px solid gray;\n"
        "    border-radius: 3px;\n"
        "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
        "}\n"
        "\n"
        "QToolButton:pressed {\n"
        "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
        "}\n"
        "\n"
        "QToolButton:flat {\n"
        "    border: none;\n"
        "}")
        self.ai_delbut_2[self.ai_acft].setAutoRaise(False)
        self.ai_delbut_2[self.ai_acft].setObjectName("ai_delButton_2_" + str(self.ai_acft))
        self.ai_horlay_2[self.ai_acft].addWidget(self.ai_delbut_2[self.ai_acft])
        spacer2 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.ai_horlay_2[self.ai_acft].addItem(spacer2)
        tmp3 = QtWidgets.QLabel()
        self.ai_lab_5.append(tmp3)
        self.ai_lab_5[self.ai_acft].setFont(font1)
        self.ai_lab_5[self.ai_acft].setMinimumSize(QtCore.QSize(90, 30))
        self.ai_lab_5[self.ai_acft].setMaximumSize(QtCore.QSize(90, 30))
        self.ai_lab_5[self.ai_acft].setText("Operator:")
        self.ai_horlay_2[self.ai_acft].addWidget(self.ai_lab_5[self.ai_acft])
        tmp4 = QtWidgets.QLabel()
        self.ai_lab_6.append(tmp4)
        self.ai_lab_6[self.ai_acft].setFont(font2)
        self.ai_lab_6[self.ai_acft].setMinimumSize(QtCore.QSize(250, 30))
        self.ai_lab_6[self.ai_acft].setMaximumSize(QtCore.QSize(16777215, 30))
        self.ai_lab_6[self.ai_acft].setText(operator)
        self.ai_horlay_2[self.ai_acft].addWidget(self.ai_lab_6[self.ai_acft])
        spacer3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.ai_horlay_2[self.ai_acft].addItem(spacer3)
        tmp5 = QtWidgets.QLabel()
        self.ai_lab_7.append(tmp5)
        self.ai_lab_7[self.ai_acft].setFont(font1)
        self.ai_lab_7[self.ai_acft].setMinimumSize(QtCore.QSize(60, 30))
        self.ai_lab_7[self.ai_acft].setMaximumSize(QtCore.QSize(60, 30))
        self.ai_lab_7[self.ai_acft].setText("Type:")
        self.ai_horlay_2[self.ai_acft].addWidget(self.ai_lab_7[self.ai_acft])
        tmp6 = QtWidgets.QLabel()
        self.ai_lab_8.append(tmp6)
        self.ai_lab_8[self.ai_acft].setFont(font2)
        self.ai_lab_8[self.ai_acft].setMinimumSize(QtCore.QSize(200, 30))
        self.ai_lab_8[self.ai_acft].setMaximumSize(QtCore.QSize(16777215, 30))
        self.ai_lab_8[self.ai_acft].setText(aircraft)
        self.ai_horlay_2[self.ai_acft].addWidget(self.ai_lab_8[self.ai_acft])
        spacer4 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.ai_horlay_2[self.ai_acft].addItem(spacer4) 
        self.verticalLayout_21.addLayout(self.ai_horlay_2[self.ai_acft])
        self.ai_delbut_2[self.ai_acft].clicked.connect(lambda: self.button_clicked())
        self.ai_acft += 1
  

def plusButton_9_clicked(self):
    model = self.ai_newname_ln.text()
    manufacturer = self.ai_newmanufacturer_ln.text()
    if model != "" and manufacturer !="":
        self.instModel_list.append(model)
        self.instManufacturer_list.append(manufacturer)
        font1 = QtGui.QFont()
        font1.setFamily("font/SourceSansPro-Regular.ttf")
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setUnderline(True)
        font1.setWeight(75)
        font1.setStyleStrategy(QtGui.QFont.PreferAntialias)
        font2 = QtGui.QFont()
        font2.setFamily("font/SourceSansPro-Regular.ttf")
        font2.setPointSize(10)
        font2.setBold(False)
        font2.setWeight(50)
        font2.setStyleStrategy(QtGui.QFont.PreferAntialias)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/del_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        tmp1 = QtWidgets.QHBoxLayout()
        self.ai_horlay.append(tmp1)
        self.ai_horlay[self.ai_inst].setObjectName("ai_horlay_" + str(self.ai_inst))
        spacer1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.ai_horlay[self.ai_inst].addItem(spacer1)
        tmp2 = QtWidgets.QToolButton()
        self.ai_delbut.append(tmp2)
        self.ai_delbut[self.ai_inst].setMinimumSize(QtCore.QSize(27, 27))
        self.ai_delbut[self.ai_inst].setMaximumSize(QtCore.QSize(27, 27))
        self.ai_delbut[self.ai_inst].setText("")
        self.ai_delbut[self.ai_inst].setIcon(icon)
        self.ai_delbut[self.ai_inst].setIconSize(QtCore.QSize(27, 27))
        self.ai_delbut[self.ai_inst].setStyleSheet("QToolButton {\n"
        "    border: 1px solid transparent;\n"
        "    background-color: transparent;\n"
        "    width: 27px;\n"
        "    height: 27px;\n"
        "}\n"
        "\n"
        "QToolButton:hover {\n"
        "    border: 1px solid gray;\n"
        "    border-radius: 3px;\n"
        "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
        "}\n"
        "\n"
        "QToolButton:pressed {\n"
        "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
        "}\n"
        "\n"
        "QToolButton:flat {\n"
        "    border: none;\n"
        "}")
        self.ai_delbut[self.ai_inst].setAutoRaise(False)
        self.ai_delbut[self.ai_inst].setObjectName("ai_delButton_" + str(self.ai_inst))
        self.ai_horlay[self.ai_inst].addWidget(self.ai_delbut[self.ai_inst])
        spacer2 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.ai_horlay[self.ai_inst].addItem(spacer2)
        tmp3 = QtWidgets.QLabel()
        self.ai_lab_1.append(tmp3)
        self.ai_lab_1[self.ai_inst].setFont(font1)
        self.ai_lab_1[self.ai_inst].setMinimumSize(QtCore.QSize(120, 30))
        self.ai_lab_1[self.ai_inst].setMaximumSize(QtCore.QSize(120, 30))
        self.ai_lab_1[self.ai_inst].setText("Manufacturer:")
        self.ai_horlay[self.ai_inst].addWidget(self.ai_lab_1[self.ai_inst])
        tmp4 = QtWidgets.QLabel()
        self.ai_lab_2.append(tmp4)
        self.ai_lab_2[self.ai_inst].setFont(font2)
        self.ai_lab_2[self.ai_inst].setMinimumSize(QtCore.QSize(250, 30))
        self.ai_lab_2[self.ai_inst].setMaximumSize(QtCore.QSize(16777215, 30))
        self.ai_lab_2[self.ai_inst].setText(manufacturer)
        self.ai_horlay[self.ai_inst].addWidget(self.ai_lab_2[self.ai_inst])
        spacer3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.ai_horlay[self.ai_inst].addItem(spacer3)
        tmp5 = QtWidgets.QLabel()
        self.ai_lab_3.append(tmp5)
        self.ai_lab_3[self.ai_inst].setFont(font1)
        self.ai_lab_3[self.ai_inst].setMinimumSize(QtCore.QSize(60, 30))
        self.ai_lab_3[self.ai_inst].setMaximumSize(QtCore.QSize(60, 30))
        self.ai_lab_3[self.ai_inst].setText("Model:")
        self.ai_horlay[self.ai_inst].addWidget(self.ai_lab_3[self.ai_inst])
        tmp6 = QtWidgets.QLabel()
        self.ai_lab_4.append(tmp6)
        self.ai_lab_4[self.ai_inst].setFont(font2)
        self.ai_lab_4[self.ai_inst].setMinimumSize(QtCore.QSize(200, 30))
        self.ai_lab_4[self.ai_inst].setMaximumSize(QtCore.QSize(16777215, 30))
        self.ai_lab_4[self.ai_inst].setText(model)
        self.ai_horlay[self.ai_inst].addWidget(self.ai_lab_4[self.ai_inst])
        spacer4 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.ai_horlay[self.ai_inst].addItem(spacer4) 
        self.verticalLayout_31.addLayout(self.ai_horlay[self.ai_inst])
        self.ai_delbut[self.ai_inst].clicked.connect(lambda: self.button_clicked())
        
        self.ai_inst += 1
        self.modified = True
        self.make_window_title()

def plusButton_8_clicked(self):
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap("icons/info_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    icon2 = QtGui.QIcon()
    icon2.addPixmap(QtGui.QPixmap("icons/del_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    font = QtGui.QFont()
    font.setFamily("font/SourceSansPro-Regular.ttf")
    font.setPointSize(10)
    font.setBold(False)
    font.setWeight(50)
    font.setStyleStrategy(QtGui.QFont.PreferAntialias)
    self.delButton_7.setEnabled(True)
    self.delButton_7.setIcon(icon2)
    self.mm_verlay_2.append(QtWidgets.QVBoxLayout())
    self.mm_verlay_2[self.mm_pofc].setObjectName("mm_verlay_2" + str(self.mm_pofc))
    self.mm_verlay_2[self.mm_pofc].addItem(QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed))
    self.mm_line_1.append(QtWidgets.QFrame())
    self.mm_line_1[self.mm_pofc].setFrameShape(QtWidgets.QFrame.HLine)
    self.mm_line_1[self.mm_pofc].setFrameShadow(QtWidgets.QFrame.Sunken)
    self.mm_line_1[self.mm_pofc].setObjectName("mm_line_1" + str(self.mm_pofc))
    self.mm_verlay_2[self.mm_pofc].addWidget(self.mm_line_1[self.mm_pofc])
    self.mm_verlay_2[self.mm_pofc].addItem(QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed))
    self.mm_horlay_3.append(QtWidgets.QHBoxLayout())
    self.mm_horlay_3[self.mm_pofc].setObjectName("mm_horlay_3" + str(self.mm_pofc))
    self.mm_verlay_1.append(QtWidgets.QVBoxLayout())
    self.mm_verlay_1[self.mm_pofc].setObjectName("mm_verlay_1" + str(self.mm_pofc))
    self.mm_horlay_1.append(QtWidgets.QHBoxLayout())
    self.mm_horlay_1[self.mm_pofc].setObjectName("mm_horlay_1" + str(self.mm_pofc))
    self.mm_lab_1.append(QtWidgets.QLabel())
    self.mm_lab_1[self.mm_pofc].setObjectName("mm_lab_1" + str(self.mm_pofc))
    self.mm_lab_1[self.mm_pofc].setFont(font)
    self.mm_horlay_1[self.mm_pofc].addWidget(self.mm_lab_1[self.mm_pofc])
    self.mm_conName_ln.append(QtWidgets.QLineEdit())
    self.mm_conName_ln[self.mm_pofc].setMinimumSize(QtCore.QSize(250, 27))
    self.mm_conName_ln[self.mm_pofc].setMaximumSize(QtCore.QSize(250, 27))
    self.mm_conName_ln[self.mm_pofc].setFrame(False)
    self.mm_conName_ln[self.mm_pofc].setFont(font)
    self.mm_conName_ln[self.mm_pofc].setStyleSheet("QLineEdit {border-radius: 3px; padding: 1px 4px"
                                                   + " 1px 4px; background-color: rgb(240, 240, 240);}")
    self.mm_conName_ln[self.mm_pofc].setObjectName("mm_conName_ln" + str(self.mm_pofc))
    self.mm_horlay_1[self.mm_pofc].addWidget(self.mm_conName_ln[self.mm_pofc])
    self.mm_verlay_1[self.mm_pofc].addLayout(self.mm_horlay_1[self.mm_pofc])
    self.mm_horlay_2.append(QtWidgets.QHBoxLayout())
    self.mm_horlay_2[self.mm_pofc].setObjectName("mm_horlay_2" + str(self.mm_pofc))
    self.mm_lab_2.append(QtWidgets.QLabel())
    self.mm_lab_2[self.mm_pofc].setFont(font)
    self.mm_lab_2[self.mm_pofc].setObjectName("mm_lab_2" + str(self.mm_pofc))
    self.mm_horlay_2[self.mm_pofc].addWidget(self.mm_lab_2[self.mm_pofc])
    self.mm_conEmail_ln.append(QtWidgets.QLineEdit())
    self.mm_conEmail_ln[self.mm_pofc].setMinimumSize(QtCore.QSize(250, 27))
    self.mm_conEmail_ln[self.mm_pofc].setMaximumSize(QtCore.QSize(250, 27))
    self.mm_conEmail_ln[self.mm_pofc].setFrame(False)
    self.mm_conEmail_ln[self.mm_pofc].setFont(font)
    self.mm_conEmail_ln[self.mm_pofc].setStyleSheet("QLineEdit {border-radius: 3px; padding: 1px 4p"
                                                    + "x 1px 4px; background-color: rgb(240, 240, 240);}")
    self.mm_conEmail_ln[self.mm_pofc].setObjectName("mm_conEmail_ln" + str(self.mm_pofc))
    self.mm_horlay_2[self.mm_pofc].addWidget(self.mm_conEmail_ln[self.mm_pofc])
    self.mm_verlay_1[self.mm_pofc].addLayout(self.mm_horlay_2[self.mm_pofc])
    self.mm_horlay_3[self.mm_pofc].addLayout(self.mm_verlay_1[self.mm_pofc])
    self.mm_horlay_3[self.mm_pofc].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum))
    self.mm_delBut.append(QtWidgets.QToolButton())
    self.mm_delBut[self.mm_pofc].setMinimumSize(QtCore.QSize(27, 27))
    self.mm_delBut[self.mm_pofc].setMaximumSize(QtCore.QSize(27, 27))
    self.mm_delBut[self.mm_pofc].setText("")
    self.mm_delBut[self.mm_pofc].setIcon(icon2)
    self.mm_delBut[self.mm_pofc].setIconSize(QtCore.QSize(27, 27))
    self.mm_delBut[self.mm_pofc].setStyleSheet("QToolButton {\n"
    "    border: 1px solid transparent;\n"
    "    background-color: transparent;\n"
    "    width: 27px;\n"
    "    height: 27px;\n"
    "}\n"
    "\n"
    "QToolButton:hover {\n"
    "    border: 1px solid gray;\n"
    "    border-radius: 3px;\n"
    "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
    "}\n"
    "\n"
    "QToolButton:pressed {\n"
    "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
    "}\n"
    "\n"
    "QToolButton:flat {\n"
    "    border: none;\n"
    "}")
    self.mm_delBut[self.mm_pofc].setAutoRaise(True)
    self.mm_delBut[self.mm_pofc].setObjectName("mm_delBut_" + str(self.mm_pofc))
    self.mm_horlay_3[self.mm_pofc].addWidget(self.mm_delBut[self.mm_pofc])
    self.mm_verlay_2[self.mm_pofc].addLayout(self.mm_horlay_3[self.mm_pofc])
    self.verticalLayout_14.addLayout(self.mm_verlay_2[self.mm_pofc])
    self.mm_lab_1[self.mm_pofc].setText("Name:")
    self.mm_lab_2[self.mm_pofc].setText("E-mail:")
    self.mm_delBut[self.mm_pofc].clicked.connect(lambda: self.button_clicked())
    self.mm_pofc += 1
    self.modified = True
    self.make_window_title()

def plusButton_7_clicked(self):
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap("icons/none_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    icon2 = QtGui.QIcon()
    icon2.addPixmap(QtGui.QPixmap("icons/del_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    font = QtGui.QFont()
    font.setFamily("font/SourceSansPro-Regular.ttf")
    font.setPointSize(10)
    font.setBold(False)
    font.setWeight(50)
    font.setStyleStrategy(QtGui.QFont.PreferAntialias)
    self.delButton_8.setEnabled(True)
    self.delButton_8.setIcon(icon2)
    self.ro_verlay_2.append(QtWidgets.QVBoxLayout())
    self.ro_verlay_2[self.ro_roPy].setObjectName("ro_verlay_2" + str(self.ro_roPy))
    self.ro_verlay_2[self.ro_roPy].addItem(QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed))
    self.ro_line_1.append(QtWidgets.QFrame())
    self.ro_line_1[self.ro_roPy].setFrameShape(QtWidgets.QFrame.HLine)
    self.ro_line_1[self.ro_roPy].setFrameShadow(QtWidgets.QFrame.Sunken)
    self.ro_line_1[self.ro_roPy].setObjectName("ro_line_1" + str(self.ro_roPy))
    self.ro_verlay_2[self.ro_roPy].addWidget(self.ro_line_1[self.ro_roPy])
    self.ro_verlay_2[self.ro_roPy].addItem(QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed))
    self.ro_grilay_1.append(QtWidgets.QGridLayout())
    self.ro_grilay_1[self.ro_roPy].setVerticalSpacing(30)
    self.ro_grilay_1[self.ro_roPy].setObjectName("gridLayout_9" + str([self.ro_roPy]))
    self.ro_verlay_2[self.ro_roPy].addLayout(self.ro_grilay_1[self.ro_roPy])
    self.ro_lab_1.append(QtWidgets.QLabel())
    self.ro_lab_1[self.ro_roPy].setFont(font)
    self.ro_lab_1[self.ro_roPy].setObjectName("ro_lab_1" + str(self.ro_roPy))
    self.ro_lab_1[self.ro_roPy].setMinimumSize(QtCore.QSize(0, 0))
    self.ro_lab_1[self.ro_roPy].setMaximumSize(QtCore.QSize(16777215, 16777215))
    self.ro_grilay_1[self.ro_roPy].addWidget(self.ro_lab_1[self.ro_roPy], 0, 0, 1, 1)
    self.ro_rlPy_ln.append(QtWidgets.QLineEdit())
    self.ro_rlPy_ln[self.ro_roPy].setMinimumSize(QtCore.QSize(250, 27))
    self.ro_rlPy_ln[self.ro_roPy].setMaximumSize(QtCore.QSize(250, 27))
    self.ro_rlPy_ln[self.ro_roPy].setFrame(False)
    self.ro_rlPy_ln[self.ro_roPy].setFont(font)
    self.ro_rlPy_ln[self.ro_roPy].setStyleSheet("QLineEdit {border-radius: 3px; padding: 1px 4px 1p"
                                                + "x 4px; background-color: rgb(240, 240, 240);}")
    self.ro_rlPy_ln[self.ro_roPy].setObjectName("ro_rlPy_ln" + str(self.ro_roPy))
    self.ro_grilay_1[self.ro_roPy].addWidget(self.ro_rlPy_ln[self.ro_roPy], 0, 1, 1, 1)
    self.ro_infBut_1.append(QtWidgets.QToolButton())
    self.ro_infBut_1[self.ro_roPy].setMaximumSize(QtCore.QSize(27, 27))
    self.ro_infBut_1[self.ro_roPy].setText("")
    self.ro_infBut_1[self.ro_roPy].setIcon(icon)
    self.ro_infBut_1[self.ro_roPy].setIconSize(QtCore.QSize(27, 27))
    self.ro_infBut_1[self.ro_roPy].setObjectName("ro_infBut_1" + str(self.ro_roPy))
    self.ro_infBut_1[self.ro_roPy].setEnabled(False)
    self.ro_infBut_1[self.ro_roPy].setStyleSheet("QToolButton {\n"
    "    border: 1px solid transparent;\n"
    "    background-color: transparent;\n"
    "    width: 27px;\n"
    "    height: 27px;\n"
    "}\n"
    "\n"
    "QToolButton:hover {\n"
    "    border: 1px solid gray;\n"
    "    border-radius: 3px;\n"
    "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
    "}\n"
    "\n"
    "QToolButton:pressed {\n"
    "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
    "}\n"
    "\n"
    "QToolButton:flat {\n"
    "    border: none;\n"
    "}")
    self.ro_infBut_1[self.ro_roPy].setAutoRaise(True)
    self.ro_grilay_1[self.ro_roPy].addWidget(self.ro_infBut_1[self.ro_roPy], 0, 2, 1, 1)
    self.ro_lab_2.append(QtWidgets.QLabel())
    self.ro_lab_2[self.ro_roPy].setFont(font)
    self.ro_lab_2[self.ro_roPy].setObjectName("ro_lab_2" + str(self.ro_roPy))
    self.ro_lab_2[self.ro_roPy].setMinimumSize(QtCore.QSize(0, 0))
    self.ro_lab_2[self.ro_roPy].setMaximumSize(QtCore.QSize(16777215, 16777215))
    self.ro_grilay_1[self.ro_roPy].addWidget(self.ro_lab_2[self.ro_roPy], 1, 0, 1, 1)
    self.ro_rlEm_ln.append(QtWidgets.QLineEdit())
    self.ro_rlEm_ln[self.ro_roPy].setMinimumSize(QtCore.QSize(250, 27))
    self.ro_rlEm_ln[self.ro_roPy].setMaximumSize(QtCore.QSize(250, 27))
    self.ro_rlEm_ln[self.ro_roPy].setFrame(False)
    self.ro_rlEm_ln[self.ro_roPy].setFont(font)
    self.ro_rlEm_ln[self.ro_roPy].setStyleSheet("QLineEdit {border-radius: 3px; padding: 1px 4px 1p"
                                                + "x 4px; background-color: rgb(240, 240, 240);}")
    self.ro_rlEm_ln[self.ro_roPy].setObjectName("ro_rlEm_ln" + str(self.ro_roPy))
    self.ro_grilay_1[self.ro_roPy].addWidget(self.ro_rlEm_ln[self.ro_roPy], 1, 1, 1, 1)
    self.ro_infBut_2.append(QtWidgets.QToolButton())
    self.ro_infBut_2[self.ro_roPy].setMaximumSize(QtCore.QSize(27, 27))
    self.ro_infBut_2[self.ro_roPy].setText("")
    self.ro_infBut_2[self.ro_roPy].setIcon(icon)
    self.ro_infBut_2[self.ro_roPy].setIconSize(QtCore.QSize(27, 27))
    self.ro_infBut_2[self.ro_roPy].setObjectName("ro_infBut_2" + str(self.ro_roPy))
    self.ro_infBut_2[self.ro_roPy].setEnabled(False)
    self.ro_infBut_2[self.ro_roPy].setStyleSheet("QToolButton {\n"
    "    border: 1px solid transparent;\n"
    "    background-color: transparent;\n"
    "    width: 27px;\n"
    "    height: 27px;\n"
    "}\n"
    "\n"
    "QToolButton:hover {\n"
    "    border: 1px solid gray;\n"
    "    border-radius: 3px;\n"
    "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
    "}\n"
    "\n"
    "QToolButton:pressed {\n"
    "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
    "}\n"
    "\n"
    "QToolButton:flat {\n"
    "    border: none;\n"
    "}")
    self.ro_infBut_2[self.ro_roPy].setAutoRaise(True)
    self.ro_grilay_1[self.ro_roPy].addWidget(self.ro_infBut_2[self.ro_roPy], 1, 2, 1, 1)
    
    self.ro_grilay_1[self.ro_roPy].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.
                                                    QSizePolicy.Minimum), 1, 3, 1, 1)
    self.ro_delBut.append(QtWidgets.QToolButton())
    self.ro_delBut[self.ro_roPy].setMinimumSize(QtCore.QSize(27, 27))
    self.ro_delBut[self.ro_roPy].setMaximumSize(QtCore.QSize(27, 27))
    self.ro_delBut[self.ro_roPy].setText("")
    self.ro_delBut[self.ro_roPy].setIcon(icon2)
    self.ro_delBut[self.ro_roPy].setIconSize(QtCore.QSize(27, 27))
    self.ro_delBut[self.ro_roPy].setStyleSheet("QToolButton {\n"
    "    border: 1px solid transparent;\n"
    "    background-color: transparent;\n"
    "    width: 27px;\n"
    "    height: 27px;\n"
    "}\n"
    "\n"
    "QToolButton:hover {\n"
    "    border: 1px solid gray;\n"
    "    border-radius: 3px;\n"
    "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
    "}\n"
    "\n"
    "QToolButton:pressed {\n"
    "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
    "}\n"
    "\n"
    "QToolButton:flat {\n"
    "    border: none;\n"
    "}")
    self.ro_delBut[self.ro_roPy].setAutoRaise(True)
    self.ro_delBut[self.ro_roPy].setObjectName("ro_delBut_" + str(self.ro_roPy))
    self.ro_grilay_1[self.ro_roPy].addWidget(self.ro_delBut[self.ro_roPy], 1, 4, 1, 1)
    self.ro_grilay_1[self.ro_roPy].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.
                                                Expanding, QtWidgets.QSizePolicy.Minimum), 1, 5, 1, 1)
    self.ro_lab_3.append(QtWidgets.QLabel())
    self.ro_lab_3[self.ro_roPy].setFont(font)
    self.ro_lab_3[self.ro_roPy].setMinimumSize(QtCore.QSize(0, 0))
    self.ro_lab_3[self.ro_roPy].setMaximumSize(QtCore.QSize(16777215, 16777215))
    self.ro_lab_3[self.ro_roPy].setObjectName("ro_lab_3" + str(self.ro_roPy))
    self.ro_grilay_1[self.ro_roPy].addWidget(self.ro_lab_3[self.ro_roPy], 2, 0, 1, 1)
    self.ro_rlRl_ln.append(QtWidgets.QComboBox())
    self.ro_rlRl_ln[self.ro_roPy].setMinimumSize(QtCore.QSize(200, 27))
    self.ro_rlRl_ln[self.ro_roPy].setMaximumSize(QtCore.QSize(200, 27))
    self.ro_rlRl_ln[self.ro_roPy].setObjectName("ro_rlRl_ln" + str(self.ro_roPy))
    for i in range(11):  # @UnusedVariable
        self.ro_rlRl_ln[self.ro_roPy].addItem("")
    self.ro_rlRl_ln[self.ro_roPy].setFont(font)
    self.ro_rlRl_ln[self.ro_roPy].setStyleSheet("QComboBox {\n"
    "    border: 1px solid #acacac;\n"
    "    border-radius: 1px;\n"
    "    padding-left: 5px;\n"
    "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
    "                                stop: 0 #f0f0f0, stop: 1 #e5e5e5);\n"
    "}\n"
    "\n"
    "QComboBox:disabled {\n"
    "    background-color:  rgb(200,200,200);\n"
    "}\n"
    "\n"
    "QComboBox:hover {\n"
    "    border: 1px solid #7eb4ea;\n"
    "    border-radius: 1px;\n"
    "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
    "                                stop: 0 #ecf4fc, stop: 1 #dcecfc);\n"
    "}\n"
    "\n"
    "QComboBox::drop-down {\n"
    "    subcontrol-origin: padding;\n"
    "    subcontrol-position: top right;\n"
    "    width: 27px;\n"
    "    border-top-right-radius: 3px;\n"
    "    border-bottom-right-radius: 3px;\n"
    "}\n"
    "\n"
    "QComboBox::drop-down:hover {\n"
    "    subcontrol-origin: padding;\n"
    "    subcontrol-position: top right;\n"
    "    width: 27px;\n"
    "    border-left-width: 1px;\n"
    "    border-left-color: darkgray;\n"
    "    border-left-style: solid;\n"
    "    border-top-right-radius: 3px;\n"
    "    border-bottom-right-radius: 3px;\n"
    "}\n"
    "\n"
    "QComboBox::down-arrow {\n"
    "    image: url(icons/arrow_down.png); \n"
    "    width: 18px;\n"
    "    height: 18px\n"
    "}\n"
    "\n"
    "QComboBox::down-arrow:on {\n"
    "    top: 1px; \n"
    "    left: 1px;\n"
    "}\n"
    "\n"
    "QComboBox QAbstractItemView {\n"
    "    selection-background-color: transparent;\n"
    "    selection-color: blue;\n"
    "    border: 0px, solid black;\n"
    "}")
    self.ro_grilay_1[self.ro_roPy].addWidget(self.ro_rlRl_ln[self.ro_roPy], 2, 1, 1, 1)
    self.ro_infBut_3.append(QtWidgets.QToolButton())
    self.ro_infBut_3[self.ro_roPy].setMaximumSize(QtCore.QSize(27, 27))
    self.ro_infBut_3[self.ro_roPy].setText("")
    self.ro_infBut_3[self.ro_roPy].setIcon(icon)
    self.ro_infBut_3[self.ro_roPy].setIconSize(QtCore.QSize(27, 27))
    self.ro_infBut_3[self.ro_roPy].setObjectName("ro_infBut_3" + str(self.ro_roPy))
    self.ro_infBut_3[self.ro_roPy].setEnabled(False)
    self.ro_infBut_3[self.ro_roPy].setStyleSheet("QToolButton {\n"
    "    border: 1px solid transparent;\n"
    "    background-color: transparent;\n"
    "    width: 27px;\n"
    "    height: 27px;\n"
    "}\n"
    "\n"
    "QToolButton:hover {\n"
    "    border: 1px solid gray;\n"
    "    border-radius: 3px;\n"
    "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
    "}\n"
    "\n"
    "QToolButton:pressed {\n"
    "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
    "}\n"
    "\n"
    "QToolButton:flat {\n"
    "    border: none;\n"
    "}")
    self.ro_infBut_3[self.ro_roPy].setAutoRaise(True)
    self.ro_grilay_1[self.ro_roPy].addWidget(self.ro_infBut_3[self.ro_roPy], 2, 2, 1, 1)
    self.verticalLayout_18.addLayout(self.ro_verlay_2[self.ro_roPy])
    self.ro_lab_1[self.ro_roPy].setText("Responsible party:")
    self.ro_lab_2[self.ro_roPy].setText("Responsible party e-mail:")
    self.ro_lab_3[self.ro_roPy].setText("Responsible party role:")
    self.ro_rlRl_ln[self.ro_roPy].setCurrentIndex(5)
    self.ro_rlRl_ln[self.ro_roPy].setItemText(0, "Author")
    self.ro_rlRl_ln[self.ro_roPy].setItemText(1, "Custodian")
    self.ro_rlRl_ln[self.ro_roPy].setItemText(2, "Distributor")
    self.ro_rlRl_ln[self.ro_roPy].setItemText(3, "Originator")
    self.ro_rlRl_ln[self.ro_roPy].setItemText(4, "Owner")
    self.ro_rlRl_ln[self.ro_roPy].setItemText(5, "Point of Contact")
    self.ro_rlRl_ln[self.ro_roPy].setItemText(6, "Principal Investigator")
    self.ro_rlRl_ln[self.ro_roPy].setItemText(7, "Processor")
    self.ro_rlRl_ln[self.ro_roPy].setItemText(8, "Publisher")
    self.ro_rlRl_ln[self.ro_roPy].setItemText(9, "Resource Provider")
    self.ro_rlRl_ln[self.ro_roPy].setItemText(10, "User")
    self.ro_delBut[self.ro_roPy].clicked.connect(lambda: self.button_clicked())
    self.ro_roPy += 1
    self.modified = True
    self.make_window_title()

def plusButton_6_clicked(self):
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap("icons/del_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    font1 = QtGui.QFont()
    font1.setFamily("font/SourceSansPro-Regular.ttf")
    font1.setPointSize(10)
    font1.setBold(False)
    font1.setWeight(50)
    font1.setStyleStrategy(QtGui.QFont.PreferAntialias)
    self.delButton_6.setEnabled(True)
    self.delButton_6.setIcon(icon)
    self.au_horlay_2.append(QtWidgets.QHBoxLayout())
    self.au_horlay_2[self.au_wn_2].setObjectName("au_horlay_2" + str(self.au_wn_2))
    self.au_wn_lim_ta.append(QtWidgets.QPlainTextEdit())
    self.au_wn_lim_ta[self.au_wn_2].setMinimumSize(QtCore.QSize(450, 100))
    self.au_wn_lim_ta[self.au_wn_2].setMaximumSize(QtCore.QSize(16777215, 100))
    self.au_wn_lim_ta[self.au_wn_2].setFrameShape(QtWidgets.QFrame.NoFrame)
    self.au_wn_lim_ta[self.au_wn_2].setObjectName("au_wn_lim_ta" + str(self.au_wn_2))
    self.au_wn_lim_ta[self.au_wn_2].setFont(font1)
    self.au_wn_lim_ta[self.au_wn_2].setStyleSheet("QPlainTextEdit {border-radius: 3px; padding: 1px 4px 1px 4px; background-color: rgb(240, 240, 240);}")
    self.au_horlay_2[self.au_wn_2].addWidget(self.au_wn_lim_ta[self.au_wn_2])
    self.au_delBut_2.append(QtWidgets.QToolButton())
    self.au_delBut_2[self.au_wn_2].setObjectName("au_delBut_2_" + str(self.au_wn_2))
    self.au_delBut_2[self.au_wn_2].setMinimumSize(QtCore.QSize(27, 27))
    self.au_delBut_2[self.au_wn_2].setMaximumSize(QtCore.QSize(27, 27))
    self.au_delBut_2[self.au_wn_2].setText("")
    self.au_delBut_2[self.au_wn_2].setIcon(icon)
    self.au_delBut_2[self.au_wn_2].setIconSize(QtCore.QSize(27, 27))
    self.au_delBut_2[self.au_wn_2].setStyleSheet("QToolButton {\n"
    "    border: 1px solid transparent;\n"
    "    background-color: transparent;\n"
    "    width: 27px;\n"
    "    height: 27px;\n"
    "}\n"
    "\n"
    "QToolButton:hover {\n"
    "    border: 1px solid gray;\n"
    "    border-radius: 3px;\n"
    "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
    "}\n"
    "\n"
    "QToolButton:pressed {\n"
    "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
    "}\n"
    "\n"
    "QToolButton:flat {\n"
    "    border: none;\n"
    "}")
    self.au_delBut_2[self.au_wn_2].setAutoRaise(True)
    self.au_horlay_2[self.au_wn_2].addWidget(self.au_delBut_2[self.au_wn_2])
    self.verticalLayout_10.addLayout(self.au_horlay_2[self.au_wn_2])
    self.au_delBut_2[self.au_wn_2].clicked.connect(lambda: self.button_clicked())
    self.au_wn_2 += 1
    self.modified = True
    self.make_window_title()

def plusButton_5_clicked(self):
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap("icons/del_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    font1 = QtGui.QFont()
    font1.setFamily("font/SourceSansPro-Regular.ttf")
    font1.setPointSize(10)
    font1.setBold(False)
    font1.setWeight(50)
    font1.setStyleStrategy(QtGui.QFont.PreferAntialias)
    self.delButton_5.setEnabled(True)
    self.delButton_5.setIcon(icon)
    self.au_horlay_1.append(QtWidgets.QHBoxLayout())
    self.au_horlay_1[self.au_wn_1].setObjectName("au_horlay_1" + str(self.au_wn_1))
    self.au_wn_con_ta.append(QtWidgets.QPlainTextEdit())
    self.au_wn_con_ta[self.au_wn_1].setMinimumSize(QtCore.QSize(450, 100))
    self.au_wn_con_ta[self.au_wn_1].setMaximumSize(QtCore.QSize(16777215, 100))
    self.au_wn_con_ta[self.au_wn_1].setFrameShape(QtWidgets.QFrame.NoFrame)
    self.au_wn_con_ta[self.au_wn_1].setObjectName("au_wn_con_ta" + str(self.au_wn_1))
    self.au_wn_con_ta[self.au_wn_1].setFont(font1)
    self.au_wn_con_ta[self.au_wn_1].setStyleSheet("QPlainTextEdit {border-radius: 3px; padding: 1px 4px 1px 4px; background-color: rgb(240, 240, 240);}")
    self.au_horlay_1[self.au_wn_1].addWidget(self.au_wn_con_ta[self.au_wn_1])
    self.au_delBut_1.append(QtWidgets.QToolButton())
    self.au_delBut_1[self.au_wn_1].setObjectName("au_delBut_1_" + str(self.au_wn_1))
    self.au_delBut_1[self.au_wn_1].setMinimumSize(QtCore.QSize(27, 27))
    self.au_delBut_1[self.au_wn_1].setMaximumSize(QtCore.QSize(27, 27))
    self.au_delBut_1[self.au_wn_1].setText("")
    self.au_delBut_1[self.au_wn_1].setIcon(icon)
    self.au_delBut_1[self.au_wn_1].setIconSize(QtCore.QSize(27, 27))
    self.au_delBut_1[self.au_wn_1].setStyleSheet("QToolButton {\n"
    "    border: 1px solid transparent;\n"
    "    background-color: transparent;\n"
    "    width: 27px;\n"
    "    height: 27px;\n"
    "}\n"
    "\n"
    "QToolButton:hover {\n"
    "    border: 1px solid gray;\n"
    "    border-radius: 3px;\n"
    "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
    "}\n"
    "\n"
    "QToolButton:pressed {\n"
    "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
    "}\n"
    "\n"
    "QToolButton:flat {\n"
    "    border: none;\n"
    "}")
    self.au_delBut_1[self.au_wn_1].setAutoRaise(True)
    self.au_horlay_1[self.au_wn_1].addWidget(self.au_delBut_1[self.au_wn_1])
    self.verticalLayout_4.addLayout(self.au_horlay_1[self.au_wn_1])
    self.au_delBut_1[self.au_wn_1].clicked.connect(lambda: self.button_clicked())
    self.au_wn_1 += 1
    self.modified = True
    self.make_window_title()

def plusButton_4_clicked(self, instrument=None):
    if instrument == None:
        instrument = str(self.ai_instrument_rl1.currentText())
    if instrument != "Make a choice...":
        index = instrument.find(" - ")
        manufacturer = instrument[: index]
        model = instrument[(index + 3):]
        try:
            index = self.instModel_list.index(model)
            if self.instManufacturer_list[index] == manufacturer:
                return
        except ValueError:
            index = 0
        self.instModel_list.append(model)
        self.instManufacturer_list.append(manufacturer)
        font1 = QtGui.QFont()
        font1.setFamily("font/SourceSansPro-Regular.ttf")
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setUnderline(True)
        font1.setWeight(75)
        font1.setStyleStrategy(QtGui.QFont.PreferAntialias)
        font2 = QtGui.QFont()
        font2.setFamily("font/SourceSansPro-Regular.ttf")
        font2.setPointSize(10)
        font2.setBold(False)
        font2.setWeight(50)
        font2.setStyleStrategy(QtGui.QFont.PreferAntialias)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/del_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ai_horlay.append(QtWidgets.QHBoxLayout())
        self.ai_horlay[self.ai_inst].setObjectName("ai_horlay_" + str(self.ai_inst))
        self.ai_horlay[self.ai_inst].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum))
        self.ai_delbut.append(QtWidgets.QToolButton())
        self.ai_delbut[self.ai_inst].setMinimumSize(QtCore.QSize(27, 27))
        self.ai_delbut[self.ai_inst].setMaximumSize(QtCore.QSize(27, 27))
        self.ai_delbut[self.ai_inst].setText("")
        self.ai_delbut[self.ai_inst].setIcon(icon)
        self.ai_delbut[self.ai_inst].setIconSize(QtCore.QSize(27, 27))
        self.ai_delbut[self.ai_inst].setStyleSheet("QToolButton {\n"
            "    border: 1px solid transparent;\n"
            "    background-color: transparent;\n"
            "    width: 27px;\n"
            "    height: 27px;\n"
            "}\n"
            "\n"
            "QToolButton:hover {\n"
            "    border: 1px solid gray;\n"
            "    border-radius: 3px;\n"
            "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
            "}\n"
            "\n"
            "QToolButton:pressed {\n"
            "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
            "}\n"
            "\n"
            "QToolButton:flat {\n"
            "    border: none;\n"
            "}")
        self.ai_delbut[self.ai_inst].setAutoRaise(True)
        self.ai_delbut[self.ai_inst].setObjectName("ai_delButton_" + str(self.ai_inst))
        
        self.ai_horlay[self.ai_inst].addWidget(self.ai_delbut[self.ai_inst])
        self.ai_horlay[self.ai_inst].addItem(QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum))
        self.ai_lab_1.append(QtWidgets.QLabel())
        self.ai_lab_1[self.ai_inst].setFont(font1)
        self.ai_lab_1[self.ai_inst].setMinimumSize(QtCore.QSize(120, 30))
        self.ai_lab_1[self.ai_inst].setMaximumSize(QtCore.QSize(120, 30))
        self.ai_lab_1[self.ai_inst].setText("Manufacturer:")
        self.ai_horlay[self.ai_inst].addWidget(self.ai_lab_1[self.ai_inst])
        self.ai_lab_2.append(QtWidgets.QLabel())
        self.ai_lab_2[self.ai_inst].setFont(font2)
        self.ai_lab_2[self.ai_inst].setMinimumSize(QtCore.QSize(250, 30))
        self.ai_lab_2[self.ai_inst].setMaximumSize(QtCore.QSize(16777215, 30))
        self.ai_lab_2[self.ai_inst].setText(manufacturer)
        self.ai_horlay[self.ai_inst].addWidget(self.ai_lab_2[self.ai_inst])
        self.ai_horlay[self.ai_inst].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum))
        self.ai_lab_3.append(QtWidgets.QLabel())
        self.ai_lab_3[self.ai_inst].setFont(font1)
        self.ai_lab_3[self.ai_inst].setMinimumSize(QtCore.QSize(60, 30))
        self.ai_lab_3[self.ai_inst].setMaximumSize(QtCore.QSize(60, 30))
        self.ai_lab_3[self.ai_inst].setText("Model:")
        self.ai_horlay[self.ai_inst].addWidget(self.ai_lab_3[self.ai_inst])
        self.ai_lab_4.append(QtWidgets.QLabel())
        self.ai_lab_4[self.ai_inst].setFont(font2)
        self.ai_lab_4[self.ai_inst].setMinimumSize(QtCore.QSize(200, 30))
        self.ai_lab_4[self.ai_inst].setMaximumSize(QtCore.QSize(16777215, 30))
        self.ai_lab_4[self.ai_inst].setText(model)
        self.ai_horlay[self.ai_inst].addWidget(self.ai_lab_4[self.ai_inst])
        self.ai_horlay[self.ai_inst].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))
        self.verticalLayout_31.addLayout(self.ai_horlay[self.ai_inst])
        self.ai_delbut[self.ai_inst].clicked.connect(lambda: self.button_clicked())
        
        self.ai_inst += 1
        self.modified = True
        self.make_window_title()

def plusButton_3_clicked(self):
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap("icons/info_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    icon2 = QtGui.QIcon()
    icon2.addPixmap(QtGui.QPixmap("icons/del_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    font = QtGui.QFont()
    font.setFamily("font/SourceSansPro-Regular.ttf")
    font.setPointSize(10)
    font.setBold(False)
    font.setWeight(50)
    font.setStyleStrategy(QtGui.QFont.PreferAntialias)
    self.delButton_10.setEnabled(True)
    self.delButton_10.setIcon(icon2)
    self.tr_horlay_1.append(QtWidgets.QHBoxLayout())
    self.tr_horlay_1[self.tr_tpex].setObjectName("tr_horlay_1" + str(self.mm_pofc))
    self.tr_lab_1.append(QtWidgets.QLabel())
    self.tr_lab_1[self.tr_tpex].setFont(font)
    self.tr_lab_1[self.tr_tpex].setMinimumSize(QtCore.QSize(60, 30))
    self.tr_lab_1[self.tr_tpex].setMaximumSize(QtCore.QSize(60, 30))
    self.tr_lab_1[self.tr_tpex].setObjectName("tr_lab_1" + str(self.tr_tpex))
    self.tr_horlay_1[self.tr_tpex].addWidget(self.tr_lab_1[self.tr_tpex])
    self.tr_horlay_1[self.tr_tpex].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum))
    self.tr_dtSt_1.append(QtWidgets.QDateEdit())
    self.tr_dtSt_1[self.tr_tpex].setMinimumSize(QtCore.QSize(130, 27))
    self.tr_dtSt_1[self.tr_tpex].setMaximumSize(QtCore.QSize(130, 27))
    self.tr_dtSt_1[self.tr_tpex].setDate(QtCore.QDate(2014, 10, 28))
    self.tr_dtSt_1[self.tr_tpex].setCurrentSection(QtWidgets.QDateTimeEdit.YearSection)
    self.tr_dtSt_1[self.tr_tpex].setAlignment(QtCore.Qt.AlignCenter)
    self.tr_dtSt_1[self.tr_tpex].setCalendarPopup(True)
    self.tr_dtSt_1[self.tr_tpex].setFont(font)
    self.tr_dtSt_1[self.tr_tpex].setStyleSheet("QDateEdit {\n"
    "    border: 1px solid #acacac;\n"
    "    border-radius: 1px;\n"
    "    padding-left: 5px;\n"
    "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
    "                                stop: 0 #f0f0f0, stop: 1 #e5e5e5);\n"
    "}\n"
    "\n"
    "QDateEdit:hover {\n"
    "    border: 1px solid #7eb4ea;\n"
    "    border-radius: 1px;\n"
    "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
    "                                stop: 0 #ecf4fc, stop: 1 #dcecfc);\n"
    "}\n"
    "\n"
    "QDateEdit::drop-down  {\n"
    "    subcontrol-origin: padding;\n"
    "    subcontrol-position: top right;\n"
    "    width: 27px;\n"
    "    border-top-right-radius: 3px;\n"
    "    border-bottom-right-radius: 3px;\n"
    "}\n"
    "\n"
    "QDateEdit::drop-down:hover{\n"
    "    subcontrol-origin: padding;\n"
    "    subcontrol-position: top right;\n"
    "    width: 27px;\n"
    "    border-left-width: 1px;\n"
    "    border-left-color: darkgray;\n"
    "    border-left-style: solid;\n"
    "    border-top-right-radius: 3px;\n"
    "    border-bottom-right-radius: 3px;\n"
    "}\n"
    "\n"
    "QDateEdit::down-arrow {\n"
    "    image: url(icons/arrow_down.png);\n"
    "    width: 18px;\n"
    "    height: 18px;\n"
    "}\n"
    "\n"
    "QDateEdit::down-arrow:on {\n"
    "    top: 1px;\n"
    "    left: 1px;\n"
    "}")
    self.tr_dtSt_1[self.tr_tpex].setObjectName("tr_dtSt_1" + str(self.tr_tpex))
    self.tr_horlay_1[self.tr_tpex].addWidget(self.tr_dtSt_1[self.tr_tpex])
    self.tr_horlay_1[self.tr_tpex].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum))
    self.tr_dtEd_1.append(QtWidgets.QDateEdit())
    self.tr_dtEd_1[self.tr_tpex].setMinimumSize(QtCore.QSize(130, 27))
    self.tr_dtEd_1[self.tr_tpex].setMaximumSize(QtCore.QSize(130, 27))
    self.tr_dtEd_1[self.tr_tpex].setDate(QtCore.QDate(2014, 10, 28))
    self.tr_dtEd_1[self.tr_tpex].setCurrentSection(QtWidgets.QDateTimeEdit.YearSection)
    self.tr_dtEd_1[self.tr_tpex].setAlignment(QtCore.Qt.AlignCenter)
    self.tr_dtEd_1[self.tr_tpex].setCalendarPopup(True)
    self.tr_dtEd_1[self.tr_tpex].setFont(font)
    self.tr_dtEd_1[self.tr_tpex].setStyleSheet("QDateEdit {\n"
    "    border: 1px solid #acacac;\n"
    "    border-radius: 1px;\n"
    "    padding-left: 5px;\n"
    "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
    "                                stop: 0 #f0f0f0, stop: 1 #e5e5e5);\n"
    "}\n"
    "\n"
    "QDateEdit:hover {\n"
    "    border: 1px solid #7eb4ea;\n"
    "    border-radius: 1px;\n"
    "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
    "                                stop: 0 #ecf4fc, stop: 1 #dcecfc);\n"
    "}\n"
    "\n"
    "QDateEdit::drop-down  {\n"
    "    subcontrol-origin: padding;\n"
    "    subcontrol-position: top right;\n"
    "    width: 27px;\n"
    "    border-top-right-radius: 3px;\n"
    "    border-bottom-right-radius: 3px;\n"
    "}\n"
    "\n"
    "QDateEdit::drop-down:hover{\n"
    "    subcontrol-origin: padding;\n"
    "    subcontrol-position: top right;\n"
    "    width: 27px;\n"
    "    border-left-width: 1px;\n"
    "    border-left-color: darkgray;\n"
    "    border-left-style: solid;\n"
    "    border-top-right-radius: 3px;\n"
    "    border-bottom-right-radius: 3px;\n"
    "}\n"
    "\n"
    "QDateEdit::down-arrow {\n"
    "    image: url(icons/arrow_down.png);\n"
    "    width: 18px;\n"
    "    height: 18px;\n"
    "}\n"
    "\n"
    "QDateEdit::down-arrow:on {\n"
    "    top: 1px;\n"
    "    left: 1px;\n"
    "}")
    self.tr_dtEd_1[self.tr_tpex].setObjectName("tr_dtEd_1" + str(self.tr_tpex))
    self.tr_horlay_1[self.tr_tpex].addWidget(self.tr_dtEd_1[self.tr_tpex])
    self.tr_horlay_1[self.tr_tpex].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum))
    self.tr_delBut.append(QtWidgets.QToolButton())
    self.tr_delBut[self.tr_tpex].setMinimumSize(QtCore.QSize(27, 27))
    self.tr_delBut[self.tr_tpex].setMaximumSize(QtCore.QSize(27, 27))
    self.tr_delBut[self.tr_tpex].setText("")
    self.tr_delBut[self.tr_tpex].setIcon(icon2)
    self.tr_delBut[self.tr_tpex].setIconSize(QtCore.QSize(27, 27))
    self.tr_delBut[self.tr_tpex].setStyleSheet("QToolButton {\n"
    "    border: 1px solid transparent;\n"
    "    background-color: transparent;\n"
    "    width: 27px;\n"
    "    height: 27px;\n"
    "}\n"
    "\n"
    "QToolButton:hover {\n"
    "    border: 1px solid gray;\n"
    "    border-radius: 3px;\n"
    "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
    "}\n"
    "\n"
    "QToolButton:pressed {\n"
    "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
    "}\n"
    "\n"
    "QToolButton:flat {\n"
    "    border: none;\n"
    "}")
    self.tr_delBut[self.tr_tpex].setAutoRaise(False)
    self.tr_delBut[self.tr_tpex].setObjectName("tr_delBut_" + str(self.tr_tpex))
    self.tr_horlay_1[self.tr_tpex].addWidget(self.tr_delBut[self.tr_tpex])
    self.verticalLayout_15.addLayout(self.tr_horlay_1[self.tr_tpex])
    self.tr_lab_1[self.tr_tpex].setText("Phase " + str(self.tr_tpex + 2) +":")
    self.tr_dtSt_1[self.tr_tpex].setDisplayFormat("yyyy-MM-dd")
    self.tr_dtEd_1[self.tr_tpex].setDisplayFormat("yyyy-MM-dd")
    self.tr_dtSt_1[self.tr_tpex].setDate(QDate.currentDate())
    self.tr_dtEd_1[self.tr_tpex].setDate(QDate.currentDate())
    self.tr_delBut[self.tr_tpex].clicked.connect(lambda: self.button_clicked())
    self.tr_tpex += 1
    self.modified = True
    self.make_window_title()


def delButton_9_clicked(self, index=None):
    if index == None:
        index = int(self.sender().objectName()[15:])
    self.aircraft_list.pop(index)
    self.ai_lab_5[index].deleteLater()
    self.ai_lab_5.pop(index)
    self.ai_lab_6[index].deleteLater()
    self.ai_lab_6.pop(index)
    self.ai_lab_7[index].deleteLater()
    self.ai_lab_7.pop(index)
    self.ai_lab_8[index].deleteLater()
    self.ai_lab_8.pop(index)
    self.ai_delbut_2[index].deleteLater()
    self.ai_delbut_2.pop(index)
    self.ai_horlay_2[index].deleteLater()
    self.ai_horlay_2.pop(index)
    self.ai_acft -= 1
    if len(self.ai_horlay_2) > 0:
        for i in range(0, len(self.ai_horlay_2)):
            self.ai_horlay_2[i].setObjectName("ai_horlay_2_" + str(i))
            self.ai_delbut_2[i].setObjectName("ai_delButton_2_" + str(i))
    self.modified = True
    self.make_window_title()




def delButton_8_clicked(self, index=None):
    if index == None:
        index = int(self.sender().objectName()[10:])
    self.ro_verlay_2[index].deleteLater()
    self.ro_verlay_2.pop(index)
    self.ro_grilay_1[index].deleteLater()
    self.ro_grilay_1.pop(index)
    self.ro_line_1[index].deleteLater()
    self.ro_line_1.pop(index)
    self.ro_lab_1[index].deleteLater()
    self.ro_lab_1.pop(index)
    self.ro_rlPy_ln[index].deleteLater()
    self.ro_rlPy_ln.pop(index)
    self.ro_infBut_1[index].deleteLater()
    self.ro_infBut_1.pop(index)
    self.ro_lab_2[index].deleteLater()
    self.ro_lab_2.pop(index)
    self.ro_rlEm_ln[index].deleteLater()
    self.ro_rlEm_ln.pop(index)
    self.ro_infBut_2[index].deleteLater()
    self.ro_infBut_2.pop(index)
    self.ro_lab_3[index].deleteLater()
    self.ro_lab_3.pop(index)
    self.ro_rlRl_ln[index].deleteLater()
    self.ro_rlRl_ln.pop(index)
    self.ro_infBut_3[index].deleteLater()
    self.ro_infBut_3.pop(index)
    self.ro_delBut[index].deleteLater()
    self.ro_delBut.pop(index)
    if len(self.ro_verlay_2) > 0:
        for i in range(0, len(self.ro_verlay_2)):
            self.ro_delBut[i].setObjectName("ro_delBut_" + str(i))
    self.ro_roPy -= 1
    if self.ro_roPy == 0:
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/none_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.delButton_8.setEnabled(False)
        self.delButton_8.setIcon(icon)
    self.modified = True
    self.make_window_title()
    
def delButton_7_clicked(self, index=None):
    if index == None:
        index = int(self.sender().objectName()[10:])
    self.mm_verlay_1[index].deleteLater()
    self.mm_verlay_1.pop(index)
    self.mm_verlay_2[index].deleteLater()
    self.mm_verlay_2.pop(index)
    self.mm_line_1[index].deleteLater()
    self.mm_line_1.pop(index)
    self.mm_horlay_1[index].deleteLater()
    self.mm_horlay_1.pop(index)
    self.mm_lab_1[index].deleteLater()
    self.mm_lab_1.pop(index)
    self.mm_conName_ln[index].deleteLater()
    self.mm_conName_ln.pop(index)
    self.mm_horlay_2[index].deleteLater()
    self.mm_horlay_2.pop(index)
    self.mm_lab_2[index].deleteLater()
    self.mm_lab_2.pop(index)
    self.mm_conEmail_ln[index].deleteLater()
    self.mm_conEmail_ln.pop(index)
    self.mm_horlay_3[index].deleteLater()
    self.mm_horlay_3.pop(index)
    self.mm_delBut[index].deleteLater()
    self.mm_delBut.pop(index)
    self.mm_pofc -= 1
    if self.mm_pofc == 0:
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/none_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.delButton_7.setEnabled(False)
        self.delButton_7.setIcon(icon)
    self.modified = True
    self.make_window_title()
    if len(self.mm_horlay_3) > 0:
        for i in range(0, len(self.mm_horlay_3)):
            self.mm_delBut[i].setObjectName("mm_delBut_" + str(i))
    
def delButton_5_clicked(self, index=None):
    if index == None:
        index = int(self.sender().objectName()[12:])
    self.au_horlay_1[index].deleteLater()
    self.au_horlay_1.pop(index)
    self.au_wn_con_ta[index].deleteLater()
    self.au_wn_con_ta.pop(index)
    self.au_delBut_1[index].deleteLater()
    self.au_delBut_1.pop(index)
    if len(self.au_horlay_1) > 0:
        for i in range(0, len(self.au_horlay_1)):
            self.au_delBut_1[i].setObjectName("au_delBut_1_" + str(i))
    self.au_wn_1 -= 1
    if self.au_wn_1 == 0:
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/none_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.delButton_5.setEnabled(False)
        self.delButton_5.setIcon(icon)
    self.modified = True
    self.make_window_title()

def delButton_6_clicked(self, index=None):
    if index == None:
        index = int(self.sender().objectName()[12:])
    self.au_horlay_2[index].deleteLater()
    self.au_horlay_2.pop(index)
    self.au_wn_lim_ta[index].deleteLater()
    self.au_wn_lim_ta.pop(index)
    self.au_delBut_2[index].deleteLater()
    self.au_delBut_2.pop(index)
    if len(self.au_horlay_2) > 0:
        for i in range(0, len(self.au_horlay_2)):
            self.au_delBut_2[i].setObjectName("au_delBut_2_" + str(i))
    self.au_wn_2 -= 1
    if self.au_wn_2 == 0:
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/none_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.delButton_6.setEnabled(False)
        self.delButton_6.setIcon(icon)
    self.modified = True
    self.make_window_title()

def delButton_4_clicked(self, index=None):
    if index == None:
        index = int(self.sender().objectName()[13:])
    self.instModel_list.pop(index)
    self.instManufacturer_list.pop(index)
    self.ai_lab_4[index].deleteLater()
    self.ai_lab_4.pop(index)
    self.ai_lab_3[index].deleteLater()
    self.ai_lab_3.pop(index)
    self.ai_lab_2[index].deleteLater()
    self.ai_lab_2.pop(index)
    self.ai_lab_1[index].deleteLater()
    self.ai_lab_1.pop(index)
    self.ai_delbut[index].deleteLater()
    self.ai_delbut.pop(index)
    self.ai_horlay[index].deleteLater()
    self.ai_horlay.pop(index)
    self.ai_inst -= 1
    if len(self.ai_horlay) > 0:
        for i in range(0, len(self.ai_horlay)):
            self.ai_horlay[i].setObjectName("ai_horlay_" + str(i))
            self.ai_delbut[i].setObjectName("ai_delButton_" + str(i))
    self.modified = True
    self.make_window_title()

def delButton_3_clicked(self, index=None):
    if index == None:
        index = int(self.sender().objectName()[10:])
    self.tr_horlay_1[index].deleteLater()
    self.tr_horlay_1.pop(index)
    self.tr_lab_1[index].deleteLater()
    self.tr_lab_1.pop(index)
    self.tr_dtSt_1[index].deleteLater()
    self.tr_dtSt_1.pop(index)
    self.tr_dtEd_1[index].deleteLater()
    self.tr_dtEd_1.pop(index)
    self.tr_delBut[index].deleteLater()
    self.tr_delBut.pop(index)
    self.tr_tpex -= 1
    if self.tr_tpex == 0:
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/none_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.delButton_10.setEnabled(False)
        self.delButton_10.setIcon(icon)
    self.modified = True
    self.make_window_title()
    if len(self.tr_horlay_1) > 0:
        for i in range(0, len(self.tr_horlay_1)):
            self.tr_horlay_1[i].setObjectName("tr_horlay_1" + str(i))
            self.tr_lab_1[i].setObjectName("tr_lab_1" + str(i))
            self.tr_lab_1[i].setText("Phase " + str(i + 2) + ":")
            self.tr_dtSt_1[i].setObjectName("tr_dtSt_1" + str(i))
            self.tr_dtEd_1[i].setObjectName("tr_dtEd_1" + str(i))
            self.tr_delBut[i].setObjectName("tr_delBut_" + str(i))

def gl_rolebox_changed(self):
    if self.gl_resolution_rl1.currentText() == 'Scale':
        if self.gl_roleBox == 0:
            pass
        else:
            font1 = QtGui.QFont()
            font1.setFamily("font/SourceSansPro-Regular.ttf")
            font1.setPointSize(10)
            font1.setBold(False)
            font1.setWeight(50)
            font1.setStyleStrategy(QtGui.QFont.PreferAntialias)
            self.gl_roleBox = 0
            self.gl_unit_lb.deleteLater()
            self.gl_unit_rl.deleteLater()
            self.gl_resolution_ln.deleteLater()
            self.horizontalLayout_27.removeItem(self.gl_spacerItem)
            self.gl_resolution_ln = QtWidgets.QLineEdit()
            self.gl_resolution_ln.setMinimumSize(QtCore.QSize(200, 27))
            self.gl_resolution_ln.setMaximumSize(QtCore.QSize(200, 27))
            self.gl_resolution_ln.setObjectName("gl_resolution_ln")
            self.gl_resolution_ln.setFrame(False)
            self.gl_resolution_ln.setFont(font1)
            self.gl_resolution_ln.setStyleSheet("QLineEdit {border-radius: 3px; padding: 1px "
                                            + "4px 1px 4px; background-color: rgb(240, 240, 240);}")
            self.horizontalLayout_27.addWidget(self.gl_resolution_ln)
    else:
        if self.gl_roleBox == 1:
            pass
        else:
            font = QtGui.QFont()
            font.setFamily("font/SourceSansPro-Regular.ttf")
            font.setPointSize(10)
            font.setBold(False)
            font.setWeight(50)
            font.setStyleStrategy(QtGui.QFont.PreferAntialias)
            font1 = QtGui.QFont()
            font1.setFamily("font/SourceSansPro-Regular.ttf")
            font1.setPointSize(10)
            font1.setBold(False)
            font1.setWeight(50)
            font1.setStyleStrategy(QtGui.QFont.PreferAntialias)
            self.gl_roleBox = 1
            self.gl_resolution_ln.deleteLater()
            self.gl_resolution_ln = QtWidgets.QLineEdit()
            self.gl_resolution_ln.setMinimumSize(QtCore.QSize(100, 27))
            self.gl_resolution_ln.setMaximumSize(QtCore.QSize(100, 27))
            self.gl_resolution_ln.setObjectName("gl_resolution_ln")
            self.gl_resolution_ln.setFrame(False)
            self.gl_resolution_ln.setFont(font1)
            self.gl_resolution_ln.setStyleSheet("QLineEdit {border-radius: 3px; padding: 1px "
                                            + "4px 1px 4px; background-color: rgb(240, 240, 240);}")
            self.gl_spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.
                                                   QSizePolicy.Minimum)
            self.gl_unit_lb = QtWidgets.QLabel()
            self.gl_unit_lb.setMinimumSize(QtCore.QSize(40, 27))
            self.gl_unit_lb.setMaximumSize(QtCore.QSize(40, 27))
            self.gl_unit_lb.setObjectName("gl_unit_lb")
            self.gl_unit_lb.setFont(font)
            self.gl_unit_lb.setText("Unit:")
            self.gl_unit_rl = QtWidgets.QComboBox()
            self.gl_unit_rl.setMinimumSize(QtCore.QSize(150, 27))
            self.gl_unit_rl.setMaximumSize(QtCore.QSize(16777215, 27))
            self.gl_unit_rl.setObjectName("gl_unit_rl")
            self.gl_unit_rl.setFrame(False)
            self.gl_unit_rl.setFont(font1)
            self.gl_unit_rl.setStyleSheet("QComboBox {\n"
            "    border: 1px solid #acacac;\n"
            "    border-radius: 1px;\n"
            "    padding-left: 5px;\n"
            "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
            "                                stop: 0 #f0f0f0, stop: 1 #e5e5e5);\n"
            "}\n"
            "\n"
            "QComboBox:disabled {\n"
            "    background-color:  rgb(200,200,200);\n"
            "}\n"
            "\n"
            "QComboBox:hover {\n"
            "    border: 1px solid #7eb4ea;\n"
            "    border-radius: 1px;\n"
            "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
            "                                stop: 0 #ecf4fc, stop: 1 #dcecfc);\n"
            "}\n"
            "\n"
            "QComboBox::drop-down {\n"
            "    subcontrol-origin: padding;\n"
            "    subcontrol-position: top right;\n"
            "    width: 27px;\n"
            "    border-top-right-radius: 3px;\n"
            "    border-bottom-right-radius: 3px;\n"
            "}\n"
            "\n"
            "QComboBox::drop-down:hover {\n"
            "    subcontrol-origin: padding;\n"
            "    subcontrol-position: top right;\n"
            "    width: 27px;\n"
            "    border-left-width: 1px;\n"
            "    border-left-color: darkgray;\n"
            "    border-left-style: solid;\n"
            "    border-top-right-radius: 3px;\n"
            "    border-bottom-right-radius: 3px;\n"
            "}\n"
            "\n"
            "QComboBox::down-arrow {\n"
            "    image: url(icons/arrow_down.png); \n"
            "    width: 18px;\n"
            "    height: 18px\n"
            "}\n"
            "\n"
            "QComboBox::down-arrow:on {\n"
            "    top: 1px; \n"
            "    left: 1px;\n"
            "}\n"
            "\n"
            "QComboBox QAbstractItemView {\n"
            "    selection-background-color: transparent;\n"
            "    selection-color: blue;\n"
            "    border: 0px, solid black;\n"
            "}")
            cur = self.db.cursor()
            query = cur.execute("SELECT Main FROM unit").fetchall()
            self.gl_unit_rl.addItem("Make a choice...")
            for item in query:
                self.gl_unit_rl.addItem(item[0])

            self.horizontalLayout_27.addWidget(self.gl_resolution_ln)
            self.horizontalLayout_27.addItem(self.gl_spacerItem)
            self.horizontalLayout_27.addWidget(self.gl_unit_lb)
            self.horizontalLayout_27.addWidget(self.gl_unit_rl)

def ai_aircraftRolebox_changed(self):
    if self.ai_aircraft_rl1.currentText() != "Other...":
        if self.ai_otherAircraft == 1:
            self.gridLayout_10.setVerticalSpacing(17)
            self.gridLayout_10.removeWidget(self.ai_manufacturer_ln)
            self.gridLayout_10.removeWidget(self.ai_type_ln)
            self.gridLayout_10.removeWidget(self.ai_operator_ln)
            self.gridLayout_10.removeWidget(self.ai_country_rl)
            self.gridLayout_10.removeWidget(self.ai_number_ln)
            self.ai_manufacturer_ln.deleteLater()
            self.ai_type_ln.deleteLater()
            self.ai_operator_ln.deleteLater()
            self.ai_country_rl.deleteLater()
            self.ai_number_ln.deleteLater()
            self.gridLayout_10.addWidget(self.ai_label_7, 0, 1, 1, 1)
            self.gridLayout_10.addWidget(self.ai_label_8, 1, 1, 1, 1)
            self.gridLayout_10.addWidget(self.ai_label_9, 2, 1, 1, 1)
            self.gridLayout_10.addWidget(self.ai_label_10, 3, 1, 1, 1)
            self.gridLayout_10.addWidget(self.ai_label_11, 4, 1, 1, 1)
        query = sql_valueRead(self, "aircraftInformations", "Id", self.ai_aircraft_rl1.currentText())
        self.ai_image_bx.setPixmap(QtGui.QPixmap("eufar_aircrafts/" + query[0][6]))
        self.ai_label_7.setText(_translate("MainWindow", query[0][1], None))
        self.ai_label_8.setText(_translate("MainWindow", query[0][2], None))
        self.ai_label_9.setText(_translate("MainWindow", query[0][3], None))
        self.ai_label_10.setText(_translate("MainWindow", query[0][4], None))
        self.ai_label_11.setText(_translate("MainWindow", query[0][5], None))
        self.ai_label_12.setText(_translate("MainWindow", query[0][7], None))
        if self.ai_aircraft_rl1.currentText() == "Make a choice...":
            self.ai_label_21.setPixmap(QtGui.QPixmap("icons/none_icon.png"))
        else:
            self.ai_label_21.setPixmap(QtGui.QPixmap("icons/copyright_icon.png"))
        self.ai_otherAircraft = 0
    else:
        self.gridLayout_10.setVerticalSpacing(28)
        self.ai_image_bx.setPixmap(QtGui.QPixmap("eufar_aircrafts/logo_eufar_emc.png"))
        self.ai_label_21.setPixmap(QtGui.QPixmap("icons/none_icon.png"))
        font = QtGui.QFont()
        font.setFamily("font/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ai_label_7.setText("")
        self.ai_label_8.setText("")
        self.ai_label_9.setText("")
        self.ai_label_10.setText("")
        self.ai_label_11.setText("")
        self.ai_label_12.setText("")
        self.gridLayout_10.removeWidget(self.ai_label_7)
        self.gridLayout_10.removeWidget(self.ai_label_8)
        self.gridLayout_10.removeWidget(self.ai_label_9)
        self.gridLayout_10.removeWidget(self.ai_label_10)
        self.gridLayout_10.removeWidget(self.ai_label_11)
        self.ai_manufacturer_ln = QtWidgets.QLineEdit()
        self.ai_manufacturer_ln.setFont(font)
        self.ai_manufacturer_ln.setFrame(False)
        self.ai_manufacturer_ln.setObjectName("ai_manufacturer_ln")
        self.ai_manufacturer_ln.setStyleSheet("QLineEdit {border-radius: 3px; padding: 1px "
                                                       + "4px 1px 4px; background-color: rgb(240, 240, 240);}")
        self.ai_type_ln = QtWidgets.QLineEdit()
        self.ai_type_ln.setFont(font)
        self.ai_type_ln.setFrame(False)
        self.ai_type_ln.setObjectName("ai_type_ln")
        self.ai_type_ln.setStyleSheet("QLineEdit {border-radius: 3px; padding: 1px "
                                                       + "4px 1px 4px; background-color: rgb(240, 240, 240);}")
        self.ai_operator_ln = QtWidgets.QLineEdit()
        self.ai_operator_ln.setFont(font)
        self.ai_operator_ln.setFrame(False)
        self.ai_operator_ln.setObjectName("ai_operator_ln")
        self.ai_operator_ln.setStyleSheet("QLineEdit {border-radius: 3px; padding: 1px "
                                                       + "4px 1px 4px; background-color: rgb(240, 240, 240);}")
        self.ai_country_rl = QtWidgets.QComboBox()
        self.ai_country_rl.setMinimumSize(QtCore.QSize(200, 27))
        self.ai_country_rl.setMaximumSize(QtCore.QSize(200, 27))
        self.ai_country_rl.setFont(font)
        self.ai_country_rl.setMaxVisibleItems(20)
        self.ai_country_rl.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToMinimumContentsLength)
        self.ai_country_rl.setMinimumContentsLength(20)
        self.ai_country_rl.setFrame(False)
        self.ai_country_rl.setModelColumn(0)
        self.ai_country_rl.setObjectName("ai_country_rl")
        self.ai_country_rl.setStyleSheet("QComboBox {\n"
        "    border: 1px solid #acacac;\n"
        "    border-radius: 1px;\n"
        "    padding-left: 5px;\n"
        "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
        "                                stop: 0 #f0f0f0, stop: 1 #e5e5e5);\n"
        "}\n"
        "\n"
        "QComboBox:disabled {\n"
        "    background-color:  rgb(200,200,200);\n"
        "}\n"
        "\n"
        "QComboBox:hover {\n"
        "    border: 1px solid #7eb4ea;\n"
        "    border-radius: 1px;\n"
        "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
        "                                stop: 0 #ecf4fc, stop: 1 #dcecfc);\n"
        "}\n"
        "\n"
        "QComboBox::drop-down {\n"
        "    subcontrol-origin: padding;\n"
        "    subcontrol-position: top right;\n"
        "    width: 27px;\n"
        "    border-top-right-radius: 3px;\n"
        "    border-bottom-right-radius: 3px;\n"
        "}\n"
        "\n"
        "QComboBox::drop-down:hover {\n"
        "    subcontrol-origin: padding;\n"
        "    subcontrol-position: top right;\n"
        "    width: 27px;\n"
        "    border-left-width: 1px;\n"
        "    border-left-color: darkgray;\n"
        "    border-left-style: solid;\n"
        "    border-top-right-radius: 3px;\n"
        "    border-bottom-right-radius: 3px;\n"
        "}\n"
        "\n"
        "QComboBox::down-arrow {\n"
        "    image: url(icons/arrow_down.png); \n"
        "    width: 18px;\n"
        "    height: 18px\n"
        "}\n"
        "\n"
        "QComboBox::down-arrow:on {\n"
        "    top: 1px; \n"
        "    left: 1px;\n"
        "}\n"
        "\n"
        "QComboBox QAbstractItemView {\n"
        "    selection-background-color: transparent;\n"
        "    selection-color: blue;\n"
        "    border: 0px, solid black;\n"
        "}")
        query = sql_valueRead(self, "emcLocations", "Category", "Countries")
        i = 0
        self.ai_country_rl.addItem("")
        self.ai_country_rl.setItemText(i, "Make a choice...")
        for item in query:
            i += 1
            self.ai_country_rl.addItem("")
            self.ai_country_rl.setItemText(i, item[1])
        self.ai_number_ln = QtWidgets.QLineEdit()
        self.ai_number_ln.setFont(font)
        self.ai_number_ln.setFrame(False)
        self.ai_number_ln.setObjectName("ai_number_ln")
        self.ai_number_ln.setStyleSheet("QLineEdit {border-radius: 3px; padding: 1px "
                                                       + "4px 1px 4px; background-color: rgb(240, 240, 240);}")
        self.ai_manufacturer_ln.setMinimumSize(QtCore.QSize(230, 27))
        self.ai_manufacturer_ln.setMaximumSize(QtCore.QSize(230, 27))
        self.ai_type_ln.setMinimumSize(QtCore.QSize(230, 27))
        self.ai_type_ln.setMaximumSize(QtCore.QSize(230, 27))
        self.ai_operator_ln.setMinimumSize(QtCore.QSize(230, 27))
        self.ai_operator_ln.setMaximumSize(QtCore.QSize(230, 27))
        self.ai_number_ln.setMinimumSize(QtCore.QSize(230, 27))
        self.ai_number_ln.setMaximumSize(QtCore.QSize(230, 27))
        self.gridLayout_10.addWidget(self.ai_manufacturer_ln, 0, 1, 1, 1)
        self.gridLayout_10.addWidget(self.ai_type_ln, 1, 1, 1, 1)
        self.gridLayout_10.addWidget(self.ai_operator_ln, 2, 1, 1, 1)
        self.gridLayout_10.addWidget(self.ai_country_rl, 3, 1, 1, 1)
        self.gridLayout_10.addWidget(self.ai_number_ln, 4, 1, 1, 1)
        self.ai_otherAircraft = 1

def ai_instrument_changed(self):
    if self.ai_instrument_rl1.currentText() == "Other...":
        if self.horizontalLayout_58.count() == 0:
            icon2 = QtGui.QIcon()
            icon2.addPixmap(QtGui.QPixmap("icons/none_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.plusButton_4.setIcon(icon2)
            self.plusButton_4.setDisabled(True)
            font = QtGui.QFont()
            font.setFamily("font/SourceSansPro-Regular.ttf")
            font.setPointSize(10)
            font.setBold(False)
            font.setWeight(50)
            font.setStyleStrategy(QtGui.QFont.PreferAntialias)
            font1 = QtGui.QFont()
            font1.setFamily("font/SourceSansPro-Regular.ttf")
            font1.setPointSize(10)
            font1.setBold(False)
            font1.setWeight(50)
            font1.setStyleStrategy(QtGui.QFont.PreferAntialias)
            self.spacer1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
            self.horizontalLayout_58.addItem(self.spacer1)
            self.ai_newname_lb = QtWidgets.QLabel()
            self.ai_newname_lb.setMinimumSize(QtCore.QSize(60, 27))
            self.ai_newname_lb.setMaximumSize(QtCore.QSize(60, 27))
            self.ai_newname_lb.setObjectName("ai_newname_lb")
            self.ai_newname_lb.setFont(font)
            self.ai_newname_lb.setText("Name:")
            self.horizontalLayout_58.addWidget(self.ai_newname_lb)
            self.ai_newname_ln = QtWidgets.QLineEdit()
            self.ai_newname_ln.setMinimumSize(QtCore.QSize(200, 27))
            self.ai_newname_ln.setMaximumSize(QtCore.QSize(200, 27))
            self.ai_newname_ln.setObjectName("ai_newname_ln")
            self.ai_newname_ln.setFrame(False)
            self.ai_newname_ln.setFont(font1)
            self.ai_newname_ln.setStyleSheet("QLineEdit {border-radius: 3px; padding: 1px" 
                                            + "4px 1px 4px; background-color: rgb(240, 240, 240);}")
            self.horizontalLayout_58.addWidget(self.ai_newname_ln)
            self.spacer2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
            self.horizontalLayout_58.addItem(self.spacer2)
            self.ai_newmanufacturer_lb = QtWidgets.QLabel()
            self.ai_newmanufacturer_lb.setMinimumSize(QtCore.QSize(120, 27))
            self.ai_newmanufacturer_lb.setMaximumSize(QtCore.QSize(120, 27))
            self.ai_newmanufacturer_lb.setObjectName("ai_newmanufacturer_lb")
            self.ai_newmanufacturer_lb.setFont(font)
            self.ai_newmanufacturer_lb.setText("Manufacturer:")
            self.horizontalLayout_58.addWidget(self.ai_newmanufacturer_lb)
            self.ai_newmanufacturer_ln = QtWidgets.QLineEdit()
            self.ai_newmanufacturer_ln.setMinimumSize(QtCore.QSize(200, 27))
            self.ai_newmanufacturer_ln.setMaximumSize(QtCore.QSize(200, 27))
            self.ai_newmanufacturer_ln.setObjectName("ai_newmanufacturer_ln")
            self.ai_newmanufacturer_ln.setFrame(False)
            self.ai_newmanufacturer_ln.setFont(font1)
            self.ai_newmanufacturer_ln.setStyleSheet("QLineEdit {border-radius: 3px; padding: 1px "
                                            + "4px 1px 4px; background-color: rgb(240, 240, 240);}")
            self.horizontalLayout_58.addWidget(self.ai_newmanufacturer_ln)
            self.spacer3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
            self.horizontalLayout_58.addItem(self.spacer3)
            self.plusButton_9 = QtWidgets.QToolButton()
            self.plusButton_9.setMinimumSize(QtCore.QSize(27, 27))
            self.plusButton_9.setMaximumSize(QtCore.QSize(27, 27))
            self.plusButton_9.setText("")
            icon1 = QtGui.QIcon()
            icon1.addPixmap(QtGui.QPixmap("icons/plus_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.plusButton_9.setIcon(icon1)
            self.plusButton_9.setIconSize(QtCore.QSize(27, 27))
            self.plusButton_9.setAutoRaise(True)
            self.plusButton_9.setObjectName("plusButton_9")
            self.plusButton_9.setStyleSheet("QToolButton {\n"
            "    border: 1px solid transparent;\n"
            "    background-color: transparent;\n"
            "    width: 27px;\n"
            "    height: 27px;\n"
            "}\n"
            "\n"
            "QToolButton:hover {\n"
            "    border: 1px solid gray;\n"
            "    border-radius: 3px;\n"
            "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
            "}\n"
            "\n"
            "QToolButton:pressed {\n"
            "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
            "}\n"
            "\n"
            "QToolButton:flat {\n"
            "    border: none;\n"
            "}")
            self.horizontalLayout_58.addWidget(self.plusButton_9)
            self.spacer4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.horizontalLayout_58.addItem(self.spacer4)
            self.ai_newname_lb.setMinimumSize(QtCore.QSize(50, 27))
            self.ai_newname_lb.setMaximumSize(QtCore.QSize(50, 27))
            self.ai_newmanufacturer_lb.setMinimumSize(QtCore.QSize(100, 27))
            self.ai_newmanufacturer_lb.setMaximumSize(QtCore.QSize(100, 27))
            self.plusButton_9.clicked.connect(lambda: self.button_clicked())
    else:  
        if self.horizontalLayout_58.count() > 0:
            icon2 = QtGui.QIcon()
            icon2.addPixmap(QtGui.QPixmap("icons/plus_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.plusButton_4.setIcon(icon2)
            self.plusButton_4.setEnabled(True)
            for i in reversed(range(self.horizontalLayout_58.count())):
                item = self.horizontalLayout_58.itemAt(i)
                if isinstance(item, QtWidgets.QWidgetItem):
                    item.widget().close()
                self.horizontalLayout_58.removeItem(item)

def gl_categoryRolebox_changed(self):
    if self.gl_category_rl1.currentText() == "Make a choice...":    
        self.gl_details_rl2.clear()
        self.gl_details_rl2.setEnabled(False)
    else:
        query = sql_valueRead(self, "emcLocations", "Category", self.gl_category_rl1.currentText())
        self.gl_details_rl2.clear()
        self.gl_details_rl2.setEnabled(True)
        i = 0
        self.gl_details_rl2.addItem("")
        self.gl_details_rl2.setItemText(i, "Make a choice...")
        for item in query:
            i += 1
            self.gl_details_rl2.addItem("")
            self.gl_details_rl2.setItemText(i, item[1])
               
def qv_domain_changed(self):
    if self.qv_obsRadio.isChecked() == True:
        if self.verticalLayout_25.count() != 41:
            clearLayout(self.verticalLayout_25)
            self.horizontalLayout_84 = QtWidgets.QHBoxLayout()
            self.horizontalLayout_84.setObjectName("horizontalLayout_84")
            self.qv_obsCalInfo = QtWidgets.QLabel()
            self.qv_obsCalInfo.setMinimumSize(QtCore.QSize(180, 27))
            self.qv_obsCalInfo.setMaximumSize(QtCore.QSize(16777215, 27))
            font = QtGui.QFont()
            font.setFamily("fonts/SourceSansPro-Regular.ttf")
            font.setPointSize(10)
            font.setBold(True)
            font.setUnderline(True)
            font.setWeight(75)
            font.setKerning(True)
            font.setStyleStrategy(QtGui.QFont.PreferAntialias)
            self.qv_obsCalInfo.setFont(font)
            self.qv_obsCalInfo.setObjectName("qv_obsCalInfo")
            self.horizontalLayout_84.addWidget(self.qv_obsCalInfo)
            self.infoButton_31 = QtWidgets.QToolButton()
            self.infoButton_31.setMaximumSize(QtCore.QSize(27, 27))
            self.infoButton_31.setStyleSheet("QToolButton {\n"
    "    border: 1px solid transparent;\n"
    "    background-color: transparent;\n"
    "    width: 27px;\n"
    "    height: 27px;\n"
    "}\n"
    "\n"
    "QToolButton:hover {\n"
    "    border: 1px solid gray;\n"
    "    border-radius: 3px;\n"
    "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
    "}\n"
    "\n"
    "QToolButton:pressed {\n"
    "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
    "}\n"
    "\n"
    "QToolButton:flat {\n"
    "    border: none;\n"
    "}")
            self.infoButton_31.setText("")
            icon1 = QtGui.QIcon()
            icon1.addPixmap(QtGui.QPixmap("icons/info_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.infoButton_31.setIcon(icon1)
            self.infoButton_31.setIconSize(QtCore.QSize(27, 27))
            self.infoButton_31.setAutoRaise(False)
            self.infoButton_31.setObjectName("infoButton_31")
            self.horizontalLayout_84.addWidget(self.infoButton_31)
            spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.horizontalLayout_84.addItem(spacerItem)
            self.verticalLayout_25.addLayout(self.horizontalLayout_84)
            self.horizontalLayout_85 = QtWidgets.QHBoxLayout()
            self.horizontalLayout_85.setObjectName("horizontalLayout_85")
            spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
            self.horizontalLayout_85.addItem(spacerItem1)
            self.gridLayout_100 = QtWidgets.QGridLayout()
            self.gridLayout_100.setHorizontalSpacing(20)
            self.gridLayout_100.setVerticalSpacing(10)
            self.gridLayout_100.setObjectName("gridLayout_100")
            self.qv_obsCalLabo_lb = QtWidgets.QLabel()
            self.qv_obsCalLabo_lb.setMinimumSize(QtCore.QSize(220, 27))
            self.qv_obsCalLabo_lb.setMaximumSize(QtCore.QSize(16777215, 27))
            font = QtGui.QFont()
            font.setFamily("fonts/SourceSansPro-Regular.ttf")
            font.setPointSize(10)
            font.setKerning(True)
            font.setStyleStrategy(QtGui.QFont.PreferAntialias)
            self.qv_obsCalLabo_lb.setFont(font)
            self.qv_obsCalLabo_lb.setObjectName("qv_obsCalLabo_lb")
            self.gridLayout_100.addWidget(self.qv_obsCalLabo_lb, 0, 0, 1, 1)
            self.qv_obsCalLabo_ln = QtWidgets.QLineEdit()
            self.qv_obsCalLabo_ln.setEnabled(True)
            self.qv_obsCalLabo_ln.setMinimumSize(QtCore.QSize(450, 27))
            self.qv_obsCalLabo_ln.setMaximumSize(QtCore.QSize(450, 27))
            font = QtGui.QFont()
            font.setFamily("fonts/SourceSansPro-Regular.ttf")
            font.setPointSize(9)
            font.setBold(False)
            font.setWeight(50)
            font.setStyleStrategy(QtGui.QFont.PreferAntialias)
            self.qv_obsCalLabo_ln.setFont(font)
            self.qv_obsCalLabo_ln.setStyleSheet("QLineEdit {\n"
    "    border-radius: 3px;\n"
    "   padding: 1px 4px 1px 4px;\n"
    "    background-color:  rgb(240, 240, 240);\n"
    "}")
            self.qv_obsCalLabo_ln.setFrame(False)
            self.qv_obsCalLabo_ln.setObjectName("qv_obsCalLabo_ln")
            self.gridLayout_100.addWidget(self.qv_obsCalLabo_ln, 0, 1, 1, 1)
            self.qv_obsRadCal = QtWidgets.QLabel()
            self.qv_obsRadCal.setMinimumSize(QtCore.QSize(220, 27))
            self.qv_obsRadCal.setMaximumSize(QtCore.QSize(16777215, 27))
            font = QtGui.QFont()
            font.setFamily("fonts/SourceSansPro-Regular.ttf")
            font.setPointSize(10)
            font.setKerning(True)
            font.setStyleStrategy(QtGui.QFont.PreferAntialias)
            self.qv_obsRadCal.setFont(font)
            self.qv_obsRadCal.setObjectName("qv_obsRadCal")
            self.gridLayout_100.addWidget(self.qv_obsRadCal, 1, 0, 1, 1)
            self.qv_obsRadCal_dt = QtWidgets.QDateEdit()
            self.qv_obsRadCal_dt.setMinimumSize(QtCore.QSize(130, 27))
            self.qv_obsRadCal_dt.setMaximumSize(QtCore.QSize(130, 27))
            font = QtGui.QFont()
            font.setFamily("fonts/SourceSansPro-Regular.ttf")
            font.setPointSize(9)
            font.setBold(False)
            font.setWeight(50)
            font.setStyleStrategy(QtGui.QFont.PreferAntialias)
            self.qv_obsRadCal_dt.setFont(font)
            self.qv_obsRadCal_dt.setStyleSheet("QDateEdit {\n"
    "    border: 1px solid #acacac;\n"
    "    border-radius: 1px;\n"
    "    padding-left: 5px;\n"
    "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
    "                                stop: 0 #f0f0f0, stop: 1 #e5e5e5);\n"
    "}\n"
    "\n"
    "QDateEdit:hover {\n"
    "    border: 1px solid #7eb4ea;\n"
    "    border-radius: 1px;\n"
    "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
    "                                stop: 0 #ecf4fc, stop: 1 #dcecfc);\n"
    "}\n"
    "\n"
    "QDateEdit::drop-down  {\n"
    "    subcontrol-origin: padding;\n"
    "    subcontrol-position: top right;\n"
    "    width: 27px;\n"
    "    border-top-right-radius: 3px;\n"
    "    border-bottom-right-radius: 3px;\n"
    "}\n"
    "\n"
    "QDateEdit::drop-down:hover{\n"
    "    subcontrol-origin: padding;\n"
    "    subcontrol-position: top right;\n"
    "    width: 27px;\n"
    "    border-left-width: 1px;\n"
    "    border-left-color: darkgray;\n"
    "    border-left-style: solid;\n"
    "    border-top-right-radius: 3px;\n"
    "    border-bottom-right-radius: 3px;\n"
    "}\n"
    "\n"
    "QDateEdit::down-arrow {\n"
    "    image: url(icons/arrow_down.png);\n"
    "    width: 18px;\n"
    "    height: 18px;\n"
    "}\n"
    "\n"
    "QDateEdit::down-arrow:on {\n"
    "    top: 1px;\n"
    "    left: 1px;\n"
    "}")
            self.qv_obsRadCal_dt.setFrame(False)
            self.qv_obsRadCal_dt.setAlignment(QtCore.Qt.AlignCenter)
            self.qv_obsRadCal_dt.setAccelerated(True)
            self.qv_obsRadCal_dt.setCurrentSection(QtWidgets.QDateTimeEdit.YearSection)
            self.qv_obsRadCal_dt.setCalendarPopup(True)
            self.qv_obsRadCal_dt.setTimeSpec(QtCore.Qt.UTC)
            self.qv_obsRadCal_dt.setDate(QtCore.QDate(2014, 10, 7))
            self.qv_obsRadCal_dt.setObjectName("qv_obsRadCal_dt")
            self.gridLayout_100.addWidget(self.qv_obsRadCal_dt, 1, 1, 1, 1)
            self.qv_obsSpeCal = QtWidgets.QLabel()
            self.qv_obsSpeCal.setMinimumSize(QtCore.QSize(220, 27))
            self.qv_obsSpeCal.setMaximumSize(QtCore.QSize(16777215, 27))
            font = QtGui.QFont()
            font.setFamily("fonts/SourceSansPro-Regular.ttf")
            font.setPointSize(10)
            font.setKerning(True)
            font.setStyleStrategy(QtGui.QFont.PreferAntialias)
            self.qv_obsSpeCal.setFont(font)
            self.qv_obsSpeCal.setObjectName("qv_obsSpeCal")
            self.gridLayout_100.addWidget(self.qv_obsSpeCal, 2, 0, 1, 1)
            self.qv_obsSpeCal_dt = QtWidgets.QDateEdit()
            self.qv_obsSpeCal_dt.setMinimumSize(QtCore.QSize(130, 27))
            self.qv_obsSpeCal_dt.setMaximumSize(QtCore.QSize(130, 27))
            font = QtGui.QFont()
            font.setFamily("fonts/SourceSansPro-Regular.ttf")
            font.setPointSize(9)
            font.setBold(False)
            font.setWeight(50)
            font.setStyleStrategy(QtGui.QFont.PreferAntialias)
            self.qv_obsSpeCal_dt.setFont(font)
            self.qv_obsSpeCal_dt.setStyleSheet("QDateEdit {\n"
    "    border: 1px solid #acacac;\n"
    "    border-radius: 1px;\n"
    "    padding-left: 5px;\n"
    "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
    "                                stop: 0 #f0f0f0, stop: 1 #e5e5e5);\n"
    "}\n"
    "\n"
    "QDateEdit:hover {\n"
    "    border: 1px solid #7eb4ea;\n"
    "    border-radius: 1px;\n"
    "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
    "                                stop: 0 #ecf4fc, stop: 1 #dcecfc);\n"
    "}\n"
    "\n"
    "QDateEdit::drop-down  {\n"
    "    subcontrol-origin: padding;\n"
    "    subcontrol-position: top right;\n"
    "    width: 27px;\n"
    "    border-top-right-radius: 3px;\n"
    "    border-bottom-right-radius: 3px;\n"
    "}\n"
    "\n"
    "QDateEdit::drop-down:hover{\n"
    "    subcontrol-origin: padding;\n"
    "    subcontrol-position: top right;\n"
    "    width: 27px;\n"
    "    border-left-width: 1px;\n"
    "    border-left-color: darkgray;\n"
    "    border-left-style: solid;\n"
    "    border-top-right-radius: 3px;\n"
    "    border-bottom-right-radius: 3px;\n"
    "}\n"
    "\n"
    "QDateEdit::down-arrow {\n"
    "    image: url(icons/arrow_down.png);\n"
    "    width: 18px;\n"
    "    height: 18px;\n"
    "}\n"
    "\n"
    "QDateEdit::down-arrow:on {\n"
    "    top: 1px;\n"
    "    left: 1px;\n"
    "}")
            self.qv_obsSpeCal_dt.setFrame(False)
            self.qv_obsSpeCal_dt.setAlignment(QtCore.Qt.AlignCenter)
            self.qv_obsSpeCal_dt.setAccelerated(True)
            self.qv_obsSpeCal_dt.setCurrentSection(QtWidgets.QDateTimeEdit.YearSection)
            self.qv_obsSpeCal_dt.setCalendarPopup(True)
            self.qv_obsSpeCal_dt.setTimeSpec(QtCore.Qt.UTC)
            self.qv_obsSpeCal_dt.setDate(QtCore.QDate(2014, 10, 7))
            self.qv_obsSpeCal_dt.setObjectName("qv_obsSpeCal_dt")
            self.gridLayout_100.addWidget(self.qv_obsSpeCal_dt, 2, 1, 1, 1)
            self.horizontalLayout_85.addLayout(self.gridLayout_100)
            spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.horizontalLayout_85.addItem(spacerItem2)
            self.verticalLayout_25.addLayout(self.horizontalLayout_85)
            spacerItem3 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
            self.verticalLayout_25.addItem(spacerItem3)
            self.horizontalLayout_86 = QtWidgets.QHBoxLayout()
            self.horizontalLayout_86.setObjectName("horizontalLayout_86")
            self.qv_obsAcqInfo = QtWidgets.QLabel()
            self.qv_obsAcqInfo.setMinimumSize(QtCore.QSize(180, 27))
            self.qv_obsAcqInfo.setMaximumSize(QtCore.QSize(16777215, 27))
            font = QtGui.QFont()
            font.setFamily("fonts/SourceSansPro-Regular.ttf")
            font.setPointSize(10)
            font.setBold(True)
            font.setUnderline(True)
            font.setWeight(75)
            font.setKerning(True)
            font.setStyleStrategy(QtGui.QFont.PreferAntialias)
            self.qv_obsAcqInfo.setFont(font)
            self.qv_obsAcqInfo.setObjectName("qv_obsAcqInfo")
            self.horizontalLayout_86.addWidget(self.qv_obsAcqInfo)
            spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.horizontalLayout_86.addItem(spacerItem4)
            self.verticalLayout_25.addLayout(self.horizontalLayout_86)
            self.horizontalLayout_87 = QtWidgets.QHBoxLayout()
            self.horizontalLayout_87.setObjectName("horizontalLayout_87")
            spacerItem5 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
            self.horizontalLayout_87.addItem(spacerItem5)
            self.gridLayout_101 = QtWidgets.QGridLayout()
            self.gridLayout_101.setHorizontalSpacing(20)
            self.gridLayout_101.setVerticalSpacing(10)
            self.gridLayout_101.setObjectName("gridLayout_101")
            self.qv_obsSpeBand_lb = QtWidgets.QLabel()
            self.qv_obsSpeBand_lb.setMinimumSize(QtCore.QSize(300, 27))
            self.qv_obsSpeBand_lb.setMaximumSize(QtCore.QSize(16777215, 27))
            font = QtGui.QFont()
            font.setFamily("fonts/SourceSansPro-Regular.ttf")
            font.setPointSize(10)
            font.setKerning(True)
            font.setStyleStrategy(QtGui.QFont.PreferAntialias)
            self.qv_obsSpeBand_lb.setFont(font)
            self.qv_obsSpeBand_lb.setObjectName("qv_obsSpeBand_lb")
            self.gridLayout_101.addWidget(self.qv_obsSpeBand_lb, 0, 0, 1, 1)
            self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
            self.horizontalLayout_3.setObjectName("horizontalLayout_3")
            self.qv_obsSpeBand_ln = QtWidgets.QLineEdit()
            self.qv_obsSpeBand_ln.setEnabled(True)
            self.qv_obsSpeBand_ln.setMinimumSize(QtCore.QSize(100, 27))
            self.qv_obsSpeBand_ln.setMaximumSize(QtCore.QSize(100, 27))
            font = QtGui.QFont()
            font.setFamily("fonts/SourceSansPro-Regular.ttf")
            font.setPointSize(9)
            font.setBold(False)
            font.setWeight(50)
            font.setStyleStrategy(QtGui.QFont.PreferAntialias)
            self.qv_obsSpeBand_ln.setFont(font)
            self.qv_obsSpeBand_ln.setStyleSheet("QLineEdit {\n"
    "    border-radius: 3px;\n"
    "   padding: 1px 4px 1px 4px;\n"
    "    background-color:  rgb(240, 240, 240);\n"
    "}")
            self.qv_obsSpeBand_ln.setFrame(False)
            self.qv_obsSpeBand_ln.setObjectName("qv_obsSpeBand_ln")
            self.horizontalLayout_3.addWidget(self.qv_obsSpeBand_ln)
            spacerItem6 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
            self.horizontalLayout_3.addItem(spacerItem6)
            self.infoButton_32 = QtWidgets.QToolButton()
            self.infoButton_32.setMaximumSize(QtCore.QSize(27, 27))
            self.infoButton_32.setStyleSheet("QToolButton {\n"
    "    border: 1px solid transparent;\n"
    "    background-color: transparent;\n"
    "    width: 27px;\n"
    "    height: 27px;\n"
    "}\n"
    "\n"
    "QToolButton:hover {\n"
    "    border: 1px solid gray;\n"
    "    border-radius: 3px;\n"
    "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
    "}\n"
    "\n"
    "QToolButton:pressed {\n"
    "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
    "}\n"
    "\n"
    "QToolButton:flat {\n"
    "    border: none;\n"
    "}")
            self.infoButton_32.setText("")
            self.infoButton_32.setIcon(icon1)
            self.infoButton_32.setIconSize(QtCore.QSize(27, 27))
            self.infoButton_32.setAutoRaise(False)
            self.infoButton_32.setObjectName("infoButton_32")
            self.horizontalLayout_3.addWidget(self.infoButton_32)
            spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.horizontalLayout_3.addItem(spacerItem7)
            self.gridLayout_101.addLayout(self.horizontalLayout_3, 0, 1, 1, 1)
            self.qv_obsFltHdg_lb = QtWidgets.QLabel()
            self.qv_obsFltHdg_lb.setMinimumSize(QtCore.QSize(300, 27))
            self.qv_obsFltHdg_lb.setMaximumSize(QtCore.QSize(16777215, 27))
            font = QtGui.QFont()
            font.setFamily("fonts/SourceSansPro-Regular.ttf")
            font.setPointSize(10)
            font.setKerning(True)
            font.setStyleStrategy(QtGui.QFont.PreferAntialias)
            self.qv_obsFltHdg_lb.setFont(font)
            self.qv_obsFltHdg_lb.setObjectName("qv_obsFltHdg_lb")
            self.gridLayout_101.addWidget(self.qv_obsFltHdg_lb, 1, 0, 1, 1)
            self.qv_obsFltHdg_ln = QtWidgets.QLineEdit()
            self.qv_obsFltHdg_ln.setEnabled(True)
            self.qv_obsFltHdg_ln.setMinimumSize(QtCore.QSize(100, 27))
            self.qv_obsFltHdg_ln.setMaximumSize(QtCore.QSize(100, 27))
            font = QtGui.QFont()
            font.setFamily("fonts/SourceSansPro-Regular.ttf")
            font.setPointSize(9)
            font.setBold(False)
            font.setWeight(50)
            font.setStyleStrategy(QtGui.QFont.PreferAntialias)
            self.qv_obsFltHdg_ln.setFont(font)
            self.qv_obsFltHdg_ln.setStyleSheet("QLineEdit {\n"
    "    border-radius: 3px;\n"
    "   padding: 1px 4px 1px 4px;\n"
    "    background-color:  rgb(240, 240, 240);\n"
    "}")
            self.qv_obsFltHdg_ln.setFrame(False)
            self.qv_obsFltHdg_ln.setObjectName("qv_obsFltHdg_ln")
            self.gridLayout_101.addWidget(self.qv_obsFltHdg_ln, 1, 1, 1, 1)
            self.qv_obsFltAlt_lb = QtWidgets.QLabel()
            self.qv_obsFltAlt_lb.setMinimumSize(QtCore.QSize(300, 27))
            self.qv_obsFltAlt_lb.setMaximumSize(QtCore.QSize(16777215, 27))
            font = QtGui.QFont()
            font.setFamily("fonts/SourceSansPro-Regular.ttf")
            font.setPointSize(10)
            font.setKerning(True)
            font.setStyleStrategy(QtGui.QFont.PreferAntialias)
            self.qv_obsFltAlt_lb.setFont(font)
            self.qv_obsFltAlt_lb.setObjectName("qv_obsFltAlt_lb")
            self.gridLayout_101.addWidget(self.qv_obsFltAlt_lb, 2, 0, 1, 1)
            self.qv_obsFltAlt_ln = QtWidgets.QLineEdit()
            self.qv_obsFltAlt_ln.setEnabled(True)
            self.qv_obsFltAlt_ln.setMinimumSize(QtCore.QSize(100, 27))
            self.qv_obsFltAlt_ln.setMaximumSize(QtCore.QSize(100, 27))
            font = QtGui.QFont()
            font.setFamily("fonts/SourceSansPro-Regular.ttf")
            font.setPointSize(9)
            font.setBold(False)
            font.setWeight(50)
            font.setStyleStrategy(QtGui.QFont.PreferAntialias)
            self.qv_obsFltAlt_ln.setFont(font)
            self.qv_obsFltAlt_ln.setStyleSheet("QLineEdit {\n"
    "    border-radius: 3px;\n"
    "   padding: 1px 4px 1px 4px;\n"
    "    background-color:  rgb(240, 240, 240);\n"
    "}")
            self.qv_obsFltAlt_ln.setFrame(False)
            self.qv_obsFltAlt_ln.setObjectName("qv_obsFltAlt_ln")
            self.gridLayout_101.addWidget(self.qv_obsFltAlt_ln, 2, 1, 1, 1)
            self.qv_obsSolZen_lb = QtWidgets.QLabel()
            self.qv_obsSolZen_lb.setMinimumSize(QtCore.QSize(300, 27))
            self.qv_obsSolZen_lb.setMaximumSize(QtCore.QSize(16777215, 27))
            font = QtGui.QFont()
            font.setFamily("fonts/SourceSansPro-Regular.ttf")
            font.setPointSize(10)
            font.setKerning(True)
            font.setStyleStrategy(QtGui.QFont.PreferAntialias)
            self.qv_obsSolZen_lb.setFont(font)
            self.qv_obsSolZen_lb.setObjectName("qv_obsSolZen_lb")
            self.gridLayout_101.addWidget(self.qv_obsSolZen_lb, 3, 0, 1, 1)
            self.qv_obsSolZen_ln = QtWidgets.QLineEdit()
            self.qv_obsSolZen_ln.setEnabled(True)
            self.qv_obsSolZen_ln.setMinimumSize(QtCore.QSize(100, 27))
            self.qv_obsSolZen_ln.setMaximumSize(QtCore.QSize(100, 27))
            font = QtGui.QFont()
            font.setFamily("fonts/SourceSansPro-Regular.ttf")
            font.setPointSize(9)
            font.setBold(False)
            font.setWeight(50)
            font.setStyleStrategy(QtGui.QFont.PreferAntialias)
            self.qv_obsSolZen_ln.setFont(font)
            self.qv_obsSolZen_ln.setStyleSheet("QLineEdit {\n"
    "    border-radius: 3px;\n"
    "   padding: 1px 4px 1px 4px;\n"
    "    background-color:  rgb(240, 240, 240);\n"
    "}")
            self.qv_obsSolZen_ln.setFrame(False)
            self.qv_obsSolZen_ln.setObjectName("qv_obsSolZen_ln")
            self.gridLayout_101.addWidget(self.qv_obsSolZen_ln, 3, 1, 1, 1)
            self.qv_obsSolAzi_lb = QtWidgets.QLabel()
            self.qv_obsSolAzi_lb.setMinimumSize(QtCore.QSize(300, 27))
            self.qv_obsSolAzi_lb.setMaximumSize(QtCore.QSize(16777215, 27))
            font = QtGui.QFont()
            font.setFamily("fonts/SourceSansPro-Regular.ttf")
            font.setPointSize(10)
            font.setKerning(True)
            font.setStyleStrategy(QtGui.QFont.PreferAntialias)
            self.qv_obsSolAzi_lb.setFont(font)
            self.qv_obsSolAzi_lb.setObjectName("qv_obsSolAzi_lb")
            self.gridLayout_101.addWidget(self.qv_obsSolAzi_lb, 4, 0, 1, 1)
            self.qv_obsSolAzi_ln = QtWidgets.QLineEdit()
            self.qv_obsSolAzi_ln.setEnabled(True)
            self.qv_obsSolAzi_ln.setMinimumSize(QtCore.QSize(100, 27))
            self.qv_obsSolAzi_ln.setMaximumSize(QtCore.QSize(100, 27))
            font = QtGui.QFont()
            font.setFamily("fonts/SourceSansPro-Regular.ttf")
            font.setPointSize(9)
            font.setBold(False)
            font.setWeight(50)
            font.setStyleStrategy(QtGui.QFont.PreferAntialias)
            self.qv_obsSolAzi_ln.setFont(font)
            self.qv_obsSolAzi_ln.setStyleSheet("QLineEdit {\n"
    "    border-radius: 3px;\n"
    "   padding: 1px 4px 1px 4px;\n"
    "    background-color:  rgb(240, 240, 240);\n"
    "}")
            self.qv_obsSolAzi_ln.setFrame(False)
            self.qv_obsSolAzi_ln.setObjectName("qv_obsSolAzi_ln")
            self.gridLayout_101.addWidget(self.qv_obsSolAzi_ln, 4, 1, 1, 1)
            self.qv_obsAnoAcq_lb = QtWidgets.QLabel()
            self.qv_obsAnoAcq_lb.setMinimumSize(QtCore.QSize(300, 27))
            self.qv_obsAnoAcq_lb.setMaximumSize(QtCore.QSize(16777215, 27))
            font = QtGui.QFont()
            font.setFamily("fonts/SourceSansPro-Regular.ttf")
            font.setPointSize(10)
            font.setKerning(True)
            font.setStyleStrategy(QtGui.QFont.PreferAntialias)
            self.qv_obsAnoAcq_lb.setFont(font)
            self.qv_obsAnoAcq_lb.setObjectName("qv_obsAnoAcq_lb")
            self.gridLayout_101.addWidget(self.qv_obsAnoAcq_lb, 5, 0, 1, 1)
            self.qv_obsAnoAcq_ln = QtWidgets.QLineEdit()
            self.qv_obsAnoAcq_ln.setEnabled(True)
            self.qv_obsAnoAcq_ln.setMinimumSize(QtCore.QSize(450, 27))
            self.qv_obsAnoAcq_ln.setMaximumSize(QtCore.QSize(450, 27))
            font = QtGui.QFont()
            font.setFamily("fonts/SourceSansPro-Regular.ttf")
            font.setPointSize(9)
            font.setBold(False)
            font.setWeight(50)
            font.setStyleStrategy(QtGui.QFont.PreferAntialias)
            self.qv_obsAnoAcq_ln.setFont(font)
            self.qv_obsAnoAcq_ln.setStyleSheet("QLineEdit {\n"
    "    border-radius: 3px;\n"
    "   padding: 1px 4px 1px 4px;\n"
    "    background-color:  rgb(240, 240, 240);\n"
    "}")
            self.qv_obsAnoAcq_ln.setFrame(False)
            self.qv_obsAnoAcq_ln.setObjectName("qv_obsAnoAcq_ln")
            self.gridLayout_101.addWidget(self.qv_obsAnoAcq_ln, 5, 1, 1, 1)
            self.horizontalLayout_87.addLayout(self.gridLayout_101)
            spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.horizontalLayout_87.addItem(spacerItem8)
            self.verticalLayout_25.addLayout(self.horizontalLayout_87)
            spacerItem9 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
            self.verticalLayout_25.addItem(spacerItem9)
            self.horizontalLayout_88 = QtWidgets.QHBoxLayout()
            self.horizontalLayout_88.setObjectName("horizontalLayout_88")
            self.qv_obsProInfo = QtWidgets.QLabel()
            self.qv_obsProInfo.setMinimumSize(QtCore.QSize(180, 27))
            self.qv_obsProInfo.setMaximumSize(QtCore.QSize(16777215, 27))
            font = QtGui.QFont()
            font.setFamily("fonts/SourceSansPro-Regular.ttf")
            font.setPointSize(10)
            font.setBold(True)
            font.setUnderline(True)
            font.setWeight(75)
            font.setKerning(True)
            font.setStyleStrategy(QtGui.QFont.PreferAntialias)
            self.qv_obsProInfo.setFont(font)
            self.qv_obsProInfo.setObjectName("qv_obsProInfo")
            self.horizontalLayout_88.addWidget(self.qv_obsProInfo)
            spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.horizontalLayout_88.addItem(spacerItem10)
            self.verticalLayout_25.addLayout(self.horizontalLayout_88)
            self.horizontalLayout_89 = QtWidgets.QHBoxLayout()
            self.horizontalLayout_89.setObjectName("horizontalLayout_89")
            spacerItem11 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
            self.horizontalLayout_89.addItem(spacerItem11)
            self.gridLayout_102 = QtWidgets.QGridLayout()
            self.gridLayout_102.setHorizontalSpacing(20)
            self.gridLayout_102.setVerticalSpacing(10)
            self.gridLayout_102.setObjectName("gridLayout_102")
            self.qv_obsProLvl = QtWidgets.QLabel()
            self.qv_obsProLvl.setMinimumSize(QtCore.QSize(210, 27))
            self.qv_obsProLvl.setMaximumSize(QtCore.QSize(16777215, 27))
            font = QtGui.QFont()
            font.setFamily("fonts/SourceSansPro-Regular.ttf")
            font.setPointSize(10)
            font.setKerning(True)
            font.setStyleStrategy(QtGui.QFont.PreferAntialias)
            self.qv_obsProLvl.setFont(font)
            self.qv_obsProLvl.setObjectName("qv_obsProLvl")
            self.gridLayout_102.addWidget(self.qv_obsProLvl, 0, 0, 1, 1)
            self.qv_obsProLvl_rl = QtWidgets.QComboBox()
            self.qv_obsProLvl_rl.setMinimumSize(QtCore.QSize(140, 27))
            self.qv_obsProLvl_rl.setMaximumSize(QtCore.QSize(180, 27))
            font = QtGui.QFont()
            font.setFamily("fonts/SourceSansPro-Regular.ttf")
            font.setPointSize(9)
            font.setBold(False)
            font.setWeight(50)
            font.setStyleStrategy(QtGui.QFont.PreferAntialias)
            self.qv_obsProLvl_rl.setFont(font)
            self.qv_obsProLvl_rl.setStyleSheet("QComboBox {\n"
    "    border: 1px solid #acacac;\n"
    "    border-radius: 1px;\n"
    "    padding-left: 5px;\n"
    "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
    "                                stop: 0 #f0f0f0, stop: 1 #e5e5e5);\n"
    "}\n"
    "\n"
    "QComboBox:disabled {\n"
    "    background-color:  rgb(200,200,200);\n"
    "}\n"
    "\n"
    "QComboBox:hover {\n"
    "    border: 1px solid #7eb4ea;\n"
    "    border-radius: 1px;\n"
    "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
    "                                stop: 0 #ecf4fc, stop: 1 #dcecfc);\n"
    "}\n"
    "\n"
    "QComboBox::drop-down {\n"
    "    subcontrol-origin: padding;\n"
    "    subcontrol-position: top right;\n"
    "    width: 27px;\n"
    "    border-top-right-radius: 3px;\n"
    "    border-bottom-right-radius: 3px;\n"
    "}\n"
    "\n"
    "QComboBox::drop-down:hover {\n"
    "    subcontrol-origin: padding;\n"
    "    subcontrol-position: top right;\n"
    "    width: 27px;\n"
    "    border-left-width: 1px;\n"
    "    border-left-color: darkgray;\n"
    "    border-left-style: solid;\n"
    "    border-top-right-radius: 3px;\n"
    "    border-bottom-right-radius: 3px;\n"
    "}\n"
    "\n"
    "QComboBox::down-arrow {\n"
    "    image: url(icons/arrow_down.png); \n"
    "    width: 18px;\n"
    "    height: 18px\n"
    "}\n"
    "\n"
    "QComboBox::down-arrow:on {\n"
    "    top: 1px; \n"
    "    left: 1px;\n"
    "}\n"
    "\n"
    "QComboBox QAbstractItemView {\n"
    "    selection-background-color: transparent;\n"
    "    selection-color: blue;\n"
    "    border: 0px, solid black;\n"
    "}")
            self.qv_obsProLvl_rl.setFrame(False)
            self.qv_obsProLvl_rl.setObjectName("qv_obsProLvl_rl")
            self.qv_obsProLvl_rl.addItem("")
            self.qv_obsProLvl_rl.addItem("")
            self.qv_obsProLvl_rl.addItem("")
            self.qv_obsProLvl_rl.addItem("")
            self.qv_obsProLvl_rl.addItem("")
            self.gridLayout_102.addWidget(self.qv_obsProLvl_rl, 0, 1, 1, 1)
            self.qv_obsDrkCur = QtWidgets.QLabel()
            self.qv_obsDrkCur.setMinimumSize(QtCore.QSize(210, 27))
            self.qv_obsDrkCur.setMaximumSize(QtCore.QSize(16777215, 27))
            font = QtGui.QFont()
            font.setFamily("fonts/SourceSansPro-Regular.ttf")
            font.setPointSize(10)
            font.setKerning(True)
            font.setStyleStrategy(QtGui.QFont.PreferAntialias)
            self.qv_obsDrkCur.setFont(font)
            self.qv_obsDrkCur.setObjectName("qv_obsDrkCur")
            self.gridLayout_102.addWidget(self.qv_obsDrkCur, 1, 0, 1, 1)
            self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
            self.horizontalLayout_4.setObjectName("horizontalLayout_4")
            self.qv_obsDrkCur_rd1 = QtWidgets.QRadioButton()
            self.qv_obsDrkCur_rd1.setMinimumSize(QtCore.QSize(51, 27))
            self.qv_obsDrkCur_rd1.setMaximumSize(QtCore.QSize(16777215, 27))
            font = QtGui.QFont()
            font.setFamily("fonts/SourceSansPro-Regular.ttf")
            font.setPointSize(10)
            font.setKerning(True)
            font.setStyleStrategy(QtGui.QFont.PreferAntialias)
            self.qv_obsDrkCur_rd1.setFont(font)
            self.qv_obsDrkCur_rd1.setObjectName("qv_obsDrkCur_rd1")
            self.buttonGroup_2 = QtWidgets.QButtonGroup()
            self.buttonGroup_2.setObjectName("buttonGroup_2")
            self.buttonGroup_2.addButton(self.qv_obsDrkCur_rd1)
            self.horizontalLayout_4.addWidget(self.qv_obsDrkCur_rd1)
            spacerItem12 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
            self.horizontalLayout_4.addItem(spacerItem12)
            self.qv_obsDrkCur_rd2 = QtWidgets.QRadioButton()
            self.qv_obsDrkCur_rd2.setMinimumSize(QtCore.QSize(51, 27))
            self.qv_obsDrkCur_rd2.setMaximumSize(QtCore.QSize(16777215, 27))
            font = QtGui.QFont()
            font.setFamily("fonts/SourceSansPro-Regular.ttf")
            font.setPointSize(10)
            font.setKerning(True)
            font.setStyleStrategy(QtGui.QFont.PreferAntialias)
            self.qv_obsDrkCur_rd2.setFont(font)
            self.qv_obsDrkCur_rd2.setObjectName("qv_obsDrkCur_rd2")
            self.buttonGroup_2.addButton(self.qv_obsDrkCur_rd2)
            self.horizontalLayout_4.addWidget(self.qv_obsDrkCur_rd2)
            self.infoButton_33 = QtWidgets.QToolButton()
            self.infoButton_33.setMaximumSize(QtCore.QSize(27, 27))
            self.infoButton_33.setStyleSheet("QToolButton {\n"
    "    border: 1px solid transparent;\n"
    "    background-color: transparent;\n"
    "    width: 27px;\n"
    "    height: 27px;\n"
    "}\n"
    "\n"
    "QToolButton:hover {\n"
    "    border: 1px solid gray;\n"
    "    border-radius: 3px;\n"
    "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
    "}\n"
    "\n"
    "QToolButton:pressed {\n"
    "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
    "}\n"
    "\n"
    "QToolButton:flat {\n"
    "    border: none;\n"
    "}")
            self.infoButton_33.setText("")
            self.infoButton_33.setIcon(icon1)
            self.infoButton_33.setIconSize(QtCore.QSize(27, 27))
            self.infoButton_33.setAutoRaise(False)
            self.infoButton_33.setObjectName("infoButton_33")
            self.horizontalLayout_4.addWidget(self.infoButton_33)
            spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.horizontalLayout_4.addItem(spacerItem13)
            self.gridLayout_102.addLayout(self.horizontalLayout_4, 1, 1, 1, 1)
            self.horizontalLayout_89.addLayout(self.gridLayout_102)
            spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.horizontalLayout_89.addItem(spacerItem14)
            self.verticalLayout_25.addLayout(self.horizontalLayout_89)
            spacerItem15 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
            self.verticalLayout_25.addItem(spacerItem15)
            self.horizontalLayout_90 = QtWidgets.QHBoxLayout()
            self.horizontalLayout_90.setObjectName("horizontalLayout_90")
            self.qv_obsQuaLay = QtWidgets.QLabel()
            self.qv_obsQuaLay.setMinimumSize(QtCore.QSize(160, 27))
            self.qv_obsQuaLay.setMaximumSize(QtCore.QSize(16777215, 27))
            font = QtGui.QFont()
            font.setFamily("fonts/SourceSansPro-Regular.ttf")
            font.setPointSize(10)
            font.setBold(True)
            font.setUnderline(True)
            font.setWeight(75)
            font.setKerning(True)
            font.setStyleStrategy(QtGui.QFont.PreferAntialias)
            self.qv_obsQuaLay.setFont(font)
            self.qv_obsQuaLay.setObjectName("qv_obsQuaLay")
            self.horizontalLayout_90.addWidget(self.qv_obsQuaLay)
            self.infoButton_34 = QtWidgets.QToolButton()
            self.infoButton_34.setMaximumSize(QtCore.QSize(27, 27))
            self.infoButton_34.setStyleSheet("QToolButton {\n"
    "    border: 1px solid transparent;\n"
    "    background-color: transparent;\n"
    "    width: 27px;\n"
    "    height: 27px;\n"
    "}\n"
    "\n"
    "QToolButton:hover {\n"
    "    border: 1px solid gray;\n"
    "    border-radius: 3px;\n"
    "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
    "}\n"
    "\n"
    "QToolButton:pressed {\n"
    "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
    "}\n"
    "\n"
    "QToolButton:flat {\n"
    "    border: none;\n"
    "}")
            self.infoButton_34.setText("")
            self.infoButton_34.setIcon(icon1)
            self.infoButton_34.setIconSize(QtCore.QSize(27, 27))
            self.infoButton_34.setAutoRaise(False)
            self.infoButton_34.setObjectName("infoButton_34")
            self.horizontalLayout_90.addWidget(self.infoButton_34)
            spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.horizontalLayout_90.addItem(spacerItem16)
            self.verticalLayout_25.addLayout(self.horizontalLayout_90)
            self.horizontalLayout_99 = QtWidgets.QHBoxLayout()
            self.horizontalLayout_99.setObjectName("horizontalLayout_99")
            spacerItem17 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
            self.horizontalLayout_99.addItem(spacerItem17)
            self.verticalLayout_100 = QtWidgets.QVBoxLayout()
            self.verticalLayout_100.setObjectName("verticalLayout_100")
            self.horizontalLayout_91 = QtWidgets.QHBoxLayout()
            self.horizontalLayout_91.setObjectName("horizontalLayout_91")
            self.qv_obsCalCorr = QtWidgets.QLabel()
            self.qv_obsCalCorr.setMinimumSize(QtCore.QSize(300, 27))
            self.qv_obsCalCorr.setMaximumSize(QtCore.QSize(16777215, 27))
            font = QtGui.QFont()
            font.setFamily("fonts/SourceSansPro-Regular.ttf")
            font.setPointSize(10)
            font.setUnderline(True)
            font.setKerning(True)
            font.setStyleStrategy(QtGui.QFont.PreferAntialias)
            self.qv_obsCalCorr.setFont(font)
            self.qv_obsCalCorr.setObjectName("qv_obsCalCorr")
            self.horizontalLayout_91.addWidget(self.qv_obsCalCorr)
            spacerItem18 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.horizontalLayout_91.addItem(spacerItem18)
            self.verticalLayout_100.addLayout(self.horizontalLayout_91)
            self.horizontalLayout_92 = QtWidgets.QHBoxLayout()
            self.horizontalLayout_92.setObjectName("horizontalLayout_92")
            spacerItem19 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
            self.horizontalLayout_92.addItem(spacerItem19)
            self.gridLayout_103 = QtWidgets.QGridLayout()
            self.gridLayout_103.setHorizontalSpacing(20)
            self.gridLayout_103.setVerticalSpacing(10)
            self.gridLayout_103.setObjectName("gridLayout_103")
            self.qv_obsIntMask = QtWidgets.QLabel()
            self.qv_obsIntMask.setMinimumSize(QtCore.QSize(380, 27))
            self.qv_obsIntMask.setMaximumSize(QtCore.QSize(16777215, 27))
            font = QtGui.QFont()
            font.setFamily("fonts/SourceSansPro-Regular.ttf")
            font.setPointSize(10)
            font.setKerning(True)
            font.setStyleStrategy(QtGui.QFont.PreferAntialias)
            self.qv_obsIntMask.setFont(font)
            self.qv_obsIntMask.setObjectName("qv_obsIntMask")
            self.gridLayout_103.addWidget(self.qv_obsIntMask, 0, 0, 1, 1)
            self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
            self.horizontalLayout_9.setObjectName("horizontalLayout_9")
            self.qv_obsIntMask_rd1 = QtWidgets.QRadioButton()
            self.qv_obsIntMask_rd1.setMinimumSize(QtCore.QSize(51, 27))
            self.qv_obsIntMask_rd1.setMaximumSize(QtCore.QSize(16777215, 27))
            font = QtGui.QFont()
            font.setFamily("fonts/SourceSansPro-Regular.ttf")
            font.setPointSize(10)
            font.setKerning(True)
            font.setStyleStrategy(QtGui.QFont.PreferAntialias)
            self.qv_obsIntMask_rd1.setFont(font)
            self.qv_obsIntMask_rd1.setObjectName("qv_obsIntMask_rd1")
            self.buttonGroup_3 = QtWidgets.QButtonGroup()
            self.buttonGroup_3.setObjectName("buttonGroup_3")
            self.buttonGroup_3.addButton(self.qv_obsIntMask_rd1)
            self.horizontalLayout_9.addWidget(self.qv_obsIntMask_rd1)
            spacerItem20 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
            self.horizontalLayout_9.addItem(spacerItem20)
            self.qv_obsIntMask_rd2 = QtWidgets.QRadioButton()
            self.qv_obsIntMask_rd2.setMinimumSize(QtCore.QSize(51, 27))
            self.qv_obsIntMask_rd2.setMaximumSize(QtCore.QSize(16777215, 27))
            font = QtGui.QFont()
            font.setFamily("fonts/SourceSansPro-Regular.ttf")
            font.setPointSize(10)
            font.setKerning(True)
            font.setStyleStrategy(QtGui.QFont.PreferAntialias)
            self.qv_obsIntMask_rd2.setFont(font)
            self.qv_obsIntMask_rd2.setObjectName("qv_obsIntMask_rd2")
            self.buttonGroup_3.addButton(self.qv_obsIntMask_rd2)
            self.horizontalLayout_9.addWidget(self.qv_obsIntMask_rd2)
            self.infoButton_35 = QtWidgets.QToolButton()
            self.infoButton_35.setMaximumSize(QtCore.QSize(27, 27))
            self.infoButton_35.setStyleSheet("QToolButton {\n"
    "    border: 1px solid transparent;\n"
    "    background-color: transparent;\n"
    "    width: 27px;\n"
    "    height: 27px;\n"
    "}\n"
    "\n"
    "QToolButton:hover {\n"
    "    border: 1px solid gray;\n"
    "    border-radius: 3px;\n"
    "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
    "}\n"
    "\n"
    "QToolButton:pressed {\n"
    "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
    "}\n"
    "\n"
    "QToolButton:flat {\n"
    "    border: none;\n"
    "}")
            self.infoButton_35.setText("")
            self.infoButton_35.setIcon(icon1)
            self.infoButton_35.setIconSize(QtCore.QSize(27, 27))
            self.infoButton_35.setAutoRaise(False)
            self.infoButton_35.setObjectName("infoButton_35")
            self.horizontalLayout_9.addWidget(self.infoButton_35)
            spacerItem21 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.horizontalLayout_9.addItem(spacerItem21)
            self.gridLayout_103.addLayout(self.horizontalLayout_9, 0, 1, 1, 1)
            self.qv_obsBadMask = QtWidgets.QLabel()
            self.qv_obsBadMask.setMinimumSize(QtCore.QSize(380, 27))
            self.qv_obsBadMask.setMaximumSize(QtCore.QSize(16777215, 27))
            font = QtGui.QFont()
            font.setFamily("fonts/SourceSansPro-Regular.ttf")
            font.setPointSize(10)
            font.setKerning(True)
            font.setStyleStrategy(QtGui.QFont.PreferAntialias)
            self.qv_obsBadMask.setFont(font)
            self.qv_obsBadMask.setObjectName("qv_obsBadMask")
            self.gridLayout_103.addWidget(self.qv_obsBadMask, 1, 0, 1, 1)
            self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
            self.horizontalLayout_10.setObjectName("horizontalLayout_10")
            self.qv_obsBadMask_rd1 = QtWidgets.QRadioButton()
            self.qv_obsBadMask_rd1.setMinimumSize(QtCore.QSize(51, 27))
            self.qv_obsBadMask_rd1.setMaximumSize(QtCore.QSize(16777215, 27))
            font = QtGui.QFont()
            font.setFamily("fonts/SourceSansPro-Regular.ttf")
            font.setPointSize(10)
            font.setKerning(True)
            font.setStyleStrategy(QtGui.QFont.PreferAntialias)
            self.qv_obsBadMask_rd1.setFont(font)
            self.qv_obsBadMask_rd1.setObjectName("qv_obsBadMask_rd1")
            self.buttonGroup_4 = QtWidgets.QButtonGroup()
            self.buttonGroup_4.setObjectName("buttonGroup_4")
            self.buttonGroup_4.addButton(self.qv_obsBadMask_rd1)
            self.horizontalLayout_10.addWidget(self.qv_obsBadMask_rd1)
            spacerItem22 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
            self.horizontalLayout_10.addItem(spacerItem22)
            self.qv_obsBadMask_rd2 = QtWidgets.QRadioButton()
            self.qv_obsBadMask_rd2.setMinimumSize(QtCore.QSize(51, 27))
            self.qv_obsBadMask_rd2.setMaximumSize(QtCore.QSize(16777215, 27))
            font = QtGui.QFont()
            font.setFamily("fonts/SourceSansPro-Regular.ttf")
            font.setPointSize(10)
            font.setKerning(True)
            font.setStyleStrategy(QtGui.QFont.PreferAntialias)
            self.qv_obsBadMask_rd2.setFont(font)
            self.qv_obsBadMask_rd2.setObjectName("qv_obsBadMask_rd2")
            self.buttonGroup_4.addButton(self.qv_obsBadMask_rd2)
            self.horizontalLayout_10.addWidget(self.qv_obsBadMask_rd2)
            self.infoButton_36 = QtWidgets.QToolButton()
            self.infoButton_36.setMaximumSize(QtCore.QSize(27, 27))
            self.infoButton_36.setStyleSheet("QToolButton {\n"
    "    border: 1px solid transparent;\n"
    "    background-color: transparent;\n"
    "    width: 27px;\n"
    "    height: 27px;\n"
    "}\n"
    "\n"
    "QToolButton:hover {\n"
    "    border: 1px solid gray;\n"
    "    border-radius: 3px;\n"
    "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
    "}\n"
    "\n"
    "QToolButton:pressed {\n"
    "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
    "}\n"
    "\n"
    "QToolButton:flat {\n"
    "    border: none;\n"
    "}")
            self.infoButton_36.setText("")
            self.infoButton_36.setIcon(icon1)
            self.infoButton_36.setIconSize(QtCore.QSize(27, 27))
            self.infoButton_36.setAutoRaise(False)
            self.infoButton_36.setObjectName("infoButton_36")
            self.horizontalLayout_10.addWidget(self.infoButton_36)
            spacerItem23 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.horizontalLayout_10.addItem(spacerItem23)
            self.gridLayout_103.addLayout(self.horizontalLayout_10, 1, 1, 1, 1)
            self.horizontalLayout_92.addLayout(self.gridLayout_103)
            spacerItem24 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.horizontalLayout_92.addItem(spacerItem24)
            self.verticalLayout_100.addLayout(self.horizontalLayout_92)
            spacerItem25 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
            self.verticalLayout_100.addItem(spacerItem25)
            self.horizontalLayout_93 = QtWidgets.QHBoxLayout()
            self.horizontalLayout_93.setObjectName("horizontalLayout_93")
            self.qv_obsProError = QtWidgets.QLabel()
            self.qv_obsProError.setMinimumSize(QtCore.QSize(300, 27))
            self.qv_obsProError.setMaximumSize(QtCore.QSize(16777215, 27))
            font = QtGui.QFont()
            font.setFamily("fonts/SourceSansPro-Regular.ttf")
            font.setPointSize(10)
            font.setUnderline(True)
            font.setKerning(True)
            font.setStyleStrategy(QtGui.QFont.PreferAntialias)
            self.qv_obsProError.setFont(font)
            self.qv_obsProError.setObjectName("qv_obsProError")
            self.horizontalLayout_93.addWidget(self.qv_obsProError)
            spacerItem26 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.horizontalLayout_93.addItem(spacerItem26)
            self.verticalLayout_100.addLayout(self.horizontalLayout_93)
            self.horizontalLayout_94 = QtWidgets.QHBoxLayout()
            self.horizontalLayout_94.setObjectName("horizontalLayout_94")
            spacerItem27 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
            self.horizontalLayout_94.addItem(spacerItem27)
            self.gridLayout_104 = QtWidgets.QGridLayout()
            self.gridLayout_104.setHorizontalSpacing(20)
            self.gridLayout_104.setVerticalSpacing(10)
            self.gridLayout_104.setObjectName("gridLayout_104")
            self.qv_obsSatPix = QtWidgets.QLabel()
            self.qv_obsSatPix.setMinimumSize(QtCore.QSize(430, 27))
            self.qv_obsSatPix.setMaximumSize(QtCore.QSize(16777215, 27))
            font = QtGui.QFont()
            font.setFamily("fonts/SourceSansPro-Regular.ttf")
            font.setPointSize(10)
            font.setKerning(True)
            font.setStyleStrategy(QtGui.QFont.PreferAntialias)
            self.qv_obsSatPix.setFont(font)
            self.qv_obsSatPix.setObjectName("qv_obsSatPix")
            self.gridLayout_104.addWidget(self.qv_obsSatPix, 0, 0, 1, 1)
            self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
            self.horizontalLayout_11.setObjectName("horizontalLayout_11")
            self.qv_obsSatPix_rd1 = QtWidgets.QRadioButton()
            self.qv_obsSatPix_rd1.setMinimumSize(QtCore.QSize(51, 27))
            self.qv_obsSatPix_rd1.setMaximumSize(QtCore.QSize(16777215, 27))
            font = QtGui.QFont()
            font.setFamily("fonts/SourceSansPro-Regular.ttf")
            font.setPointSize(10)
            font.setKerning(True)
            font.setStyleStrategy(QtGui.QFont.PreferAntialias)
            self.qv_obsSatPix_rd1.setFont(font)
            self.qv_obsSatPix_rd1.setObjectName("qv_obsSatPix_rd1")
            self.buttonGroup_5 = QtWidgets.QButtonGroup()
            self.buttonGroup_5.setObjectName("buttonGroup_5")
            self.buttonGroup_5.addButton(self.qv_obsSatPix_rd1)
            self.horizontalLayout_11.addWidget(self.qv_obsSatPix_rd1)
            spacerItem28 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
            self.horizontalLayout_11.addItem(spacerItem28)
            self.qv_obsSatPix_rd2 = QtWidgets.QRadioButton()
            self.qv_obsSatPix_rd2.setMinimumSize(QtCore.QSize(51, 27))
            self.qv_obsSatPix_rd2.setMaximumSize(QtCore.QSize(16777215, 27))
            font = QtGui.QFont()
            font.setFamily("fonts/SourceSansPro-Regular.ttf")
            font.setPointSize(10)
            font.setKerning(True)
            font.setStyleStrategy(QtGui.QFont.PreferAntialias)
            self.qv_obsSatPix_rd2.setFont(font)
            self.qv_obsSatPix_rd2.setObjectName("qv_obsSatPix_rd2")
            self.buttonGroup_5.addButton(self.qv_obsSatPix_rd2)
            self.horizontalLayout_11.addWidget(self.qv_obsSatPix_rd2)
            self.infoButton_37 = QtWidgets.QToolButton()
            self.infoButton_37.setMaximumSize(QtCore.QSize(27, 27))
            self.infoButton_37.setStyleSheet("QToolButton {\n"
    "    border: 1px solid transparent;\n"
    "    background-color: transparent;\n"
    "    width: 27px;\n"
    "    height: 27px;\n"
    "}\n"
    "\n"
    "QToolButton:hover {\n"
    "    border: 1px solid gray;\n"
    "    border-radius: 3px;\n"
    "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
    "}\n"
    "\n"
    "QToolButton:pressed {\n"
    "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
    "}\n"
    "\n"
    "QToolButton:flat {\n"
    "    border: none;\n"
    "}")
            self.infoButton_37.setText("")
            self.infoButton_37.setIcon(icon1)
            self.infoButton_37.setIconSize(QtCore.QSize(27, 27))
            self.infoButton_37.setAutoRaise(False)
            self.infoButton_37.setObjectName("infoButton_37")
            self.horizontalLayout_11.addWidget(self.infoButton_37)
            spacerItem29 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.horizontalLayout_11.addItem(spacerItem29)
            self.gridLayout_104.addLayout(self.horizontalLayout_11, 0, 1, 1, 1)
            self.qv_obsSpeNeigh = QtWidgets.QLabel()
            self.qv_obsSpeNeigh.setMinimumSize(QtCore.QSize(430, 27))
            self.qv_obsSpeNeigh.setMaximumSize(QtCore.QSize(16777215, 27))
            font = QtGui.QFont()
            font.setFamily("fonts/SourceSansPro-Regular.ttf")
            font.setPointSize(10)
            font.setKerning(True)
            font.setStyleStrategy(QtGui.QFont.PreferAntialias)
            self.qv_obsSpeNeigh.setFont(font)
            self.qv_obsSpeNeigh.setObjectName("qv_obsSpeNeigh")
            self.gridLayout_104.addWidget(self.qv_obsSpeNeigh, 1, 0, 1, 1)
            self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
            self.horizontalLayout_12.setObjectName("horizontalLayout_12")
            self.qv_obsSpeNeigh_rd1 = QtWidgets.QRadioButton()
            self.qv_obsSpeNeigh_rd1.setMinimumSize(QtCore.QSize(51, 27))
            self.qv_obsSpeNeigh_rd1.setMaximumSize(QtCore.QSize(16777215, 27))
            font = QtGui.QFont()
            font.setFamily("fonts/SourceSansPro-Regular.ttf")
            font.setPointSize(10)
            font.setKerning(True)
            font.setStyleStrategy(QtGui.QFont.PreferAntialias)
            self.qv_obsSpeNeigh_rd1.setFont(font)
            self.qv_obsSpeNeigh_rd1.setObjectName("qv_obsSpeNeigh_rd1")
            self.buttonGroup_6 = QtWidgets.QButtonGroup()
            self.buttonGroup_6.setObjectName("buttonGroup_6")
            self.buttonGroup_6.addButton(self.qv_obsSpeNeigh_rd1)
            self.horizontalLayout_12.addWidget(self.qv_obsSpeNeigh_rd1)
            spacerItem30 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
            self.horizontalLayout_12.addItem(spacerItem30)
            self.qv_obsSpeNeigh_rd2 = QtWidgets.QRadioButton()
            self.qv_obsSpeNeigh_rd2.setMinimumSize(QtCore.QSize(51, 27))
            self.qv_obsSpeNeigh_rd2.setMaximumSize(QtCore.QSize(16777215, 27))
            font = QtGui.QFont()
            font.setFamily("fonts/SourceSansPro-Regular.ttf")
            font.setPointSize(10)
            font.setKerning(True)
            font.setStyleStrategy(QtGui.QFont.PreferAntialias)
            self.qv_obsSpeNeigh_rd2.setFont(font)
            self.qv_obsSpeNeigh_rd2.setObjectName("qv_obsSpeNeigh_rd2")
            self.buttonGroup_6.addButton(self.qv_obsSpeNeigh_rd2)
            self.horizontalLayout_12.addWidget(self.qv_obsSpeNeigh_rd2)
            self.infoButton_38 = QtWidgets.QToolButton()
            self.infoButton_38.setMaximumSize(QtCore.QSize(27, 27))
            self.infoButton_38.setStyleSheet("QToolButton {\n"
    "    border: 1px solid transparent;\n"
    "    background-color: transparent;\n"
    "    width: 27px;\n"
    "    height: 27px;\n"
    "}\n"
    "\n"
    "QToolButton:hover {\n"
    "    border: 1px solid gray;\n"
    "    border-radius: 3px;\n"
    "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
    "}\n"
    "\n"
    "QToolButton:pressed {\n"
    "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
    "}\n"
    "\n"
    "QToolButton:flat {\n"
    "    border: none;\n"
    "}")
            self.infoButton_38.setText("")
            self.infoButton_38.setIcon(icon1)
            self.infoButton_38.setIconSize(QtCore.QSize(27, 27))
            self.infoButton_38.setAutoRaise(False)
            self.infoButton_38.setObjectName("infoButton_38")
            self.horizontalLayout_12.addWidget(self.infoButton_38)
            spacerItem31 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.horizontalLayout_12.addItem(spacerItem31)
            self.gridLayout_104.addLayout(self.horizontalLayout_12, 1, 1, 1, 1)
            self.horizontalLayout_94.addLayout(self.gridLayout_104)
            spacerItem32 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.horizontalLayout_94.addItem(spacerItem32)
            self.verticalLayout_100.addLayout(self.horizontalLayout_94)
            spacerItem33 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
            self.verticalLayout_100.addItem(spacerItem33)
            self.horizontalLayout_95 = QtWidgets.QHBoxLayout()
            self.horizontalLayout_95.setObjectName("horizontalLayout_95")
            self.qv_obsGeoCorr = QtWidgets.QLabel()
            self.qv_obsGeoCorr.setMinimumSize(QtCore.QSize(310, 27))
            self.qv_obsGeoCorr.setMaximumSize(QtCore.QSize(16777215, 27))
            font = QtGui.QFont()
            font.setFamily("fonts/SourceSansPro-Regular.ttf")
            font.setPointSize(10)
            font.setUnderline(True)
            font.setKerning(True)
            font.setStyleStrategy(QtGui.QFont.PreferAntialias)
            self.qv_obsGeoCorr.setFont(font)
            self.qv_obsGeoCorr.setObjectName("qv_obsGeoCorr")
            self.horizontalLayout_95.addWidget(self.qv_obsGeoCorr)
            self.infoButton_39 = QtWidgets.QToolButton()
            self.infoButton_39.setMaximumSize(QtCore.QSize(27, 27))
            self.infoButton_39.setStyleSheet("QToolButton {\n"
    "    border: 1px solid transparent;\n"
    "    background-color: transparent;\n"
    "    width: 27px;\n"
    "    height: 27px;\n"
    "}\n"
    "\n"
    "QToolButton:hover {\n"
    "    border: 1px solid gray;\n"
    "    border-radius: 3px;\n"
    "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
    "}\n"
    "\n"
    "QToolButton:pressed {\n"
    "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
    "}\n"
    "\n"
    "QToolButton:flat {\n"
    "    border: none;\n"
    "}")
            self.infoButton_39.setText("")
            self.infoButton_39.setIcon(icon1)
            self.infoButton_39.setIconSize(QtCore.QSize(27, 27))
            self.infoButton_39.setAutoRaise(False)
            self.infoButton_39.setObjectName("infoButton_39")
            self.horizontalLayout_95.addWidget(self.infoButton_39)
            spacerItem34 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.horizontalLayout_95.addItem(spacerItem34)
            self.verticalLayout_100.addLayout(self.horizontalLayout_95)
            self.horizontalLayout_96 = QtWidgets.QHBoxLayout()
            self.horizontalLayout_96.setObjectName("horizontalLayout_96")
            spacerItem35 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
            self.horizontalLayout_96.addItem(spacerItem35)
            self.gridLayout_105 = QtWidgets.QGridLayout()
            self.gridLayout_105.setHorizontalSpacing(20)
            self.gridLayout_105.setVerticalSpacing(10)
            self.gridLayout_105.setObjectName("gridLayout_105")
            self.qv_obsPosInfo = QtWidgets.QLabel()
            self.qv_obsPosInfo.setMinimumSize(QtCore.QSize(480, 27))
            self.qv_obsPosInfo.setMaximumSize(QtCore.QSize(16777215, 27))
            font = QtGui.QFont()
            font.setFamily("fonts/SourceSansPro-Regular.ttf")
            font.setPointSize(10)
            font.setKerning(True)
            font.setStyleStrategy(QtGui.QFont.PreferAntialias)
            self.qv_obsPosInfo.setFont(font)
            self.qv_obsPosInfo.setObjectName("qv_obsPosInfo")
            self.gridLayout_105.addWidget(self.qv_obsPosInfo, 0, 0, 1, 1)
            self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
            self.horizontalLayout_15.setObjectName("horizontalLayout_15")
            self.qv_obsPosInfo_rd1 = QtWidgets.QRadioButton()
            self.qv_obsPosInfo_rd1.setMinimumSize(QtCore.QSize(51, 27))
            self.qv_obsPosInfo_rd1.setMaximumSize(QtCore.QSize(16777215, 27))
            font = QtGui.QFont()
            font.setFamily("fonts/SourceSansPro-Regular.ttf")
            font.setPointSize(10)
            font.setKerning(True)
            font.setStyleStrategy(QtGui.QFont.PreferAntialias)
            self.qv_obsPosInfo_rd1.setFont(font)
            self.qv_obsPosInfo_rd1.setObjectName("qv_obsPosInfo_rd1")
            self.buttonGroup_7 = QtWidgets.QButtonGroup()
            self.buttonGroup_7.setObjectName("buttonGroup_7")
            self.buttonGroup_7.addButton(self.qv_obsPosInfo_rd1)
            self.horizontalLayout_15.addWidget(self.qv_obsPosInfo_rd1)
            spacerItem36 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
            self.horizontalLayout_15.addItem(spacerItem36)
            self.qv_obsPosInfo_rd2 = QtWidgets.QRadioButton()
            self.qv_obsPosInfo_rd2.setMinimumSize(QtCore.QSize(51, 27))
            self.qv_obsPosInfo_rd2.setMaximumSize(QtCore.QSize(16777215, 27))
            font = QtGui.QFont()
            font.setFamily("fonts/SourceSansPro-Regular.ttf")
            font.setPointSize(10)
            font.setKerning(True)
            font.setStyleStrategy(QtGui.QFont.PreferAntialias)
            self.qv_obsPosInfo_rd2.setFont(font)
            self.qv_obsPosInfo_rd2.setObjectName("qv_obsPosInfo_rd2")
            self.buttonGroup_7.addButton(self.qv_obsPosInfo_rd2)
            self.horizontalLayout_15.addWidget(self.qv_obsPosInfo_rd2)
            spacerItem37 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.horizontalLayout_15.addItem(spacerItem37)
            self.gridLayout_105.addLayout(self.horizontalLayout_15, 0, 1, 1, 1)
            self.qv_obsAttInfo = QtWidgets.QLabel()
            self.qv_obsAttInfo.setMinimumSize(QtCore.QSize(480, 27))
            self.qv_obsAttInfo.setMaximumSize(QtCore.QSize(16777215, 27))
            font = QtGui.QFont()
            font.setFamily("fonts/SourceSansPro-Regular.ttf")
            font.setPointSize(10)
            font.setKerning(True)
            font.setStyleStrategy(QtGui.QFont.PreferAntialias)
            self.qv_obsAttInfo.setFont(font)
            self.qv_obsAttInfo.setObjectName("qv_obsAttInfo")
            self.gridLayout_105.addWidget(self.qv_obsAttInfo, 1, 0, 1, 1)
            self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
            self.horizontalLayout_16.setObjectName("horizontalLayout_16")
            self.qv_obsAttInf_rd1 = QtWidgets.QRadioButton()
            self.qv_obsAttInf_rd1.setMinimumSize(QtCore.QSize(51, 27))
            self.qv_obsAttInf_rd1.setMaximumSize(QtCore.QSize(16777215, 27))
            font = QtGui.QFont()
            font.setFamily("fonts/SourceSansPro-Regular.ttf")
            font.setPointSize(10)
            font.setKerning(True)
            font.setStyleStrategy(QtGui.QFont.PreferAntialias)
            self.qv_obsAttInf_rd1.setFont(font)
            self.qv_obsAttInf_rd1.setObjectName("qv_obsAttInf_rd1")
            self.buttonGroup_8 = QtWidgets.QButtonGroup()
            self.buttonGroup_8.setObjectName("buttonGroup_8")
            self.buttonGroup_8.addButton(self.qv_obsAttInf_rd1)
            self.horizontalLayout_16.addWidget(self.qv_obsAttInf_rd1)
            spacerItem38 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
            self.horizontalLayout_16.addItem(spacerItem38)
            self.qv_obsAttInf_rd2 = QtWidgets.QRadioButton()
            self.qv_obsAttInf_rd2.setMinimumSize(QtCore.QSize(51, 27))
            self.qv_obsAttInf_rd2.setMaximumSize(QtCore.QSize(16777215, 27))
            font = QtGui.QFont()
            font.setFamily("fonts/SourceSansPro-Regular.ttf")
            font.setPointSize(10)
            font.setKerning(True)
            font.setStyleStrategy(QtGui.QFont.PreferAntialias)
            self.qv_obsAttInf_rd2.setFont(font)
            self.qv_obsAttInf_rd2.setObjectName("qv_obsAttInf_rd2")
            self.buttonGroup_8.addButton(self.qv_obsAttInf_rd2)
            self.horizontalLayout_16.addWidget(self.qv_obsAttInf_rd2)
            spacerItem39 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.horizontalLayout_16.addItem(spacerItem39)
            self.gridLayout_105.addLayout(self.horizontalLayout_16, 1, 1, 1, 1)
            self.qv_obsSynprob = QtWidgets.QLabel()
            self.qv_obsSynprob.setMinimumSize(QtCore.QSize(480, 27))
            self.qv_obsSynprob.setMaximumSize(QtCore.QSize(16777215, 27))
            font = QtGui.QFont()
            font.setFamily("fonts/SourceSansPro-Regular.ttf")
            font.setPointSize(10)
            font.setKerning(True)
            font.setStyleStrategy(QtGui.QFont.PreferAntialias)
            self.qv_obsSynprob.setFont(font)
            self.qv_obsSynprob.setObjectName("qv_obsSynprob")
            self.gridLayout_105.addWidget(self.qv_obsSynprob, 2, 0, 1, 1)
            self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
            self.horizontalLayout_17.setObjectName("horizontalLayout_17")
            self.qv_obsSynprob_rd1 = QtWidgets.QRadioButton()
            self.qv_obsSynprob_rd1.setMinimumSize(QtCore.QSize(51, 27))
            self.qv_obsSynprob_rd1.setMaximumSize(QtCore.QSize(16777215, 27))
            font = QtGui.QFont()
            font.setFamily("fonts/SourceSansPro-Regular.ttf")
            font.setPointSize(10)
            font.setKerning(True)
            font.setStyleStrategy(QtGui.QFont.PreferAntialias)
            self.qv_obsSynprob_rd1.setFont(font)
            self.qv_obsSynprob_rd1.setObjectName("qv_obsSynprob_rd1")
            self.buttonGroup_9 = QtWidgets.QButtonGroup()
            self.buttonGroup_9.setObjectName("buttonGroup_9")
            self.buttonGroup_9.addButton(self.qv_obsSynprob_rd1)
            self.horizontalLayout_17.addWidget(self.qv_obsSynprob_rd1)
            spacerItem40 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
            self.horizontalLayout_17.addItem(spacerItem40)
            self.qv_obsSynprob_rd2 = QtWidgets.QRadioButton()
            self.qv_obsSynprob_rd2.setMinimumSize(QtCore.QSize(51, 27))
            self.qv_obsSynprob_rd2.setMaximumSize(QtCore.QSize(16777215, 27))
            font = QtGui.QFont()
            font.setFamily("fonts/SourceSansPro-Regular.ttf")
            font.setPointSize(10)
            font.setKerning(True)
            font.setStyleStrategy(QtGui.QFont.PreferAntialias)
            self.qv_obsSynprob_rd2.setFont(font)
            self.qv_obsSynprob_rd2.setObjectName("qv_obsSynprob_rd2")
            self.buttonGroup_9.addButton(self.qv_obsSynprob_rd2)
            self.horizontalLayout_17.addWidget(self.qv_obsSynprob_rd2)
            spacerItem41 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.horizontalLayout_17.addItem(spacerItem41)
            self.gridLayout_105.addLayout(self.horizontalLayout_17, 2, 1, 1, 1)
            self.qv_obsIntGeo = QtWidgets.QLabel()
            self.qv_obsIntGeo.setMinimumSize(QtCore.QSize(480, 27))
            self.qv_obsIntGeo.setMaximumSize(QtCore.QSize(16777215, 27))
            font = QtGui.QFont()
            font.setFamily("fonts/SourceSansPro-Regular.ttf")
            font.setPointSize(10)
            font.setKerning(True)
            font.setStyleStrategy(QtGui.QFont.PreferAntialias)
            self.qv_obsIntGeo.setFont(font)
            self.qv_obsIntGeo.setObjectName("qv_obsIntGeo")
            self.gridLayout_105.addWidget(self.qv_obsIntGeo, 3, 0, 1, 1)
            self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
            self.horizontalLayout_18.setObjectName("horizontalLayout_18")
            self.qv_obsIntGeo_rd1 = QtWidgets.QRadioButton()
            self.qv_obsIntGeo_rd1.setMinimumSize(QtCore.QSize(51, 27))
            self.qv_obsIntGeo_rd1.setMaximumSize(QtCore.QSize(16777215, 27))
            font = QtGui.QFont()
            font.setFamily("fonts/SourceSansPro-Regular.ttf")
            font.setPointSize(10)
            font.setKerning(True)
            font.setStyleStrategy(QtGui.QFont.PreferAntialias)
            self.qv_obsIntGeo_rd1.setFont(font)
            self.qv_obsIntGeo_rd1.setObjectName("qv_obsIntGeo_rd1")
            self.buttonGroup_10 = QtWidgets.QButtonGroup()
            self.buttonGroup_10.setObjectName("buttonGroup_10")
            self.buttonGroup_10.addButton(self.qv_obsIntGeo_rd1)
            self.horizontalLayout_18.addWidget(self.qv_obsIntGeo_rd1)
            spacerItem42 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
            self.horizontalLayout_18.addItem(spacerItem42)
            self.qv_obsIntGeo_rd2 = QtWidgets.QRadioButton()
            self.qv_obsIntGeo_rd2.setMinimumSize(QtCore.QSize(51, 27))
            self.qv_obsIntGeo_rd2.setMaximumSize(QtCore.QSize(16777215, 27))
            font = QtGui.QFont()
            font.setFamily("fonts/SourceSansPro-Regular.ttf")
            font.setPointSize(10)
            font.setKerning(True)
            font.setStyleStrategy(QtGui.QFont.PreferAntialias)
            self.qv_obsIntGeo_rd2.setFont(font)
            self.qv_obsIntGeo_rd2.setObjectName("qv_obsIntGeo_rd2")
            self.buttonGroup_10.addButton(self.qv_obsIntGeo_rd2)
            self.horizontalLayout_18.addWidget(self.qv_obsIntGeo_rd2)
            spacerItem43 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.horizontalLayout_18.addItem(spacerItem43)
            self.gridLayout_105.addLayout(self.horizontalLayout_18, 3, 1, 1, 1)
            self.horizontalLayout_96.addLayout(self.gridLayout_105)
            spacerItem44 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.horizontalLayout_96.addItem(spacerItem44)
            self.verticalLayout_100.addLayout(self.horizontalLayout_96)
            spacerItem45 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
            self.verticalLayout_100.addItem(spacerItem45)
            self.horizontalLayout_97 = QtWidgets.QHBoxLayout()
            self.horizontalLayout_97.setObjectName("horizontalLayout_97")
            self.qv_obsAtmCond = QtWidgets.QLabel()
            self.qv_obsAtmCond.setMinimumSize(QtCore.QSize(400, 27))
            self.qv_obsAtmCond.setMaximumSize(QtCore.QSize(16777215, 27))
            font = QtGui.QFont()
            font.setFamily("fonts/SourceSansPro-Regular.ttf")
            font.setPointSize(10)
            font.setUnderline(True)
            font.setKerning(True)
            font.setStyleStrategy(QtGui.QFont.PreferAntialias)
            self.qv_obsAtmCond.setFont(font)
            self.qv_obsAtmCond.setObjectName("qv_obsAtmCond")
            self.horizontalLayout_97.addWidget(self.qv_obsAtmCond)
            spacerItem46 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.horizontalLayout_97.addItem(spacerItem46)
            self.verticalLayout_100.addLayout(self.horizontalLayout_97)
            self.horizontalLayout_98 = QtWidgets.QHBoxLayout()
            self.horizontalLayout_98.setObjectName("horizontalLayout_98")
            spacerItem47 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
            self.horizontalLayout_98.addItem(spacerItem47)
            self.gridLayout_106 = QtWidgets.QGridLayout()
            self.gridLayout_106.setHorizontalSpacing(20)
            self.gridLayout_106.setVerticalSpacing(10)
            self.gridLayout_106.setObjectName("gridLayout_106")
            self.qv_obsAtmCorr = QtWidgets.QLabel()
            self.qv_obsAtmCorr.setMinimumSize(QtCore.QSize(450, 27))
            self.qv_obsAtmCorr.setMaximumSize(QtCore.QSize(16777215, 27))
            font = QtGui.QFont()
            font.setFamily("fonts/SourceSansPro-Regular.ttf")
            font.setPointSize(10)
            font.setKerning(True)
            font.setStyleStrategy(QtGui.QFont.PreferAntialias)
            self.qv_obsAtmCorr.setFont(font)
            self.qv_obsAtmCorr.setObjectName("qv_obsAtmCorr")
            self.gridLayout_106.addWidget(self.qv_obsAtmCorr, 0, 0, 1, 1)
            self.horizontalLayout_23 = QtWidgets.QHBoxLayout()
            self.horizontalLayout_23.setObjectName("horizontalLayout_23")
            self.qv_obsAtmCorr_rd1 = QtWidgets.QRadioButton()
            self.qv_obsAtmCorr_rd1.setMinimumSize(QtCore.QSize(51, 27))
            self.qv_obsAtmCorr_rd1.setMaximumSize(QtCore.QSize(16777215, 27))
            font = QtGui.QFont()
            font.setFamily("fonts/SourceSansPro-Regular.ttf")
            font.setPointSize(10)
            font.setKerning(True)
            font.setStyleStrategy(QtGui.QFont.PreferAntialias)
            self.qv_obsAtmCorr_rd1.setFont(font)
            self.qv_obsAtmCorr_rd1.setObjectName("qv_obsAtmCorr_rd1")
            self.buttonGroup_11 = QtWidgets.QButtonGroup()
            self.buttonGroup_11.setObjectName("buttonGroup_11")
            self.buttonGroup_11.addButton(self.qv_obsAtmCorr_rd1)
            self.horizontalLayout_23.addWidget(self.qv_obsAtmCorr_rd1)
            spacerItem48 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
            self.horizontalLayout_23.addItem(spacerItem48)
            self.qv_obsAtmCorr_rd2 = QtWidgets.QRadioButton()
            self.qv_obsAtmCorr_rd2.setMinimumSize(QtCore.QSize(51, 27))
            self.qv_obsAtmCorr_rd2.setMaximumSize(QtCore.QSize(16777215, 27))
            font = QtGui.QFont()
            font.setFamily("fonts/SourceSansPro-Regular.ttf")
            font.setPointSize(10)
            font.setKerning(True)
            font.setStyleStrategy(QtGui.QFont.PreferAntialias)
            self.qv_obsAtmCorr_rd2.setFont(font)
            self.qv_obsAtmCorr_rd2.setObjectName("qv_obsAtmCorr_rd2")
            self.buttonGroup_11.addButton(self.qv_obsAtmCorr_rd2)
            self.horizontalLayout_23.addWidget(self.qv_obsAtmCorr_rd2)
            self.infoButton_40 = QtWidgets.QToolButton()
            self.infoButton_40.setMaximumSize(QtCore.QSize(27, 27))
            self.infoButton_40.setStyleSheet("QToolButton {\n"
    "    border: 1px solid transparent;\n"
    "    background-color: transparent;\n"
    "    width: 27px;\n"
    "    height: 27px;\n"
    "}\n"
    "\n"
    "QToolButton:hover {\n"
    "    border: 1px solid gray;\n"
    "    border-radius: 3px;\n"
    "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
    "}\n"
    "\n"
    "QToolButton:pressed {\n"
    "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
    "}\n"
    "\n"
    "QToolButton:flat {\n"
    "    border: none;\n"
    "}")
            self.infoButton_40.setText("")
            self.infoButton_40.setIcon(icon1)
            self.infoButton_40.setIconSize(QtCore.QSize(27, 27))
            self.infoButton_40.setAutoRaise(False)
            self.infoButton_40.setObjectName("infoButton_40")
            self.horizontalLayout_23.addWidget(self.infoButton_40)
            spacerItem49 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.horizontalLayout_23.addItem(spacerItem49)
            self.gridLayout_106.addLayout(self.horizontalLayout_23, 0, 1, 1, 1)
            self.qv_obsCldMask = QtWidgets.QLabel()
            self.qv_obsCldMask.setMinimumSize(QtCore.QSize(450, 27))
            self.qv_obsCldMask.setMaximumSize(QtCore.QSize(16777215, 27))
            font = QtGui.QFont()
            font.setFamily("fonts/SourceSansPro-Regular.ttf")
            font.setPointSize(10)
            font.setKerning(True)
            font.setStyleStrategy(QtGui.QFont.PreferAntialias)
            self.qv_obsCldMask.setFont(font)
            self.qv_obsCldMask.setObjectName("qv_obsCldMask")
            self.gridLayout_106.addWidget(self.qv_obsCldMask, 1, 0, 1, 1)
            self.horizontalLayout_24 = QtWidgets.QHBoxLayout()
            self.horizontalLayout_24.setObjectName("horizontalLayout_24")
            self.qv_obsCldMask_rd1 = QtWidgets.QRadioButton()
            self.qv_obsCldMask_rd1.setMinimumSize(QtCore.QSize(51, 27))
            self.qv_obsCldMask_rd1.setMaximumSize(QtCore.QSize(16777215, 27))
            font = QtGui.QFont()
            font.setFamily("fonts/SourceSansPro-Regular.ttf")
            font.setPointSize(10)
            font.setKerning(True)
            font.setStyleStrategy(QtGui.QFont.PreferAntialias)
            self.qv_obsCldMask_rd1.setFont(font)
            self.qv_obsCldMask_rd1.setObjectName("qv_obsCldMask_rd1")
            self.buttonGroup_12 = QtWidgets.QButtonGroup()
            self.buttonGroup_12.setObjectName("buttonGroup_12")
            self.buttonGroup_12.addButton(self.qv_obsCldMask_rd1)
            self.horizontalLayout_24.addWidget(self.qv_obsCldMask_rd1)
            spacerItem50 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
            self.horizontalLayout_24.addItem(spacerItem50)
            self.qv_obsCldMask_rd2 = QtWidgets.QRadioButton()
            self.qv_obsCldMask_rd2.setMinimumSize(QtCore.QSize(51, 27))
            self.qv_obsCldMask_rd2.setMaximumSize(QtCore.QSize(16777215, 27))
            font = QtGui.QFont()
            font.setFamily("fonts/SourceSansPro-Regular.ttf")
            font.setPointSize(10)
            font.setKerning(True)
            font.setStyleStrategy(QtGui.QFont.PreferAntialias)
            self.qv_obsCldMask_rd2.setFont(font)
            self.qv_obsCldMask_rd2.setObjectName("qv_obsCldMask_rd2")
            self.buttonGroup_12.addButton(self.qv_obsCldMask_rd2)
            self.horizontalLayout_24.addWidget(self.qv_obsCldMask_rd2)
            spacerItem51 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.horizontalLayout_24.addItem(spacerItem51)
            self.gridLayout_106.addLayout(self.horizontalLayout_24, 1, 1, 1, 1)
            self.qv_obsShdMask = QtWidgets.QLabel()
            self.qv_obsShdMask.setMinimumSize(QtCore.QSize(450, 27))
            self.qv_obsShdMask.setMaximumSize(QtCore.QSize(16777215, 27))
            font = QtGui.QFont()
            font.setFamily("fonts/SourceSansPro-Regular.ttf")
            font.setPointSize(10)
            font.setKerning(True)
            font.setStyleStrategy(QtGui.QFont.PreferAntialias)
            self.qv_obsShdMask.setFont(font)
            self.qv_obsShdMask.setObjectName("qv_obsShdMask")
            self.gridLayout_106.addWidget(self.qv_obsShdMask, 2, 0, 1, 1)
            self.horizontalLayout_25 = QtWidgets.QHBoxLayout()
            self.horizontalLayout_25.setObjectName("horizontalLayout_25")
            self.qv_obsShdMask_rd1 = QtWidgets.QRadioButton()
            self.qv_obsShdMask_rd1.setMinimumSize(QtCore.QSize(51, 27))
            self.qv_obsShdMask_rd1.setMaximumSize(QtCore.QSize(16777215, 27))
            font = QtGui.QFont()
            font.setFamily("fonts/SourceSansPro-Regular.ttf")
            font.setPointSize(10)
            font.setKerning(True)
            font.setStyleStrategy(QtGui.QFont.PreferAntialias)
            self.qv_obsShdMask_rd1.setFont(font)
            self.qv_obsShdMask_rd1.setObjectName("qv_obsShdMask_rd1")
            self.buttonGroup_13 = QtWidgets.QButtonGroup()
            self.buttonGroup_13.setObjectName("buttonGroup_13")
            self.buttonGroup_13.addButton(self.qv_obsShdMask_rd1)
            self.horizontalLayout_25.addWidget(self.qv_obsShdMask_rd1)
            spacerItem52 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
            self.horizontalLayout_25.addItem(spacerItem52)
            self.qv_obsShdMask_rd2 = QtWidgets.QRadioButton()
            self.qv_obsShdMask_rd2.setMinimumSize(QtCore.QSize(51, 27))
            self.qv_obsShdMask_rd2.setMaximumSize(QtCore.QSize(16777215, 27))
            font = QtGui.QFont()
            font.setFamily("fonts/SourceSansPro-Regular.ttf")
            font.setPointSize(10)
            font.setKerning(True)
            font.setStyleStrategy(QtGui.QFont.PreferAntialias)
            self.qv_obsShdMask_rd2.setFont(font)
            self.qv_obsShdMask_rd2.setObjectName("qv_obsShdMask_rd2")
            self.buttonGroup_13.addButton(self.qv_obsShdMask_rd2)
            self.horizontalLayout_25.addWidget(self.qv_obsShdMask_rd2)
            spacerItem53 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.horizontalLayout_25.addItem(spacerItem53)
            self.gridLayout_106.addLayout(self.horizontalLayout_25, 2, 1, 1, 1)
            self.qv_obsHazMask = QtWidgets.QLabel()
            self.qv_obsHazMask.setMinimumSize(QtCore.QSize(450, 27))
            self.qv_obsHazMask.setMaximumSize(QtCore.QSize(16777215, 27))
            font = QtGui.QFont()
            font.setFamily("fonts/SourceSansPro-Regular.ttf")
            font.setPointSize(10)
            font.setKerning(True)
            font.setStyleStrategy(QtGui.QFont.PreferAntialias)
            self.qv_obsHazMask.setFont(font)
            self.qv_obsHazMask.setObjectName("qv_obsHazMask")
            self.gridLayout_106.addWidget(self.qv_obsHazMask, 3, 0, 1, 1)
            self.horizontalLayout_26 = QtWidgets.QHBoxLayout()
            self.horizontalLayout_26.setObjectName("horizontalLayout_26")
            self.qv_obsHazMask_rd1 = QtWidgets.QRadioButton()
            self.qv_obsHazMask_rd1.setMinimumSize(QtCore.QSize(51, 27))
            self.qv_obsHazMask_rd1.setMaximumSize(QtCore.QSize(16777215, 27))
            font = QtGui.QFont()
            font.setFamily("fonts/SourceSansPro-Regular.ttf")
            font.setPointSize(10)
            font.setKerning(True)
            font.setStyleStrategy(QtGui.QFont.PreferAntialias)
            self.qv_obsHazMask_rd1.setFont(font)
            self.qv_obsHazMask_rd1.setObjectName("qv_obsHazMask_rd1")
            self.buttonGroup_14 = QtWidgets.QButtonGroup()
            self.buttonGroup_14.setObjectName("buttonGroup_14")
            self.buttonGroup_14.addButton(self.qv_obsHazMask_rd1)
            self.horizontalLayout_26.addWidget(self.qv_obsHazMask_rd1)
            spacerItem54 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
            self.horizontalLayout_26.addItem(spacerItem54)
            self.qv_obsHazMask_rd2 = QtWidgets.QRadioButton()
            self.qv_obsHazMask_rd2.setMinimumSize(QtCore.QSize(51, 27))
            self.qv_obsHazMask_rd2.setMaximumSize(QtCore.QSize(16777215, 27))
            font = QtGui.QFont()
            font.setFamily("fonts/SourceSansPro-Regular.ttf")
            font.setPointSize(10)
            font.setKerning(True)
            font.setStyleStrategy(QtGui.QFont.PreferAntialias)
            self.qv_obsHazMask_rd2.setFont(font)
            self.qv_obsHazMask_rd2.setObjectName("qv_obsHazMask_rd2")
            self.buttonGroup_14.addButton(self.qv_obsHazMask_rd2)
            self.horizontalLayout_26.addWidget(self.qv_obsHazMask_rd2)
            spacerItem55 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.horizontalLayout_26.addItem(spacerItem55)
            self.gridLayout_106.addLayout(self.horizontalLayout_26, 3, 1, 1, 1)
            self.qv_obsDEMMea = QtWidgets.QLabel()
            self.qv_obsDEMMea.setMinimumSize(QtCore.QSize(450, 27))
            self.qv_obsDEMMea.setMaximumSize(QtCore.QSize(16777215, 27))
            font = QtGui.QFont()
            font.setFamily("fonts/SourceSansPro-Regular.ttf")
            font.setPointSize(10)
            font.setKerning(True)
            font.setStyleStrategy(QtGui.QFont.PreferAntialias)
            self.qv_obsDEMMea.setFont(font)
            self.qv_obsDEMMea.setObjectName("qv_obsDEMMea")
            self.gridLayout_106.addWidget(self.qv_obsDEMMea, 4, 0, 1, 1)
            self.horizontalLayout_27 = QtWidgets.QHBoxLayout()
            self.horizontalLayout_27.setObjectName("horizontalLayout_27")
            self.qv_obsDEMMea_rd1 = QtWidgets.QRadioButton()
            self.qv_obsDEMMea_rd1.setMinimumSize(QtCore.QSize(51, 27))
            self.qv_obsDEMMea_rd1.setMaximumSize(QtCore.QSize(16777215, 27))
            font = QtGui.QFont()
            font.setFamily("fonts/SourceSansPro-Regular.ttf")
            font.setPointSize(10)
            font.setKerning(True)
            font.setStyleStrategy(QtGui.QFont.PreferAntialias)
            self.qv_obsDEMMea_rd1.setFont(font)
            self.qv_obsDEMMea_rd1.setObjectName("qv_obsDEMMea_rd1")
            self.buttonGroup_15 = QtWidgets.QButtonGroup()
            self.buttonGroup_15.setObjectName("buttonGroup_15")
            self.buttonGroup_15.addButton(self.qv_obsDEMMea_rd1)
            self.horizontalLayout_27.addWidget(self.qv_obsDEMMea_rd1)
            spacerItem56 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
            self.horizontalLayout_27.addItem(spacerItem56)
            self.qv_obsDEMMea_rd2 = QtWidgets.QRadioButton()
            self.qv_obsDEMMea_rd2.setMinimumSize(QtCore.QSize(51, 27))
            self.qv_obsDEMMea_rd2.setMaximumSize(QtCore.QSize(16777215, 27))
            font = QtGui.QFont()
            font.setFamily("fonts/SourceSansPro-Regular.ttf")
            font.setPointSize(10)
            font.setKerning(True)
            font.setStyleStrategy(QtGui.QFont.PreferAntialias)
            self.qv_obsDEMMea_rd2.setFont(font)
            self.qv_obsDEMMea_rd2.setObjectName("qv_obsDEMMea_rd2")
            self.buttonGroup_15.addButton(self.qv_obsDEMMea_rd2)
            self.horizontalLayout_27.addWidget(self.qv_obsDEMMea_rd2)
            self.infoButton_41 = QtWidgets.QToolButton()
            self.infoButton_41.setMaximumSize(QtCore.QSize(27, 27))
            self.infoButton_41.setStyleSheet("QToolButton {\n"
    "    border: 1px solid transparent;\n"
    "    background-color: transparent;\n"
    "    width: 27px;\n"
    "    height: 27px;\n"
    "}\n"
    "\n"
    "QToolButton:hover {\n"
    "    border: 1px solid gray;\n"
    "    border-radius: 3px;\n"
    "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
    "}\n"
    "\n"
    "QToolButton:pressed {\n"
    "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
    "}\n"
    "\n"
    "QToolButton:flat {\n"
    "    border: none;\n"
    "}")
            self.infoButton_41.setText("")
            self.infoButton_41.setIcon(icon1)
            self.infoButton_41.setIconSize(QtCore.QSize(27, 27))
            self.infoButton_41.setAutoRaise(False)
            self.infoButton_41.setObjectName("infoButton_41")
            self.horizontalLayout_27.addWidget(self.infoButton_41)
            spacerItem57 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.horizontalLayout_27.addItem(spacerItem57)
            self.gridLayout_106.addLayout(self.horizontalLayout_27, 4, 1, 1, 1)
            self.qv_obsIllAng = QtWidgets.QLabel()
            self.qv_obsIllAng.setMinimumSize(QtCore.QSize(450, 27))
            self.qv_obsIllAng.setMaximumSize(QtCore.QSize(16777215, 27))
            font = QtGui.QFont()
            font.setFamily("fonts/SourceSansPro-Regular.ttf")
            font.setPointSize(10)
            font.setKerning(True)
            font.setStyleStrategy(QtGui.QFont.PreferAntialias)
            self.qv_obsIllAng.setFont(font)
            self.qv_obsIllAng.setObjectName("qv_obsIllAng")
            self.gridLayout_106.addWidget(self.qv_obsIllAng, 5, 0, 1, 1)
            self.horizontalLayout_28 = QtWidgets.QHBoxLayout()
            self.horizontalLayout_28.setObjectName("horizontalLayout_28")
            self.qv_obsIllAng_rd1 = QtWidgets.QRadioButton()
            self.qv_obsIllAng_rd1.setMinimumSize(QtCore.QSize(51, 27))
            self.qv_obsIllAng_rd1.setMaximumSize(QtCore.QSize(16777215, 27))
            font = QtGui.QFont()
            font.setFamily("fonts/SourceSansPro-Regular.ttf")
            font.setPointSize(10)
            font.setKerning(True)
            font.setStyleStrategy(QtGui.QFont.PreferAntialias)
            self.qv_obsIllAng_rd1.setFont(font)
            self.qv_obsIllAng_rd1.setObjectName("qv_obsIllAng_rd1")
            self.buttonGroup_16 = QtWidgets.QButtonGroup()
            self.buttonGroup_16.setObjectName("buttonGroup_16")
            self.buttonGroup_16.addButton(self.qv_obsIllAng_rd1)
            self.horizontalLayout_28.addWidget(self.qv_obsIllAng_rd1)
            spacerItem58 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
            self.horizontalLayout_28.addItem(spacerItem58)
            self.qv_obsIllAng_rd2 = QtWidgets.QRadioButton()
            self.qv_obsIllAng_rd2.setMinimumSize(QtCore.QSize(51, 27))
            self.qv_obsIllAng_rd2.setMaximumSize(QtCore.QSize(16777215, 27))
            font = QtGui.QFont()
            font.setFamily("fonts/SourceSansPro-Regular.ttf")
            font.setPointSize(10)
            font.setKerning(True)
            font.setStyleStrategy(QtGui.QFont.PreferAntialias)
            self.qv_obsIllAng_rd2.setFont(font)
            self.qv_obsIllAng_rd2.setObjectName("qv_obsIllAng_rd2")
            self.buttonGroup_16.addButton(self.qv_obsIllAng_rd2)
            self.horizontalLayout_28.addWidget(self.qv_obsIllAng_rd2)
            self.infoButton_42 = QtWidgets.QToolButton()
            self.infoButton_42.setMaximumSize(QtCore.QSize(27, 27))
            self.infoButton_42.setStyleSheet("QToolButton {\n"
    "    border: 1px solid transparent;\n"
    "    background-color: transparent;\n"
    "    width: 27px;\n"
    "    height: 27px;\n"
    "}\n"
    "\n"
    "QToolButton:hover {\n"
    "    border: 1px solid gray;\n"
    "    border-radius: 3px;\n"
    "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
    "}\n"
    "\n"
    "QToolButton:pressed {\n"
    "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
    "}\n"
    "\n"
    "QToolButton:flat {\n"
    "    border: none;\n"
    "}")
            self.infoButton_42.setText("")
            self.infoButton_42.setIcon(icon1)
            self.infoButton_42.setIconSize(QtCore.QSize(27, 27))
            self.infoButton_42.setAutoRaise(False)
            self.infoButton_42.setObjectName("infoButton_42")
            self.horizontalLayout_28.addWidget(self.infoButton_42)
            spacerItem59 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.horizontalLayout_28.addItem(spacerItem59)
            self.gridLayout_106.addLayout(self.horizontalLayout_28, 5, 1, 1, 1)
            self.qv_obsBRDFGeo = QtWidgets.QLabel()
            self.qv_obsBRDFGeo.setMinimumSize(QtCore.QSize(450, 27))
            self.qv_obsBRDFGeo.setMaximumSize(QtCore.QSize(16777215, 27))
            font = QtGui.QFont()
            font.setFamily("fonts/SourceSansPro-Regular.ttf")
            font.setPointSize(10)
            font.setKerning(True)
            font.setStyleStrategy(QtGui.QFont.PreferAntialias)
            self.qv_obsBRDFGeo.setFont(font)
            self.qv_obsBRDFGeo.setObjectName("qv_obsBRDFGeo")
            self.gridLayout_106.addWidget(self.qv_obsBRDFGeo, 6, 0, 1, 1)
            self.horizontalLayout_29 = QtWidgets.QHBoxLayout()
            self.horizontalLayout_29.setObjectName("horizontalLayout_29")
            self.qv_obsBRDFGeo_rd1 = QtWidgets.QRadioButton()
            self.qv_obsBRDFGeo_rd1.setMinimumSize(QtCore.QSize(51, 27))
            self.qv_obsBRDFGeo_rd1.setMaximumSize(QtCore.QSize(16777215, 27))
            font = QtGui.QFont()
            font.setFamily("fonts/SourceSansPro-Regular.ttf")
            font.setPointSize(10)
            font.setKerning(True)
            font.setStyleStrategy(QtGui.QFont.PreferAntialias)
            self.qv_obsBRDFGeo_rd1.setFont(font)
            self.qv_obsBRDFGeo_rd1.setObjectName("qv_obsBRDFGeo_rd1")
            self.buttonGroup_17 = QtWidgets.QButtonGroup()
            self.buttonGroup_17.setObjectName("buttonGroup_17")
            self.buttonGroup_17.addButton(self.qv_obsBRDFGeo_rd1)
            self.horizontalLayout_29.addWidget(self.qv_obsBRDFGeo_rd1)
            spacerItem60 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
            self.horizontalLayout_29.addItem(spacerItem60)
            self.qv_obsBRDFGeo_rd2 = QtWidgets.QRadioButton()
            self.qv_obsBRDFGeo_rd2.setMinimumSize(QtCore.QSize(51, 27))
            self.qv_obsBRDFGeo_rd2.setMaximumSize(QtCore.QSize(16777215, 27))
            font = QtGui.QFont()
            font.setFamily("fonts/SourceSansPro-Regular.ttf")
            font.setPointSize(10)
            font.setKerning(True)
            font.setStyleStrategy(QtGui.QFont.PreferAntialias)
            self.qv_obsBRDFGeo_rd2.setFont(font)
            self.qv_obsBRDFGeo_rd2.setObjectName("qv_obsBRDFGeo_rd2")
            self.buttonGroup_17.addButton(self.qv_obsBRDFGeo_rd2)
            self.horizontalLayout_29.addWidget(self.qv_obsBRDFGeo_rd2)
            self.infoButton_43 = QtWidgets.QToolButton()
            self.infoButton_43.setMaximumSize(QtCore.QSize(27, 27))
            self.infoButton_43.setStyleSheet("QToolButton {\n"
    "    border: 1px solid transparent;\n"
    "    background-color: transparent;\n"
    "    width: 27px;\n"
    "    height: 27px;\n"
    "}\n"
    "\n"
    "QToolButton:hover {\n"
    "    border: 1px solid gray;\n"
    "    border-radius: 3px;\n"
    "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
    "}\n"
    "\n"
    "QToolButton:pressed {\n"
    "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
    "}\n"
    "\n"
    "QToolButton:flat {\n"
    "    border: none;\n"
    "}")
            self.infoButton_43.setText("")
            self.infoButton_43.setIcon(icon1)
            self.infoButton_43.setIconSize(QtCore.QSize(27, 27))
            self.infoButton_43.setAutoRaise(False)
            self.infoButton_43.setObjectName("infoButton_43")
            self.horizontalLayout_29.addWidget(self.infoButton_43)
            spacerItem61 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.horizontalLayout_29.addItem(spacerItem61)
            self.gridLayout_106.addLayout(self.horizontalLayout_29, 6, 1, 1, 1)
            self.horizontalLayout_98.addLayout(self.gridLayout_106)
            spacerItem62 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.horizontalLayout_98.addItem(spacerItem62)
            self.verticalLayout_100.addLayout(self.horizontalLayout_98)
            self.horizontalLayout_99.addLayout(self.verticalLayout_100)
            self.verticalLayout_25.addLayout(self.horizontalLayout_99)
                
            self.qv_obsCalInfo.setText("Calibration information")
            self.qv_obsCalLabo_lb.setText("Name of calibration laboratory:")
            self.qv_obsRadCal.setText("Date of radimetric calibration:")
            self.qv_obsRadCal_dt.setDisplayFormat("yyyy-MM-dd")
            self.qv_obsSpeCal.setText("Date of spectral calibration:")
            self.qv_obsSpeCal_dt.setDisplayFormat("yyyy-MM-dd")
            self.qv_obsAcqInfo.setText("Acquisition information")
            self.qv_obsSpeBand_lb.setText("Number of spectral bands (spectral mode):")
            self.qv_obsFltHdg_lb.setText("Overall heading / flight direction (dd):")
            self.qv_obsFltAlt_lb.setText("Overall altitude / average height ASL (m):")
            self.qv_obsSolZen_lb.setText("Solar zenith (dd):")
            self.qv_obsSolAzi_lb.setText("Solar azimuth (dd):")
            self.qv_obsAnoAcq_lb.setText("Report anomalies in data acquisition:")
            self.qv_obsProInfo.setText("Processing information")
            self.qv_obsProLvl.setText("Processing level:")
            self.qv_obsProLvl_rl.setItemText(0, "Make a choice...")
            self.qv_obsProLvl_rl.setItemText(1, "Level 1")
            self.qv_obsProLvl_rl.setItemText(2, "Level 2 geo")
            self.qv_obsProLvl_rl.setItemText(3, "Level 2 atm")
            self.qv_obsProLvl_rl.setItemText(4, "Level 2")
            self.qv_obsDrkCur.setText("Dark current (DC) correction ?")
            self.qv_obsDrkCur_rd1.setText("Yes")
            self.qv_obsDrkCur_rd2.setText("No")
            self.qv_obsQuaLay.setText("Data Quality Layers")
            self.qv_obsCalCorr.setText("Sensor calibration and system correction:")
            self.qv_obsIntMask.setText("Aggregated interpolated pixel mask (\'corrected pixels\') ?")
            self.qv_obsIntMask_rd1.setText("Yes")
            self.qv_obsIntMask_rd2.setText("No")
            self.qv_obsBadMask.setText("Aggregated bad pixel mask (\'not corrected pixels\') ?")
            self.qv_obsBadMask_rd1.setText("Yes")
            self.qv_obsBadMask_rd2.setText("No")
            self.qv_obsProError.setText("Image data artefacts and processing errors:")
            self.qv_obsSatPix.setText("Saturated pixels / overflow ?")
            self.qv_obsSatPix_rd1.setText("Yes")
            self.qv_obsSatPix_rd2.setText("No")
            self.qv_obsSpeNeigh.setText("Pixels affected by saturation in spatial/spectral neighbourhood ?")
            self.qv_obsSpeNeigh_rd1.setText("Yes")
            self.qv_obsSpeNeigh_rd2.setText("No")
            self.qv_obsGeoCorr.setText("GPS/IMU related errors, geometric correction:")
            self.qv_obsPosInfo.setText("Problems with position information / Interpolated position information ?")
            self.qv_obsPosInfo_rd1.setText("Yes")
            self.qv_obsPosInfo_rd2.setText("No")
            self.qv_obsAttInfo.setText("Problems with attitude information / Interpolated attitude information ?")
            self.qv_obsAttInf_rd1.setText("Yes")
            self.qv_obsAttInf_rd2.setText("No")
            self.qv_obsSynprob.setText("Synchronization problems ?")
            self.qv_obsSynprob_rd1.setText("Yes")
            self.qv_obsSynprob_rd2.setText("No")
            self.qv_obsIntGeo.setText("Interpolated pixels during geocoding ?")
            self.qv_obsIntGeo_rd1.setText("Yes")
            self.qv_obsIntGeo_rd2.setText("No")
            self.qv_obsAtmCond.setText("Atmospheric correction and atmospheric conditions:")
            self.qv_obsAtmCorr.setText("Failure of atmospheric correction ?")
            self.qv_obsAtmCorr_rd1.setText("Yes")
            self.qv_obsAtmCorr_rd2.setText("No")
            self.qv_obsCldMask.setText("Cloud mask ?")
            self.qv_obsCldMask_rd1.setText("Yes")
            self.qv_obsCldMask_rd2.setText("No")
            self.qv_obsShdMask.setText("Cloud shadow mask ?")
            self.qv_obsShdMask_rd1.setText("Yes")
            self.qv_obsShdMask_rd2.setText("No")
            self.qv_obsHazMask.setText("Haze mask ?")
            self.qv_obsHazMask_rd1.setText("Yes")
            self.qv_obsHazMask_rd2.setText("No")
            self.qv_obsDEMMea.setText("Critical terrain correction based on DEM roughness measure ?")
            self.qv_obsDEMMea_rd1.setText("Yes")
            self.qv_obsDEMMea_rd2.setText("No")
            self.qv_obsIllAng.setText("Critical terrain correction based on slope/local illumination angle ?")
            self.qv_obsIllAng_rd1.setText("Yes")
            self.qv_obsIllAng_rd2.setText("No")
            self.qv_obsBRDFGeo.setText("Critical BRFD geometry based on sun-sensor-terrain geometry ?")
            self.qv_obsBRDFGeo_rd1.setText("Yes")
            self.qv_obsBRDFGeo_rd2.setText("No")
            self.qv_obsRadCal_dt.setDate(QDate.currentDate())
            self.qv_obsSpeCal_dt.setDate(QDate.currentDate())
            all_info_boxes = self.tabWidgetPage7.findChildren(QtWidgets.QToolButton)
            for widget in all_info_boxes:
                widget.clicked.connect(lambda: self.button_clicked())
            all_radiobuttons = self.tabWidgetPage7.findChildren(QtWidgets.QRadioButton)
            for widget in all_radiobuttons:
                if widget.objectName() != "qv_obsRadio" and widget.objectName() != "qv_insituRadio":
                    widget.clicked.connect(lambda: self.set_modified())
            all_date_edits = self.tabWidgetPage7.findChildren(QtWidgets.QDateEdit)
            for widget in all_date_edits:
                widget.dateChanged.connect(lambda: self.set_modified())
            all_line_edits = self.tabWidgetPage7.findChildren(QtWidgets.QLineEdit)
            for widget in all_line_edits:
                widget.textChanged.connect(lambda: self.set_modified())
            all_rolbox_edits = self.tabWidgetPage7.findChildren(QtWidgets.QComboBox)
            for widget in all_rolbox_edits:
                widget.activated.connect(lambda: self.set_modified())
    elif self.qv_insituRadio.isChecked() == True:
        clearLayout(self.verticalLayout_25)
        if self.verticalLayout_25.count() != 17:
            font2 = QtGui.QFont()
            font2.setFamily("font/SourceSansPro-Regular.ttf")
            font2.setPointSize(10)
            font2.setBold(True)
            font2.setUnderline(True)
            font2.setWeight(75)
            font2.setStyleStrategy(QtGui.QFont.PreferAntialias)
            font = QtGui.QFont()
            font.setFamily("font/SourceSansPro-Regular.ttf")
            font.setPointSize(10)
            font.setBold(False)
            font.setWeight(50)
            font.setStyleStrategy(QtGui.QFont.PreferAntialias)
            icon1 = QtGui.QIcon()
            icon1.addPixmap(QtGui.QPixmap("icons/info_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            spacerItem99 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
            self.verticalLayout_25.addItem(spacerItem99)
            self.horizontalLayout_84 = QtWidgets.QHBoxLayout()
            self.horizontalLayout_84.setObjectName("horizontalLayout_84")
            self.qv_insituCalInfo = QtWidgets.QLabel()
            self.qv_insituCalInfo.setMinimumSize(QtCore.QSize(540, 27))
            self.qv_insituCalInfo.setMaximumSize(QtCore.QSize(16777215, 27))
            font = QtGui.QFont()
            font.setFamily("fonts/SourceSansPro-Regular.ttf")
            font.setPointSize(10)
            font.setBold(True)
            font.setUnderline(True)
            font.setWeight(75)
            font.setKerning(True)
            font.setStyleStrategy(QtGui.QFont.PreferAntialias)
            self.qv_insituCalInfo.setFont(font)
            self.qv_insituCalInfo.setObjectName("qv_insituCalInfo")
            self.horizontalLayout_84.addWidget(self.qv_insituCalInfo)
            self.infoButton_27 = QtWidgets.QToolButton()
            self.infoButton_27.setMaximumSize(QtCore.QSize(27, 27))
            self.infoButton_27.setStyleSheet("QToolButton {\n"
            "    border: 1px solid transparent;\n"
            "    background-color: transparent;\n"
            "    width: 27px;\n"
            "    height: 27px;\n"
            "}\n"
            "\n"
            "QToolButton:hover {\n"
            "    border: 1px solid gray;\n"
            "    border-radius: 3px;\n"
            "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
            "}\n"
            "\n"
            "QToolButton:pressed {\n"
            "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
            "}\n"
            "\n"
            "QToolButton:flat {\n"
            "    border: none;\n"
            "}")
            self.infoButton_27.setText("")
            icon1 = QtGui.QIcon()
            icon1.addPixmap(QtGui.QPixmap("icons/info_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.infoButton_27.setIcon(icon1)
            self.infoButton_27.setIconSize(QtCore.QSize(27, 27))
            self.infoButton_27.setAutoRaise(False)
            self.infoButton_27.setObjectName("infoButton_27")
            self.horizontalLayout_84.addWidget(self.infoButton_27)
            spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.horizontalLayout_84.addItem(spacerItem)
            self.verticalLayout_25.addLayout(self.horizontalLayout_84)
            self.horizontalLayout_85 = QtWidgets.QHBoxLayout()
            self.horizontalLayout_85.setObjectName("horizontalLayout_85")
            spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
            self.horizontalLayout_85.addItem(spacerItem1)
            self.qv_insituCalDesc_lb = QtWidgets.QLabel()
            self.qv_insituCalDesc_lb.setMinimumSize(QtCore.QSize(0, 27))
            self.qv_insituCalDesc_lb.setMaximumSize(QtCore.QSize(16777215, 27))
            font = QtGui.QFont()
            font.setFamily("fonts/SourceSansPro-Regular.ttf")
            font.setPointSize(10)
            font.setKerning(True)
            font.setStyleStrategy(QtGui.QFont.PreferAntialias)
            self.qv_insituCalDesc_lb.setFont(font)
            self.qv_insituCalDesc_lb.setObjectName("qv_insituCalDesc_lb")
            self.horizontalLayout_85.addWidget(self.qv_insituCalDesc_lb)
            spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.horizontalLayout_85.addItem(spacerItem2)
            self.verticalLayout_25.addLayout(self.horizontalLayout_85)
            self.horizontalLayout_86 = QtWidgets.QHBoxLayout()
            self.horizontalLayout_86.setObjectName("horizontalLayout_86")
            spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
            self.horizontalLayout_86.addItem(spacerItem3)
            self.qv_insituCalDesc_ln = QtWidgets.QPlainTextEdit()
            self.qv_insituCalDesc_ln.setMinimumSize(QtCore.QSize(600, 100))
            self.qv_insituCalDesc_ln.setMaximumSize(QtCore.QSize(16777215, 100))
            font = QtGui.QFont()
            font.setFamily("fonts/SourceSansPro-Regular.ttf")
            font.setPointSize(9)
            font.setKerning(True)
            font.setStyleStrategy(QtGui.QFont.PreferAntialias)
            self.qv_insituCalDesc_ln.setFont(font)
            self.qv_insituCalDesc_ln.setStyleSheet("QPlainTextEdit {\n"
            "    border-radius: 3px;\n"
            "    padding: 1px 4px 1px 4px;\n"
            "    background-color:  rgb(240, 240, 240);\n"
            "}")
            self.qv_insituCalDesc_ln.setObjectName("qv_insituCalDesc_ln")
            self.horizontalLayout_86.addWidget(self.qv_insituCalDesc_ln)
            spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.horizontalLayout_86.addItem(spacerItem4)
            self.verticalLayout_25.addLayout(self.horizontalLayout_86)
            spacerItem5 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
            self.verticalLayout_25.addItem(spacerItem5)
            self.horizontalLayout_87 = QtWidgets.QHBoxLayout()
            self.horizontalLayout_87.setObjectName("horizontalLayout_87")
            spacerItem6 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
            self.horizontalLayout_87.addItem(spacerItem6)
            self.qv_insituCalCons_lb = QtWidgets.QLabel()
            self.qv_insituCalCons_lb.setMinimumSize(QtCore.QSize(0, 27))
            self.qv_insituCalCons_lb.setMaximumSize(QtCore.QSize(16777215, 27))
            font = QtGui.QFont()
            font.setFamily("fonts/SourceSansPro-Regular.ttf")
            font.setPointSize(10)
            font.setKerning(True)
            font.setStyleStrategy(QtGui.QFont.PreferAntialias)
            self.qv_insituCalCons_lb.setFont(font)
            self.qv_insituCalCons_lb.setObjectName("qv_insituCalCons_lb")
            self.horizontalLayout_87.addWidget(self.qv_insituCalCons_lb)
            spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.horizontalLayout_87.addItem(spacerItem7)
            self.verticalLayout_25.addLayout(self.horizontalLayout_87)
            self.horizontalLayout_88 = QtWidgets.QHBoxLayout()
            self.horizontalLayout_88.setObjectName("horizontalLayout_88")
            spacerItem8 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
            self.horizontalLayout_88.addItem(spacerItem8)
            self.qv_insituCalCons_ln = QtWidgets.QPlainTextEdit()
            self.qv_insituCalCons_ln.setMinimumSize(QtCore.QSize(600, 100))
            self.qv_insituCalCons_ln.setMaximumSize(QtCore.QSize(16777215, 100))
            font = QtGui.QFont()
            font.setFamily("fonts/SourceSansPro-Regular.ttf")
            font.setPointSize(9)
            font.setKerning(True)
            font.setStyleStrategy(QtGui.QFont.PreferAntialias)
            self.qv_insituCalCons_ln.setFont(font)
            self.qv_insituCalCons_ln.setStyleSheet("QPlainTextEdit {\n"
            "    border-radius: 3px;\n"
            "    padding: 1px 4px 1px 4px;\n"
            "    background-color:  rgb(240, 240, 240);\n"
            "}")
            self.qv_insituCalCons_ln.setObjectName("qv_insituCalCons_ln")
            self.horizontalLayout_88.addWidget(self.qv_insituCalCons_ln)
            spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.horizontalLayout_88.addItem(spacerItem9)
            self.verticalLayout_25.addLayout(self.horizontalLayout_88)
            spacerItem10 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
            self.verticalLayout_25.addItem(spacerItem10)
            self.horizontalLayout_89 = QtWidgets.QHBoxLayout()
            self.horizontalLayout_89.setObjectName("horizontalLayout_89")
            spacerItem11 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
            self.horizontalLayout_89.addItem(spacerItem11)
            self.qv_insituCalMat_lb = QtWidgets.QLabel()
            self.qv_insituCalMat_lb.setMinimumSize(QtCore.QSize(0, 27))
            self.qv_insituCalMat_lb.setMaximumSize(QtCore.QSize(16777215, 27))
            font = QtGui.QFont()
            font.setFamily("fonts/SourceSansPro-Regular.ttf")
            font.setPointSize(10)
            font.setKerning(True)
            font.setStyleStrategy(QtGui.QFont.PreferAntialias)
            self.qv_insituCalMat_lb.setFont(font)
            self.qv_insituCalMat_lb.setObjectName("qv_insituCalMat_lb")
            self.horizontalLayout_89.addWidget(self.qv_insituCalMat_lb)
            spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.horizontalLayout_89.addItem(spacerItem12)
            self.verticalLayout_25.addLayout(self.horizontalLayout_89)
            self.horizontalLayout_90 = QtWidgets.QHBoxLayout()
            self.horizontalLayout_90.setObjectName("horizontalLayout_90")
            spacerItem13 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
            self.horizontalLayout_90.addItem(spacerItem13)
            self.qv_insituCalMat_ln = QtWidgets.QPlainTextEdit()
            self.qv_insituCalMat_ln.setMinimumSize(QtCore.QSize(600, 100))
            self.qv_insituCalMat_ln.setMaximumSize(QtCore.QSize(16777215, 100))
            font = QtGui.QFont()
            font.setFamily("fonts/SourceSansPro-Regular.ttf")
            font.setPointSize(9)
            font.setKerning(True)
            font.setStyleStrategy(QtGui.QFont.PreferAntialias)
            self.qv_insituCalMat_ln.setFont(font)
            self.qv_insituCalMat_ln.setStyleSheet("QPlainTextEdit {\n"
            "    border-radius: 3px;\n"
            "    padding: 1px 4px 1px 4px;\n"
            "    background-color:  rgb(240, 240, 240);\n"
            "}")
            self.qv_insituCalMat_ln.setObjectName("qv_insituCalMat_ln")
            self.horizontalLayout_90.addWidget(self.qv_insituCalMat_ln)
            spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.horizontalLayout_90.addItem(spacerItem14)
            self.verticalLayout_25.addLayout(self.horizontalLayout_90)
            spacerItem15 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
            self.verticalLayout_25.addItem(spacerItem15)
            self.horizontalLayout_91 = QtWidgets.QHBoxLayout()
            self.horizontalLayout_91.setObjectName("horizontalLayout_91")
            self.qv_insituGeoUnit = QtWidgets.QLabel()
            self.qv_insituGeoUnit.setMinimumSize(QtCore.QSize(260, 27))
            self.qv_insituGeoUnit.setMaximumSize(QtCore.QSize(16777215, 27))
            font = QtGui.QFont()
            font.setFamily("fonts/SourceSansPro-Regular.ttf")
            font.setPointSize(10)
            font.setBold(True)
            font.setUnderline(True)
            font.setWeight(75)
            font.setKerning(True)
            font.setStyleStrategy(QtGui.QFont.PreferAntialias)
            self.qv_insituGeoUnit.setFont(font)
            self.qv_insituGeoUnit.setObjectName("qv_insituGeoUnit")
            self.horizontalLayout_91.addWidget(self.qv_insituGeoUnit)
            spacerItem16 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
            self.horizontalLayout_91.addItem(spacerItem16)
            self.qv_insituGeoUnit_rd1 = QtWidgets.QRadioButton()
            self.qv_insituGeoUnit_rd1.setMinimumSize(QtCore.QSize(51, 27))
            self.qv_insituGeoUnit_rd1.setMaximumSize(QtCore.QSize(16777215, 27))
            font = QtGui.QFont()
            font.setFamily("fonts/SourceSansPro-Regular.ttf")
            font.setPointSize(10)
            font.setKerning(True)
            font.setStyleStrategy(QtGui.QFont.PreferAntialias)
            self.qv_insituGeoUnit_rd1.setFont(font)
            self.qv_insituGeoUnit_rd1.setObjectName("qv_insituGeoUnit_rd1")
            self.buttonGroup_2 = QtWidgets.QButtonGroup()
            self.buttonGroup_2.setObjectName("buttonGroup_2")
            self.buttonGroup_2.addButton(self.qv_insituGeoUnit_rd1)
            self.horizontalLayout_91.addWidget(self.qv_insituGeoUnit_rd1)
            spacerItem17 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
            self.horizontalLayout_91.addItem(spacerItem17)
            self.qv_insituGeoUnit_rd2 = QtWidgets.QRadioButton()
            self.qv_insituGeoUnit_rd2.setMinimumSize(QtCore.QSize(51, 27))
            self.qv_insituGeoUnit_rd2.setMaximumSize(QtCore.QSize(16777215, 27))
            font = QtGui.QFont()
            font.setFamily("fonts/SourceSansPro-Regular.ttf")
            font.setPointSize(10)
            font.setKerning(True)
            font.setStyleStrategy(QtGui.QFont.PreferAntialias)
            self.qv_insituGeoUnit_rd2.setFont(font)
            self.qv_insituGeoUnit_rd2.setObjectName("qv_insituGeoUnit_rd2")
            self.buttonGroup_2.addButton(self.qv_insituGeoUnit_rd2)
            self.horizontalLayout_91.addWidget(self.qv_insituGeoUnit_rd2)
            spacerItem18 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.horizontalLayout_91.addItem(spacerItem18)
            self.verticalLayout_25.addLayout(self.horizontalLayout_91)
            spacerItem19 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
            self.verticalLayout_25.addItem(spacerItem19)
            self.horizontalLayout_92 = QtWidgets.QHBoxLayout()
            self.horizontalLayout_92.setObjectName("horizontalLayout_92")
            self.qv_insituOutFormat_lb = QtWidgets.QLabel()
            self.qv_insituOutFormat_lb.setMinimumSize(QtCore.QSize(230, 27))
            self.qv_insituOutFormat_lb.setMaximumSize(QtCore.QSize(16777215, 27))
            font = QtGui.QFont()
            font.setFamily("fonts/SourceSansPro-Regular.ttf")
            font.setPointSize(10)
            font.setBold(True)
            font.setUnderline(True)
            font.setWeight(75)
            font.setKerning(True)
            font.setStyleStrategy(QtGui.QFont.PreferAntialias)
            self.qv_insituOutFormat_lb.setFont(font)
            self.qv_insituOutFormat_lb.setObjectName("qv_insituOutFormat_lb")
            self.horizontalLayout_92.addWidget(self.qv_insituOutFormat_lb)
            self.infoButton_28 = QtWidgets.QToolButton()
            self.infoButton_28.setMaximumSize(QtCore.QSize(27, 27))
            self.infoButton_28.setStyleSheet("QToolButton {\n"
            "    border: 1px solid transparent;\n"
            "    background-color: transparent;\n"
            "    width: 27px;\n"
            "    height: 27px;\n"
            "}\n"
            "\n"
            "QToolButton:hover {\n"
            "    border: 1px solid gray;\n"
            "    border-radius: 3px;\n"
            "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
            "}\n"
            "\n"
            "QToolButton:pressed {\n"
            "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
            "}\n"
            "\n"
            "QToolButton:flat {\n"
            "    border: none;\n"
            "}")
            self.infoButton_28.setText("")
            self.infoButton_28.setIcon(icon1)
            self.infoButton_28.setIconSize(QtCore.QSize(27, 27))
            self.infoButton_28.setAutoRaise(False)
            self.infoButton_28.setObjectName("infoButton_28")
            self.horizontalLayout_92.addWidget(self.infoButton_28)
            spacerItem20 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.horizontalLayout_92.addItem(spacerItem20)
            self.verticalLayout_25.addLayout(self.horizontalLayout_92)
            self.horizontalLayout_93 = QtWidgets.QHBoxLayout()
            self.horizontalLayout_93.setObjectName("horizontalLayout_93")
            spacerItem21 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
            self.horizontalLayout_93.addItem(spacerItem21)
            self.gridLayout = QtWidgets.QGridLayout()
            self.gridLayout.setHorizontalSpacing(40)
            self.gridLayout.setVerticalSpacing(20)
            self.gridLayout.setObjectName("gridLayout")
            self.qv_insituOutFormat_ck1 = QtWidgets.QCheckBox()
            self.qv_insituOutFormat_ck1.setMinimumSize(QtCore.QSize(80, 27))
            self.qv_insituOutFormat_ck1.setMaximumSize(QtCore.QSize(16777215, 27))
            font = QtGui.QFont()
            font.setFamily("fonts/SourceSansPro-Regular.ttf")
            font.setPointSize(10)
            font.setKerning(True)
            font.setStyleStrategy(QtGui.QFont.PreferAntialias)
            self.qv_insituOutFormat_ck1.setFont(font)
            self.qv_insituOutFormat_ck1.setObjectName("qv_insituOutFormat_ck1")
            self.gridLayout.addWidget(self.qv_insituOutFormat_ck1, 0, 0, 1, 1)
            self.horizontalLayout_94 = QtWidgets.QHBoxLayout()
            self.horizontalLayout_94.setObjectName("horizontalLayout_94")
            self.qv_insituOutFormat_ck3 = QtWidgets.QCheckBox()
            self.qv_insituOutFormat_ck3.setMinimumSize(QtCore.QSize(110, 27))
            self.qv_insituOutFormat_ck3.setMaximumSize(QtCore.QSize(16777215, 27))
            font = QtGui.QFont()
            font.setFamily("fonts/SourceSansPro-Regular.ttf")
            font.setPointSize(10)
            font.setKerning(True)
            font.setStyleStrategy(QtGui.QFont.PreferAntialias)
            self.qv_insituOutFormat_ck3.setFont(font)
            self.qv_insituOutFormat_ck3.setObjectName("qv_insituOutFormat_ck3")
            self.horizontalLayout_94.addWidget(self.qv_insituOutFormat_ck3)
            spacerItem22 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.horizontalLayout_94.addItem(spacerItem22)
            self.gridLayout.addLayout(self.horizontalLayout_94, 0, 1, 1, 1)
            self.qv_insituOutFormat_ck2 = QtWidgets.QCheckBox()
            self.qv_insituOutFormat_ck2.setMinimumSize(QtCore.QSize(80, 27))
            self.qv_insituOutFormat_ck2.setMaximumSize(QtCore.QSize(16777215, 27))
            font = QtGui.QFont()
            font.setFamily("fonts/SourceSansPro-Regular.ttf")
            font.setPointSize(10)
            font.setKerning(True)
            font.setStyleStrategy(QtGui.QFont.PreferAntialias)
            self.qv_insituOutFormat_ck2.setFont(font)
            self.qv_insituOutFormat_ck2.setObjectName("qv_insituOutFormat_ck2")
            self.gridLayout.addWidget(self.qv_insituOutFormat_ck2, 1, 0, 1, 1)
            self.horizontalLayout_95 = QtWidgets.QHBoxLayout()
            self.horizontalLayout_95.setObjectName("horizontalLayout_95")
            self.qv_insituOutFormat_ck4 = QtWidgets.QCheckBox()
            self.qv_insituOutFormat_ck4.setMinimumSize(QtCore.QSize(80, 27))
            self.qv_insituOutFormat_ck4.setMaximumSize(QtCore.QSize(16777215, 27))
            font = QtGui.QFont()
            font.setFamily("fonts/SourceSansPro-Regular.ttf")
            font.setPointSize(10)
            font.setKerning(True)
            font.setStyleStrategy(QtGui.QFont.PreferAntialias)
            self.qv_insituOutFormat_ck4.setFont(font)
            self.qv_insituOutFormat_ck4.setObjectName("qv_insituOutFormat_ck4")
            self.horizontalLayout_95.addWidget(self.qv_insituOutFormat_ck4)
            spacerItem23 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
            self.horizontalLayout_95.addItem(spacerItem23)
            self.qv_insituOutFormat_im = QtWidgets.QLabel()
            self.qv_insituOutFormat_im.setMinimumSize(QtCore.QSize(15, 8))
            self.qv_insituOutFormat_im.setMaximumSize(QtCore.QSize(15, 8))
            self.qv_insituOutFormat_im.setLineWidth(0)
            self.qv_insituOutFormat_im.setText("")
            self.qv_insituOutFormat_im.setPixmap(QtGui.QPixmap("icons/fwd_arrow.png"))
            self.qv_insituOutFormat_im.setScaledContents(True)
            self.qv_insituOutFormat_im.setAlignment(QtCore.Qt.AlignCenter)
            self.qv_insituOutFormat_im.setObjectName("qv_insituOutFormat_im")
            self.horizontalLayout_95.addWidget(self.qv_insituOutFormat_im)
            spacerItem24 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
            self.horizontalLayout_95.addItem(spacerItem24)
            self.qv_insituOutFormat_ln = QtWidgets.QLineEdit()
            self.qv_insituOutFormat_ln.setEnabled(False)
            self.qv_insituOutFormat_ln.setMinimumSize(QtCore.QSize(250, 27))
            self.qv_insituOutFormat_ln.setMaximumSize(QtCore.QSize(250, 27))
            font = QtGui.QFont()
            font.setFamily("fonts/SourceSansPro-Regular.ttf")
            font.setPointSize(9)
            font.setBold(False)
            font.setWeight(50)
            font.setStyleStrategy(QtGui.QFont.PreferAntialias)
            self.qv_insituOutFormat_ln.setFont(font)
            self.qv_insituOutFormat_ln.setStyleSheet("QLineEdit {\n"
            "    border-radius: 3px;\n"
            "    padding: 1px 4px 1px 4px;\n"
            "    background-color:  rgb(240, 240, 240);\n"
            "}")
            self.qv_insituOutFormat_ln.setFrame(False)
            self.qv_insituOutFormat_ln.setObjectName("qv_insituOutFormat_ln")
            self.horizontalLayout_95.addWidget(self.qv_insituOutFormat_ln)
            self.horizontalLayout_95.addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))
            self.gridLayout.addLayout(self.horizontalLayout_95, 1, 1, 1, 1)
            self.horizontalLayout_93.addLayout(self.gridLayout)
            spacerItem25 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.horizontalLayout_93.addItem(spacerItem25)
            self.verticalLayout_25.addLayout(self.horizontalLayout_93)
            spacerItem26 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
            self.verticalLayout_25.addItem(spacerItem26)
            self.horizontalLayout_96 = QtWidgets.QHBoxLayout()
            self.horizontalLayout_96.setObjectName("horizontalLayout_96")
            self.qv_insituQuaFlag_lb = QtWidgets.QLabel()
            self.qv_insituQuaFlag_lb.setMinimumSize(QtCore.QSize(440, 27))
            self.qv_insituQuaFlag_lb.setMaximumSize(QtCore.QSize(16777215, 27))
            font = QtGui.QFont()
            font.setFamily("fonts/SourceSansPro-Regular.ttf")
            font.setPointSize(10)
            font.setBold(True)
            font.setUnderline(True)
            font.setWeight(75)
            font.setKerning(True)
            font.setStyleStrategy(QtGui.QFont.PreferAntialias)
            self.qv_insituQuaFlag_lb.setFont(font)
            self.qv_insituQuaFlag_lb.setObjectName("qv_insituQuaFlag_lb")
            self.horizontalLayout_96.addWidget(self.qv_insituQuaFlag_lb)
            self.infoButton_29 = QtWidgets.QToolButton()
            self.infoButton_29.setMaximumSize(QtCore.QSize(27, 27))
            self.infoButton_29.setStyleSheet("QToolButton {\n"
            "    border: 1px solid transparent;\n"
            "    background-color: transparent;\n"
            "    width: 27px;\n"
            "    height: 27px;\n"
            "}\n"
            "\n"
            "QToolButton:hover {\n"
            "    border: 1px solid gray;\n"
            "    border-radius: 3px;\n"
            "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
            "}\n"
            "\n"
            "QToolButton:pressed {\n"
            "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
            "}\n"
            "\n"
            "QToolButton:flat {\n"
            "    border: none;\n"
            "}")
            self.infoButton_29.setText("")
            self.infoButton_29.setIcon(icon1)
            self.infoButton_29.setIconSize(QtCore.QSize(27, 27))
            self.infoButton_29.setAutoRaise(False)
            self.infoButton_29.setObjectName("infoButton_29")
            self.horizontalLayout_96.addWidget(self.infoButton_29)
            spacerItem27 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.horizontalLayout_96.addItem(spacerItem27)
            self.verticalLayout_25.addLayout(self.horizontalLayout_96)
            self.horizontalLayout_97 = QtWidgets.QHBoxLayout()
            self.horizontalLayout_97.setObjectName("horizontalLayout_97")
            spacerItem28 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
            self.horizontalLayout_97.addItem(spacerItem28)
            self.qv_insituQuaFlag_ln = QtWidgets.QPlainTextEdit()
            self.qv_insituQuaFlag_ln.setMinimumSize(QtCore.QSize(600, 100))
            self.qv_insituQuaFlag_ln.setMaximumSize(QtCore.QSize(16777215, 100))
            font = QtGui.QFont()
            font.setFamily("fonts/SourceSansPro-Regular.ttf")
            font.setPointSize(9)
            font.setKerning(True)
            font.setStyleStrategy(QtGui.QFont.PreferAntialias)
            self.qv_insituQuaFlag_ln.setFont(font)
            self.qv_insituQuaFlag_ln.setStyleSheet("QPlainTextEdit {\n"
            "    border-radius: 3px;\n"
            "    padding: 1px 4px 1px 4px;\n"
            "    background-color:  rgb(240, 240, 240);\n"
            "}")
            self.qv_insituQuaFlag_ln.setObjectName("qv_insituQuaFlag_ln")
            self.horizontalLayout_97.addWidget(self.qv_insituQuaFlag_ln)
            spacerItem29 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.horizontalLayout_97.addItem(spacerItem29)
            self.verticalLayout_25.addLayout(self.horizontalLayout_97)
            spacerItem30 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
            self.verticalLayout_25.addItem(spacerItem30)
            self.horizontalLayout_98 = QtWidgets.QHBoxLayout()
            self.horizontalLayout_98.setObjectName("horizontalLayout_98")
            self.qv_insituAssumption_lb = QtWidgets.QLabel()
            self.qv_insituAssumption_lb.setMinimumSize(QtCore.QSize(100, 27))
            self.qv_insituAssumption_lb.setMaximumSize(QtCore.QSize(16777215, 27))
            font = QtGui.QFont()
            font.setFamily("fonts/SourceSansPro-Regular.ttf")
            font.setPointSize(10)
            font.setBold(True)
            font.setUnderline(True)
            font.setWeight(75)
            font.setKerning(True)
            font.setStyleStrategy(QtGui.QFont.PreferAntialias)
            self.qv_insituAssumption_lb.setFont(font)
            self.qv_insituAssumption_lb.setObjectName("qv_insituAssumption_lb")
            self.horizontalLayout_98.addWidget(self.qv_insituAssumption_lb)
            self.infoButton_30 = QtWidgets.QToolButton()
            self.infoButton_30.setMaximumSize(QtCore.QSize(27, 27))
            self.infoButton_30.setStyleSheet("QToolButton {\n"
            "    border: 1px solid transparent;\n"
            "    background-color: transparent;\n"
            "    width: 27px;\n"
            "    height: 27px;\n"
            "}\n"
            "\n"
            "QToolButton:hover {\n"
            "    border: 1px solid gray;\n"
            "    border-radius: 3px;\n"
            "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
            "}\n"
            "\n"
            "QToolButton:pressed {\n"
            "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
            "}\n"
            "\n"
            "QToolButton:flat {\n"
            "    border: none;\n"
            "}")
            self.infoButton_30.setText("")
            self.infoButton_30.setIcon(icon1)
            self.infoButton_30.setIconSize(QtCore.QSize(27, 27))
            self.infoButton_30.setAutoRaise(False)
            self.infoButton_30.setObjectName("infoButton_30")
            self.horizontalLayout_98.addWidget(self.infoButton_30)
            spacerItem31 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.horizontalLayout_98.addItem(spacerItem31)
            self.verticalLayout_25.addLayout(self.horizontalLayout_98)
            self.horizontalLayout_99 = QtWidgets.QHBoxLayout()
            self.horizontalLayout_99.setObjectName("horizontalLayout_99")
            spacerItem32 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
            self.horizontalLayout_99.addItem(spacerItem32)
            self.qv_insituAssumption_ln = QtWidgets.QPlainTextEdit()
            self.qv_insituAssumption_ln.setMinimumSize(QtCore.QSize(600, 100))
            self.qv_insituAssumption_ln.setMaximumSize(QtCore.QSize(16777215, 100))
            font = QtGui.QFont()
            font.setFamily("fonts/SourceSansPro-Regular.ttf")
            font.setPointSize(9)
            font.setKerning(True)
            font.setStyleStrategy(QtGui.QFont.PreferAntialias)
            self.qv_insituAssumption_ln.setFont(font)
            self.qv_insituAssumption_ln.setStyleSheet("QPlainTextEdit {\n"
            "    border-radius: 3px;\n"
            "    padding: 1px 4px 1px 4px;\n"
            "    background-color:  rgb(240, 240, 240);\n"
            "}")
            self.qv_insituAssumption_ln.setObjectName("qv_insituAssumption_ln")
            self.horizontalLayout_99.addWidget(self.qv_insituAssumption_ln)
            spacerItem33 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.horizontalLayout_99.addItem(spacerItem33)
            self.verticalLayout_25.addLayout(self.horizontalLayout_99)
            self.qv_insituCalInfo.setText("Operator's standard calibration procedures applied to raw digital data")
            self.qv_insituCalDesc_lb.setText("Link to the procedure\'s description(s):")
            self.qv_insituCalCons_lb.setText("Source(s) of calibration constants:")
            self.qv_insituCalMat_lb.setText("Source(s) of calibration materials:")
            self.qv_insituGeoUnit.setText("Conversion to geophysical units ?")
            self.qv_insituGeoUnit_rd1.setText("Yes")
            self.qv_insituGeoUnit_rd2.setText("No")
            self.qv_insituOutFormat_lb.setText("Output in standardized format")
            self.qv_insituOutFormat_ck1.setText("NetCDF")
            self.qv_insituOutFormat_ck3.setText("NASA/Ames")
            self.qv_insituOutFormat_ck2.setText("HDF")
            self.qv_insituOutFormat_ck4.setText("Other")
            self.qv_insituQuaFlag_lb.setText("Quality-control flagging(s) applied to individual data points")
            self.qv_insituAssumption_lb.setText("Assumption(s)")
            self.qv_insituOutFormat_im.hide()
            self.qv_insituOutFormat_ln.hide()
            all_info_boxes = self.tabWidgetPage7.findChildren(QToolButton)
            for widget in all_info_boxes:
                widget.clicked.connect(lambda: self.button_clicked())
            all_radiobuttons = self.tabWidgetPage7.findChildren(QtWidgets.QRadioButton)
            for widget in all_radiobuttons:
                if widget.objectName() != "qv_obsRadio" and widget.objectName() != "qv_insituRadio":
                    widget.clicked.connect(lambda: self.set_modified())
            all_line_edits = self.tabWidgetPage7.findChildren(QtWidgets.QLineEdit)
            for widget in all_line_edits:
                widget.textChanged.connect(lambda: self.set_modified())
            all_text_edits = self.tabWidgetPage7.findChildren(QtWidgets.QPlainTextEdit)
            for widget in all_text_edits:
                widget.textChanged.connect(lambda: self.set_modified())
            all_checkboxes = self.tabWidgetPage7.findChildren(QtWidgets.QCheckBox)
            for widget in all_checkboxes:
                widget.clicked.connect(lambda: self.set_modified())
            self.qv_insituOutFormat_ck4.clicked.connect(lambda: self.output_other())
    else:
        if self.verticalLayout_25.count() != 0:
            clearLayout(self.verticalLayout_25)
    
def clearLayout(layout):
    for i in reversed(range(layout.count())):   
        item = layout.itemAt(i)
        if isinstance(item, QtWidgets.QWidgetItem):
            item.widget().deleteLater()
        elif isinstance(item, QtWidgets.QLayout):
            clearLayout(item.layout())
        layout.removeItem(item)        
    
def qv_output_other(self):
    if self.qv_insituOutFormat_ck4.isChecked() == True:
        self.qv_insituOutFormat_im.show()
        self.qv_insituOutFormat_ln.show()
        self.qv_insituOutFormat_ln.setEnabled(True)
    else:
        self.qv_insituOutFormat_im.hide()
        self.qv_insituOutFormat_ln.hide()
        self.qv_insituOutFormat_ln.setDisabled(True)


class MyInfo(QtWidgets.QDialog, Ui_infoWindow):
    def __init__(self, infoText):
        QWidget.__init__(self)
        self.setupUi(self)
        self.iw_label_1.setText(infoText)
        self.iw_okButton.clicked.connect(self.closeWindow)

    def closeWindow(self):
        self.close()