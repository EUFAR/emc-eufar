# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QWidget, QToolButton, QDateEdit
from PyQt5.QtGui import QCursor
from functions.sql_functions import sql_valueRead
from ui.Ui_infowindow import Ui_infoWindow


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


def plusButton_11_clicked(self):
    if self.qv_insitu == 0 and self.qv_imagery == 0:
        self.qv_tabWidget.setVisible(True)
        self.qv_tabWidget.setEnabled(True)
        self.qv_spacerItem.changeSize(20, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.qv_tabWidget.setStyleSheet("QTabWidget::pane {\n"
        "    border: 1px solid rgb(180,180,180);\n"
        "    border-bottom-left-radius: 5px;\n"
        "    border-bottom-right-radius: 5px;\n"
        "    border-top-right-radius: 5px;\n"
        "    top: -1px;\n"
        "    background-color: rgb(230,230,230);\n"
        "}\n"
        "\n"
        "QTabWidget::tab-bar {\n"
        "    left: 0px; \n"
        "}\n"
        "\n"
        "QTabBar::tab {\n"
        "    background: transparent;\n"
        "    border-top: 1px solid rgb(180,180,180);\n"
        "    border-left: 1px solid rgb(180,180,180);\n"
        "    border-right: 1px solid rgb(180,180,180);\n"
        "    border-top-right-radius: 5px;\n"
        "    border-top-left-radius: 5px;\n"
        "    padding: 2px 10px 2px 10px;\n"
        "    margin-right: 2px;\n"
        "}\n"
        "\n"
        "QTabBar::tab:hover {\n"
        "    background-color: rgb(210,210,210);\n"
        "}\n"
        "\n"
        "QTabBar::tab:selected {\n"
        "    background: rgb(230,230,230);\n"
        "}\n"
        "\n"
        "QTabBar::tab:!selected {\n"
        "    margin-top: 4px; \n"
        "}\n"
        "\n"
        "QTabBar::scroller {\n"
        "}\n"
        "\n"
        "QTabBar QToolButton {\n"
        "    border: 1px solid rgb(180,180,180);\n"
        "    background-color: rgb(240,240,240);\n"
        "}\n"
        "\n"
        "QTabBar QToolButton:hover {\n"
        "    background-color: rgb(219, 219, 219);\n"
        "}\n"
        "\n"
        "QTabBar QToolButton::right-arrow {\n"
        "    image: url(icons/right_arrow_icon.svg); \n"
        "    width: 16px;\n"
        "    height: 16px;\n"
        "    margin : 2px 2px 2px 2px;\n"
        "}\n"
        "\n"
        "QTabBar QToolButton::right-arrow:pressed {\n"
        "    right: -1px;\n"
        "    bottom: -1px;\n"
        "}\n"
        "\n"
        "QTabBar QToolButton::left-arrow {\n"
        "    image: url(icons/left_arrow_icon.svg); \n"
        "    width: 16px;\n"
        "    height: 16px;\n"
        "    margin : 2px 2px 2px 2px;\n"
        "}\n"
        "\n"
        "QTabBar QToolButton::left-arrow:pressed {\n"
        "    right: -1px;\n"
        "    bottom: -1px;\n"
        "}")
    font2 = QtGui.QFont()
    font2.setFamily("font/SourceSansPro-Regular.ttf")
    font2.setPointSize(10)
    font2.setBold(True)
    font2.setUnderline(True)
    font2.setWeight(75)
    font2.setStyleStrategy(QtGui.QFont.PreferAntialias)
    font2.setKerning(True)
    font = QtGui.QFont()
    font.setFamily("font/SourceSansPro-Regular.ttf")
    font.setPointSize(10)
    font.setStyleStrategy(QtGui.QFont.PreferAntialias)
    font.setKerning(True)
    font3 = QtGui.QFont()
    font3.setFamily("font/SourceSansPro-Regular.ttf")
    font3.setPointSize(9)
    font3.setStyleStrategy(QtGui.QFont.PreferAntialias)
    font3.setKerning(True)
    font4 = QtGui.QFont()
    font4.setFamily("font/SourceSansPro-Regular.ttf")
    font4.setPointSize(10)
    font4.setStyleStrategy(QtGui.QFont.PreferAntialias)
    font4.setUnderline(True)
    font4.setKerning(True)
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap("icons/info_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    icon2 = QtGui.QIcon()
    icon2.addPixmap(QtGui.QPixmap("icons/continue_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    self.qv_imagery_tab_1.append(QtWidgets.QWidget())
    self.qv_imagery_tab_1[self.qv_imagery].setObjectName("qv_imagery_tab_1_" + str(self.qv_imagery))
    self.qv_tabWidget.addTab(self.qv_imagery_tab_1[self.qv_imagery], "Earth observation/Remote sensing data " + str(self.qv_imagery + 1))
    self.qv_imagery_gridlay_8.append(QtWidgets.QGridLayout(self.qv_imagery_tab_1[self.qv_imagery]))
    self.qv_imagery_gridlay_8[self.qv_imagery].setContentsMargins(0, 0, 0, 0)
    self.qv_imagery_gridlay_8[self.qv_imagery].setObjectName("qv_imagery_gridlay_8_" + str(self.qv_imagery))
    self.qv_imagery_scroll_1.append(QtWidgets.QScrollArea(self.qv_imagery_tab_1[self.qv_imagery]))
    self.qv_imagery_scroll_1[self.qv_imagery].setStyleSheet("QScrollArea { background: transparent; }\n"
    "\n"
    "QScrollArea > QWidget > QWidget { background: transparent; }\n"
    "\n"
    "QScrollBar:vertical {\n"
    "  border: 1px solid white;\n"
    "  background-color: rgb(240, 240, 240);\n"
    "  width: 20px;\n"
    "  margin: 21px 0px 21px 0px;\n"
    "}\n"
    "\n"
    "QScrollBar:horizontal {\n"
    "  border: 1px solid white;\n"
    "  background-color: rgb(240, 240, 240);\n"
    "  height: 20px;\n"
    "  margin: 0px 21px 0px 21px;\n"
    "}\n"
    "\n"
    "QScrollBar::handle:vertical {\n"
    "  background-color: rgb(205, 205, 205);\n"
    "  min-height: 25px;\n"
    "}\n"
    "\n"
    "QScrollBar:handle:vertical:hover {\n"
    "  background-color: rgb(167, 167, 167);\n"
    "}\n"
    "\n"
    "QScrollBar::handle:horizontal {\n"
    "  background-color: rgb(205, 205, 205);\n"
    "  min-width: 25px;\n"
    "}\n"
    "\n"
    "QScrollBar:handle:horizontal:hover {\n"
    "  background-color: rgb(167, 167, 167);\n"
    "}\n"
    "\n"
    "QScrollBar::add-line:vertical {\n"
    "  border-top: 1px solid rgb(240,240,240);\n"
    "  border-left: 1px solid white;\n"
    "  border-right: 1px solid white;\n"
    "  border-bottom: 1px solid white;\n"
    "  background-color: rgb(240, 240, 240);\n"
    "  height: 20px;\n"
    "  subcontrol-position: bottom;\n"
    "  subcontrol-origin: margin;\n"
    "}\n"
    "\n"
    "QScrollBar::add-line:vertical:hover {\n"
    "  background-color: rgb(219, 219, 219);\n"
    "}\n"
    "\n"
    "QScrollBar::sub-line:vertical {\n"
    "  border-top: 1px solid white;\n"
    "  border-left: 1px solid white;\n"
    "  border-right: 1px solid white;\n"
    "  border-bottom: 1px solid rgb(240,240,240);\n"
    "  background-color: rgb(240, 240, 240);\n"
    "  height: 20px;\n"
    "  subcontrol-position: top;\n"
    "  subcontrol-origin: margin;\n"
    "}\n"
    "\n"
    "QScrollBar::sub-line:vertical:hover {\n"
    "  background-color: rgb(219, 219, 219);\n"
    "}\n"
    "\n"
    "QScrollBar::up-arrow:vertical {\n"
    "  image: url(icons/up_arrow_icon.svg); \n"
    "  width: 16px;\n"
    "  height: 16px;\n"
    "}\n"
    "\n"
    "QScrollBar::up-arrow:vertical:pressed {\n"
    "  right: -1px;\n"
    "  bottom: -1px;\n"
    "}\n"
    "\n"
    "QScrollBar::down-arrow:vertical {\n"
    "  image: url(icons/down_arrow_icon.svg); \n"
    "  width: 16px;\n"
    "  height: 16px;\n"
    "}\n"
    "\n"
    "QScrollBar::down-arrow:vertical:pressed {\n"
    "  right: -1px;\n"
    "  bottom: -1px;\n"
    "}\n"
    "\n"
    "QScrollBar::add-line:horizontal {\n"
    "  border-top: 1px solid white;\n"
    "  border-left: 1px solid rgb(240,240,240);\n"
    "  border-right: 1px solid white;\n"
    "  border-bottom: 1px solid white;\n"
    "  background-color: rgb(240, 240, 240);\n"
    "  width: 20px;\n"
    "  subcontrol-position: right;\n"
    "  subcontrol-origin: margin;\n"
    "}\n"
    "\n"
    "QScrollBar::add-line:horizontal:hover {\n"
    "  background-color: rgb(219, 219, 219);\n"
    "}\n"
    "\n"
    "QScrollBar::sub-line:horizontal {\n"
    "  border-top: 1px solid white;\n"
    "  border-left: 1px solid white;\n"
    "  border-right: 1px solid rgb(240,240,240);\n"
    "  border-bottom: 1px solid white;\n"
    "  background-color: rgb(240, 240, 240);\n"
    "  width: 20px;\n"
    "  subcontrol-position: left;\n"
    "  subcontrol-origin: margin;\n"
    "}\n"
    "\n"
    "QScrollBar::sub-line:horizontal:hover {\n"
    "  background-color: rgb(219, 219, 219);\n"
    "}\n"
    "\n"
    "QScrollBar::left-arrow:horizontal {\n"
    "  image: url(icons/left_arrow_icon.svg); \n"
    "  width: 16px;\n"
    "  height: 16px;\n"
    "}\n"
    "\n"
    "QScrollBar::left-arrow:horizontal:pressed {\n"
    "  right: -1px;\n"
    "  bottom: -1px;\n"
    "}\n"
    "\n"
    "QScrollBar::right-arrow:horizontal {\n"
    "  image: url(icons/right_arrow_icon.svg); \n"
    "  width: 16px;\n"
    "  height: 16px;\n"
    "}\n"
    "\n"
    "QScrollBar::right-arrow:horizontal:pressed {\n"
    "  right: -1px;\n"
    "  bottom: -1px;\n"
    "}")
    self.qv_imagery_scroll_1[self.qv_imagery].setFrameShape(QtWidgets.QFrame.NoFrame)
    self.qv_imagery_scroll_1[self.qv_imagery].setWidgetResizable(True)
    self.qv_imagery_scroll_1[self.qv_imagery].setObjectName("qv_imagery_scroll_1_" + str(self.qv_imagery))
    self.qv_imagery_scroll_2.append(QtWidgets.QWidget())
    self.qv_imagery_scroll_2[self.qv_imagery].setObjectName("qv_imagery_scroll_2_" + str(self.qv_imagery))
    self.qv_imagery_scroll_1[self.qv_imagery].setWidget(self.qv_imagery_scroll_2[self.qv_imagery])
    self.qv_imagery_gridlay_8[self.qv_imagery].addWidget(self.qv_imagery_scroll_1[self.qv_imagery], 0, 0, 1, 1)
    self.qv_imagery_verlay_1.append(QtWidgets.QVBoxLayout(self.qv_imagery_scroll_2[self.qv_imagery]))
    self.qv_imagery_verlay_1[self.qv_imagery].setObjectName("qv_imagery_verlay_1_" + str(self.qv_imagery))
    self.qv_imagery_verlay_1[self.qv_imagery].addItem(QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, 
                                                                          QtWidgets.QSizePolicy.Fixed))
    self.qv_imagery_horlay_34.append(QtWidgets.QHBoxLayout())
    self.qv_imagery_horlay_34[self.qv_imagery].setObjectName("qv_imagery_horlay_34_" + str(self.qv_imagery))
    self.qv_imagery_verlay_1[self.qv_imagery].addLayout(self.qv_imagery_horlay_34[self.qv_imagery])
    self.qv_imagery_horlay_34[self.qv_imagery].addItem(QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Fixed, 
                                                                          QtWidgets.QSizePolicy.Minimum))
    self.qv_imagery_lab_36.append(QtWidgets.QLabel())
    self.qv_imagery_lab_36[self.qv_imagery].setMinimumSize(QtCore.QSize(0, 27))
    self.qv_imagery_lab_36[self.qv_imagery].setMaximumSize(QtCore.QSize(16777215, 27))
    self.qv_imagery_lab_36[self.qv_imagery].setFont(font2)
    self.qv_imagery_lab_36[self.qv_imagery].setObjectName("qv_imagery_lab_36_" + str(self.qv_imagery))
    self.qv_imagery_lab_36[self.qv_imagery].setText("Tab controls")
    self.qv_imagery_horlay_34[self.qv_imagery].addWidget(self.qv_imagery_lab_36[self.qv_imagery])
    self.qv_imagery_horlay_34[self.qv_imagery].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, 
                                                                          QtWidgets.QSizePolicy.Minimum))
    self.qv_imagery_list_3.append(QtWidgets.QComboBox())
    self.qv_imagery_list_3[self.qv_imagery].setMinimumSize(QtCore.QSize(310, 27))
    self.qv_imagery_list_3[self.qv_imagery].setMaximumSize(QtCore.QSize(310, 27))
    self.qv_imagery_list_3[self.qv_imagery].setFont(font3)
    self.qv_imagery_list_3[self.qv_imagery].setStyleSheet("QComboBox {\n"
    "    border: 1px solid #acacac;\n"
    "    border-radius: 1px;\n"
    "    padding-left: 5px;\n"
    "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
    "stop: 0 #f0f0f0, stop: 1 #e5e5e5);\n"
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
    "stop: 0 #ecf4fc, stop: 1 #dcecfc);\n"
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
    self.qv_imagery_list_3[self.qv_imagery].setFrame(False)
    self.qv_imagery_list_3[self.qv_imagery].setObjectName("qv_imagery_list_3_" + str(self.qv_imagery))
    self.qv_imagery_list_3[self.qv_imagery].addItem("Make a choice...")
    self.qv_imagery_list_3[self.qv_imagery].addItem("Copy all form content to a new tab")
    self.qv_imagery_list_3[self.qv_imagery].addItem("Copy all form content to an existing tab")
    self.qv_imagery_horlay_34[self.qv_imagery].addWidget(self.qv_imagery_list_3[self.qv_imagery])
    self.qv_imagery_lab_37.append(QtWidgets.QLabel())
    self.qv_imagery_lab_37[self.qv_imagery].setMinimumSize(QtCore.QSize(15, 15))
    self.qv_imagery_lab_37[self.qv_imagery].setMaximumSize(QtCore.QSize(15, 15))
    self.qv_imagery_lab_37[self.qv_imagery].setObjectName("qv_imagery_lab_12_" + str(self.qv_imagery))
    self.qv_imagery_lab_37[self.qv_imagery].setText("")
    self.qv_imagery_lab_37[self.qv_imagery].setPixmap(QtGui.QPixmap("icons/fwdarrow_icon.svg"))
    self.qv_imagery_lab_37[self.qv_imagery].setScaledContents(True)
    self.qv_imagery_lab_37[self.qv_imagery].setAlignment(QtCore.Qt.AlignCenter)
    self.qv_imagery_horlay_34[self.qv_imagery].addWidget(self.qv_imagery_lab_37[self.qv_imagery])
    self.qv_imagery_lab_37[self.qv_imagery].hide()
    self.qv_imagery_lab_37[self.qv_imagery].setDisabled(True)
    self.qv_imagery_list_4.append(QtWidgets.QComboBox())
    self.qv_imagery_list_4[self.qv_imagery].setMinimumSize(QtCore.QSize(320, 27))
    self.qv_imagery_list_4[self.qv_imagery].setMaximumSize(QtCore.QSize(320, 27))
    self.qv_imagery_list_4[self.qv_imagery].setFont(font3)
    self.qv_imagery_list_4[self.qv_imagery].setStyleSheet("QComboBox {\n"
    "    border: 1px solid #acacac;\n"
    "    border-radius: 1px;\n"
    "    padding-left: 5px;\n"
    "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
    "stop: 0 #f0f0f0, stop: 1 #e5e5e5);\n"
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
    "stop: 0 #ecf4fc, stop: 1 #dcecfc);\n"
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
    self.qv_imagery_list_4[self.qv_imagery].setFrame(False)
    self.qv_imagery_list_4[self.qv_imagery].setObjectName("qv_imagery_list_4_" + str(self.qv_imagery))
    self.qv_imagery_list_4[self.qv_imagery].hide()
    self.qv_imagery_list_4[self.qv_imagery].setDisabled(True)
    self.qv_imagery_horlay_34[self.qv_imagery].addWidget(self.qv_imagery_list_4[self.qv_imagery])
    self.qv_imagery_contBut_1.append(QtWidgets.QToolButton())
    self.qv_imagery_contBut_1[self.qv_imagery].setMaximumSize(QtCore.QSize(27, 27))
    self.qv_imagery_contBut_1[self.qv_imagery].setStyleSheet("QToolButton {\n"
    "    border: 1px solid transparent;\n"
    "    background-color: transparent;\n"
    "    width: 27px;\n"
    "    height: 27px;\n"
    "}\n"
    "QToolButton:flat {\n"
    "    border: none;\n"
    "}")
    self.qv_imagery_contBut_1[self.qv_imagery].setText("")
    self.qv_imagery_contBut_1[self.qv_imagery].setIcon(icon2)
    self.qv_imagery_contBut_1[self.qv_imagery].setIconSize(QtCore.QSize(23, 23))
    self.qv_imagery_contBut_1[self.qv_imagery].setAutoRaise(False)
    self.qv_imagery_contBut_1[self.qv_imagery].setObjectName("qv_imagery_contBut_1_" + str(self.qv_imagery))
    self.qv_imagery_horlay_34[self.qv_imagery].addWidget(self.qv_imagery_contBut_1[self.qv_imagery])
    self.qv_imagery_horlay_34[self.qv_imagery].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, 
                                                    QtWidgets.QSizePolicy.Minimum))
    self.qv_imagery_infBut_15.append(QtWidgets.QToolButton())
    self.qv_imagery_infBut_15[self.qv_imagery].setMaximumSize(QtCore.QSize(27, 27))
    self.qv_imagery_infBut_15[self.qv_imagery].setStyleSheet("QToolButton {\n"
    "    border: 1px solid transparent;\n"
    "    background-color: transparent;\n"
    "    width: 27px;\n"
    "    height: 27px;\n"
    "}\n"
    "QToolButton:flat {\n"
    "    border: none;\n"
    "}")
    self.qv_imagery_infBut_15[self.qv_imagery].setText("")
    self.qv_imagery_infBut_15[self.qv_imagery].setIcon(icon)
    self.qv_imagery_infBut_15[self.qv_imagery].setIconSize(QtCore.QSize(23, 23))
    self.qv_imagery_infBut_15[self.qv_imagery].setAutoRaise(False)
    self.qv_imagery_infBut_15[self.qv_imagery].setObjectName("infoButton_45")
    self.qv_imagery_horlay_34[self.qv_imagery].addWidget(self.qv_imagery_infBut_15[self.qv_imagery])
    self.qv_imagery_horlay_34[self.qv_imagery].addItem(QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, 
                                                                          QtWidgets.QSizePolicy.Minimum))
    self.qv_imagery_verlay_1[self.qv_imagery].addItem(QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, 
                                                                          QtWidgets.QSizePolicy.Fixed))
    self.qv_imagery_horlay_33.append(QtWidgets.QHBoxLayout())
    self.qv_imagery_horlay_33[self.qv_imagery].setObjectName("qv_imagery_horlay_33_" + str(self.qv_imagery))
    self.qv_imagery_verlay_1[self.qv_imagery].addLayout(self.qv_imagery_horlay_33[self.qv_imagery])
    self.qv_imagery_lab_35.append(QtWidgets.QLabel())
    self.qv_imagery_lab_35[self.qv_imagery].setMinimumSize(QtCore.QSize(0, 27))
    self.qv_imagery_lab_35[self.qv_imagery].setMaximumSize(QtCore.QSize(16777215, 27))
    self.qv_imagery_lab_35[self.qv_imagery].setFont(font2)
    self.qv_imagery_lab_35[self.qv_imagery].setObjectName("qv_imagery_lab_35_" + str(self.qv_imagery))
    self.qv_imagery_lab_35[self.qv_imagery].setText("The current form is linked to the following instrument")
    self.qv_imagery_horlay_33[self.qv_imagery].addWidget(self.qv_imagery_lab_35[self.qv_imagery])
    self.qv_imagery_horlay_33[self.qv_imagery].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, 
                                                                          QtWidgets.QSizePolicy.Minimum))
    
    self.qv_imagery_list_2.append(QtWidgets.QComboBox())
    self.qv_imagery_list_2[self.qv_imagery].setMinimumSize(QtCore.QSize(220, 27))
    self.qv_imagery_list_2[self.qv_imagery].setMaximumSize(QtCore.QSize(220, 27))
    self.qv_imagery_list_2[self.qv_imagery].setFont(font3)
    self.qv_imagery_list_2[self.qv_imagery].setStyleSheet("QComboBox {\n"
    "    border: 1px solid #acacac;\n"
    "    border-radius: 1px;\n"
    "    padding-left: 5px;\n"
    "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
    "stop: 0 #f0f0f0, stop: 1 #e5e5e5);\n"
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
    "stop: 0 #ecf4fc, stop: 1 #dcecfc);\n"
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
    self.qv_imagery_list_2[self.qv_imagery].setFrame(False)
    self.qv_imagery_list_2[self.qv_imagery].setObjectName("qv_imagery_list_2_" + str(self.qv_imagery))
    self.qv_imagery_horlay_33[self.qv_imagery].addWidget(self.qv_imagery_list_2[self.qv_imagery])
    
    self.qv_imagery_infBut_14.append(QtWidgets.QToolButton())
    self.qv_imagery_infBut_14[self.qv_imagery].setMaximumSize(QtCore.QSize(27, 27))
    self.qv_imagery_infBut_14[self.qv_imagery].setStyleSheet("QToolButton {\n"
    "    border: 1px solid transparent;\n"
    "    background-color: transparent;\n"
    "    width: 27px;\n"
    "    height: 27px;\n"
    "}\n"
    "QToolButton:flat {\n"
    "    border: none;\n"
    "}")
    self.qv_imagery_infBut_14[self.qv_imagery].setText("")
    self.qv_imagery_infBut_14[self.qv_imagery].setIcon(icon)
    self.qv_imagery_infBut_14[self.qv_imagery].setIconSize(QtCore.QSize(23, 23))
    self.qv_imagery_infBut_14[self.qv_imagery].setAutoRaise(False)
    self.qv_imagery_infBut_14[self.qv_imagery].setObjectName("infoButton_44")
    self.qv_imagery_horlay_33[self.qv_imagery].addWidget(self.qv_imagery_infBut_14[self.qv_imagery])
    self.qv_imagery_horlay_33[self.qv_imagery].addItem(QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, 
                                                                          QtWidgets.QSizePolicy.Minimum))
    self.qv_imagery_verlay_1[self.qv_imagery].addItem(QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, 
                                                                          QtWidgets.QSizePolicy.Fixed))
    self.qv_imagery_horlay_1.append(QtWidgets.QHBoxLayout())
    self.qv_imagery_horlay_1[self.qv_imagery].setObjectName("qv_imagery_horlay_1_" + str(self.qv_imagery))
    self.qv_imagery_verlay_1[self.qv_imagery].addLayout(self.qv_imagery_horlay_1[self.qv_imagery])
    self.qv_imagery_lab_1.append(QtWidgets.QLabel())
    self.qv_imagery_lab_1[self.qv_imagery].setMinimumSize(QtCore.QSize(0, 27))
    self.qv_imagery_lab_1[self.qv_imagery].setMaximumSize(QtCore.QSize(16777215, 27))
    self.qv_imagery_lab_1[self.qv_imagery].setFont(font2)
    self.qv_imagery_lab_1[self.qv_imagery].setObjectName("qv_imagery_lab_1_" + str(self.qv_imagery))
    self.qv_imagery_lab_1[self.qv_imagery].setText("Calibration information")
    self.qv_imagery_horlay_1[self.qv_imagery].addWidget(self.qv_imagery_lab_1[self.qv_imagery])
    self.qv_imagery_infBut_1.append(QtWidgets.QToolButton())
    self.qv_imagery_infBut_1[self.qv_imagery].setMaximumSize(QtCore.QSize(27, 27))
    self.qv_imagery_infBut_1[self.qv_imagery].setStyleSheet("QToolButton {\n"
    "    border: 1px solid transparent;\n"
    "    background-color: transparent;\n"
    "    width: 27px;\n"
    "    height: 27px;\n"
    "}\n"
    "QToolButton:flat {\n"
    "    border: none;\n"
    "}")
    self.qv_imagery_infBut_1[self.qv_imagery].setText("")
    self.qv_imagery_infBut_1[self.qv_imagery].setIcon(icon)
    self.qv_imagery_infBut_1[self.qv_imagery].setIconSize(QtCore.QSize(23, 23))
    self.qv_imagery_infBut_1[self.qv_imagery].setAutoRaise(False)
    self.qv_imagery_infBut_1[self.qv_imagery].setObjectName("infoButton_31")
    self.qv_imagery_horlay_1[self.qv_imagery].addWidget(self.qv_imagery_infBut_1[self.qv_imagery])
    self.qv_imagery_horlay_1[self.qv_imagery].addItem(QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, 
                                                                            QtWidgets.QSizePolicy.Minimum))
    self.qv_imagery_horlay_2.append(QtWidgets.QHBoxLayout())
    self.qv_imagery_horlay_2[self.qv_imagery].setObjectName("qv_imagery_horlay_2_" + str(self.qv_imagery))
    self.qv_imagery_horlay_2[self.qv_imagery].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, 
                                                                            QtWidgets.QSizePolicy.Minimum))
    self.qv_imagery_verlay_1[self.qv_imagery].addLayout(self.qv_imagery_horlay_2[self.qv_imagery])
    self.qv_imagery_gridlay_1.append(QtWidgets.QGridLayout())
    self.qv_imagery_gridlay_1[self.qv_imagery].setObjectName("qv_imagery_gridlay_1_" + str(self.qv_imagery))
    self.qv_imagery_horlay_2[self.qv_imagery].addLayout(self.qv_imagery_gridlay_1[self.qv_imagery])
    self.qv_imagery_horlay_2[self.qv_imagery].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, 
                                                                            QtWidgets.QSizePolicy.Minimum))
    self.qv_imagery_lab_2.append(QtWidgets.QLabel())
    self.qv_imagery_lab_2[self.qv_imagery].setMinimumSize(QtCore.QSize(0, 27))
    self.qv_imagery_lab_2[self.qv_imagery].setMaximumSize(QtCore.QSize(16777215, 27))
    self.qv_imagery_lab_2[self.qv_imagery].setFont(font)
    self.qv_imagery_lab_2[self.qv_imagery].setObjectName("qv_imagery_lab_2_" + str(self.qv_imagery))
    self.qv_imagery_lab_2[self.qv_imagery].setText("Name of calibration laboratory:")
    self.qv_imagery_gridlay_1[self.qv_imagery].addWidget(self.qv_imagery_lab_2[self.qv_imagery], 0, 0, 1, 1)
    self.qv_imagery_line_1.append(QtWidgets.QLineEdit())
    self.qv_imagery_line_1[self.qv_imagery].setMinimumSize(QtCore.QSize(450, 27))
    self.qv_imagery_line_1[self.qv_imagery].setMaximumSize(QtCore.QSize(450, 27))
    self.qv_imagery_line_1[self.qv_imagery].setFont(font3)
    self.qv_imagery_line_1[self.qv_imagery].setStyleSheet("QLineEdit {\n"
    "    border-radius: 3px;\n"
    "   padding: 1px 4px 1px 4px;\n"
    "    background-color:  rgb(240, 240, 240);\n"
    "}")
    self.qv_imagery_line_1[self.qv_imagery].setFrame(False)
    self.qv_imagery_line_1[self.qv_imagery].setObjectName("qv_imagery_line_1_" + str(self.qv_imagery))
    self.qv_imagery_gridlay_1[self.qv_imagery].addWidget(self.qv_imagery_line_1[self.qv_imagery], 0, 1, 1, 1)
    self.qv_imagery_lab_3.append(QtWidgets.QLabel())
    self.qv_imagery_lab_3[self.qv_imagery].setMinimumSize(QtCore.QSize(0, 27))
    self.qv_imagery_lab_3[self.qv_imagery].setMaximumSize(QtCore.QSize(16777215, 27))
    self.qv_imagery_lab_3[self.qv_imagery].setFont(font)
    self.qv_imagery_lab_3[self.qv_imagery].setObjectName("qv_imagery_lab_3_" + str(self.qv_imagery))
    self.qv_imagery_lab_3[self.qv_imagery].setText("Date of radimetric calibration:")
    self.qv_imagery_gridlay_1[self.qv_imagery].addWidget(self.qv_imagery_lab_3[self.qv_imagery], 1, 0, 1, 1)
    self.qv_imagery_date_1.append(QtWidgets.QDateEdit())
    self.qv_imagery_date_1[self.qv_imagery].setMinimumSize(QtCore.QSize(130, 27))
    self.qv_imagery_date_1[self.qv_imagery].setMaximumSize(QtCore.QSize(130, 27))
    self.qv_imagery_date_1[self.qv_imagery].setDate(QtCore.QDate(2014, 10, 28))
    self.qv_imagery_date_1[self.qv_imagery].setCurrentSection(QtWidgets.QDateTimeEdit.YearSection)
    self.qv_imagery_date_1[self.qv_imagery].setAlignment(QtCore.Qt.AlignCenter)
    self.qv_imagery_date_1[self.qv_imagery].setCalendarPopup(True)
    self.qv_imagery_date_1[self.qv_imagery].setFont(font)
    self.qv_imagery_date_1[self.qv_imagery].setDisplayFormat("yyyy-MM-dd")
    self.qv_imagery_date_1[self.qv_imagery].setStyleSheet("QDateEdit {\n"
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
    self.qv_imagery_date_1[self.qv_imagery].setObjectName("qv_imagery_date_1" + str(self.qv_imagery))
    self.qv_imagery_gridlay_1[self.qv_imagery].addWidget(self.qv_imagery_date_1[self.qv_imagery])
    self.qv_imagery_lab_4.append(QtWidgets.QLabel())
    self.qv_imagery_lab_4[self.qv_imagery].setMinimumSize(QtCore.QSize(0, 27))
    self.qv_imagery_lab_4[self.qv_imagery].setMaximumSize(QtCore.QSize(16777215, 27))
    self.qv_imagery_lab_4[self.qv_imagery].setFont(font)
    self.qv_imagery_lab_4[self.qv_imagery].setObjectName("qv_imagery_lab_4_" + str(self.qv_imagery))
    self.qv_imagery_lab_4[self.qv_imagery].setText("Date of radimetric calibration:")
    self.qv_imagery_gridlay_1[self.qv_imagery].addWidget(self.qv_imagery_lab_4[self.qv_imagery], 2, 0, 1, 1)
    self.qv_imagery_date_2.append(QtWidgets.QDateEdit())
    self.qv_imagery_date_2[self.qv_imagery].setMinimumSize(QtCore.QSize(130, 27))
    self.qv_imagery_date_2[self.qv_imagery].setMaximumSize(QtCore.QSize(130, 27))
    self.qv_imagery_date_2[self.qv_imagery].setDate(QtCore.QDate(2014, 10, 28))
    self.qv_imagery_date_2[self.qv_imagery].setCurrentSection(QtWidgets.QDateTimeEdit.YearSection)
    self.qv_imagery_date_2[self.qv_imagery].setAlignment(QtCore.Qt.AlignCenter)
    self.qv_imagery_date_2[self.qv_imagery].setCalendarPopup(True)
    self.qv_imagery_date_2[self.qv_imagery].setFont(font)
    self.qv_imagery_date_2[self.qv_imagery].setDisplayFormat("yyyy-MM-dd")
    self.qv_imagery_date_2[self.qv_imagery].setStyleSheet("QDateEdit {\n"
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
    self.qv_imagery_date_2[self.qv_imagery].setObjectName("qv_imagery_date_2_" + str(self.qv_imagery))
    self.qv_imagery_gridlay_1[self.qv_imagery].addWidget(self.qv_imagery_date_2[self.qv_imagery])
    self.qv_imagery_verlay_1[self.qv_imagery].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, 
                                                                           QtWidgets.QSizePolicy.Fixed))
    self.qv_imagery_horlay_3.append(QtWidgets.QHBoxLayout())
    self.qv_imagery_horlay_3[self.qv_imagery].setObjectName("qv_imagery_horlay_3_" + str(self.qv_imagery))
    self.qv_imagery_verlay_1[self.qv_imagery].addLayout(self.qv_imagery_horlay_3[self.qv_imagery])
    self.qv_imagery_lab_5.append(QtWidgets.QLabel())
    self.qv_imagery_lab_5[self.qv_imagery].setMinimumSize(QtCore.QSize(0, 27))
    self.qv_imagery_lab_5[self.qv_imagery].setMaximumSize(QtCore.QSize(16777215, 27))
    self.qv_imagery_lab_5[self.qv_imagery].setFont(font2)
    self.qv_imagery_lab_5[self.qv_imagery].setObjectName("qv_imagery_lab_5_" + str(self.qv_imagery))
    self.qv_imagery_lab_5[self.qv_imagery].setText("Acquisition information")
    self.qv_imagery_horlay_3[self.qv_imagery].addWidget(self.qv_imagery_lab_5[self.qv_imagery])
    self.qv_imagery_horlay_3[self.qv_imagery].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, 
                                                                           QtWidgets.QSizePolicy.Minimum))
    self.qv_imagery_horlay_4.append(QtWidgets.QHBoxLayout())
    self.qv_imagery_horlay_4[self.qv_imagery].setObjectName("qv_imagery_horlay_4_" + str(self.qv_imagery))
    self.qv_imagery_horlay_4[self.qv_imagery].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, 
                                                                            QtWidgets.QSizePolicy.Minimum))
    self.qv_imagery_verlay_1[self.qv_imagery].addLayout(self.qv_imagery_horlay_4[self.qv_imagery])
    self.qv_imagery_gridlay_2.append(QtWidgets.QGridLayout())
    self.qv_imagery_gridlay_2[self.qv_imagery].setObjectName("qv_imagery_gridlay_2_" + str(self.qv_imagery))
    self.qv_imagery_horlay_4[self.qv_imagery].addLayout(self.qv_imagery_gridlay_2[self.qv_imagery])
    self.qv_imagery_horlay_4[self.qv_imagery].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, 
                                                                            QtWidgets.QSizePolicy.Minimum))
    self.qv_imagery_lab_6.append(QtWidgets.QLabel())
    self.qv_imagery_lab_6[self.qv_imagery].setMinimumSize(QtCore.QSize(0, 27))
    self.qv_imagery_lab_6[self.qv_imagery].setMaximumSize(QtCore.QSize(16777215, 27))
    self.qv_imagery_lab_6[self.qv_imagery].setFont(font)
    self.qv_imagery_lab_6[self.qv_imagery].setObjectName("qv_imagery_lab_6_" + str(self.qv_imagery))
    self.qv_imagery_lab_6[self.qv_imagery].setText("Number of spectral bands (spectral mode):")
    self.qv_imagery_gridlay_2[self.qv_imagery].addWidget(self.qv_imagery_lab_6[self.qv_imagery], 0, 0, 1, 1)
    self.qv_imagery_horlay_8.append(QtWidgets.QHBoxLayout())
    self.qv_imagery_horlay_8[self.qv_imagery].setObjectName("qv_imagery_horlay_8_" + str(self.qv_imagery))
    self.qv_imagery_gridlay_2[self.qv_imagery].addLayout(self.qv_imagery_horlay_8[self.qv_imagery], 0, 1, 1, 1)
    self.qv_imagery_line_2.append(QtWidgets.QLineEdit())
    self.qv_imagery_line_2[self.qv_imagery].setMinimumSize(QtCore.QSize(100, 27))
    self.qv_imagery_line_2[self.qv_imagery].setMaximumSize(QtCore.QSize(100, 27))
    self.qv_imagery_line_2[self.qv_imagery].setFont(font3)
    self.qv_imagery_line_2[self.qv_imagery].setStyleSheet("QLineEdit {\n"
    "    border-radius: 3px;\n"
    "   padding: 1px 4px 1px 4px;\n"
    "    background-color:  rgb(240, 240, 240);\n"
    "}")
    self.qv_imagery_line_2[self.qv_imagery].setFrame(False)
    self.qv_imagery_line_2[self.qv_imagery].setObjectName("qv_imagery_line_2_" + str(self.qv_imagery))
    self.qv_imagery_horlay_8[self.qv_imagery].addWidget(self.qv_imagery_line_2[self.qv_imagery])
    self.qv_imagery_infBut_2.append(QtWidgets.QToolButton())
    self.qv_imagery_infBut_2[self.qv_imagery].setMaximumSize(QtCore.QSize(27, 27))
    self.qv_imagery_infBut_2[self.qv_imagery].setStyleSheet("QToolButton {\n"
    "    border: 1px solid transparent;\n"
    "    background-color: transparent;\n"
    "    width: 27px;\n"
    "    height: 27px;\n"
    "}\n"
    "QToolButton:flat {\n"
    "    border: none;\n"
    "}")
    self.qv_imagery_infBut_2[self.qv_imagery].setText("")
    self.qv_imagery_infBut_2[self.qv_imagery].setIcon(icon)
    self.qv_imagery_infBut_2[self.qv_imagery].setIconSize(QtCore.QSize(23, 23))
    self.qv_imagery_infBut_2[self.qv_imagery].setAutoRaise(False)
    self.qv_imagery_infBut_2[self.qv_imagery].setObjectName("infoButton_32")
    self.qv_imagery_horlay_8[self.qv_imagery].addWidget(self.qv_imagery_infBut_2[self.qv_imagery])
    self.qv_imagery_horlay_8[self.qv_imagery].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, 
                                                                            QtWidgets.QSizePolicy.Minimum))
    self.qv_imagery_lab_7.append(QtWidgets.QLabel())
    self.qv_imagery_lab_7[self.qv_imagery].setMinimumSize(QtCore.QSize(0, 27))
    self.qv_imagery_lab_7[self.qv_imagery].setMaximumSize(QtCore.QSize(16777215, 27))
    self.qv_imagery_lab_7[self.qv_imagery].setFont(font)
    self.qv_imagery_lab_7[self.qv_imagery].setObjectName("qv_imagery_lab_7_" + str(self.qv_imagery))
    self.qv_imagery_lab_7[self.qv_imagery].setText("Overall heading / flight direction (dd):")
    self.qv_imagery_gridlay_2[self.qv_imagery].addWidget(self.qv_imagery_lab_7[self.qv_imagery], 1, 0, 1, 1)
    self.qv_imagery_line_3.append(QtWidgets.QLineEdit())
    self.qv_imagery_line_3[self.qv_imagery].setMinimumSize(QtCore.QSize(100, 27))
    self.qv_imagery_line_3[self.qv_imagery].setMaximumSize(QtCore.QSize(100, 27))
    self.qv_imagery_line_3[self.qv_imagery].setFont(font3)
    self.qv_imagery_line_3[self.qv_imagery].setStyleSheet("QLineEdit {\n"
    "    border-radius: 3px;\n"
    "   padding: 1px 4px 1px 4px;\n"
    "    background-color:  rgb(240, 240, 240);\n"
    "}")
    self.qv_imagery_line_3[self.qv_imagery].setFrame(False)
    self.qv_imagery_line_3[self.qv_imagery].setObjectName("qv_imagery_line_3_" + str(self.qv_imagery))
    self.qv_imagery_gridlay_2[self.qv_imagery].addWidget(self.qv_imagery_line_3[self.qv_imagery], 1, 1, 1, 1)
    self.qv_imagery_lab_8.append(QtWidgets.QLabel())
    self.qv_imagery_lab_8[self.qv_imagery].setMinimumSize(QtCore.QSize(0, 27))
    self.qv_imagery_lab_8[self.qv_imagery].setMaximumSize(QtCore.QSize(16777215, 27))
    self.qv_imagery_lab_8[self.qv_imagery].setFont(font)
    self.qv_imagery_lab_8[self.qv_imagery].setObjectName("qv_imagery_lab_8_" + str(self.qv_imagery))
    self.qv_imagery_lab_8[self.qv_imagery].setText("Overall altitude / average height ASL (m):")
    self.qv_imagery_gridlay_2[self.qv_imagery].addWidget(self.qv_imagery_lab_8[self.qv_imagery], 2, 0, 1, 1)
    self.qv_imagery_line_4.append(QtWidgets.QLineEdit())
    self.qv_imagery_line_4[self.qv_imagery].setMinimumSize(QtCore.QSize(100, 27))
    self.qv_imagery_line_4[self.qv_imagery].setMaximumSize(QtCore.QSize(100, 27))
    self.qv_imagery_line_4[self.qv_imagery].setFont(font3)
    self.qv_imagery_line_4[self.qv_imagery].setStyleSheet("QLineEdit {\n"
    "    border-radius: 3px;\n"
    "   padding: 1px 4px 1px 4px;\n"
    "    background-color:  rgb(240, 240, 240);\n"
    "}")
    self.qv_imagery_line_4[self.qv_imagery].setFrame(False)
    self.qv_imagery_line_4[self.qv_imagery].setObjectName("qv_imagery_line_4_" + str(self.qv_imagery))
    self.qv_imagery_gridlay_2[self.qv_imagery].addWidget(self.qv_imagery_line_4[self.qv_imagery], 2, 1, 1, 1)
    self.qv_imagery_lab_9.append(QtWidgets.QLabel())
    self.qv_imagery_lab_9[self.qv_imagery].setMinimumSize(QtCore.QSize(0, 27))
    self.qv_imagery_lab_9[self.qv_imagery].setMaximumSize(QtCore.QSize(16777215, 27))
    self.qv_imagery_lab_9[self.qv_imagery].setFont(font)
    self.qv_imagery_lab_9[self.qv_imagery].setObjectName("qv_imagery_lab_9_" + str(self.qv_imagery))
    self.qv_imagery_lab_9[self.qv_imagery].setText("Solar zenith (dd):")
    self.qv_imagery_gridlay_2[self.qv_imagery].addWidget(self.qv_imagery_lab_9[self.qv_imagery], 3, 0, 1, 1)
    self.qv_imagery_line_5.append(QtWidgets.QLineEdit())
    self.qv_imagery_line_5[self.qv_imagery].setMinimumSize(QtCore.QSize(100, 27))
    self.qv_imagery_line_5[self.qv_imagery].setMaximumSize(QtCore.QSize(100, 27))
    self.qv_imagery_line_5[self.qv_imagery].setFont(font3)
    self.qv_imagery_line_5[self.qv_imagery].setStyleSheet("QLineEdit {\n"
    "    border-radius: 3px;\n"
    "   padding: 1px 4px 1px 4px;\n"
    "    background-color:  rgb(240, 240, 240);\n"
    "}")
    self.qv_imagery_line_5[self.qv_imagery].setFrame(False)
    self.qv_imagery_line_5[self.qv_imagery].setObjectName("qv_imagery_line_5_" + str(self.qv_imagery))
    self.qv_imagery_gridlay_2[self.qv_imagery].addWidget(self.qv_imagery_line_5[self.qv_imagery], 3, 1, 1, 1)
    self.qv_imagery_lab_10.append(QtWidgets.QLabel())
    self.qv_imagery_lab_10[self.qv_imagery].setMinimumSize(QtCore.QSize(0, 27))
    self.qv_imagery_lab_10[self.qv_imagery].setMaximumSize(QtCore.QSize(16777215, 27))
    self.qv_imagery_lab_10[self.qv_imagery].setFont(font)
    self.qv_imagery_lab_10[self.qv_imagery].setObjectName("qv_imagery_lab_10_" + str(self.qv_imagery))
    self.qv_imagery_lab_10[self.qv_imagery].setText("Solar azimuth (dd):")
    self.qv_imagery_gridlay_2[self.qv_imagery].addWidget(self.qv_imagery_lab_10[self.qv_imagery], 4, 0, 1, 1)
    self.qv_imagery_line_6.append(QtWidgets.QLineEdit())
    self.qv_imagery_line_6[self.qv_imagery].setMinimumSize(QtCore.QSize(100, 27))
    self.qv_imagery_line_6[self.qv_imagery].setMaximumSize(QtCore.QSize(100, 27))
    self.qv_imagery_line_6[self.qv_imagery].setFont(font3)
    self.qv_imagery_line_6[self.qv_imagery].setStyleSheet("QLineEdit {\n"
    "    border-radius: 3px;\n"
    "   padding: 1px 4px 1px 4px;\n"
    "    background-color:  rgb(240, 240, 240);\n"
    "}")
    self.qv_imagery_line_6[self.qv_imagery].setFrame(False)
    self.qv_imagery_line_6[self.qv_imagery].setObjectName("qv_imagery_line_6_" + str(self.qv_imagery))
    self.qv_imagery_gridlay_2[self.qv_imagery].addWidget(self.qv_imagery_line_6[self.qv_imagery], 4, 1, 1, 1)
    self.qv_imagery_lab_11.append(QtWidgets.QLabel())
    self.qv_imagery_lab_11[self.qv_imagery].setMinimumSize(QtCore.QSize(0, 27))
    self.qv_imagery_lab_11[self.qv_imagery].setMaximumSize(QtCore.QSize(16777215, 27))
    self.qv_imagery_lab_11[self.qv_imagery].setFont(font)
    self.qv_imagery_lab_11[self.qv_imagery].setObjectName("qv_imagery_lab_11_" + str(self.qv_imagery))
    self.qv_imagery_lab_11[self.qv_imagery].setText("Report anomalies in data acquisition:")
    self.qv_imagery_gridlay_2[self.qv_imagery].addWidget(self.qv_imagery_lab_11[self.qv_imagery], 5, 0, 1, 1)
    self.qv_imagery_line_7.append(QtWidgets.QLineEdit())
    self.qv_imagery_line_7[self.qv_imagery].setMinimumSize(QtCore.QSize(450, 27))
    self.qv_imagery_line_7[self.qv_imagery].setMaximumSize(QtCore.QSize(450, 27))
    self.qv_imagery_line_7[self.qv_imagery].setFont(font3)
    self.qv_imagery_line_7[self.qv_imagery].setStyleSheet("QLineEdit {\n"
    "    border-radius: 3px;\n"
    "   padding: 1px 4px 1px 4px;\n"
    "    background-color:  rgb(240, 240, 240);\n"
    "}")
    self.qv_imagery_line_7[self.qv_imagery].setFrame(False)
    self.qv_imagery_line_7[self.qv_imagery].setObjectName("qv_imagery_line_7_" + str(self.qv_imagery))
    self.qv_imagery_gridlay_2[self.qv_imagery].addWidget(self.qv_imagery_line_7[self.qv_imagery], 5, 1, 1, 1)
    self.qv_imagery_verlay_1[self.qv_imagery].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, 
                                                                           QtWidgets.QSizePolicy.Fixed))
    self.qv_imagery_horlay_5.append(QtWidgets.QHBoxLayout())
    self.qv_imagery_horlay_5[self.qv_imagery].setObjectName("qv_imagery_horlay_5_" + str(self.qv_imagery))
    self.qv_imagery_verlay_1[self.qv_imagery].addLayout(self.qv_imagery_horlay_5[self.qv_imagery])
    self.qv_imagery_lab_12.append(QtWidgets.QLabel())
    self.qv_imagery_lab_12[self.qv_imagery].setMinimumSize(QtCore.QSize(0, 27))
    self.qv_imagery_lab_12[self.qv_imagery].setMaximumSize(QtCore.QSize(16777215, 27))
    self.qv_imagery_lab_12[self.qv_imagery].setFont(font2)
    self.qv_imagery_lab_12[self.qv_imagery].setObjectName("qv_imagery_lab_12_" + str(self.qv_imagery))
    self.qv_imagery_lab_12[self.qv_imagery].setText("Processing information")
    self.qv_imagery_horlay_5[self.qv_imagery].addWidget(self.qv_imagery_lab_12[self.qv_imagery])
    self.qv_imagery_horlay_5[self.qv_imagery].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, 
                                                                           QtWidgets.QSizePolicy.Minimum))
    self.qv_imagery_horlay_6.append(QtWidgets.QHBoxLayout())
    self.qv_imagery_horlay_6[self.qv_imagery].setObjectName("qv_imagery_horlay_6_" + str(self.qv_imagery))
    self.qv_imagery_horlay_6[self.qv_imagery].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, 
                                                                           QtWidgets.QSizePolicy.Minimum))
    self.qv_imagery_verlay_1[self.qv_imagery].addLayout(self.qv_imagery_horlay_6[self.qv_imagery])
    self.qv_imagery_gridlay_3.append(QtWidgets.QGridLayout())
    self.qv_imagery_gridlay_3[self.qv_imagery].setObjectName("qv_imagery_gridlay_3_" + str(self.qv_imagery))
    self.qv_imagery_horlay_6[self.qv_imagery].addLayout(self.qv_imagery_gridlay_3[self.qv_imagery])
    self.qv_imagery_horlay_6[self.qv_imagery].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, 
                                                                            QtWidgets.QSizePolicy.Minimum))
    self.qv_imagery_lab_13.append(QtWidgets.QLabel())
    self.qv_imagery_lab_13[self.qv_imagery].setMinimumSize(QtCore.QSize(0, 27))
    self.qv_imagery_lab_13[self.qv_imagery].setMaximumSize(QtCore.QSize(16777215, 27))
    self.qv_imagery_lab_13[self.qv_imagery].setFont(font)
    self.qv_imagery_lab_13[self.qv_imagery].setObjectName("qv_imagery_lab_13_" + str(self.qv_imagery))
    self.qv_imagery_lab_13[self.qv_imagery].setText("Processing level:")
    self.qv_imagery_gridlay_3[self.qv_imagery].addWidget(self.qv_imagery_lab_13[self.qv_imagery], 0, 0, 1, 1)
    self.qv_imagery_list_1.append(QtWidgets.QComboBox())
    self.qv_imagery_list_1[self.qv_imagery].setMinimumSize(QtCore.QSize(140, 27))
    self.qv_imagery_list_1[self.qv_imagery].setMaximumSize(QtCore.QSize(180, 27))
    self.qv_imagery_list_1[self.qv_imagery].setFont(font3)
    self.qv_imagery_list_1[self.qv_imagery].setStyleSheet("QComboBox {\n"
    "    border: 1px solid #acacac;\n"
    "    border-radius: 1px;\n"
    "    padding-left: 5px;\n"
    "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
    "stop: 0 #f0f0f0, stop: 1 #e5e5e5);\n"
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
    "stop: 0 #ecf4fc, stop: 1 #dcecfc);\n"
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
    self.qv_imagery_list_1[self.qv_imagery].setFrame(False)
    self.qv_imagery_list_1[self.qv_imagery].setObjectName("qv_imagery_list_1_" + str(self.qv_imagery))
    self.qv_imagery_list_1[self.qv_imagery].addItem("Make a choice...")
    self.qv_imagery_list_1[self.qv_imagery].addItem("Level 1")
    self.qv_imagery_list_1[self.qv_imagery].addItem("Level 2 geo")
    self.qv_imagery_list_1[self.qv_imagery].addItem("Level 2 atm")
    self.qv_imagery_list_1[self.qv_imagery].addItem("Level 2")
    self.qv_imagery_gridlay_3[self.qv_imagery].addWidget(self.qv_imagery_list_1[self.qv_imagery], 0, 1, 1, 1)
    self.qv_imagery_lab_14.append(QtWidgets.QLabel())
    self.qv_imagery_lab_14[self.qv_imagery].setMinimumSize(QtCore.QSize(0, 27))
    self.qv_imagery_lab_14[self.qv_imagery].setMaximumSize(QtCore.QSize(16777215, 27))
    self.qv_imagery_lab_14[self.qv_imagery].setFont(font)
    self.qv_imagery_lab_14[self.qv_imagery].setObjectName("qv_imagery_lab_14_" + str(self.qv_imagery))
    self.qv_imagery_lab_14[self.qv_imagery].setText("Dark current (DC) correction ?")
    self.qv_imagery_gridlay_3[self.qv_imagery].addWidget(self.qv_imagery_lab_14[self.qv_imagery], 1, 0, 1, 1)
    self.qv_imagery_horlay_7.append(QtWidgets.QHBoxLayout())
    self.qv_imagery_horlay_7[self.qv_imagery].setObjectName("qv_imagery_horlay_7_" + str(self.qv_imagery))
    self.qv_imagery_gridlay_3[self.qv_imagery].addLayout(self.qv_imagery_horlay_7[self.qv_imagery], 1, 1, 1, 1)
    self.qv_imagery_check_1.append(QtWidgets.QRadioButton())
    self.qv_imagery_check_1[self.qv_imagery].setMinimumSize(QtCore.QSize(0, 27))
    self.qv_imagery_check_1[self.qv_imagery].setMaximumSize(QtCore.QSize(16777215, 27))
    self.qv_imagery_check_1[self.qv_imagery].setFont(font)
    self.qv_imagery_check_1[self.qv_imagery].setObjectName("qv_imagery_check_1_" + str(self.qv_imagery))
    self.qv_imagery_check_1[self.qv_imagery].setText("Yes")
    self.qv_imagery_horlay_7[self.qv_imagery].addWidget(self.qv_imagery_check_1[self.qv_imagery])
    self.qv_imagery_check_2.append(QtWidgets.QRadioButton())
    self.qv_imagery_check_2[self.qv_imagery].setMinimumSize(QtCore.QSize(0, 27))
    self.qv_imagery_check_2[self.qv_imagery].setMaximumSize(QtCore.QSize(16777215, 27))
    self.qv_imagery_check_2[self.qv_imagery].setFont(font)
    self.qv_imagery_check_2[self.qv_imagery].setObjectName("qv_imagery_check_2_" + str(self.qv_imagery))
    self.qv_imagery_check_2[self.qv_imagery].setText("No")
    self.qv_imagery_horlay_7[self.qv_imagery].addWidget(self.qv_imagery_check_2[self.qv_imagery])
    self.qv_imagery_group_1.append(QtWidgets.QButtonGroup())
    self.qv_imagery_group_1[self.qv_imagery].setObjectName("qv_imagery_group_1_" + str(self.qv_imagery))
    self.qv_imagery_group_1[self.qv_imagery].addButton(self.qv_imagery_check_1[self.qv_imagery])
    self.qv_imagery_group_1[self.qv_imagery].addButton(self.qv_imagery_check_2[self.qv_imagery])
    self.qv_imagery_infBut_3.append(QtWidgets.QToolButton())
    self.qv_imagery_infBut_3[self.qv_imagery].setMaximumSize(QtCore.QSize(27, 27))
    self.qv_imagery_infBut_3[self.qv_imagery].setStyleSheet("QToolButton {\n"
    "    border: 1px solid transparent;\n"
    "    background-color: transparent;\n"
    "    width: 27px;\n"
    "    height: 27px;\n"
    "}\n"
    "QToolButton:flat {\n"
    "    border: none;\n"
    "}")
    self.qv_imagery_infBut_3[self.qv_imagery].setText("")
    self.qv_imagery_infBut_3[self.qv_imagery].setIcon(icon)
    self.qv_imagery_infBut_3[self.qv_imagery].setIconSize(QtCore.QSize(23, 23))
    self.qv_imagery_infBut_3[self.qv_imagery].setAutoRaise(False)
    self.qv_imagery_infBut_3[self.qv_imagery].setObjectName("infoButton_33")
    self.qv_imagery_horlay_7[self.qv_imagery].addWidget(self.qv_imagery_infBut_3[self.qv_imagery])
    self.qv_imagery_verlay_1[self.qv_imagery].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, 
                                                                           QtWidgets.QSizePolicy.Fixed))
    self.qv_imagery_horlay_9.append(QtWidgets.QHBoxLayout())
    self.qv_imagery_horlay_9[self.qv_imagery].setObjectName("qv_imagery_horlay_9_" + str(self.qv_imagery))
    self.qv_imagery_verlay_1[self.qv_imagery].addLayout(self.qv_imagery_horlay_9[self.qv_imagery])
    self.qv_imagery_lab_15.append(QtWidgets.QLabel())
    self.qv_imagery_lab_15[self.qv_imagery].setMinimumSize(QtCore.QSize(0, 27))
    self.qv_imagery_lab_15[self.qv_imagery].setMaximumSize(QtCore.QSize(16777215, 27))
    self.qv_imagery_lab_15[self.qv_imagery].setFont(font2)
    self.qv_imagery_lab_15[self.qv_imagery].setObjectName("qv_imagery_lab_15_" + str(self.qv_imagery))
    self.qv_imagery_lab_15[self.qv_imagery].setText("Data Quality Layers")
    self.qv_imagery_horlay_9[self.qv_imagery].addWidget(self.qv_imagery_lab_15[self.qv_imagery])
    self.qv_imagery_infBut_4.append(QtWidgets.QToolButton())
    self.qv_imagery_infBut_4[self.qv_imagery].setMaximumSize(QtCore.QSize(27, 27))
    self.qv_imagery_infBut_4[self.qv_imagery].setStyleSheet("QToolButton {\n"
    "    border: 1px solid transparent;\n"
    "    background-color: transparent;\n"
    "    width: 27px;\n"
    "    height: 27px;\n"
    "}\n"
    "QToolButton:flat {\n"
    "    border: none;\n"
    "}")
    self.qv_imagery_infBut_4[self.qv_imagery].setText("")
    self.qv_imagery_infBut_4[self.qv_imagery].setIcon(icon)
    self.qv_imagery_infBut_4[self.qv_imagery].setIconSize(QtCore.QSize(23, 23))
    self.qv_imagery_infBut_4[self.qv_imagery].setAutoRaise(False)
    self.qv_imagery_infBut_4[self.qv_imagery].setObjectName("infoButton_34")
    self.qv_imagery_horlay_9[self.qv_imagery].addWidget(self.qv_imagery_infBut_4[self.qv_imagery])
    self.qv_imagery_horlay_9[self.qv_imagery].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, 
                                                                           QtWidgets.QSizePolicy.Minimum))
    self.qv_imagery_horlay_10.append(QtWidgets.QHBoxLayout())
    self.qv_imagery_horlay_10[self.qv_imagery].setObjectName("qv_imagery_horlay_10_" + str(self.qv_imagery))
    self.qv_imagery_horlay_10[self.qv_imagery].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, 
                                                                           QtWidgets.QSizePolicy.Minimum))
    self.qv_imagery_verlay_1[self.qv_imagery].addLayout(self.qv_imagery_horlay_10[self.qv_imagery])
    self.qv_imagery_lab_16.append(QtWidgets.QLabel())
    self.qv_imagery_lab_16[self.qv_imagery].setMinimumSize(QtCore.QSize(0, 27))
    self.qv_imagery_lab_16[self.qv_imagery].setMaximumSize(QtCore.QSize(16777215, 27))
    self.qv_imagery_lab_16[self.qv_imagery].setFont(font4)
    self.qv_imagery_lab_16[self.qv_imagery].setObjectName("qv_imagery_lab_16_" + str(self.qv_imagery))
    self.qv_imagery_lab_16[self.qv_imagery].setText("Sensor calibration and system correction:")
    self.qv_imagery_horlay_10[self.qv_imagery].addWidget(self.qv_imagery_lab_16[self.qv_imagery])
    self.qv_imagery_horlay_10[self.qv_imagery].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, 
                                                                           QtWidgets.QSizePolicy.Minimum))
    self.qv_imagery_horlay_11.append(QtWidgets.QHBoxLayout())
    self.qv_imagery_horlay_11[self.qv_imagery].setObjectName("qv_imagery_horlay_11_" + str(self.qv_imagery))
    self.qv_imagery_horlay_11[self.qv_imagery].addItem(QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, 
                                                                           QtWidgets.QSizePolicy.Minimum))
    self.qv_imagery_verlay_1[self.qv_imagery].addLayout(self.qv_imagery_horlay_11[self.qv_imagery])
    self.qv_imagery_gridlay_4.append(QtWidgets.QGridLayout())
    self.qv_imagery_gridlay_4[self.qv_imagery].setObjectName("qv_imagery_gridlay_4_" + str(self.qv_imagery))
    self.qv_imagery_horlay_11[self.qv_imagery].addLayout(self.qv_imagery_gridlay_4[self.qv_imagery])
    self.qv_imagery_horlay_11[self.qv_imagery].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, 
                                                                            QtWidgets.QSizePolicy.Minimum))
    self.qv_imagery_lab_17.append(QtWidgets.QLabel())
    self.qv_imagery_lab_17[self.qv_imagery].setMinimumSize(QtCore.QSize(0, 27))
    self.qv_imagery_lab_17[self.qv_imagery].setMaximumSize(QtCore.QSize(16777215, 27))
    self.qv_imagery_lab_17[self.qv_imagery].setFont(font)
    self.qv_imagery_lab_17[self.qv_imagery].setObjectName("qv_imagery_lab_17_" + str(self.qv_imagery))
    self.qv_imagery_lab_17[self.qv_imagery].setText("Aggregated interpolated pixel mask ('corrected pixels') ?")
    self.qv_imagery_gridlay_4[self.qv_imagery].addWidget(self.qv_imagery_lab_17[self.qv_imagery], 0, 0, 1, 1)
    self.qv_imagery_lab_18.append(QtWidgets.QLabel())
    self.qv_imagery_lab_18[self.qv_imagery].setMinimumSize(QtCore.QSize(0, 27))
    self.qv_imagery_lab_18[self.qv_imagery].setMaximumSize(QtCore.QSize(16777215, 27))
    self.qv_imagery_lab_18[self.qv_imagery].setFont(font)
    self.qv_imagery_lab_18[self.qv_imagery].setObjectName("qv_imagery_lab_18_" + str(self.qv_imagery))
    self.qv_imagery_lab_18[self.qv_imagery].setText("Aggregated bad pixel mask ('not corrected pixels') ?")
    self.qv_imagery_gridlay_4[self.qv_imagery].addWidget(self.qv_imagery_lab_18[self.qv_imagery], 1, 0, 1, 1)
    self.qv_imagery_horlay_12.append(QtWidgets.QHBoxLayout())
    self.qv_imagery_horlay_12[self.qv_imagery].setObjectName("qv_imagery_horlay_12_" + str(self.qv_imagery))
    self.qv_imagery_gridlay_4[self.qv_imagery].addLayout(self.qv_imagery_horlay_12[self.qv_imagery], 0, 1, 1, 1)
    self.qv_imagery_check_3.append(QtWidgets.QRadioButton())
    self.qv_imagery_check_3[self.qv_imagery].setMinimumSize(QtCore.QSize(0, 27))
    self.qv_imagery_check_3[self.qv_imagery].setMaximumSize(QtCore.QSize(16777215, 27))
    self.qv_imagery_check_3[self.qv_imagery].setFont(font)
    self.qv_imagery_check_3[self.qv_imagery].setObjectName("qv_imagery_check_3_" + str(self.qv_imagery))
    self.qv_imagery_check_3[self.qv_imagery].setText("Yes")
    self.qv_imagery_horlay_12[self.qv_imagery].addWidget(self.qv_imagery_check_3[self.qv_imagery])
    self.qv_imagery_check_4.append(QtWidgets.QRadioButton())
    self.qv_imagery_check_4[self.qv_imagery].setMinimumSize(QtCore.QSize(0, 27))
    self.qv_imagery_check_4[self.qv_imagery].setMaximumSize(QtCore.QSize(16777215, 27))
    self.qv_imagery_check_4[self.qv_imagery].setFont(font)
    self.qv_imagery_check_4[self.qv_imagery].setObjectName("qv_imagery_check_4_" + str(self.qv_imagery))
    self.qv_imagery_check_4[self.qv_imagery].setText("No")
    self.qv_imagery_horlay_12[self.qv_imagery].addWidget(self.qv_imagery_check_4[self.qv_imagery])
    self.qv_imagery_group_2.append(QtWidgets.QButtonGroup())
    self.qv_imagery_group_2[self.qv_imagery].setObjectName("qv_imagery_group_2_" + str(self.qv_imagery))
    self.qv_imagery_group_2[self.qv_imagery].addButton(self.qv_imagery_check_3[self.qv_imagery])
    self.qv_imagery_group_2[self.qv_imagery].addButton(self.qv_imagery_check_4[self.qv_imagery])
    self.qv_imagery_infBut_5.append(QtWidgets.QToolButton())
    self.qv_imagery_infBut_5[self.qv_imagery].setMaximumSize(QtCore.QSize(27, 27))
    self.qv_imagery_infBut_5[self.qv_imagery].setStyleSheet("QToolButton {\n"
    "    border: 1px solid transparent;\n"
    "    background-color: transparent;\n"
    "    width: 27px;\n"
    "    height: 27px;\n"
    "}\n"
    "QToolButton:flat {\n"
    "    border: none;\n"
    "}")
    self.qv_imagery_infBut_5[self.qv_imagery].setText("")
    self.qv_imagery_infBut_5[self.qv_imagery].setIcon(icon)
    self.qv_imagery_infBut_5[self.qv_imagery].setIconSize(QtCore.QSize(23, 23))
    self.qv_imagery_infBut_5[self.qv_imagery].setAutoRaise(False)
    self.qv_imagery_infBut_5[self.qv_imagery].setObjectName("infoButton_35")
    self.qv_imagery_horlay_12[self.qv_imagery].addWidget(self.qv_imagery_infBut_5[self.qv_imagery])
    self.qv_imagery_horlay_13.append(QtWidgets.QHBoxLayout())
    self.qv_imagery_horlay_13[self.qv_imagery].setObjectName("qv_imagery_horlay_13_" + str(self.qv_imagery))
    self.qv_imagery_gridlay_4[self.qv_imagery].addLayout(self.qv_imagery_horlay_13[self.qv_imagery], 1, 1, 1, 1)
    self.qv_imagery_check_5.append(QtWidgets.QRadioButton())
    self.qv_imagery_check_5[self.qv_imagery].setMinimumSize(QtCore.QSize(0, 27))
    self.qv_imagery_check_5[self.qv_imagery].setMaximumSize(QtCore.QSize(16777215, 27))
    self.qv_imagery_check_5[self.qv_imagery].setFont(font)
    self.qv_imagery_check_5[self.qv_imagery].setObjectName("qv_imagery_check_5_" + str(self.qv_imagery))
    self.qv_imagery_check_5[self.qv_imagery].setText("Yes")
    self.qv_imagery_horlay_13[self.qv_imagery].addWidget(self.qv_imagery_check_5[self.qv_imagery])
    self.qv_imagery_check_6.append(QtWidgets.QRadioButton())
    self.qv_imagery_check_6[self.qv_imagery].setMinimumSize(QtCore.QSize(0, 27))
    self.qv_imagery_check_6[self.qv_imagery].setMaximumSize(QtCore.QSize(16777215, 27))
    self.qv_imagery_check_6[self.qv_imagery].setFont(font)
    self.qv_imagery_check_6[self.qv_imagery].setObjectName("qv_imagery_check_6_" + str(self.qv_imagery))
    self.qv_imagery_check_6[self.qv_imagery].setText("No")
    self.qv_imagery_horlay_13[self.qv_imagery].addWidget(self.qv_imagery_check_6[self.qv_imagery])
    self.qv_imagery_group_3.append(QtWidgets.QButtonGroup())
    self.qv_imagery_group_3[self.qv_imagery].setObjectName("qv_imagery_group_3_" + str(self.qv_imagery))
    self.qv_imagery_group_3[self.qv_imagery].addButton(self.qv_imagery_check_5[self.qv_imagery])
    self.qv_imagery_group_3[self.qv_imagery].addButton(self.qv_imagery_check_6[self.qv_imagery])
    self.qv_imagery_infBut_6.append(QtWidgets.QToolButton())
    self.qv_imagery_infBut_6[self.qv_imagery].setMaximumSize(QtCore.QSize(27, 27))
    self.qv_imagery_infBut_6[self.qv_imagery].setStyleSheet("QToolButton {\n"
    "    border: 1px solid transparent;\n"
    "    background-color: transparent;\n"
    "    width: 27px;\n"
    "    height: 27px;\n"
    "}\n"
    "QToolButton:flat {\n"
    "    border: none;\n"
    "}")
    self.qv_imagery_infBut_6[self.qv_imagery].setText("")
    self.qv_imagery_infBut_6[self.qv_imagery].setIcon(icon)
    self.qv_imagery_infBut_6[self.qv_imagery].setIconSize(QtCore.QSize(23, 23))
    self.qv_imagery_infBut_6[self.qv_imagery].setAutoRaise(False)
    self.qv_imagery_infBut_6[self.qv_imagery].setObjectName("infoButton_36")
    self.qv_imagery_horlay_13[self.qv_imagery].addWidget(self.qv_imagery_infBut_6[self.qv_imagery])
    self.qv_imagery_horlay_14.append(QtWidgets.QHBoxLayout())
    self.qv_imagery_horlay_14[self.qv_imagery].setObjectName("qv_imagery_horlay_14_" + str(self.qv_imagery))
    self.qv_imagery_horlay_14[self.qv_imagery].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, 
                                                                           QtWidgets.QSizePolicy.Minimum))
    self.qv_imagery_verlay_1[self.qv_imagery].addLayout(self.qv_imagery_horlay_14[self.qv_imagery])
    self.qv_imagery_lab_19.append(QtWidgets.QLabel())
    self.qv_imagery_lab_19[self.qv_imagery].setMinimumSize(QtCore.QSize(0, 27))
    self.qv_imagery_lab_19[self.qv_imagery].setMaximumSize(QtCore.QSize(16777215, 27))
    self.qv_imagery_lab_19[self.qv_imagery].setFont(font4)
    self.qv_imagery_lab_19[self.qv_imagery].setObjectName("qv_imagery_lab_19_" + str(self.qv_imagery))
    self.qv_imagery_lab_19[self.qv_imagery].setText("Image data artefacts and processing errors:")
    self.qv_imagery_horlay_14[self.qv_imagery].addWidget(self.qv_imagery_lab_19[self.qv_imagery])
    self.qv_imagery_horlay_14[self.qv_imagery].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, 
                                                                           QtWidgets.QSizePolicy.Minimum))
    self.qv_imagery_horlay_15.append(QtWidgets.QHBoxLayout())
    self.qv_imagery_horlay_15[self.qv_imagery].setObjectName("qv_imagery_horlay_15_" + str(self.qv_imagery))
    self.qv_imagery_horlay_15[self.qv_imagery].addItem(QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, 
                                                                           QtWidgets.QSizePolicy.Minimum))
    self.qv_imagery_verlay_1[self.qv_imagery].addLayout(self.qv_imagery_horlay_15[self.qv_imagery])
    self.qv_imagery_gridlay_5.append(QtWidgets.QGridLayout())
    self.qv_imagery_gridlay_5[self.qv_imagery].setObjectName("qv_imagery_gridlay_5_" + str(self.qv_imagery))
    self.qv_imagery_horlay_15[self.qv_imagery].addLayout(self.qv_imagery_gridlay_5[self.qv_imagery])
    self.qv_imagery_horlay_15[self.qv_imagery].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, 
                                                                            QtWidgets.QSizePolicy.Minimum))
    self.qv_imagery_lab_20.append(QtWidgets.QLabel())
    self.qv_imagery_lab_20[self.qv_imagery].setMinimumSize(QtCore.QSize(0, 27))
    self.qv_imagery_lab_20[self.qv_imagery].setMaximumSize(QtCore.QSize(16777215, 27))
    self.qv_imagery_lab_20[self.qv_imagery].setFont(font)
    self.qv_imagery_lab_20[self.qv_imagery].setObjectName("qv_imagery_lab_20_" + str(self.qv_imagery))
    self.qv_imagery_lab_20[self.qv_imagery].setText("Saturated pixels / overflow ?")
    self.qv_imagery_gridlay_5[self.qv_imagery].addWidget(self.qv_imagery_lab_20[self.qv_imagery], 0, 0, 1, 1)
    self.qv_imagery_lab_21.append(QtWidgets.QLabel())
    self.qv_imagery_lab_21[self.qv_imagery].setMinimumSize(QtCore.QSize(0, 27))
    self.qv_imagery_lab_21[self.qv_imagery].setMaximumSize(QtCore.QSize(16777215, 27))
    self.qv_imagery_lab_21[self.qv_imagery].setFont(font)
    self.qv_imagery_lab_21[self.qv_imagery].setObjectName("qv_imagery_lab_21_" + str(self.qv_imagery))
    self.qv_imagery_lab_21[self.qv_imagery].setText("Pixels affected by saturation in spatial/spectral neighbourhood ?")
    self.qv_imagery_gridlay_5[self.qv_imagery].addWidget(self.qv_imagery_lab_21[self.qv_imagery], 1, 0, 1, 1)
    self.qv_imagery_horlay_16.append(QtWidgets.QHBoxLayout())
    self.qv_imagery_horlay_16[self.qv_imagery].setObjectName("qv_imagery_horlay_16_" + str(self.qv_imagery))
    self.qv_imagery_gridlay_5[self.qv_imagery].addLayout(self.qv_imagery_horlay_16[self.qv_imagery], 0, 1, 1, 1)
    self.qv_imagery_check_7.append(QtWidgets.QRadioButton())
    self.qv_imagery_check_7[self.qv_imagery].setMinimumSize(QtCore.QSize(0, 27))
    self.qv_imagery_check_7[self.qv_imagery].setMaximumSize(QtCore.QSize(16777215, 27))
    self.qv_imagery_check_7[self.qv_imagery].setFont(font)
    self.qv_imagery_check_7[self.qv_imagery].setObjectName("qv_imagery_check_7_" + str(self.qv_imagery))
    self.qv_imagery_check_7[self.qv_imagery].setText("Yes")
    self.qv_imagery_horlay_16[self.qv_imagery].addWidget(self.qv_imagery_check_7[self.qv_imagery])
    self.qv_imagery_check_8.append(QtWidgets.QRadioButton())
    self.qv_imagery_check_8[self.qv_imagery].setMinimumSize(QtCore.QSize(0, 27))
    self.qv_imagery_check_8[self.qv_imagery].setMaximumSize(QtCore.QSize(16777215, 27))
    self.qv_imagery_check_8[self.qv_imagery].setFont(font)
    self.qv_imagery_check_8[self.qv_imagery].setObjectName("qv_imagery_check_8_" + str(self.qv_imagery))
    self.qv_imagery_check_8[self.qv_imagery].setText("No")
    self.qv_imagery_horlay_16[self.qv_imagery].addWidget(self.qv_imagery_check_8[self.qv_imagery])
    self.qv_imagery_group_4.append(QtWidgets.QButtonGroup())
    self.qv_imagery_group_4[self.qv_imagery].setObjectName("qv_imagery_group_4_" + str(self.qv_imagery))
    self.qv_imagery_group_4[self.qv_imagery].addButton(self.qv_imagery_check_7[self.qv_imagery])
    self.qv_imagery_group_4[self.qv_imagery].addButton(self.qv_imagery_check_8[self.qv_imagery])
    self.qv_imagery_infBut_7.append(QtWidgets.QToolButton())
    self.qv_imagery_infBut_7[self.qv_imagery].setMaximumSize(QtCore.QSize(27, 27))
    self.qv_imagery_infBut_7[self.qv_imagery].setStyleSheet("QToolButton {\n"
    "    border: 1px solid transparent;\n"
    "    background-color: transparent;\n"
    "    width: 27px;\n"
    "    height: 27px;\n"
    "}\n"
    "QToolButton:flat {\n"
    "    border: none;\n"
    "}")
    self.qv_imagery_infBut_7[self.qv_imagery].setText("")
    self.qv_imagery_infBut_7[self.qv_imagery].setIcon(icon)
    self.qv_imagery_infBut_7[self.qv_imagery].setIconSize(QtCore.QSize(23, 23))
    self.qv_imagery_infBut_7[self.qv_imagery].setAutoRaise(False)
    self.qv_imagery_infBut_7[self.qv_imagery].setObjectName("infoButton_37")
    self.qv_imagery_horlay_16[self.qv_imagery].addWidget(self.qv_imagery_infBut_7[self.qv_imagery])
    self.qv_imagery_horlay_17.append(QtWidgets.QHBoxLayout())
    self.qv_imagery_horlay_17[self.qv_imagery].setObjectName("qv_imagery_horlay_17_" + str(self.qv_imagery))
    self.qv_imagery_gridlay_5[self.qv_imagery].addLayout(self.qv_imagery_horlay_17[self.qv_imagery], 1, 1, 1, 1)
    self.qv_imagery_check_9.append(QtWidgets.QRadioButton())
    self.qv_imagery_check_9[self.qv_imagery].setMinimumSize(QtCore.QSize(0, 27))
    self.qv_imagery_check_9[self.qv_imagery].setMaximumSize(QtCore.QSize(16777215, 27))
    self.qv_imagery_check_9[self.qv_imagery].setFont(font)
    self.qv_imagery_check_9[self.qv_imagery].setObjectName("qv_imagery_check_9_" + str(self.qv_imagery))
    self.qv_imagery_check_9[self.qv_imagery].setText("Yes")
    self.qv_imagery_horlay_17[self.qv_imagery].addWidget(self.qv_imagery_check_9[self.qv_imagery])
    self.qv_imagery_check_10.append(QtWidgets.QRadioButton())
    self.qv_imagery_check_10[self.qv_imagery].setMinimumSize(QtCore.QSize(0, 27))
    self.qv_imagery_check_10[self.qv_imagery].setMaximumSize(QtCore.QSize(16777215, 27))
    self.qv_imagery_check_10[self.qv_imagery].setFont(font)
    self.qv_imagery_check_10[self.qv_imagery].setObjectName("qv_imagery_check_10_" + str(self.qv_imagery))
    self.qv_imagery_check_10[self.qv_imagery].setText("No")
    self.qv_imagery_horlay_17[self.qv_imagery].addWidget(self.qv_imagery_check_10[self.qv_imagery])
    self.qv_imagery_group_5.append(QtWidgets.QButtonGroup())
    self.qv_imagery_group_5[self.qv_imagery].setObjectName("qv_imagery_group_5_" + str(self.qv_imagery))
    self.qv_imagery_group_5[self.qv_imagery].addButton(self.qv_imagery_check_9[self.qv_imagery])
    self.qv_imagery_group_5[self.qv_imagery].addButton(self.qv_imagery_check_10[self.qv_imagery])
    self.qv_imagery_infBut_8.append(QtWidgets.QToolButton())
    self.qv_imagery_infBut_8[self.qv_imagery].setMaximumSize(QtCore.QSize(27, 27))
    self.qv_imagery_infBut_8[self.qv_imagery].setStyleSheet("QToolButton {\n"
    "    border: 1px solid transparent;\n"
    "    background-color: transparent;\n"
    "    width: 27px;\n"
    "    height: 27px;\n"
    "}\n"
    "QToolButton:flat {\n"
    "    border: none;\n"
    "}")
    self.qv_imagery_infBut_8[self.qv_imagery].setText("")
    self.qv_imagery_infBut_8[self.qv_imagery].setIcon(icon)
    self.qv_imagery_infBut_8[self.qv_imagery].setIconSize(QtCore.QSize(23, 23))
    self.qv_imagery_infBut_8[self.qv_imagery].setAutoRaise(False)
    self.qv_imagery_infBut_8[self.qv_imagery].setObjectName("infoButton_38")
    self.qv_imagery_horlay_17[self.qv_imagery].addWidget(self.qv_imagery_infBut_8[self.qv_imagery])
    self.qv_imagery_horlay_18.append(QtWidgets.QHBoxLayout())
    self.qv_imagery_horlay_18[self.qv_imagery].setObjectName("qv_imagery_horlay_18_" + str(self.qv_imagery))
    self.qv_imagery_horlay_18[self.qv_imagery].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, 
                                                                           QtWidgets.QSizePolicy.Minimum))
    self.qv_imagery_verlay_1[self.qv_imagery].addLayout(self.qv_imagery_horlay_18[self.qv_imagery])
    self.qv_imagery_lab_22.append(QtWidgets.QLabel())
    self.qv_imagery_lab_22[self.qv_imagery].setMinimumSize(QtCore.QSize(0, 27))
    self.qv_imagery_lab_22[self.qv_imagery].setMaximumSize(QtCore.QSize(16777215, 27))
    self.qv_imagery_lab_22[self.qv_imagery].setFont(font4)
    self.qv_imagery_lab_22[self.qv_imagery].setObjectName("qv_imagery_lab_22_" + str(self.qv_imagery))
    self.qv_imagery_lab_22[self.qv_imagery].setText("GPS/IMU related errors, geometric correction:")
    self.qv_imagery_horlay_18[self.qv_imagery].addWidget(self.qv_imagery_lab_22[self.qv_imagery])
    self.qv_imagery_infBut_9.append(QtWidgets.QToolButton())
    self.qv_imagery_infBut_9[self.qv_imagery].setMaximumSize(QtCore.QSize(27, 27))
    self.qv_imagery_infBut_9[self.qv_imagery].setStyleSheet("QToolButton {\n"
    "    border: 1px solid transparent;\n"
    "    background-color: transparent;\n"
    "    width: 27px;\n"
    "    height: 27px;\n"
    "}\n"
    "QToolButton:flat {\n"
    "    border: none;\n"
    "}")
    self.qv_imagery_infBut_9[self.qv_imagery].setText("")
    self.qv_imagery_infBut_9[self.qv_imagery].setIcon(icon)
    self.qv_imagery_infBut_9[self.qv_imagery].setIconSize(QtCore.QSize(23, 23))
    self.qv_imagery_infBut_9[self.qv_imagery].setAutoRaise(False)
    self.qv_imagery_infBut_9[self.qv_imagery].setObjectName("infoButton_39")
    self.qv_imagery_horlay_18[self.qv_imagery].addWidget(self.qv_imagery_infBut_9[self.qv_imagery])
    self.qv_imagery_horlay_18[self.qv_imagery].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, 
                                                                           QtWidgets.QSizePolicy.Minimum))
    self.qv_imagery_horlay_19.append(QtWidgets.QHBoxLayout())
    self.qv_imagery_horlay_19[self.qv_imagery].setObjectName("qv_imagery_horlay_19_" + str(self.qv_imagery))
    self.qv_imagery_horlay_19[self.qv_imagery].addItem(QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, 
                                                                           QtWidgets.QSizePolicy.Minimum))
    self.qv_imagery_verlay_1[self.qv_imagery].addLayout(self.qv_imagery_horlay_19[self.qv_imagery])
    self.qv_imagery_gridlay_6.append(QtWidgets.QGridLayout())
    self.qv_imagery_gridlay_6[self.qv_imagery].setObjectName("qv_imagery_gridlay_6_" + str(self.qv_imagery))
    self.qv_imagery_horlay_19[self.qv_imagery].addLayout(self.qv_imagery_gridlay_6[self.qv_imagery])
    self.qv_imagery_horlay_19[self.qv_imagery].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, 
                                                                            QtWidgets.QSizePolicy.Minimum))
    self.qv_imagery_lab_23.append(QtWidgets.QLabel())
    self.qv_imagery_lab_23[self.qv_imagery].setMinimumSize(QtCore.QSize(0, 27))
    self.qv_imagery_lab_23[self.qv_imagery].setMaximumSize(QtCore.QSize(16777215, 27))
    self.qv_imagery_lab_23[self.qv_imagery].setFont(font)
    self.qv_imagery_lab_23[self.qv_imagery].setObjectName("qv_imagery_lab_23_" + str(self.qv_imagery))
    self.qv_imagery_lab_23[self.qv_imagery].setText("Problems with position information / Interpolated position information ?")
    self.qv_imagery_gridlay_6[self.qv_imagery].addWidget(self.qv_imagery_lab_23[self.qv_imagery], 0, 0, 1, 1)
    self.qv_imagery_lab_24.append(QtWidgets.QLabel())
    self.qv_imagery_lab_24[self.qv_imagery].setMinimumSize(QtCore.QSize(0, 27))
    self.qv_imagery_lab_24[self.qv_imagery].setMaximumSize(QtCore.QSize(16777215, 27))
    self.qv_imagery_lab_24[self.qv_imagery].setFont(font)
    self.qv_imagery_lab_24[self.qv_imagery].setObjectName("qv_imagery_lab_24_" + str(self.qv_imagery))
    self.qv_imagery_lab_24[self.qv_imagery].setText("Problems with attitude information / Interpolated attitude information ?")
    self.qv_imagery_gridlay_6[self.qv_imagery].addWidget(self.qv_imagery_lab_24[self.qv_imagery], 1, 0, 1, 1)
    self.qv_imagery_lab_25.append(QtWidgets.QLabel())
    self.qv_imagery_lab_25[self.qv_imagery].setMinimumSize(QtCore.QSize(0, 27))
    self.qv_imagery_lab_25[self.qv_imagery].setMaximumSize(QtCore.QSize(16777215, 27))
    self.qv_imagery_lab_25[self.qv_imagery].setFont(font)
    self.qv_imagery_lab_25[self.qv_imagery].setObjectName("qv_imagery_lab_25_" + str(self.qv_imagery))
    self.qv_imagery_lab_25[self.qv_imagery].setText("Synchronization problems ?")
    self.qv_imagery_gridlay_6[self.qv_imagery].addWidget(self.qv_imagery_lab_25[self.qv_imagery], 2, 0, 1, 1)
    self.qv_imagery_lab_26.append(QtWidgets.QLabel())
    self.qv_imagery_lab_26[self.qv_imagery].setMinimumSize(QtCore.QSize(0, 27))
    self.qv_imagery_lab_26[self.qv_imagery].setMaximumSize(QtCore.QSize(16777215, 27))
    self.qv_imagery_lab_26[self.qv_imagery].setFont(font)
    self.qv_imagery_lab_26[self.qv_imagery].setObjectName("qv_imagery_lab_26_" + str(self.qv_imagery))
    self.qv_imagery_lab_26[self.qv_imagery].setText("Interpolated pixels during geocoding ?")
    self.qv_imagery_gridlay_6[self.qv_imagery].addWidget(self.qv_imagery_lab_26[self.qv_imagery], 3, 0, 1, 1)
    self.qv_imagery_horlay_20.append(QtWidgets.QHBoxLayout())
    self.qv_imagery_horlay_20[self.qv_imagery].setObjectName("qv_imagery_horlay_20_" + str(self.qv_imagery))
    self.qv_imagery_gridlay_6[self.qv_imagery].addLayout(self.qv_imagery_horlay_20[self.qv_imagery], 0, 1, 1, 1)
    self.qv_imagery_check_11.append(QtWidgets.QRadioButton())
    self.qv_imagery_check_11[self.qv_imagery].setMinimumSize(QtCore.QSize(0, 27))
    self.qv_imagery_check_11[self.qv_imagery].setMaximumSize(QtCore.QSize(16777215, 27))
    self.qv_imagery_check_11[self.qv_imagery].setFont(font)
    self.qv_imagery_check_11[self.qv_imagery].setObjectName("qv_imagery_check_11_" + str(self.qv_imagery))
    self.qv_imagery_check_11[self.qv_imagery].setText("Yes")
    self.qv_imagery_horlay_20[self.qv_imagery].addWidget(self.qv_imagery_check_11[self.qv_imagery])
    self.qv_imagery_check_12.append(QtWidgets.QRadioButton())
    self.qv_imagery_check_12[self.qv_imagery].setMinimumSize(QtCore.QSize(0, 27))
    self.qv_imagery_check_12[self.qv_imagery].setMaximumSize(QtCore.QSize(16777215, 27))
    self.qv_imagery_check_12[self.qv_imagery].setFont(font)
    self.qv_imagery_check_12[self.qv_imagery].setObjectName("qv_imagery_check_12_" + str(self.qv_imagery))
    self.qv_imagery_check_12[self.qv_imagery].setText("No")
    self.qv_imagery_horlay_20[self.qv_imagery].addWidget(self.qv_imagery_check_12[self.qv_imagery])
    self.qv_imagery_group_6.append(QtWidgets.QButtonGroup())
    self.qv_imagery_group_6[self.qv_imagery].setObjectName("qv_imagery_group_6_" + str(self.qv_imagery))
    self.qv_imagery_group_6[self.qv_imagery].addButton(self.qv_imagery_check_11[self.qv_imagery])
    self.qv_imagery_group_6[self.qv_imagery].addButton(self.qv_imagery_check_12[self.qv_imagery])
    self.qv_imagery_horlay_21.append(QtWidgets.QHBoxLayout())
    self.qv_imagery_horlay_21[self.qv_imagery].setObjectName("qv_imagery_horlay_21_" + str(self.qv_imagery))
    self.qv_imagery_gridlay_6[self.qv_imagery].addLayout(self.qv_imagery_horlay_21[self.qv_imagery], 1, 1, 1, 1)
    self.qv_imagery_check_13.append(QtWidgets.QRadioButton())
    self.qv_imagery_check_13[self.qv_imagery].setMinimumSize(QtCore.QSize(0, 27))
    self.qv_imagery_check_13[self.qv_imagery].setMaximumSize(QtCore.QSize(16777215, 27))
    self.qv_imagery_check_13[self.qv_imagery].setFont(font)
    self.qv_imagery_check_13[self.qv_imagery].setObjectName("qv_imagery_check_13_" + str(self.qv_imagery))
    self.qv_imagery_check_13[self.qv_imagery].setText("Yes")
    self.qv_imagery_horlay_21[self.qv_imagery].addWidget(self.qv_imagery_check_13[self.qv_imagery])
    self.qv_imagery_check_14.append(QtWidgets.QRadioButton())
    self.qv_imagery_check_14[self.qv_imagery].setMinimumSize(QtCore.QSize(0, 27))
    self.qv_imagery_check_14[self.qv_imagery].setMaximumSize(QtCore.QSize(16777215, 27))
    self.qv_imagery_check_14[self.qv_imagery].setFont(font)
    self.qv_imagery_check_14[self.qv_imagery].setObjectName("qv_imagery_check_14_" + str(self.qv_imagery))
    self.qv_imagery_check_14[self.qv_imagery].setText("No")
    self.qv_imagery_horlay_21[self.qv_imagery].addWidget(self.qv_imagery_check_14[self.qv_imagery])
    self.qv_imagery_group_7.append(QtWidgets.QButtonGroup())
    self.qv_imagery_group_7[self.qv_imagery].setObjectName("qv_imagery_group_7_" + str(self.qv_imagery))
    self.qv_imagery_group_7[self.qv_imagery].addButton(self.qv_imagery_check_13[self.qv_imagery])
    self.qv_imagery_group_7[self.qv_imagery].addButton(self.qv_imagery_check_14[self.qv_imagery])
    self.qv_imagery_horlay_22.append(QtWidgets.QHBoxLayout())
    self.qv_imagery_horlay_22[self.qv_imagery].setObjectName("qv_imagery_horlay_22_" + str(self.qv_imagery))
    self.qv_imagery_gridlay_6[self.qv_imagery].addLayout(self.qv_imagery_horlay_22[self.qv_imagery], 2, 1, 1, 1)
    self.qv_imagery_check_15.append(QtWidgets.QRadioButton())
    self.qv_imagery_check_15[self.qv_imagery].setMinimumSize(QtCore.QSize(0, 27))
    self.qv_imagery_check_15[self.qv_imagery].setMaximumSize(QtCore.QSize(16777215, 27))
    self.qv_imagery_check_15[self.qv_imagery].setFont(font)
    self.qv_imagery_check_15[self.qv_imagery].setObjectName("qv_imagery_check_15_" + str(self.qv_imagery))
    self.qv_imagery_check_15[self.qv_imagery].setText("Yes")
    self.qv_imagery_horlay_22[self.qv_imagery].addWidget(self.qv_imagery_check_15[self.qv_imagery])
    self.qv_imagery_check_16.append(QtWidgets.QRadioButton())
    self.qv_imagery_check_16[self.qv_imagery].setMinimumSize(QtCore.QSize(0, 27))
    self.qv_imagery_check_16[self.qv_imagery].setMaximumSize(QtCore.QSize(16777215, 27))
    self.qv_imagery_check_16[self.qv_imagery].setFont(font)
    self.qv_imagery_check_16[self.qv_imagery].setObjectName("qv_imagery_check_16_" + str(self.qv_imagery))
    self.qv_imagery_check_16[self.qv_imagery].setText("No")
    self.qv_imagery_horlay_22[self.qv_imagery].addWidget(self.qv_imagery_check_16[self.qv_imagery])
    self.qv_imagery_group_8.append(QtWidgets.QButtonGroup())
    self.qv_imagery_group_8[self.qv_imagery].setObjectName("qv_imagery_group_8_" + str(self.qv_imagery))
    self.qv_imagery_group_8[self.qv_imagery].addButton(self.qv_imagery_check_15[self.qv_imagery])
    self.qv_imagery_group_8[self.qv_imagery].addButton(self.qv_imagery_check_16[self.qv_imagery])
    self.qv_imagery_horlay_23.append(QtWidgets.QHBoxLayout())
    self.qv_imagery_horlay_23[self.qv_imagery].setObjectName("qv_imagery_horlay_23_" + str(self.qv_imagery))
    self.qv_imagery_gridlay_6[self.qv_imagery].addLayout(self.qv_imagery_horlay_23[self.qv_imagery], 3, 1, 1, 1)
    self.qv_imagery_check_17.append(QtWidgets.QRadioButton())
    self.qv_imagery_check_17[self.qv_imagery].setMinimumSize(QtCore.QSize(0, 27))
    self.qv_imagery_check_17[self.qv_imagery].setMaximumSize(QtCore.QSize(16777215, 27))
    self.qv_imagery_check_17[self.qv_imagery].setFont(font)
    self.qv_imagery_check_17[self.qv_imagery].setObjectName("qv_imagery_check_17_" + str(self.qv_imagery))
    self.qv_imagery_check_17[self.qv_imagery].setText("Yes")
    self.qv_imagery_horlay_23[self.qv_imagery].addWidget(self.qv_imagery_check_17[self.qv_imagery])
    self.qv_imagery_check_18.append(QtWidgets.QRadioButton())
    self.qv_imagery_check_18[self.qv_imagery].setMinimumSize(QtCore.QSize(0, 27))
    self.qv_imagery_check_18[self.qv_imagery].setMaximumSize(QtCore.QSize(16777215, 27))
    self.qv_imagery_check_18[self.qv_imagery].setFont(font)
    self.qv_imagery_check_18[self.qv_imagery].setObjectName("qv_imagery_check_18_" + str(self.qv_imagery))
    self.qv_imagery_check_18[self.qv_imagery].setText("No")
    self.qv_imagery_horlay_23[self.qv_imagery].addWidget(self.qv_imagery_check_18[self.qv_imagery])
    self.qv_imagery_group_9.append(QtWidgets.QButtonGroup())
    self.qv_imagery_group_9[self.qv_imagery].setObjectName("qv_imagery_group_9_" + str(self.qv_imagery))
    self.qv_imagery_group_9[self.qv_imagery].addButton(self.qv_imagery_check_17[self.qv_imagery])
    self.qv_imagery_group_9[self.qv_imagery].addButton(self.qv_imagery_check_18[self.qv_imagery])
    self.qv_imagery_horlay_24.append(QtWidgets.QHBoxLayout())
    self.qv_imagery_horlay_24[self.qv_imagery].setObjectName("qv_imagery_horlay_24_" + str(self.qv_imagery))
    self.qv_imagery_horlay_24[self.qv_imagery].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, 
                                                                           QtWidgets.QSizePolicy.Minimum))
    self.qv_imagery_verlay_1[self.qv_imagery].addLayout(self.qv_imagery_horlay_24[self.qv_imagery])
    self.qv_imagery_lab_27.append(QtWidgets.QLabel())
    self.qv_imagery_lab_27[self.qv_imagery].setMinimumSize(QtCore.QSize(0, 27))
    self.qv_imagery_lab_27[self.qv_imagery].setMaximumSize(QtCore.QSize(16777215, 27))
    self.qv_imagery_lab_27[self.qv_imagery].setFont(font4)
    self.qv_imagery_lab_27[self.qv_imagery].setObjectName("qv_imagery_lab_27_" + str(self.qv_imagery))
    self.qv_imagery_lab_27[self.qv_imagery].setText("Atmospheric correction and atmospheric conditions:")
    self.qv_imagery_horlay_24[self.qv_imagery].addWidget(self.qv_imagery_lab_27[self.qv_imagery])
    self.qv_imagery_horlay_24[self.qv_imagery].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, 
                                                                           QtWidgets.QSizePolicy.Minimum))
    self.qv_imagery_horlay_25.append(QtWidgets.QHBoxLayout())
    self.qv_imagery_horlay_25[self.qv_imagery].setObjectName("qv_imagery_horlay_25_" + str(self.qv_imagery))
    self.qv_imagery_horlay_25[self.qv_imagery].addItem(QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, 
                                                                           QtWidgets.QSizePolicy.Minimum))
    self.qv_imagery_verlay_1[self.qv_imagery].addLayout(self.qv_imagery_horlay_25[self.qv_imagery])
    self.qv_imagery_gridlay_7.append(QtWidgets.QGridLayout())
    self.qv_imagery_gridlay_7[self.qv_imagery].setObjectName("qv_imagery_gridlay_7_" + str(self.qv_imagery))
    self.qv_imagery_horlay_25[self.qv_imagery].addLayout(self.qv_imagery_gridlay_7[self.qv_imagery])
    self.qv_imagery_horlay_25[self.qv_imagery].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, 
                                                                            QtWidgets.QSizePolicy.Minimum))
    self.qv_imagery_lab_28.append(QtWidgets.QLabel())
    self.qv_imagery_lab_28[self.qv_imagery].setMinimumSize(QtCore.QSize(0, 27))
    self.qv_imagery_lab_28[self.qv_imagery].setMaximumSize(QtCore.QSize(16777215, 27))
    self.qv_imagery_lab_28[self.qv_imagery].setFont(font)
    self.qv_imagery_lab_28[self.qv_imagery].setObjectName("qv_imagery_lab_28_" + str(self.qv_imagery))
    self.qv_imagery_lab_28[self.qv_imagery].setText("Failure of atmospheric correction ?")
    self.qv_imagery_gridlay_7[self.qv_imagery].addWidget(self.qv_imagery_lab_28[self.qv_imagery], 0, 0, 1, 1)
    self.qv_imagery_lab_29.append(QtWidgets.QLabel())
    self.qv_imagery_lab_29[self.qv_imagery].setMinimumSize(QtCore.QSize(0, 27))
    self.qv_imagery_lab_29[self.qv_imagery].setMaximumSize(QtCore.QSize(16777215, 27))
    self.qv_imagery_lab_29[self.qv_imagery].setFont(font)
    self.qv_imagery_lab_29[self.qv_imagery].setObjectName("qv_imagery_lab_29_" + str(self.qv_imagery))
    self.qv_imagery_lab_29[self.qv_imagery].setText("Cloud mask ?")
    self.qv_imagery_gridlay_7[self.qv_imagery].addWidget(self.qv_imagery_lab_29[self.qv_imagery], 1, 0, 1, 1)
    self.qv_imagery_lab_30.append(QtWidgets.QLabel())
    self.qv_imagery_lab_30[self.qv_imagery].setMinimumSize(QtCore.QSize(0, 27))
    self.qv_imagery_lab_30[self.qv_imagery].setMaximumSize(QtCore.QSize(16777215, 27))
    self.qv_imagery_lab_30[self.qv_imagery].setFont(font)
    self.qv_imagery_lab_30[self.qv_imagery].setObjectName("qv_imagery_lab_30_" + str(self.qv_imagery))
    self.qv_imagery_lab_30[self.qv_imagery].setText("Cloud shadow mask ?")
    self.qv_imagery_gridlay_7[self.qv_imagery].addWidget(self.qv_imagery_lab_30[self.qv_imagery], 2, 0, 1, 1)
    self.qv_imagery_lab_31.append(QtWidgets.QLabel())
    self.qv_imagery_lab_31[self.qv_imagery].setMinimumSize(QtCore.QSize(0, 27))
    self.qv_imagery_lab_31[self.qv_imagery].setMaximumSize(QtCore.QSize(16777215, 27))
    self.qv_imagery_lab_31[self.qv_imagery].setFont(font)
    self.qv_imagery_lab_31[self.qv_imagery].setObjectName("qv_imagery_lab_31_" + str(self.qv_imagery))
    self.qv_imagery_lab_31[self.qv_imagery].setText("Haze mask ?")
    self.qv_imagery_gridlay_7[self.qv_imagery].addWidget(self.qv_imagery_lab_31[self.qv_imagery], 3, 0, 1, 1)
    self.qv_imagery_lab_32.append(QtWidgets.QLabel())
    self.qv_imagery_lab_32[self.qv_imagery].setMinimumSize(QtCore.QSize(0, 27))
    self.qv_imagery_lab_32[self.qv_imagery].setMaximumSize(QtCore.QSize(16777215, 27))
    self.qv_imagery_lab_32[self.qv_imagery].setFont(font)
    self.qv_imagery_lab_32[self.qv_imagery].setObjectName("qv_imagery_lab_32_" + str(self.qv_imagery))
    self.qv_imagery_lab_32[self.qv_imagery].setText("Critical terrain correction based on DEM roughness measure ?")
    self.qv_imagery_gridlay_7[self.qv_imagery].addWidget(self.qv_imagery_lab_32[self.qv_imagery], 4, 0, 1, 1)
    self.qv_imagery_lab_33.append(QtWidgets.QLabel())
    self.qv_imagery_lab_33[self.qv_imagery].setMinimumSize(QtCore.QSize(0, 27))
    self.qv_imagery_lab_33[self.qv_imagery].setMaximumSize(QtCore.QSize(16777215, 27))
    self.qv_imagery_lab_33[self.qv_imagery].setFont(font)
    self.qv_imagery_lab_33[self.qv_imagery].setObjectName("qv_imagery_lab_33_" + str(self.qv_imagery))
    self.qv_imagery_lab_33[self.qv_imagery].setText("Critical terrain correction based on slope/local illumination angle ?")
    self.qv_imagery_gridlay_7[self.qv_imagery].addWidget(self.qv_imagery_lab_33[self.qv_imagery], 5, 0, 1, 1)
    self.qv_imagery_lab_34.append(QtWidgets.QLabel())
    self.qv_imagery_lab_34[self.qv_imagery].setMinimumSize(QtCore.QSize(0, 27))
    self.qv_imagery_lab_34[self.qv_imagery].setMaximumSize(QtCore.QSize(16777215, 27))
    self.qv_imagery_lab_34[self.qv_imagery].setFont(font)
    self.qv_imagery_lab_34[self.qv_imagery].setObjectName("qv_imagery_lab_34_" + str(self.qv_imagery))
    self.qv_imagery_lab_34[self.qv_imagery].setText("Critical BRFD geometry based on sun-sensor-terrain geometry ?")
    self.qv_imagery_gridlay_7[self.qv_imagery].addWidget(self.qv_imagery_lab_34[self.qv_imagery], 6, 0, 1, 1)
    self.qv_imagery_horlay_26.append(QtWidgets.QHBoxLayout())
    self.qv_imagery_horlay_26[self.qv_imagery].setObjectName("qv_imagery_horlay_26_" + str(self.qv_imagery))
    self.qv_imagery_gridlay_7[self.qv_imagery].addLayout(self.qv_imagery_horlay_26[self.qv_imagery], 0, 1, 1, 1)
    self.qv_imagery_check_19.append(QtWidgets.QRadioButton())
    self.qv_imagery_check_19[self.qv_imagery].setMinimumSize(QtCore.QSize(0, 27))
    self.qv_imagery_check_19[self.qv_imagery].setMaximumSize(QtCore.QSize(16777215, 27))
    self.qv_imagery_check_19[self.qv_imagery].setFont(font)
    self.qv_imagery_check_19[self.qv_imagery].setObjectName("qv_imagery_check_19_" + str(self.qv_imagery))
    self.qv_imagery_check_19[self.qv_imagery].setText("Yes")
    self.qv_imagery_horlay_26[self.qv_imagery].addWidget(self.qv_imagery_check_19[self.qv_imagery])
    self.qv_imagery_check_20.append(QtWidgets.QRadioButton())
    self.qv_imagery_check_20[self.qv_imagery].setMinimumSize(QtCore.QSize(0, 27))
    self.qv_imagery_check_20[self.qv_imagery].setMaximumSize(QtCore.QSize(16777215, 27))
    self.qv_imagery_check_20[self.qv_imagery].setFont(font)
    self.qv_imagery_check_20[self.qv_imagery].setObjectName("qv_imagery_check_20_" + str(self.qv_imagery))
    self.qv_imagery_check_20[self.qv_imagery].setText("No")
    self.qv_imagery_horlay_26[self.qv_imagery].addWidget(self.qv_imagery_check_20[self.qv_imagery])
    self.qv_imagery_group_10.append(QtWidgets.QButtonGroup())
    self.qv_imagery_group_10[self.qv_imagery].setObjectName("qv_imagery_group_10_" + str(self.qv_imagery))
    self.qv_imagery_group_10[self.qv_imagery].addButton(self.qv_imagery_check_19[self.qv_imagery])
    self.qv_imagery_group_10[self.qv_imagery].addButton(self.qv_imagery_check_20[self.qv_imagery])
    self.qv_imagery_infBut_10.append(QtWidgets.QToolButton())
    self.qv_imagery_infBut_10[self.qv_imagery].setMaximumSize(QtCore.QSize(27, 27))
    self.qv_imagery_infBut_10[self.qv_imagery].setStyleSheet("QToolButton {\n"
    "    border: 1px solid transparent;\n"
    "    background-color: transparent;\n"
    "    width: 27px;\n"
    "    height: 27px;\n"
    "}\n"
    "QToolButton:flat {\n"
    "    border: none;\n"
    "}")
    self.qv_imagery_infBut_10[self.qv_imagery].setText("")
    self.qv_imagery_infBut_10[self.qv_imagery].setIcon(icon)
    self.qv_imagery_infBut_10[self.qv_imagery].setIconSize(QtCore.QSize(23, 23))
    self.qv_imagery_infBut_10[self.qv_imagery].setAutoRaise(False)
    self.qv_imagery_infBut_10[self.qv_imagery].setObjectName("infoButton_40")
    self.qv_imagery_horlay_26[self.qv_imagery].addWidget(self.qv_imagery_infBut_10[self.qv_imagery])
    self.qv_imagery_horlay_27.append(QtWidgets.QHBoxLayout())
    self.qv_imagery_horlay_27[self.qv_imagery].setObjectName("qv_imagery_horlay_27_" + str(self.qv_imagery))
    self.qv_imagery_gridlay_7[self.qv_imagery].addLayout(self.qv_imagery_horlay_27[self.qv_imagery], 1, 1, 1, 1)
    self.qv_imagery_check_21.append(QtWidgets.QRadioButton())
    self.qv_imagery_check_21[self.qv_imagery].setMinimumSize(QtCore.QSize(0, 27))
    self.qv_imagery_check_21[self.qv_imagery].setMaximumSize(QtCore.QSize(16777215, 27))
    self.qv_imagery_check_21[self.qv_imagery].setFont(font)
    self.qv_imagery_check_21[self.qv_imagery].setObjectName("qv_imagery_check_21_" + str(self.qv_imagery))
    self.qv_imagery_check_21[self.qv_imagery].setText("Yes")
    self.qv_imagery_horlay_27[self.qv_imagery].addWidget(self.qv_imagery_check_21[self.qv_imagery])
    self.qv_imagery_check_22.append(QtWidgets.QRadioButton())
    self.qv_imagery_check_22[self.qv_imagery].setMinimumSize(QtCore.QSize(0, 27))
    self.qv_imagery_check_22[self.qv_imagery].setMaximumSize(QtCore.QSize(16777215, 27))
    self.qv_imagery_check_22[self.qv_imagery].setFont(font)
    self.qv_imagery_check_22[self.qv_imagery].setObjectName("qv_imagery_check_22_" + str(self.qv_imagery))
    self.qv_imagery_check_22[self.qv_imagery].setText("No")
    self.qv_imagery_horlay_27[self.qv_imagery].addWidget(self.qv_imagery_check_22[self.qv_imagery])
    self.qv_imagery_group_11.append(QtWidgets.QButtonGroup())
    self.qv_imagery_group_11[self.qv_imagery].setObjectName("qv_imagery_group_11_" + str(self.qv_imagery))
    self.qv_imagery_group_11[self.qv_imagery].addButton(self.qv_imagery_check_21[self.qv_imagery])
    self.qv_imagery_group_11[self.qv_imagery].addButton(self.qv_imagery_check_22[self.qv_imagery])
    self.qv_imagery_horlay_27[self.qv_imagery].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, 
                                                                           QtWidgets.QSizePolicy.Minimum))
    self.qv_imagery_horlay_28.append(QtWidgets.QHBoxLayout())
    self.qv_imagery_horlay_28[self.qv_imagery].setObjectName("qv_imagery_horlay_28_" + str(self.qv_imagery))
    self.qv_imagery_gridlay_7[self.qv_imagery].addLayout(self.qv_imagery_horlay_28[self.qv_imagery], 2, 1, 1, 1)
    self.qv_imagery_check_23.append(QtWidgets.QRadioButton())
    self.qv_imagery_check_23[self.qv_imagery].setMinimumSize(QtCore.QSize(0, 27))
    self.qv_imagery_check_23[self.qv_imagery].setMaximumSize(QtCore.QSize(16777215, 27))
    self.qv_imagery_check_23[self.qv_imagery].setFont(font)
    self.qv_imagery_check_23[self.qv_imagery].setObjectName("qv_imagery_check_23_" + str(self.qv_imagery))
    self.qv_imagery_check_23[self.qv_imagery].setText("Yes")
    self.qv_imagery_horlay_28[self.qv_imagery].addWidget(self.qv_imagery_check_23[self.qv_imagery])
    self.qv_imagery_check_24.append(QtWidgets.QRadioButton())
    self.qv_imagery_check_24[self.qv_imagery].setMinimumSize(QtCore.QSize(0, 27))
    self.qv_imagery_check_24[self.qv_imagery].setMaximumSize(QtCore.QSize(16777215, 27))
    self.qv_imagery_check_24[self.qv_imagery].setFont(font)
    self.qv_imagery_check_24[self.qv_imagery].setObjectName("qv_imagery_check_24_" + str(self.qv_imagery))
    self.qv_imagery_check_24[self.qv_imagery].setText("No")
    self.qv_imagery_horlay_28[self.qv_imagery].addWidget(self.qv_imagery_check_24[self.qv_imagery])
    self.qv_imagery_group_12.append(QtWidgets.QButtonGroup())
    self.qv_imagery_group_12[self.qv_imagery].setObjectName("qv_imagery_group_12_" + str(self.qv_imagery))
    self.qv_imagery_group_12[self.qv_imagery].addButton(self.qv_imagery_check_23[self.qv_imagery])
    self.qv_imagery_group_12[self.qv_imagery].addButton(self.qv_imagery_check_24[self.qv_imagery])
    self.qv_imagery_horlay_28[self.qv_imagery].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, 
                                                                           QtWidgets.QSizePolicy.Minimum))
    self.qv_imagery_horlay_29.append(QtWidgets.QHBoxLayout())
    self.qv_imagery_horlay_29[self.qv_imagery].setObjectName("qv_imagery_horlay_29_" + str(self.qv_imagery))
    self.qv_imagery_gridlay_7[self.qv_imagery].addLayout(self.qv_imagery_horlay_29[self.qv_imagery], 3, 1, 1, 1)
    self.qv_imagery_check_25.append(QtWidgets.QRadioButton())
    self.qv_imagery_check_25[self.qv_imagery].setMinimumSize(QtCore.QSize(0, 27))
    self.qv_imagery_check_25[self.qv_imagery].setMaximumSize(QtCore.QSize(16777215, 27))
    self.qv_imagery_check_25[self.qv_imagery].setFont(font)
    self.qv_imagery_check_25[self.qv_imagery].setObjectName("qv_imagery_check_25_" + str(self.qv_imagery))
    self.qv_imagery_check_25[self.qv_imagery].setText("Yes")
    self.qv_imagery_horlay_29[self.qv_imagery].addWidget(self.qv_imagery_check_25[self.qv_imagery])
    self.qv_imagery_check_26.append(QtWidgets.QRadioButton())
    self.qv_imagery_check_26[self.qv_imagery].setMinimumSize(QtCore.QSize(0, 27))
    self.qv_imagery_check_26[self.qv_imagery].setMaximumSize(QtCore.QSize(16777215, 27))
    self.qv_imagery_check_26[self.qv_imagery].setFont(font)
    self.qv_imagery_check_26[self.qv_imagery].setObjectName("qv_imagery_check_26_" + str(self.qv_imagery))
    self.qv_imagery_check_26[self.qv_imagery].setText("No")
    self.qv_imagery_horlay_29[self.qv_imagery].addWidget(self.qv_imagery_check_26[self.qv_imagery])
    self.qv_imagery_group_13.append(QtWidgets.QButtonGroup())
    self.qv_imagery_group_13[self.qv_imagery].setObjectName("qv_imagery_group_13_" + str(self.qv_imagery))
    self.qv_imagery_group_13[self.qv_imagery].addButton(self.qv_imagery_check_25[self.qv_imagery])
    self.qv_imagery_group_13[self.qv_imagery].addButton(self.qv_imagery_check_26[self.qv_imagery])
    self.qv_imagery_horlay_29[self.qv_imagery].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, 
                                                                           QtWidgets.QSizePolicy.Minimum))
    self.qv_imagery_horlay_30.append(QtWidgets.QHBoxLayout())
    self.qv_imagery_horlay_30[self.qv_imagery].setObjectName("qv_imagery_horlay_30_" + str(self.qv_imagery))
    self.qv_imagery_gridlay_7[self.qv_imagery].addLayout(self.qv_imagery_horlay_30[self.qv_imagery], 4, 1, 1, 1)
    self.qv_imagery_check_27.append(QtWidgets.QRadioButton())
    self.qv_imagery_check_27[self.qv_imagery].setMinimumSize(QtCore.QSize(0, 27))
    self.qv_imagery_check_27[self.qv_imagery].setMaximumSize(QtCore.QSize(16777215, 27))
    self.qv_imagery_check_27[self.qv_imagery].setFont(font)
    self.qv_imagery_check_27[self.qv_imagery].setObjectName("qv_imagery_check_27_" + str(self.qv_imagery))
    self.qv_imagery_check_27[self.qv_imagery].setText("Yes")
    self.qv_imagery_horlay_30[self.qv_imagery].addWidget(self.qv_imagery_check_27[self.qv_imagery])
    self.qv_imagery_check_28.append(QtWidgets.QRadioButton())
    self.qv_imagery_check_28[self.qv_imagery].setMinimumSize(QtCore.QSize(0, 27))
    self.qv_imagery_check_28[self.qv_imagery].setMaximumSize(QtCore.QSize(16777215, 27))
    self.qv_imagery_check_28[self.qv_imagery].setFont(font)
    self.qv_imagery_check_28[self.qv_imagery].setObjectName("qv_imagery_check_28_" + str(self.qv_imagery))
    self.qv_imagery_check_28[self.qv_imagery].setText("No")
    self.qv_imagery_horlay_30[self.qv_imagery].addWidget(self.qv_imagery_check_28[self.qv_imagery])
    self.qv_imagery_group_14.append(QtWidgets.QButtonGroup())
    self.qv_imagery_group_14[self.qv_imagery].setObjectName("qv_imagery_group_14_" + str(self.qv_imagery))
    self.qv_imagery_group_14[self.qv_imagery].addButton(self.qv_imagery_check_27[self.qv_imagery])
    self.qv_imagery_group_14[self.qv_imagery].addButton(self.qv_imagery_check_28[self.qv_imagery])
    self.qv_imagery_infBut_11.append(QtWidgets.QToolButton())
    self.qv_imagery_infBut_11[self.qv_imagery].setMaximumSize(QtCore.QSize(27, 27))
    self.qv_imagery_infBut_11[self.qv_imagery].setStyleSheet("QToolButton {\n"
    "    border: 1px solid transparent;\n"
    "    background-color: transparent;\n"
    "    width: 27px;\n"
    "    height: 27px;\n"
    "}\n"
    "QToolButton:flat {\n"
    "    border: none;\n"
    "}")
    self.qv_imagery_infBut_11[self.qv_imagery].setText("")
    self.qv_imagery_infBut_11[self.qv_imagery].setIcon(icon)
    self.qv_imagery_infBut_11[self.qv_imagery].setIconSize(QtCore.QSize(23, 23))
    self.qv_imagery_infBut_11[self.qv_imagery].setAutoRaise(False)
    self.qv_imagery_infBut_11[self.qv_imagery].setObjectName("infoButton_41")
    self.qv_imagery_horlay_30[self.qv_imagery].addWidget(self.qv_imagery_infBut_11[self.qv_imagery])
    self.qv_imagery_horlay_31.append(QtWidgets.QHBoxLayout())
    self.qv_imagery_horlay_31[self.qv_imagery].setObjectName("qv_imagery_horlay_31_" + str(self.qv_imagery))
    self.qv_imagery_gridlay_7[self.qv_imagery].addLayout(self.qv_imagery_horlay_31[self.qv_imagery], 5, 1, 1, 1)
    self.qv_imagery_check_29.append(QtWidgets.QRadioButton())
    self.qv_imagery_check_29[self.qv_imagery].setMinimumSize(QtCore.QSize(0, 27))
    self.qv_imagery_check_29[self.qv_imagery].setMaximumSize(QtCore.QSize(16777215, 27))
    self.qv_imagery_check_29[self.qv_imagery].setFont(font)
    self.qv_imagery_check_29[self.qv_imagery].setObjectName("qv_imagery_check_29_" + str(self.qv_imagery))
    self.qv_imagery_check_29[self.qv_imagery].setText("Yes")
    self.qv_imagery_horlay_31[self.qv_imagery].addWidget(self.qv_imagery_check_29[self.qv_imagery])
    self.qv_imagery_check_30.append(QtWidgets.QRadioButton())
    self.qv_imagery_check_30[self.qv_imagery].setMinimumSize(QtCore.QSize(0, 27))
    self.qv_imagery_check_30[self.qv_imagery].setMaximumSize(QtCore.QSize(16777215, 27))
    self.qv_imagery_check_30[self.qv_imagery].setFont(font)
    self.qv_imagery_check_30[self.qv_imagery].setObjectName("qv_imagery_check_30_" + str(self.qv_imagery))
    self.qv_imagery_check_30[self.qv_imagery].setText("No")
    self.qv_imagery_horlay_31[self.qv_imagery].addWidget(self.qv_imagery_check_30[self.qv_imagery])
    self.qv_imagery_group_15.append(QtWidgets.QButtonGroup())
    self.qv_imagery_group_15[self.qv_imagery].setObjectName("qv_imagery_group_15_" + str(self.qv_imagery))
    self.qv_imagery_group_15[self.qv_imagery].addButton(self.qv_imagery_check_29[self.qv_imagery])
    self.qv_imagery_group_15[self.qv_imagery].addButton(self.qv_imagery_check_30[self.qv_imagery])
    self.qv_imagery_infBut_12.append(QtWidgets.QToolButton())
    self.qv_imagery_infBut_12[self.qv_imagery].setMaximumSize(QtCore.QSize(27, 27))
    self.qv_imagery_infBut_12[self.qv_imagery].setStyleSheet("QToolButton {\n"
    "    border: 1px solid transparent;\n"
    "    background-color: transparent;\n"
    "    width: 27px;\n"
    "    height: 27px;\n"
    "}\n"
    "QToolButton:flat {\n"
    "    border: none;\n"
    "}")
    self.qv_imagery_infBut_12[self.qv_imagery].setText("")
    self.qv_imagery_infBut_12[self.qv_imagery].setIcon(icon)
    self.qv_imagery_infBut_12[self.qv_imagery].setIconSize(QtCore.QSize(23, 23))
    self.qv_imagery_infBut_12[self.qv_imagery].setAutoRaise(False)
    self.qv_imagery_infBut_12[self.qv_imagery].setObjectName("infoButton_42")
    self.qv_imagery_horlay_31[self.qv_imagery].addWidget(self.qv_imagery_infBut_12[self.qv_imagery])
    self.qv_imagery_horlay_32.append(QtWidgets.QHBoxLayout())
    self.qv_imagery_horlay_32[self.qv_imagery].setObjectName("qv_imagery_horlay_32_" + str(self.qv_imagery))
    self.qv_imagery_gridlay_7[self.qv_imagery].addLayout(self.qv_imagery_horlay_32[self.qv_imagery], 6, 1, 1, 1)
    self.qv_imagery_check_31.append(QtWidgets.QRadioButton())
    self.qv_imagery_check_31[self.qv_imagery].setMinimumSize(QtCore.QSize(0, 27))
    self.qv_imagery_check_31[self.qv_imagery].setMaximumSize(QtCore.QSize(16777215, 27))
    self.qv_imagery_check_31[self.qv_imagery].setFont(font)
    self.qv_imagery_check_31[self.qv_imagery].setObjectName("qv_imagery_check_31_" + str(self.qv_imagery))
    self.qv_imagery_check_31[self.qv_imagery].setText("Yes")
    self.qv_imagery_horlay_32[self.qv_imagery].addWidget(self.qv_imagery_check_31[self.qv_imagery])
    self.qv_imagery_check_32.append(QtWidgets.QRadioButton())
    self.qv_imagery_check_32[self.qv_imagery].setMinimumSize(QtCore.QSize(0, 27))
    self.qv_imagery_check_32[self.qv_imagery].setMaximumSize(QtCore.QSize(16777215, 27))
    self.qv_imagery_check_32[self.qv_imagery].setFont(font)
    self.qv_imagery_check_32[self.qv_imagery].setObjectName("qv_imagery_check_32_" + str(self.qv_imagery))
    self.qv_imagery_check_32[self.qv_imagery].setText("No")
    self.qv_imagery_horlay_32[self.qv_imagery].addWidget(self.qv_imagery_check_32[self.qv_imagery])
    self.qv_imagery_group_16.append(QtWidgets.QButtonGroup())
    self.qv_imagery_group_16[self.qv_imagery].setObjectName("qv_imagery_group_16_" + str(self.qv_imagery))
    self.qv_imagery_group_16[self.qv_imagery].addButton(self.qv_imagery_check_31[self.qv_imagery])
    self.qv_imagery_group_16[self.qv_imagery].addButton(self.qv_imagery_check_32[self.qv_imagery])
    self.qv_imagery_infBut_13.append(QtWidgets.QToolButton())
    self.qv_imagery_infBut_13[self.qv_imagery].setMaximumSize(QtCore.QSize(27, 27))
    self.qv_imagery_infBut_13[self.qv_imagery].setStyleSheet("QToolButton {\n"
    "    border: 1px solid transparent;\n"
    "    background-color: transparent;\n"
    "    width: 27px;\n"
    "    height: 27px;\n"
    "}\n"
    "QToolButton:flat {\n"
    "    border: none;\n"
    "}")
    self.qv_imagery_infBut_13[self.qv_imagery].setText("")
    self.qv_imagery_infBut_13[self.qv_imagery].setIcon(icon)
    self.qv_imagery_infBut_13[self.qv_imagery].setIconSize(QtCore.QSize(23, 23))
    self.qv_imagery_infBut_13[self.qv_imagery].setAutoRaise(False)
    self.qv_imagery_infBut_13[self.qv_imagery].setObjectName("infoButton_43")
    self.qv_imagery_horlay_32[self.qv_imagery].addWidget(self.qv_imagery_infBut_13[self.qv_imagery])
    self.qv_imagery_verlay_1[self.qv_imagery].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, 
                                                                           QtWidgets.QSizePolicy.Expanding))
    all_info_boxes = self.qv_imagery_tab_1[self.qv_imagery].findChildren(QToolButton)
    for widget in all_info_boxes:
        widget.clicked.connect(lambda: self.button_clicked())
    all_radio_buttons = self.qv_imagery_tab_1[self.qv_imagery].findChildren(QtWidgets.QRadioButton)
    for widget in all_radio_buttons:
        widget.clicked.connect(lambda: self.set_modified())
    all_line_edits = self.qv_imagery_tab_1[self.qv_imagery].findChildren(QtWidgets.QLineEdit)
    for widget in all_line_edits:
        widget.textChanged.connect(lambda: self.set_modified())
    all_date_edits = self.qv_imagery_tab_1[self.qv_imagery].findChildren(QDateEdit)
    for widget in all_date_edits:    
        widget.dateChanged.connect(lambda: self.set_modified())
        widget.setDate(QDate.currentDate())
    self.qv_imagery_list_1[self.qv_imagery].activated.connect(lambda: self.set_modified())
    self.qv_imagery_list_2[self.qv_imagery].activated.connect(lambda: self.set_modified())
    self.qv_imagery_list_3[self.qv_imagery].activated.connect(lambda: qv_activate_tab_list(self))
    self.qv_imagery_line_list[0].append([self.qv_imagery_line_1[self.qv_imagery], self.qv_imagery_lab_2[self.qv_imagery], "text", 
                                        self.qv_tabWidget.indexOf(self.qv_imagery_tab_1[self.qv_imagery])])
    self.qv_imagery_line_list[1].append([self.qv_imagery_line_2[self.qv_imagery], self.qv_imagery_lab_6[self.qv_imagery], "float", 
                                        self.qv_tabWidget.indexOf(self.qv_imagery_tab_1[self.qv_imagery])])
    self.qv_imagery_line_list[2].append([self.qv_imagery_line_3[self.qv_imagery], self.qv_imagery_lab_7[self.qv_imagery], "float", 
                                        self.qv_tabWidget.indexOf(self.qv_imagery_tab_1[self.qv_imagery])])
    self.qv_imagery_line_list[3].append([self.qv_imagery_line_4[self.qv_imagery], self.qv_imagery_lab_8[self.qv_imagery], "float", 
                                        self.qv_tabWidget.indexOf(self.qv_imagery_tab_1[self.qv_imagery])])
    self.qv_imagery_line_list[4].append([self.qv_imagery_line_5[self.qv_imagery], self.qv_imagery_lab_9[self.qv_imagery], "float", 
                                        self.qv_tabWidget.indexOf(self.qv_imagery_tab_1[self.qv_imagery])])
    self.qv_imagery_line_list[5].append([self.qv_imagery_line_6[self.qv_imagery], self.qv_imagery_lab_10[self.qv_imagery], "float", 
                                        self.qv_tabWidget.indexOf(self.qv_imagery_tab_1[self.qv_imagery])])
    self.qv_imagery_line_list[6].append([self.qv_imagery_line_7[self.qv_imagery], self.qv_imagery_lab_11[self.qv_imagery], "text", 
                                        self.qv_tabWidget.indexOf(self.qv_imagery_tab_1[self.qv_imagery])])
    self.qv_imagery_combo_list[0].append([self.qv_imagery_list_1[self.qv_imagery], self.qv_imagery_lab_13[self.qv_imagery], 
                                          self.qv_tabWidget.indexOf(self.qv_imagery_tab_1[self.qv_imagery])])
    self.qv_imagery_combo_list[1].append([self.qv_imagery_list_2[self.qv_imagery], self.qv_imagery_lab_35[self.qv_imagery], 
                                          self.qv_tabWidget.indexOf(self.qv_imagery_tab_1[self.qv_imagery])])
    self.qv_imagery_date_list[0].append([self.qv_imagery_date_1[self.qv_imagery], self.qv_imagery_lab_3[self.qv_imagery], 
                                         self.qv_tabWidget.indexOf(self.qv_imagery_tab_1[self.qv_imagery])])
    self.qv_imagery_date_list[1].append([self.qv_imagery_date_2[self.qv_imagery], self.qv_imagery_lab_4[self.qv_imagery], 
                                         self.qv_tabWidget.indexOf(self.qv_imagery_tab_1[self.qv_imagery])])
    self.qv_imagery_radio_list[0].append([self.qv_imagery_group_1[self.qv_imagery], self.qv_imagery_lab_14[self.qv_imagery], 
                                        self.qv_tabWidget.indexOf(self.qv_imagery_tab_1[self.qv_imagery])])
    self.qv_imagery_radio_list[1].append([self.qv_imagery_group_2[self.qv_imagery], self.qv_imagery_lab_17[self.qv_imagery], 
                                        self.qv_tabWidget.indexOf(self.qv_imagery_tab_1[self.qv_imagery])])
    self.qv_imagery_radio_list[2].append([self.qv_imagery_group_3[self.qv_imagery], self.qv_imagery_lab_18[self.qv_imagery], 
                                        self.qv_tabWidget.indexOf(self.qv_imagery_tab_1[self.qv_imagery])])
    self.qv_imagery_radio_list[3].append([self.qv_imagery_group_4[self.qv_imagery], self.qv_imagery_lab_20[self.qv_imagery], 
                                        self.qv_tabWidget.indexOf(self.qv_imagery_tab_1[self.qv_imagery])])
    self.qv_imagery_radio_list[4].append([self.qv_imagery_group_5[self.qv_imagery], self.qv_imagery_lab_21[self.qv_imagery], 
                                        self.qv_tabWidget.indexOf(self.qv_imagery_tab_1[self.qv_imagery])])
    self.qv_imagery_radio_list[5].append([self.qv_imagery_group_6[self.qv_imagery], self.qv_imagery_lab_23[self.qv_imagery], 
                                        self.qv_tabWidget.indexOf(self.qv_imagery_tab_1[self.qv_imagery])])
    self.qv_imagery_radio_list[6].append([self.qv_imagery_group_7[self.qv_imagery], self.qv_imagery_lab_24[self.qv_imagery], 
                                        self.qv_tabWidget.indexOf(self.qv_imagery_tab_1[self.qv_imagery])])
    self.qv_imagery_radio_list[7].append([self.qv_imagery_group_8[self.qv_imagery], self.qv_imagery_lab_25[self.qv_imagery], 
                                        self.qv_tabWidget.indexOf(self.qv_imagery_tab_1[self.qv_imagery])])
    self.qv_imagery_radio_list[8].append([self.qv_imagery_group_9[self.qv_imagery], self.qv_imagery_lab_26[self.qv_imagery], 
                                        self.qv_tabWidget.indexOf(self.qv_imagery_tab_1[self.qv_imagery])])
    self.qv_imagery_radio_list[9].append([self.qv_imagery_group_10[self.qv_imagery], self.qv_imagery_lab_28[self.qv_imagery], 
                                        self.qv_tabWidget.indexOf(self.qv_imagery_tab_1[self.qv_imagery])])
    self.qv_imagery_radio_list[10].append([self.qv_imagery_group_11[self.qv_imagery], self.qv_imagery_lab_29[self.qv_imagery], 
                                        self.qv_tabWidget.indexOf(self.qv_imagery_tab_1[self.qv_imagery])])
    self.qv_imagery_radio_list[11].append([self.qv_imagery_group_12[self.qv_imagery], self.qv_imagery_lab_30[self.qv_imagery], 
                                        self.qv_tabWidget.indexOf(self.qv_imagery_tab_1[self.qv_imagery])])
    self.qv_imagery_radio_list[12].append([self.qv_imagery_group_13[self.qv_imagery], self.qv_imagery_lab_31[self.qv_imagery], 
                                        self.qv_tabWidget.indexOf(self.qv_imagery_tab_1[self.qv_imagery])])
    self.qv_imagery_radio_list[13].append([self.qv_imagery_group_14[self.qv_imagery], self.qv_imagery_lab_32[self.qv_imagery], 
                                        self.qv_tabWidget.indexOf(self.qv_imagery_tab_1[self.qv_imagery])])
    self.qv_imagery_radio_list[14].append([self.qv_imagery_group_15[self.qv_imagery], self.qv_imagery_lab_33[self.qv_imagery], 
                                        self.qv_tabWidget.indexOf(self.qv_imagery_tab_1[self.qv_imagery])])
    self.qv_imagery_radio_list[15].append([self.qv_imagery_group_16[self.qv_imagery], self.qv_imagery_lab_34[self.qv_imagery], 
                                        self.qv_tabWidget.indexOf(self.qv_imagery_tab_1[self.qv_imagery])])
    qv_update_instrument_list(self)
    qv_update_tab_list(self, "imagery")
    self.qv_imagery += 1

def close_imagery_tab(self, index, insitu_index):
    self.qv_tabWidget.removeTab(index)
    self.qv_imagery_verlay_1[insitu_index].deleteLater()
    self.qv_imagery_horlay_1[insitu_index].deleteLater()
    self.qv_imagery_horlay_2[insitu_index].deleteLater()
    self.qv_imagery_horlay_3[insitu_index].deleteLater()
    self.qv_imagery_horlay_4[insitu_index].deleteLater()
    self.qv_imagery_horlay_5[insitu_index].deleteLater()
    self.qv_imagery_horlay_6[insitu_index].deleteLater()
    self.qv_imagery_horlay_7[insitu_index].deleteLater()
    self.qv_imagery_horlay_8[insitu_index].deleteLater()
    self.qv_imagery_horlay_9[insitu_index].deleteLater()
    self.qv_imagery_horlay_10[insitu_index].deleteLater()
    self.qv_imagery_horlay_11[insitu_index].deleteLater()
    self.qv_imagery_horlay_12[insitu_index].deleteLater()
    self.qv_imagery_horlay_13[insitu_index].deleteLater()
    self.qv_imagery_horlay_14[insitu_index].deleteLater()
    self.qv_imagery_horlay_15[insitu_index].deleteLater()
    self.qv_imagery_horlay_16[insitu_index].deleteLater()
    self.qv_imagery_horlay_17[insitu_index].deleteLater()
    self.qv_imagery_horlay_18[insitu_index].deleteLater()
    self.qv_imagery_horlay_19[insitu_index].deleteLater()
    self.qv_imagery_horlay_20[insitu_index].deleteLater()
    self.qv_imagery_horlay_21[insitu_index].deleteLater()
    self.qv_imagery_horlay_22[insitu_index].deleteLater()
    self.qv_imagery_horlay_23[insitu_index].deleteLater()
    self.qv_imagery_horlay_24[insitu_index].deleteLater()
    self.qv_imagery_horlay_25[insitu_index].deleteLater()
    self.qv_imagery_horlay_26[insitu_index].deleteLater()
    self.qv_imagery_horlay_27[insitu_index].deleteLater()
    self.qv_imagery_horlay_28[insitu_index].deleteLater()
    self.qv_imagery_horlay_29[insitu_index].deleteLater()
    self.qv_imagery_horlay_30[insitu_index].deleteLater()
    self.qv_imagery_horlay_31[insitu_index].deleteLater()
    self.qv_imagery_horlay_32[insitu_index].deleteLater()
    self.qv_imagery_gridlay_1[insitu_index].deleteLater()
    self.qv_imagery_gridlay_2[insitu_index].deleteLater()
    self.qv_imagery_gridlay_3[insitu_index].deleteLater()
    self.qv_imagery_gridlay_4[insitu_index].deleteLater()
    self.qv_imagery_gridlay_5[insitu_index].deleteLater()
    self.qv_imagery_gridlay_6[insitu_index].deleteLater()
    self.qv_imagery_gridlay_7[insitu_index].deleteLater()
    self.qv_imagery_gridlay_8[insitu_index].deleteLater()
    self.qv_imagery_infBut_1[insitu_index].deleteLater()
    self.qv_imagery_infBut_2[insitu_index].deleteLater()
    self.qv_imagery_infBut_3[insitu_index].deleteLater()
    self.qv_imagery_infBut_4[insitu_index].deleteLater()
    self.qv_imagery_infBut_5[insitu_index].deleteLater()
    self.qv_imagery_infBut_6[insitu_index].deleteLater()
    self.qv_imagery_infBut_7[insitu_index].deleteLater()
    self.qv_imagery_infBut_8[insitu_index].deleteLater()
    self.qv_imagery_infBut_9[insitu_index].deleteLater()
    self.qv_imagery_infBut_10[insitu_index].deleteLater()
    self.qv_imagery_infBut_11[insitu_index].deleteLater()
    self.qv_imagery_infBut_12[insitu_index].deleteLater()
    self.qv_imagery_infBut_13[insitu_index].deleteLater()
    self.qv_imagery_lab_1[insitu_index].deleteLater()
    self.qv_imagery_lab_2[insitu_index].deleteLater()
    self.qv_imagery_lab_3[insitu_index].deleteLater()
    self.qv_imagery_lab_4[insitu_index].deleteLater()
    self.qv_imagery_lab_5[insitu_index].deleteLater()
    self.qv_imagery_lab_6[insitu_index].deleteLater()
    self.qv_imagery_lab_7[insitu_index].deleteLater()
    self.qv_imagery_lab_8[insitu_index].deleteLater()
    self.qv_imagery_lab_9[insitu_index].deleteLater()
    self.qv_imagery_lab_10[insitu_index].deleteLater()
    self.qv_imagery_lab_11[insitu_index].deleteLater()
    self.qv_imagery_lab_12[insitu_index].deleteLater()
    self.qv_imagery_lab_13[insitu_index].deleteLater()
    self.qv_imagery_lab_14[insitu_index].deleteLater()
    self.qv_imagery_lab_15[insitu_index].deleteLater()
    self.qv_imagery_lab_16[insitu_index].deleteLater()
    self.qv_imagery_lab_17[insitu_index].deleteLater()
    self.qv_imagery_lab_18[insitu_index].deleteLater()
    self.qv_imagery_lab_19[insitu_index].deleteLater()
    self.qv_imagery_lab_20[insitu_index].deleteLater()
    self.qv_imagery_lab_21[insitu_index].deleteLater()
    self.qv_imagery_lab_22[insitu_index].deleteLater()
    self.qv_imagery_lab_23[insitu_index].deleteLater()
    self.qv_imagery_lab_24[insitu_index].deleteLater()
    self.qv_imagery_lab_25[insitu_index].deleteLater()
    self.qv_imagery_lab_26[insitu_index].deleteLater()
    self.qv_imagery_lab_27[insitu_index].deleteLater()
    self.qv_imagery_lab_28[insitu_index].deleteLater()
    self.qv_imagery_lab_29[insitu_index].deleteLater()
    self.qv_imagery_lab_30[insitu_index].deleteLater()
    self.qv_imagery_lab_31[insitu_index].deleteLater()
    self.qv_imagery_lab_32[insitu_index].deleteLater()
    self.qv_imagery_lab_33[insitu_index].deleteLater()
    self.qv_imagery_lab_34[insitu_index].deleteLater()
    self.qv_imagery_line_1[insitu_index].deleteLater()
    self.qv_imagery_line_2[insitu_index].deleteLater()
    self.qv_imagery_line_3[insitu_index].deleteLater()
    self.qv_imagery_line_4[insitu_index].deleteLater()
    self.qv_imagery_line_5[insitu_index].deleteLater()
    self.qv_imagery_line_6[insitu_index].deleteLater()
    self.qv_imagery_line_7[insitu_index].deleteLater()
    self.qv_imagery_date_1[insitu_index].deleteLater()
    self.qv_imagery_date_2[insitu_index].deleteLater()
    self.qv_imagery_list_1[insitu_index].deleteLater()
    self.qv_imagery_check_1[insitu_index].deleteLater()
    self.qv_imagery_check_2[insitu_index].deleteLater()
    self.qv_imagery_check_3[insitu_index].deleteLater()
    self.qv_imagery_check_4[insitu_index].deleteLater()
    self.qv_imagery_check_5[insitu_index].deleteLater()
    self.qv_imagery_check_6[insitu_index].deleteLater()
    self.qv_imagery_check_7[insitu_index].deleteLater()
    self.qv_imagery_check_8[insitu_index].deleteLater()
    self.qv_imagery_check_9[insitu_index].deleteLater()
    self.qv_imagery_check_10[insitu_index].deleteLater()
    self.qv_imagery_check_11[insitu_index].deleteLater()
    self.qv_imagery_check_12[insitu_index].deleteLater()
    self.qv_imagery_check_13[insitu_index].deleteLater()
    self.qv_imagery_check_14[insitu_index].deleteLater()
    self.qv_imagery_check_15[insitu_index].deleteLater()
    self.qv_imagery_check_16[insitu_index].deleteLater()
    self.qv_imagery_check_17[insitu_index].deleteLater()
    self.qv_imagery_check_18[insitu_index].deleteLater()
    self.qv_imagery_check_19[insitu_index].deleteLater()
    self.qv_imagery_check_20[insitu_index].deleteLater()
    self.qv_imagery_check_21[insitu_index].deleteLater()
    self.qv_imagery_check_22[insitu_index].deleteLater()
    self.qv_imagery_check_23[insitu_index].deleteLater()
    self.qv_imagery_check_24[insitu_index].deleteLater()
    self.qv_imagery_check_25[insitu_index].deleteLater()
    self.qv_imagery_check_26[insitu_index].deleteLater()
    self.qv_imagery_check_27[insitu_index].deleteLater()
    self.qv_imagery_check_28[insitu_index].deleteLater()
    self.qv_imagery_check_29[insitu_index].deleteLater()
    self.qv_imagery_check_30[insitu_index].deleteLater()
    self.qv_imagery_check_31[insitu_index].deleteLater()
    self.qv_imagery_check_32[insitu_index].deleteLater()
    self.qv_imagery_group_1[insitu_index].deleteLater()
    self.qv_imagery_group_2[insitu_index].deleteLater()
    self.qv_imagery_group_3[insitu_index].deleteLater()
    self.qv_imagery_group_4[insitu_index].deleteLater()
    self.qv_imagery_group_5[insitu_index].deleteLater()
    self.qv_imagery_group_6[insitu_index].deleteLater()
    self.qv_imagery_group_7[insitu_index].deleteLater()
    self.qv_imagery_group_8[insitu_index].deleteLater()
    self.qv_imagery_group_9[insitu_index].deleteLater()
    self.qv_imagery_group_10[insitu_index].deleteLater()
    self.qv_imagery_group_11[insitu_index].deleteLater()
    self.qv_imagery_group_12[insitu_index].deleteLater()
    self.qv_imagery_group_13[insitu_index].deleteLater()
    self.qv_imagery_group_14[insitu_index].deleteLater()
    self.qv_imagery_group_15[insitu_index].deleteLater()
    self.qv_imagery_group_16[insitu_index].deleteLater()
    self.qv_imagery_tab_1[insitu_index].deleteLater()
    self.qv_imagery_scroll_1[insitu_index].deleteLater()
    self.qv_imagery_scroll_2[insitu_index].deleteLater()
    self.qv_imagery_verlay_1.pop(insitu_index)
    self.qv_imagery_horlay_1.pop(insitu_index)
    self.qv_imagery_horlay_2.pop(insitu_index)
    self.qv_imagery_horlay_3.pop(insitu_index)
    self.qv_imagery_horlay_4.pop(insitu_index)
    self.qv_imagery_horlay_5.pop(insitu_index)
    self.qv_imagery_horlay_6.pop(insitu_index)
    self.qv_imagery_horlay_7.pop(insitu_index)
    self.qv_imagery_horlay_8.pop(insitu_index)
    self.qv_imagery_horlay_9.pop(insitu_index)
    self.qv_imagery_horlay_10.pop(insitu_index)
    self.qv_imagery_horlay_11.pop(insitu_index)
    self.qv_imagery_horlay_12.pop(insitu_index)
    self.qv_imagery_horlay_13.pop(insitu_index)
    self.qv_imagery_horlay_14.pop(insitu_index)
    self.qv_imagery_horlay_15.pop(insitu_index)
    self.qv_imagery_horlay_16.pop(insitu_index)
    self.qv_imagery_horlay_17.pop(insitu_index)
    self.qv_imagery_horlay_18.pop(insitu_index)
    self.qv_imagery_horlay_19.pop(insitu_index)
    self.qv_imagery_horlay_20.pop(insitu_index)
    self.qv_imagery_horlay_21.pop(insitu_index)
    self.qv_imagery_horlay_22.pop(insitu_index)
    self.qv_imagery_horlay_23.pop(insitu_index)
    self.qv_imagery_horlay_24.pop(insitu_index)
    self.qv_imagery_horlay_25.pop(insitu_index)
    self.qv_imagery_horlay_26.pop(insitu_index)
    self.qv_imagery_horlay_27.pop(insitu_index)
    self.qv_imagery_horlay_28.pop(insitu_index)
    self.qv_imagery_horlay_29.pop(insitu_index)
    self.qv_imagery_horlay_30.pop(insitu_index)
    self.qv_imagery_horlay_31.pop(insitu_index)
    self.qv_imagery_horlay_32.pop(insitu_index)
    self.qv_imagery_gridlay_1.pop(insitu_index)
    self.qv_imagery_gridlay_2.pop(insitu_index)
    self.qv_imagery_gridlay_3.pop(insitu_index)
    self.qv_imagery_gridlay_4.pop(insitu_index)
    self.qv_imagery_gridlay_5.pop(insitu_index)
    self.qv_imagery_gridlay_6.pop(insitu_index)
    self.qv_imagery_gridlay_7.pop(insitu_index)
    self.qv_imagery_gridlay_8.pop(insitu_index)
    self.qv_imagery_infBut_1.pop(insitu_index)
    self.qv_imagery_infBut_2.pop(insitu_index)
    self.qv_imagery_infBut_3.pop(insitu_index)
    self.qv_imagery_infBut_4.pop(insitu_index)
    self.qv_imagery_infBut_5.pop(insitu_index)
    self.qv_imagery_infBut_6.pop(insitu_index)
    self.qv_imagery_infBut_7.pop(insitu_index)
    self.qv_imagery_infBut_8.pop(insitu_index)
    self.qv_imagery_infBut_9.pop(insitu_index)
    self.qv_imagery_infBut_10.pop(insitu_index)
    self.qv_imagery_infBut_11.pop(insitu_index)
    self.qv_imagery_infBut_12.pop(insitu_index)
    self.qv_imagery_infBut_13.pop(insitu_index)
    self.qv_imagery_lab_1.pop(insitu_index)
    self.qv_imagery_lab_2.pop(insitu_index)
    self.qv_imagery_lab_3.pop(insitu_index)
    self.qv_imagery_lab_4.pop(insitu_index)
    self.qv_imagery_lab_5.pop(insitu_index)
    self.qv_imagery_lab_6.pop(insitu_index)
    self.qv_imagery_lab_7.pop(insitu_index)
    self.qv_imagery_lab_8.pop(insitu_index)
    self.qv_imagery_lab_9.pop(insitu_index)
    self.qv_imagery_lab_10.pop(insitu_index)
    self.qv_imagery_lab_11.pop(insitu_index)
    self.qv_imagery_lab_12.pop(insitu_index)
    self.qv_imagery_lab_13.pop(insitu_index)
    self.qv_imagery_lab_14.pop(insitu_index)
    self.qv_imagery_lab_15.pop(insitu_index)
    self.qv_imagery_lab_16.pop(insitu_index)
    self.qv_imagery_lab_17.pop(insitu_index)
    self.qv_imagery_lab_18.pop(insitu_index)
    self.qv_imagery_lab_19.pop(insitu_index)
    self.qv_imagery_lab_20.pop(insitu_index)
    self.qv_imagery_lab_21.pop(insitu_index)
    self.qv_imagery_lab_22.pop(insitu_index)
    self.qv_imagery_lab_23.pop(insitu_index)
    self.qv_imagery_lab_24.pop(insitu_index)
    self.qv_imagery_lab_25.pop(insitu_index)
    self.qv_imagery_lab_26.pop(insitu_index)
    self.qv_imagery_lab_27.pop(insitu_index)
    self.qv_imagery_lab_28.pop(insitu_index)
    self.qv_imagery_lab_29.pop(insitu_index)
    self.qv_imagery_lab_30.pop(insitu_index)
    self.qv_imagery_lab_31.pop(insitu_index)
    self.qv_imagery_lab_32.pop(insitu_index)
    self.qv_imagery_lab_33.pop(insitu_index)
    self.qv_imagery_lab_34.pop(insitu_index)
    self.qv_imagery_line_1.pop(insitu_index)
    self.qv_imagery_line_2.pop(insitu_index)
    self.qv_imagery_line_3.pop(insitu_index)
    self.qv_imagery_line_4.pop(insitu_index)
    self.qv_imagery_line_5.pop(insitu_index)
    self.qv_imagery_line_6.pop(insitu_index)
    self.qv_imagery_line_7.pop(insitu_index)
    self.qv_imagery_date_1.pop(insitu_index)
    self.qv_imagery_date_2.pop(insitu_index)
    self.qv_imagery_list_1.pop(insitu_index)
    self.qv_imagery_check_1.pop(insitu_index)
    self.qv_imagery_check_2.pop(insitu_index)
    self.qv_imagery_check_3.pop(insitu_index)
    self.qv_imagery_check_4.pop(insitu_index)
    self.qv_imagery_check_5.pop(insitu_index)
    self.qv_imagery_check_6.pop(insitu_index)
    self.qv_imagery_check_7.pop(insitu_index)
    self.qv_imagery_check_8.pop(insitu_index)
    self.qv_imagery_check_9.pop(insitu_index)
    self.qv_imagery_check_10.pop(insitu_index)
    self.qv_imagery_check_11.pop(insitu_index)
    self.qv_imagery_check_12.pop(insitu_index)
    self.qv_imagery_check_13.pop(insitu_index)
    self.qv_imagery_check_14.pop(insitu_index)
    self.qv_imagery_check_15.pop(insitu_index)
    self.qv_imagery_check_16.pop(insitu_index)
    self.qv_imagery_check_17.pop(insitu_index)
    self.qv_imagery_check_18.pop(insitu_index)
    self.qv_imagery_check_19.pop(insitu_index)
    self.qv_imagery_check_20.pop(insitu_index)
    self.qv_imagery_check_21.pop(insitu_index)
    self.qv_imagery_check_22.pop(insitu_index)
    self.qv_imagery_check_23.pop(insitu_index)
    self.qv_imagery_check_24.pop(insitu_index)
    self.qv_imagery_check_25.pop(insitu_index)
    self.qv_imagery_check_26.pop(insitu_index)
    self.qv_imagery_check_27.pop(insitu_index)
    self.qv_imagery_check_28.pop(insitu_index)
    self.qv_imagery_check_29.pop(insitu_index)
    self.qv_imagery_check_30.pop(insitu_index)
    self.qv_imagery_check_31.pop(insitu_index)
    self.qv_imagery_check_32.pop(insitu_index)
    self.qv_imagery_group_1.pop(insitu_index)
    self.qv_imagery_group_2.pop(insitu_index)
    self.qv_imagery_group_3.pop(insitu_index)
    self.qv_imagery_group_4.pop(insitu_index)
    self.qv_imagery_group_5.pop(insitu_index)
    self.qv_imagery_group_6.pop(insitu_index)
    self.qv_imagery_group_7.pop(insitu_index)
    self.qv_imagery_group_8.pop(insitu_index)
    self.qv_imagery_group_9.pop(insitu_index)
    self.qv_imagery_group_10.pop(insitu_index)
    self.qv_imagery_group_11.pop(insitu_index)
    self.qv_imagery_group_12.pop(insitu_index)
    self.qv_imagery_group_13.pop(insitu_index)
    self.qv_imagery_group_14.pop(insitu_index)
    self.qv_imagery_group_15.pop(insitu_index)
    self.qv_imagery_group_16.pop(insitu_index)
    self.qv_imagery_tab_1.pop(insitu_index)
    self.qv_imagery_scroll_1.pop(insitu_index)
    self.qv_imagery_scroll_2.pop(insitu_index)
    self.qv_imagery_line_list[0].pop(insitu_index)
    self.qv_imagery_line_list[1].pop(insitu_index)
    self.qv_imagery_line_list[2].pop(insitu_index)
    self.qv_imagery_line_list[3].pop(insitu_index)
    self.qv_imagery_line_list[4].pop(insitu_index)
    self.qv_imagery_line_list[5].pop(insitu_index)
    self.qv_imagery_line_list[6].pop(insitu_index)
    self.qv_imagery_combo_list[0].pop(insitu_index)
    self.qv_imagery_combo_list[1].pop(insitu_index)
    self.qv_imagery_date_list[0].pop(insitu_index)
    self.qv_imagery_date_list[1].pop(insitu_index)
    self.qv_imagery_radio_list[0].pop(insitu_index)
    self.qv_imagery_radio_list[1].pop(insitu_index)
    self.qv_imagery_radio_list[2].pop(insitu_index)
    self.qv_imagery_radio_list[3].pop(insitu_index)
    self.qv_imagery_radio_list[4].pop(insitu_index)
    self.qv_imagery_radio_list[5].pop(insitu_index)
    self.qv_imagery_radio_list[6].pop(insitu_index)
    self.qv_imagery_radio_list[7].pop(insitu_index)
    self.qv_imagery_radio_list[8].pop(insitu_index)
    self.qv_imagery_radio_list[9].pop(insitu_index)
    self.qv_imagery_radio_list[10].pop(insitu_index)
    self.qv_imagery_radio_list[11].pop(insitu_index)
    self.qv_imagery_radio_list[12].pop(insitu_index)
    self.qv_imagery_radio_list[13].pop(insitu_index)
    self.qv_imagery_radio_list[14].pop(insitu_index)
    self.qv_imagery_radio_list[15].pop(insitu_index)
    self.qv_imagery_horlay_33[insitu_index].deleteLater()
    self.qv_imagery_horlay_33.pop(insitu_index)
    self.qv_imagery_lab_35[insitu_index].deleteLater()
    self.qv_imagery_lab_35.pop(insitu_index)
    self.qv_imagery_list_2[insitu_index].deleteLater()
    self.qv_imagery_list_2.pop(insitu_index)
    self.qv_imagery_infBut_14[insitu_index].deleteLater()
    self.qv_imagery_infBut_14.pop(insitu_index)
    self.qv_imagery_horlay_34[insitu_index].deleteLater()
    self.qv_imagery_lab_36[insitu_index].deleteLater()
    self.qv_imagery_list_3[insitu_index].deleteLater()
    self.qv_imagery_lab_37[insitu_index].deleteLater()
    self.qv_imagery_list_4[insitu_index].deleteLater()
    self.qv_imagery_contBut_1[insitu_index].deleteLater()
    self.qv_imagery_infBut_15[insitu_index].deleteLater()
    self.qv_imagery_horlay_34.pop(insitu_index)
    self.qv_imagery_lab_36.pop(insitu_index)
    self.qv_imagery_list_3.pop(insitu_index)
    self.qv_imagery_lab_37.pop(insitu_index)
    self.qv_imagery_list_4.pop(insitu_index)
    self.qv_imagery_contBut_1.pop(insitu_index)
    self.qv_imagery_infBut_15.pop(insitu_index)
    self.qv_imagery -= 1
    if self.qv_insitu == 0 and self.qv_imagery == 0:
        self.qv_tabWidget.setVisible(False)
        self.qv_tabWidget.setEnabled(False)
        self.qv_spacerItem.changeSize(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
    else:
        j = 0
        for i in range(self.qv_tabWidget.count()):
            if "Earth" in self.qv_tabWidget.tabText(i):
                self.qv_tabWidget.setTabText(i, "Earth observation/Remote sensing data " + str(j + 1))
                self.qv_imagery_line_list[0][j][3] = i
                self.qv_imagery_line_list[1][j][3] = i
                self.qv_imagery_line_list[2][j][3] = i
                self.qv_imagery_line_list[3][j][3] = i
                self.qv_imagery_line_list[4][j][3] = i
                self.qv_imagery_line_list[5][j][3] = i
                self.qv_imagery_line_list[6][j][3] = i
                self.qv_imagery_combo_list[0][j][2] = i
                self.qv_imagery_combo_list[1][j][2] = i
                self.qv_imagery_date_list[0][j][2] = i
                self.qv_imagery_date_list[1][j][2] = i
                self.qv_imagery_radio_list[0][j][2] = i
                self.qv_imagery_radio_list[1][j][2] = i
                self.qv_imagery_radio_list[2][j][2] = i
                self.qv_imagery_radio_list[3][j][2] = i
                self.qv_imagery_radio_list[4][j][2] = i
                self.qv_imagery_radio_list[5][j][2] = i
                self.qv_imagery_radio_list[6][j][2] = i
                self.qv_imagery_radio_list[7][j][2] = i
                self.qv_imagery_radio_list[8][j][2] = i
                self.qv_imagery_radio_list[9][j][2] = i
                self.qv_imagery_radio_list[10][j][2] = i
                self.qv_imagery_radio_list[11][j][2] = i
                self.qv_imagery_radio_list[12][j][2] = i
                self.qv_imagery_radio_list[13][j][2] = i
                self.qv_imagery_radio_list[14][j][2] = i
                self.qv_imagery_radio_list[15][j][2] = i
                j += 1
        if len(self.qv_imagery_verlay_1) > 0:
            for i in range(len(self.qv_imagery_verlay_1)):
                self.qv_imagery_tab_1[i].setObjectName("qv_imagery_tab_1_" + str(i))
                self.qv_imagery_gridlay_8[i].setObjectName("qv_imagery_gridlay_8_" + str(i))
                self.qv_imagery_scroll_1[i].setObjectName("qv_imagery_scroll_1_" + str(i))
                self.qv_imagery_scroll_2[i].setObjectName("qv_imagery_scroll_2_" + str(i))
                self.qv_imagery_verlay_1[i].setObjectName("qv_imagery_verlay_1_" + str(i))
                self.qv_imagery_horlay_1[i].setObjectName("qv_imagery_horlay_1_" + str(i))
                self.qv_imagery_lab_1[i].setObjectName("qv_imagery_lab_1_" + str(i))
                self.qv_imagery_horlay_2[i].setObjectName("qv_imagery_horlay_2_" + str(i))
                self.qv_imagery_gridlay_1[i].setObjectName("qv_imagery_gridlay_1_" + str(i))
                self.qv_imagery_lab_2[i].setObjectName("qv_imagery_lab_2_" + str(i))
                self.qv_imagery_line_1[i].setObjectName("qv_imagery_line_1_" + str(i))
                self.qv_imagery_lab_3[i].setObjectName("qv_imagery_lab_3_" + str(i))
                self.qv_imagery_date_1[i].setObjectName("qv_imagery_date_1" + str(i))
                self.qv_imagery_lab_4[i].setObjectName("qv_imagery_lab_4_" + str(i))
                self.qv_imagery_date_2[i].setObjectName("qv_imagery_date_2_" + str(i))
                self.qv_imagery_horlay_3[i].setObjectName("qv_imagery_horlay_3_" + str(i))
                self.qv_imagery_lab_5[i].setObjectName("qv_imagery_lab_5_" + str(i))
                self.qv_imagery_horlay_4[i].setObjectName("qv_imagery_horlay_4_" + str(i))
                self.qv_imagery_gridlay_2[i].setObjectName("qv_imagery_gridlay_2_" + str(i))
                self.qv_imagery_lab_6[i].setObjectName("qv_imagery_lab_6_" + str(i))
                self.qv_imagery_horlay_8[i].setObjectName("qv_imagery_horlay_8_" + str(i))
                self.qv_imagery_line_2[i].setObjectName("qv_imagery_line_2_" + str(i))
                self.qv_imagery_lab_7[i].setObjectName("qv_imagery_lab_7_" + str(i))
                self.qv_imagery_line_3[i].setObjectName("qv_imagery_line_3_" + str(i))
                self.qv_imagery_lab_8[i].setObjectName("qv_imagery_lab_8_" + str(i))
                self.qv_imagery_line_4[i].setObjectName("qv_imagery_line_4_" + str(i))
                self.qv_imagery_lab_9[i].setObjectName("qv_imagery_lab_9_" + str(i))
                self.qv_imagery_line_5[i].setObjectName("qv_imagery_line_5_" + str(i))
                self.qv_imagery_lab_10[i].setObjectName("qv_imagery_lab_10_" + str(i))
                self.qv_imagery_line_6[i].setObjectName("qv_imagery_line_6_" + str(i))
                self.qv_imagery_lab_11[i].setObjectName("qv_imagery_lab_11_" + str(i))
                self.qv_imagery_line_7[i].setObjectName("qv_imagery_line_7_" + str(i))
                self.qv_imagery_horlay_5[i].setObjectName("qv_imagery_horlay_5_" + str(i))
                self.qv_imagery_lab_12[i].setObjectName("qv_imagery_lab_12_" + str(i))
                self.qv_imagery_horlay_6[i].setObjectName("qv_imagery_horlay_6_" + str(i))
                self.qv_imagery_gridlay_3[i].setObjectName("qv_imagery_gridlay_3_" + str(i))
                self.qv_imagery_lab_13[i].setObjectName("qv_imagery_lab_13_" + str(i))
                self.qv_imagery_list_1[i].setObjectName("qv_imagery_list_1_" + str(i))
                self.qv_imagery_lab_14[i].setObjectName("qv_imagery_lab_14_" + str(i))
                self.qv_imagery_horlay_7[i].setObjectName("qv_imagery_horlay_7_" + str(i))
                self.qv_imagery_check_1[i].setObjectName("qv_imagery_check_1_" + str(i))
                self.qv_imagery_check_2[i].setObjectName("qv_imagery_check_2_" + str(i))
                self.qv_imagery_group_1[i].setObjectName("qv_imagery_group_1_" + str(i))
                self.qv_imagery_horlay_9[i].setObjectName("qv_imagery_horlay_9_" + str(i))
                self.qv_imagery_lab_15[i].setObjectName("qv_imagery_lab_15_" + str(i))
                self.qv_imagery_horlay_10[i].setObjectName("qv_imagery_horlay_10_" + str(i))
                self.qv_imagery_lab_16[i].setObjectName("qv_imagery_lab_16_" + str(i))
                self.qv_imagery_horlay_11[i].setObjectName("qv_imagery_horlay_11_" + str(i))
                self.qv_imagery_gridlay_4[i].setObjectName("qv_imagery_gridlay_4_" + str(i))
                self.qv_imagery_lab_17[i].setObjectName("qv_imagery_lab_17_" + str(i))
                self.qv_imagery_lab_18[i].setObjectName("qv_imagery_lab_18_" + str(i))
                self.qv_imagery_horlay_12[i].setObjectName("qv_imagery_horlay_12_" + str(i))
                self.qv_imagery_check_3[i].setObjectName("qv_imagery_check_3_" + str(i))
                self.qv_imagery_check_4[i].setObjectName("qv_imagery_check_4_" + str(i))
                self.qv_imagery_group_2[i].setObjectName("qv_imagery_group_2_" + str(i))
                self.qv_imagery_horlay_13[i].setObjectName("qv_imagery_horlay_13_" + str(i))
                self.qv_imagery_check_5[i].setObjectName("qv_imagery_check_5_" + str(i))
                self.qv_imagery_check_6[i].setObjectName("qv_imagery_check_6_" + str(i))
                self.qv_imagery_group_3[i].setObjectName("qv_imagery_group_3_" + str(i))
                self.qv_imagery_horlay_14[i].setObjectName("qv_imagery_horlay_14_" + str(i))
                self.qv_imagery_lab_19[i].setObjectName("qv_imagery_lab_19_" + str(i))
                self.qv_imagery_horlay_15[i].setObjectName("qv_imagery_horlay_15_" + str(i))
                self.qv_imagery_gridlay_5[i].setObjectName("qv_imagery_gridlay_5_" + str(i))
                self.qv_imagery_lab_20[i].setObjectName("qv_imagery_lab_20_" + str(i))
                self.qv_imagery_lab_21[i].setObjectName("qv_imagery_lab_21_" + str(i))
                self.qv_imagery_horlay_16[i].setObjectName("qv_imagery_horlay_16_" + str(i))
                self.qv_imagery_check_7[i].setObjectName("qv_imagery_check_7_" + str(i))
                self.qv_imagery_check_8[i].setObjectName("qv_imagery_check_8_" + str(i))
                self.qv_imagery_group_4[i].setObjectName("qv_imagery_group_4_" + str(i))
                self.qv_imagery_horlay_17[i].setObjectName("qv_imagery_horlay_17_" + str(i))
                self.qv_imagery_check_9[i].setObjectName("qv_imagery_check_9_" + str(i))
                self.qv_imagery_check_10[i].setObjectName("qv_imagery_check_10_" + str(i))
                self.qv_imagery_group_5[i].setObjectName("qv_imagery_group_5_" + str(i))
                self.qv_imagery_horlay_18[i].setObjectName("qv_imagery_horlay_18_" + str(i))
                self.qv_imagery_lab_22[i].setObjectName("qv_imagery_lab_22_" + str(i))
                self.qv_imagery_horlay_19[i].setObjectName("qv_imagery_horlay_19_" + str(i))
                self.qv_imagery_gridlay_6[i].setObjectName("qv_imagery_gridlay_6_" + str(i))
                self.qv_imagery_lab_23[i].setObjectName("qv_imagery_lab_23_" + str(i))
                self.qv_imagery_lab_24[i].setObjectName("qv_imagery_lab_24_" + str(i))
                self.qv_imagery_lab_25[i].setObjectName("qv_imagery_lab_25_" + str(i))
                self.qv_imagery_lab_26[i].setObjectName("qv_imagery_lab_26_" + str(i))
                self.qv_imagery_horlay_20[i].setObjectName("qv_imagery_horlay_20_" + str(i))
                self.qv_imagery_check_11[i].setObjectName("qv_imagery_check_11_" + str(i))
                self.qv_imagery_check_12[i].setObjectName("qv_imagery_check_12_" + str(i))
                self.qv_imagery_group_6[i].setObjectName("qv_imagery_group_6_" + str(i))
                self.qv_imagery_horlay_21[i].setObjectName("qv_imagery_horlay_21_" + str(i))
                self.qv_imagery_check_13[i].setObjectName("qv_imagery_check_13_" + str(i))
                self.qv_imagery_check_14[i].setObjectName("qv_imagery_check_14_" + str(i))
                self.qv_imagery_group_7[i].setObjectName("qv_imagery_group_7_" + str(i))
                self.qv_imagery_horlay_22[i].setObjectName("qv_imagery_horlay_22_" + str(i))
                self.qv_imagery_check_15[i].setObjectName("qv_imagery_check_15_" + str(i))
                self.qv_imagery_check_16[i].setObjectName("qv_imagery_check_16_" + str(i))
                self.qv_imagery_group_8[i].setObjectName("qv_imagery_group_8_" + str(i))
                self.qv_imagery_horlay_23[i].setObjectName("qv_imagery_horlay_23_" + str(i))
                self.qv_imagery_check_17[i].setObjectName("qv_imagery_check_17_" + str(i))
                self.qv_imagery_check_18[i].setObjectName("qv_imagery_check_18_" + str(i))
                self.qv_imagery_group_9[i].setObjectName("qv_imagery_group_9_" + str(i))
                self.qv_imagery_horlay_24[i].setObjectName("qv_imagery_horlay_24_" + str(i))
                self.qv_imagery_lab_27[i].setObjectName("qv_imagery_lab_27_" + str(i))
                self.qv_imagery_horlay_25[i].setObjectName("qv_imagery_horlay_25_" + str(i))
                self.qv_imagery_gridlay_7[i].setObjectName("qv_imagery_gridlay_7_" + str(i))
                self.qv_imagery_lab_28[i].setObjectName("qv_imagery_lab_28_" + str(i))
                self.qv_imagery_lab_29[i].setObjectName("qv_imagery_lab_29_" + str(i))
                self.qv_imagery_lab_30[i].setObjectName("qv_imagery_lab_30_" + str(i))
                self.qv_imagery_lab_31[i].setObjectName("qv_imagery_lab_31_" + str(i))
                self.qv_imagery_lab_32[i].setObjectName("qv_imagery_lab_32_" + str(i))
                self.qv_imagery_lab_33[i].setObjectName("qv_imagery_lab_33_" + str(i))
                self.qv_imagery_lab_34[i].setObjectName("qv_imagery_lab_34_" + str(i))
                self.qv_imagery_horlay_26[i].setObjectName("qv_imagery_horlay_26_" + str(i))
                self.qv_imagery_check_19[i].setObjectName("qv_imagery_check_19_" + str(i))
                self.qv_imagery_check_20[i].setObjectName("qv_imagery_check_20_" + str(i))
                self.qv_imagery_group_10[i].setObjectName("qv_imagery_group_10_" + str(i))
                self.qv_imagery_horlay_27[i].setObjectName("qv_imagery_horlay_27_" + str(i))
                self.qv_imagery_check_21[i].setObjectName("qv_imagery_check_21_" + str(i))
                self.qv_imagery_check_22[i].setObjectName("qv_imagery_check_22_" + str(i))
                self.qv_imagery_group_11[i].setObjectName("qv_imagery_group_11_" + str(i))
                self.qv_imagery_horlay_28[i].setObjectName("qv_imagery_horlay_28_" + str(i))
                self.qv_imagery_check_23[i].setObjectName("qv_imagery_check_23_" + str(i))
                self.qv_imagery_check_24[i].setObjectName("qv_imagery_check_24_" + str(i))
                self.qv_imagery_group_12[i].setObjectName("qv_imagery_group_12_" + str(i))
                self.qv_imagery_horlay_29[i].setObjectName("qv_imagery_horlay_29_" + str(i))
                self.qv_imagery_check_25[i].setObjectName("qv_imagery_check_25_" + str(i))
                self.qv_imagery_check_26[i].setObjectName("qv_imagery_check_26_" + str(i))
                self.qv_imagery_group_13[i].setObjectName("qv_imagery_group_13_" + str(i))
                self.qv_imagery_horlay_30[i].setObjectName("qv_imagery_horlay_30_" + str(i))
                self.qv_imagery_check_27[i].setObjectName("qv_imagery_check_27_" + str(i))
                self.qv_imagery_check_28[i].setObjectName("qv_imagery_check_28_" + str(i))
                self.qv_imagery_group_14[i].setObjectName("qv_imagery_group_14_" + str(i))
                self.qv_imagery_horlay_31[i].setObjectName("qv_imagery_horlay_31_" + str(i))
                self.qv_imagery_check_29[i].setObjectName("qv_imagery_check_29_" + str(i))
                self.qv_imagery_check_30[i].setObjectName("qv_imagery_check_30_" + str(i))
                self.qv_imagery_group_15[i].setObjectName("qv_imagery_group_15_" + str(i))
                self.qv_imagery_horlay_32[i].setObjectName("qv_imagery_horlay_32_" + str(i))
                self.qv_imagery_check_31[i].setObjectName("qv_imagery_check_31_" + str(i))
                self.qv_imagery_check_32[i].setObjectName("qv_imagery_check_32_" + str(i))
                self.qv_imagery_group_16[i].setObjectName("qv_imagery_group_16_" + str(i))
                self.qv_imagery_horlay_33[i].setObjectName("qv_imagery_horlay_33_" + str(i))
                self.qv_imagery_lab_35[i].setObjectName("qv_imagery_lab_35_" + str(i))
                self.qv_imagery_list_2[i].setObjectName("qv_imagery_list_2_" + str(i))
                self.qv_imagery_horlay_34[i].setObjectName("qv_imagery_horlay_34_" + str(i))
                self.qv_imagery_lab_36[i].setObjectName("qv_imagery_lab_36_" + str(i))
                self.qv_imagery_list_3[i].setObjectName("qv_imagery_list_3_" + str(i))
                self.qv_imagery_lab_37[i].setObjectName("qv_imagery_lab_37_" + str(i))
                self.qv_imagery_list_4[i].setObjectName("qv_imagery_list_4_" + str(i))
                self.qv_imagery_contBut_1[i].setObjectName("qv_imagery_contBut_1_" + str(i))
                self.qv_imagery_infBut_15[i].setObjectName("qv_imagery_infBut_15_" + str(i))
    qv_update_tab_list(self, "imagery")

def plusButton_12_clicked(self):
    if self.qv_insitu == 0 and self.qv_imagery == 0:
        self.qv_tabWidget.setVisible(True)
        self.qv_tabWidget.setEnabled(True)
        self.qv_spacerItem.changeSize(20, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.qv_tabWidget.setStyleSheet("QTabWidget::pane {\n"
        "    border: 1px solid rgb(180,180,180);\n"
        "    border-bottom-left-radius: 5px;\n"
        "    border-bottom-right-radius: 5px;\n"
        "    border-top-right-radius: 5px;\n"
        "    top: -1px;\n"
        "    background-color: rgb(230,230,230);\n"
        "}\n"
        "\n"
        "QTabWidget::tab-bar {\n"
        "    left: 0px; \n"
        "}\n"
        "\n"
        "QTabBar::tab {\n"
        "    background: transparent;\n"
        "    border-top: 1px solid rgb(180,180,180);\n"
        "    border-left: 1px solid rgb(180,180,180);\n"
        "    border-right: 1px solid rgb(180,180,180);\n"
        "    border-top-right-radius: 5px;\n"
        "    border-top-left-radius: 5px;\n"
        "    padding: 2px 10px 2px 10px;\n"
        "    margin-right: 2px;\n"
        "}\n"
        "\n"
        "QTabBar::tab:hover {\n"
        "    background-color: rgb(210,210,210);\n"
        "}\n"
        "\n"
        "QTabBar::tab:selected {\n"
        "    background: rgb(230,230,230);\n"
        "}\n"
        "\n"
        "QTabBar::tab:!selected {\n"
        "    margin-top: 4px; \n"
        "}\n"
        "\n"
        "QTabBar::scroller {\n"
        "}\n"
        "\n"
        "QTabBar QToolButton {\n"
        "    border: 1px solid rgb(180,180,180);\n"
        "    background-color: rgb(240,240,240);\n"
        "}\n"
        "\n"
        "QTabBar QToolButton:hover {\n"
        "    background-color: rgb(219, 219, 219);\n"
        "}\n"
        "\n"
        "QTabBar QToolButton::right-arrow {\n"
        "    image: url(icons/right_arrow_icon.svg); \n"
        "    width: 16px;\n"
        "    height: 16px;\n"
        "    margin : 2px 2px 2px 2px;\n"
        "}\n"
        "\n"
        "QTabBar QToolButton::right-arrow:pressed {\n"
        "    right: -1px;\n"
        "    bottom: -1px;\n"
        "}\n"
        "\n"
        "QTabBar QToolButton::left-arrow {\n"
        "    image: url(icons/left_arrow_icon.svg); \n"
        "    width: 16px;\n"
        "    height: 16px;\n"
        "    margin : 2px 2px 2px 2px;\n"
        "}\n"
        "\n"
        "QTabBar QToolButton::left-arrow:pressed {\n"
        "    right: -1px;\n"
        "    bottom: -1px;\n"
        "}")
    font2 = QtGui.QFont()
    font2.setFamily("font/SourceSansPro-Regular.ttf")
    font2.setPointSize(10)
    font2.setBold(True)
    font2.setUnderline(True)
    font2.setWeight(75)
    font2.setStyleStrategy(QtGui.QFont.PreferAntialias)
    font2.setKerning(True)
    font = QtGui.QFont()
    font.setFamily("font/SourceSansPro-Regular.ttf")
    font.setPointSize(10)
    font.setStyleStrategy(QtGui.QFont.PreferAntialias)
    font.setKerning(True)
    font3 = QtGui.QFont()
    font3.setFamily("font/SourceSansPro-Regular.ttf")
    font3.setPointSize(9)
    font3.setStyleStrategy(QtGui.QFont.PreferAntialias)
    font3.setKerning(True)
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap("icons/info_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    icon2 = QtGui.QIcon()
    icon2.addPixmap(QtGui.QPixmap("icons/continue_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    self.qv_insitu_tab_1.append(QtWidgets.QWidget())
    self.qv_insitu_tab_1[self.qv_insitu].setObjectName("qv_insitu_tab_1_" + str(self.qv_insitu))
    self.qv_tabWidget.addTab(self.qv_insitu_tab_1[self.qv_insitu], "Atmospheric/In-situ data " + str(self.qv_insitu + 1))
    self.qv_insitu_gridlay_3.append(QtWidgets.QGridLayout(self.qv_insitu_tab_1[self.qv_insitu]))
    self.qv_insitu_gridlay_3[self.qv_insitu].setContentsMargins(0, 0, 0, 0)
    self.qv_insitu_gridlay_3[self.qv_insitu].setObjectName("qv_insitu_gridlay_3_" + str(self.qv_insitu))
    self.qv_insitu_scroll_1.append(QtWidgets.QScrollArea(self.qv_insitu_tab_1[self.qv_insitu]))
    self.qv_insitu_scroll_1[self.qv_insitu].setStyleSheet("QScrollArea { background: transparent; }\n"
    "\n"
    "QScrollArea > QWidget > QWidget { background: transparent; }\n"
    "\n"
    "QScrollBar:vertical {\n"
    "  border: 1px solid white;\n"
    "  background-color: rgb(240, 240, 240);\n"
    "  width: 20px;\n"
    "  margin: 21px 0px 21px 0px;\n"
    "}\n"
    "\n"
    "QScrollBar:horizontal {\n"
    "  border: 1px solid white;\n"
    "  background-color: rgb(240, 240, 240);\n"
    "  height: 20px;\n"
    "  margin: 0px 21px 0px 21px;\n"
    "}\n"
    "\n"
    "QScrollBar::handle:vertical {\n"
    "  background-color: rgb(205, 205, 205);\n"
    "  min-height: 25px;\n"
    "}\n"
    "\n"
    "QScrollBar:handle:vertical:hover {\n"
    "  background-color: rgb(167, 167, 167);\n"
    "}\n"
    "\n"
    "QScrollBar::handle:horizontal {\n"
    "  background-color: rgb(205, 205, 205);\n"
    "  min-width: 25px;\n"
    "}\n"
    "\n"
    "QScrollBar:handle:horizontal:hover {\n"
    "  background-color: rgb(167, 167, 167);\n"
    "}\n"
    "\n"
    "QScrollBar::add-line:vertical {\n"
    "  border-top: 1px solid rgb(240,240,240);\n"
    "  border-left: 1px solid white;\n"
    "  border-right: 1px solid white;\n"
    "  border-bottom: 1px solid white;\n"
    "  background-color: rgb(240, 240, 240);\n"
    "  height: 20px;\n"
    "  subcontrol-position: bottom;\n"
    "  subcontrol-origin: margin;\n"
    "}\n"
    "\n"
    "QScrollBar::add-line:vertical:hover {\n"
    "  background-color: rgb(219, 219, 219);\n"
    "}\n"
    "\n"
    "QScrollBar::sub-line:vertical {\n"
    "  border-top: 1px solid white;\n"
    "  border-left: 1px solid white;\n"
    "  border-right: 1px solid white;\n"
    "  border-bottom: 1px solid rgb(240,240,240);\n"
    "  background-color: rgb(240, 240, 240);\n"
    "  height: 20px;\n"
    "  subcontrol-position: top;\n"
    "  subcontrol-origin: margin;\n"
    "}\n"
    "\n"
    "QScrollBar::sub-line:vertical:hover {\n"
    "  background-color: rgb(219, 219, 219);\n"
    "}\n"
    "\n"
    "QScrollBar::up-arrow:vertical {\n"
    "  image: url(icons/up_arrow_icon.svg); \n"
    "  width: 16px;\n"
    "  height: 16px;\n"
    "}\n"
    "\n"
    "QScrollBar::up-arrow:vertical:pressed {\n"
    "  right: -1px;\n"
    "  bottom: -1px;\n"
    "}\n"
    "\n"
    "QScrollBar::down-arrow:vertical {\n"
    "  image: url(icons/down_arrow_icon.svg); \n"
    "  width: 16px;\n"
    "  height: 16px;\n"
    "}\n"
    "\n"
    "QScrollBar::down-arrow:vertical:pressed {\n"
    "  right: -1px;\n"
    "  bottom: -1px;\n"
    "}\n"
    "\n"
    "\n"
    "\n"
    "\n"
    "QScrollBar::add-line:horizontal {\n"
    "  border-top: 1px solid white;\n"
    "  border-left: 1px solid rgb(240,240,240);\n"
    "  border-right: 1px solid white;\n"
    "  border-bottom: 1px solid white;\n"
    "  background-color: rgb(240, 240, 240);\n"
    "  width: 20px;\n"
    "  subcontrol-position: right;\n"
    "  subcontrol-origin: margin;\n"
    "}\n"
    "\n"
    "QScrollBar::add-line:horizontal:hover {\n"
    "  background-color: rgb(219, 219, 219);\n"
    "}\n"
    "\n"
    "QScrollBar::sub-line:horizontal {\n"
    "  border-top: 1px solid white;\n"
    "  border-left: 1px solid white;\n"
    "  border-right: 1px solid rgb(240,240,240);\n"
    "  border-bottom: 1px solid white;\n"
    "  background-color: rgb(240, 240, 240);\n"
    "  width: 20px;\n"
    "  subcontrol-position: left;\n"
    "  subcontrol-origin: margin;\n"
    "}\n"
    "\n"
    "QScrollBar::sub-line:horizontal:hover {\n"
    "  background-color: rgb(219, 219, 219);\n"
    "}\n"
    "\n"
    "QScrollBar::left-arrow:horizontal {\n"
    "  image: url(icons/left_arrow_icon.svg); \n"
    "  width: 16px;\n"
    "  height: 16px;\n"
    "}\n"
    "\n"
    "QScrollBar::left-arrow:horizontal:pressed {\n"
    "  right: -1px;\n"
    "  bottom: -1px;\n"
    "}\n"
    "\n"
    "QScrollBar::right-arrow:horizontal {\n"
    "  image: url(icons/right_arrow_icon.svg); \n"
    "  width: 16px;\n"
    "  height: 16px;\n"
    "}\n"
    "\n"
    "QScrollBar::right-arrow:horizontal:pressed {\n"
    "  right: -1px;\n"
    "  bottom: -1px;\n"
    "}")
    self.qv_insitu_scroll_1[self.qv_insitu].setFrameShape(QtWidgets.QFrame.NoFrame)
    self.qv_insitu_scroll_1[self.qv_insitu].setWidgetResizable(True)
    self.qv_insitu_scroll_1[self.qv_insitu].setObjectName("qv_insitu_scroll_1_" + str(self.qv_insitu))
    self.qv_insitu_scroll_2.append(QtWidgets.QWidget())
    self.qv_insitu_scroll_2[self.qv_insitu].setObjectName("qv_insitu_scroll_2_" + str(self.qv_insitu))
    self.qv_insitu_scroll_1[self.qv_insitu].setWidget(self.qv_insitu_scroll_2[self.qv_insitu])
    self.qv_insitu_gridlay_3[self.qv_insitu].addWidget(self.qv_insitu_scroll_1[self.qv_insitu], 0, 0, 1, 1)
    self.qv_insitu_verlay_1.append(QtWidgets.QVBoxLayout(self.qv_insitu_scroll_2[self.qv_insitu]))
    self.qv_insitu_verlay_1[self.qv_insitu].setObjectName("qv_insitu_verlay_1_" + str(self.qv_insitu))
    self.qv_insitu_verlay_1[self.qv_insitu].addItem(QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, 
                                                                          QtWidgets.QSizePolicy.Fixed))
    self.qv_insitu_horlay_15.append(QtWidgets.QHBoxLayout())
    self.qv_insitu_horlay_15[self.qv_insitu].setObjectName("qv_insitu_horlay_15_" + str(self.qv_insitu))
    self.qv_insitu_verlay_1[self.qv_insitu].addLayout(self.qv_insitu_horlay_15[self.qv_insitu])
    self.qv_insitu_horlay_15[self.qv_insitu].addItem(QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Fixed, 
                                                                          QtWidgets.QSizePolicy.Minimum))
    self.qv_insitu_lab_11.append(QtWidgets.QLabel())
    self.qv_insitu_lab_11[self.qv_insitu].setMinimumSize(QtCore.QSize(0, 27))
    self.qv_insitu_lab_11[self.qv_insitu].setMaximumSize(QtCore.QSize(16777215, 27))
    self.qv_insitu_lab_11[self.qv_insitu].setFont(font2)
    self.qv_insitu_lab_11[self.qv_insitu].setObjectName("qv_insitu_lab_11_" + str(self.qv_insitu))
    self.qv_insitu_lab_11[self.qv_insitu].setText("Tab controls")
    self.qv_insitu_horlay_15[self.qv_insitu].addWidget(self.qv_insitu_lab_11[self.qv_insitu])
    self.qv_insitu_horlay_15[self.qv_insitu].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, 
                                                                          QtWidgets.QSizePolicy.Minimum))
    self.qv_insitu_list_2.append(QtWidgets.QComboBox())
    self.qv_insitu_list_2[self.qv_insitu].setMinimumSize(QtCore.QSize(310, 27))
    self.qv_insitu_list_2[self.qv_insitu].setMaximumSize(QtCore.QSize(310, 27))
    self.qv_insitu_list_2[self.qv_insitu].setFont(font3)
    self.qv_insitu_list_2[self.qv_insitu].setStyleSheet("QComboBox {\n"
    "    border: 1px solid #acacac;\n"
    "    border-radius: 1px;\n"
    "    padding-left: 5px;\n"
    "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
    "stop: 0 #f0f0f0, stop: 1 #e5e5e5);\n"
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
    "stop: 0 #ecf4fc, stop: 1 #dcecfc);\n"
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
    self.qv_insitu_list_2[self.qv_insitu].setFrame(False)
    self.qv_insitu_list_2[self.qv_insitu].setObjectName("qv_insitu_list_2_" + str(self.qv_insitu))
    self.qv_insitu_list_2[self.qv_insitu].addItem("Make a choice...")
    self.qv_insitu_list_2[self.qv_insitu].addItem("Copy all form content to a new tab")
    self.qv_insitu_list_2[self.qv_insitu].addItem("Copy all form content to an existing tab")
    self.qv_insitu_horlay_15[self.qv_insitu].addWidget(self.qv_insitu_list_2[self.qv_insitu])
    self.qv_insitu_lab_12.append(QtWidgets.QLabel())
    self.qv_insitu_lab_12[self.qv_insitu].setMinimumSize(QtCore.QSize(15, 15))
    self.qv_insitu_lab_12[self.qv_insitu].setMaximumSize(QtCore.QSize(15, 15))
    self.qv_insitu_lab_12[self.qv_insitu].setObjectName("qv_insitu_lab_12_" + str(self.qv_insitu))
    self.qv_insitu_lab_12[self.qv_insitu].setText("")
    self.qv_insitu_lab_12[self.qv_insitu].setPixmap(QtGui.QPixmap("icons/fwdarrow_icon.svg"))
    self.qv_insitu_lab_12[self.qv_insitu].setScaledContents(True)
    self.qv_insitu_lab_12[self.qv_insitu].setAlignment(QtCore.Qt.AlignCenter)
    self.qv_insitu_horlay_15[self.qv_insitu].addWidget(self.qv_insitu_lab_12[self.qv_insitu])
    self.qv_insitu_lab_12[self.qv_insitu].hide()
    self.qv_insitu_lab_12[self.qv_insitu].setDisabled(True)
    self.qv_insitu_list_3.append(QtWidgets.QComboBox())
    self.qv_insitu_list_3[self.qv_insitu].setMinimumSize(QtCore.QSize(220, 27))
    self.qv_insitu_list_3[self.qv_insitu].setMaximumSize(QtCore.QSize(220, 27))
    self.qv_insitu_list_3[self.qv_insitu].setFont(font3)
    self.qv_insitu_list_3[self.qv_insitu].setStyleSheet("QComboBox {\n"
    "    border: 1px solid #acacac;\n"
    "    border-radius: 1px;\n"
    "    padding-left: 5px;\n"
    "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
    "stop: 0 #f0f0f0, stop: 1 #e5e5e5);\n"
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
    "stop: 0 #ecf4fc, stop: 1 #dcecfc);\n"
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
    self.qv_insitu_list_3[self.qv_insitu].setFrame(False)
    self.qv_insitu_list_3[self.qv_insitu].setObjectName("qv_insitu_list_3_" + str(self.qv_insitu))
    self.qv_insitu_list_3[self.qv_insitu].hide()
    self.qv_insitu_list_3[self.qv_insitu].setDisabled(True)
    self.qv_insitu_horlay_15[self.qv_insitu].addWidget(self.qv_insitu_list_3[self.qv_insitu])
    self.qv_insitu_contBut_1.append(QtWidgets.QToolButton())
    self.qv_insitu_contBut_1[self.qv_insitu].setMaximumSize(QtCore.QSize(27, 27))
    self.qv_insitu_contBut_1[self.qv_insitu].setStyleSheet("QToolButton {\n"
    "    border: 1px solid transparent;\n"
    "    background-color: transparent;\n"
    "    width: 27px;\n"
    "    height: 27px;\n"
    "}\n"
    "QToolButton:flat {\n"
    "    border: none;\n"
    "}")
    self.qv_insitu_contBut_1[self.qv_insitu].setText("")
    self.qv_insitu_contBut_1[self.qv_insitu].setIcon(icon2)
    self.qv_insitu_contBut_1[self.qv_insitu].setIconSize(QtCore.QSize(23, 23))
    self.qv_insitu_contBut_1[self.qv_insitu].setAutoRaise(False)
    self.qv_insitu_contBut_1[self.qv_insitu].setObjectName("qv_insitu_contBut_1_" + str(self.qv_insitu))
    self.qv_insitu_horlay_15[self.qv_insitu].addWidget(self.qv_insitu_contBut_1[self.qv_insitu])
    self.qv_insitu_horlay_15[self.qv_insitu].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, 
                                                    QtWidgets.QSizePolicy.Minimum))
    self.qv_insitu_infBut_6.append(QtWidgets.QToolButton())
    self.qv_insitu_infBut_6[self.qv_insitu].setMaximumSize(QtCore.QSize(27, 27))
    self.qv_insitu_infBut_6[self.qv_insitu].setStyleSheet("QToolButton {\n"
    "    border: 1px solid transparent;\n"
    "    background-color: transparent;\n"
    "    width: 27px;\n"
    "    height: 27px;\n"
    "}\n"
    "QToolButton:flat {\n"
    "    border: none;\n"
    "}")
    self.qv_insitu_infBut_6[self.qv_insitu].setText("")
    self.qv_insitu_infBut_6[self.qv_insitu].setIcon(icon)
    self.qv_insitu_infBut_6[self.qv_insitu].setIconSize(QtCore.QSize(23, 23))
    self.qv_insitu_infBut_6[self.qv_insitu].setAutoRaise(False)
    self.qv_insitu_infBut_6[self.qv_insitu].setObjectName("infoButton_45")
    self.qv_insitu_horlay_15[self.qv_insitu].addWidget(self.qv_insitu_infBut_6[self.qv_insitu])
    self.qv_insitu_horlay_15[self.qv_insitu].addItem(QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, 
                                                                          QtWidgets.QSizePolicy.Minimum))
    self.qv_insitu_verlay_1[self.qv_insitu].addItem(QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, 
                                                                          QtWidgets.QSizePolicy.Fixed))
    self.qv_insitu_horlay_14.append(QtWidgets.QHBoxLayout())
    self.qv_insitu_horlay_14[self.qv_insitu].setObjectName("qv_insitu_horlay_14_" + str(self.qv_insitu))
    self.qv_insitu_verlay_1[self.qv_insitu].addLayout(self.qv_insitu_horlay_14[self.qv_insitu])
    
    self.qv_insitu_lab_10.append(QtWidgets.QLabel())
    self.qv_insitu_lab_10[self.qv_insitu].setMinimumSize(QtCore.QSize(0, 27))
    self.qv_insitu_lab_10[self.qv_insitu].setMaximumSize(QtCore.QSize(16777215, 27))
    self.qv_insitu_lab_10[self.qv_insitu].setFont(font2)
    self.qv_insitu_lab_10[self.qv_insitu].setObjectName("qv_insitu_lab_10_" + str(self.qv_insitu))
    self.qv_insitu_lab_10[self.qv_insitu].setText("The current form is linked to the following instrument")
    self.qv_insitu_horlay_14[self.qv_insitu].addWidget(self.qv_insitu_lab_10[self.qv_insitu])
    self.qv_insitu_horlay_14[self.qv_insitu].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, 
                                                                          QtWidgets.QSizePolicy.Minimum))
    self.qv_insitu_list_1.append(QtWidgets.QComboBox())
    self.qv_insitu_list_1[self.qv_insitu].setMinimumSize(QtCore.QSize(220, 27))
    self.qv_insitu_list_1[self.qv_insitu].setMaximumSize(QtCore.QSize(220, 27))
    self.qv_insitu_list_1[self.qv_insitu].setFont(font3)
    self.qv_insitu_list_1[self.qv_insitu].setStyleSheet("QComboBox {\n"
    "    border: 1px solid #acacac;\n"
    "    border-radius: 1px;\n"
    "    padding-left: 5px;\n"
    "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
    "stop: 0 #f0f0f0, stop: 1 #e5e5e5);\n"
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
    "stop: 0 #ecf4fc, stop: 1 #dcecfc);\n"
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
    self.qv_insitu_list_1[self.qv_insitu].setFrame(False)
    self.qv_insitu_list_1[self.qv_insitu].setObjectName("qv_insitu_list_1_" + str(self.qv_insitu))
    self.qv_insitu_horlay_14[self.qv_insitu].addWidget(self.qv_insitu_list_1[self.qv_insitu])
    
    self.qv_insitu_infBut_5.append(QtWidgets.QToolButton())
    self.qv_insitu_infBut_5[self.qv_insitu].setMaximumSize(QtCore.QSize(27, 27))
    self.qv_insitu_infBut_5[self.qv_insitu].setStyleSheet("QToolButton {\n"
    "    border: 1px solid transparent;\n"
    "    background-color: transparent;\n"
    "    width: 27px;\n"
    "    height: 27px;\n"
    "}\n"
    "QToolButton:flat {\n"
    "    border: none;\n"
    "}")
    self.qv_insitu_infBut_5[self.qv_insitu].setText("")
    self.qv_insitu_infBut_5[self.qv_insitu].setIcon(icon)
    self.qv_insitu_infBut_5[self.qv_insitu].setIconSize(QtCore.QSize(23, 23))
    self.qv_insitu_infBut_5[self.qv_insitu].setAutoRaise(False)
    self.qv_insitu_infBut_5[self.qv_insitu].setObjectName("infoButton_44")
    self.qv_insitu_horlay_14[self.qv_insitu].addWidget(self.qv_insitu_infBut_5[self.qv_insitu])
    self.qv_insitu_horlay_14[self.qv_insitu].addItem(QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, 
                                                                          QtWidgets.QSizePolicy.Minimum))
    self.qv_insitu_verlay_1[self.qv_insitu].addItem(QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, 
                                                                          QtWidgets.QSizePolicy.Fixed))
    self.qv_insitu_horlay_1.append(QtWidgets.QHBoxLayout())
    self.qv_insitu_horlay_1[self.qv_insitu].setObjectName("qv_insitu_horlay_1_" + str(self.qv_insitu))
    self.qv_insitu_verlay_1[self.qv_insitu].addLayout(self.qv_insitu_horlay_1[self.qv_insitu])
    self.qv_insitu_lab_1.append(QtWidgets.QLabel())
    self.qv_insitu_lab_1[self.qv_insitu].setMinimumSize(QtCore.QSize(0, 27))
    self.qv_insitu_lab_1[self.qv_insitu].setMaximumSize(QtCore.QSize(16777215, 27))
    self.qv_insitu_lab_1[self.qv_insitu].setFont(font2)
    self.qv_insitu_lab_1[self.qv_insitu].setObjectName("qv_insitu_lab_1_" + str(self.qv_insitu))
    self.qv_insitu_lab_1[self.qv_insitu].setText("Operator's standard calibration procedures applied to raw digital data")
    self.qv_insitu_horlay_1[self.qv_insitu].addWidget(self.qv_insitu_lab_1[self.qv_insitu])
    self.qv_insitu_infBut_1.append(QtWidgets.QToolButton())
    self.qv_insitu_infBut_1[self.qv_insitu].setMaximumSize(QtCore.QSize(27, 27))
    self.qv_insitu_infBut_1[self.qv_insitu].setStyleSheet("QToolButton {\n"
    "    border: 1px solid transparent;\n"
    "    background-color: transparent;\n"
    "    width: 27px;\n"
    "    height: 27px;\n"
    "}\n"
    "QToolButton:flat {\n"
    "    border: none;\n"
    "}")
    self.qv_insitu_infBut_1[self.qv_insitu].setText("")
    self.qv_insitu_infBut_1[self.qv_insitu].setIcon(icon)
    self.qv_insitu_infBut_1[self.qv_insitu].setIconSize(QtCore.QSize(23, 23))
    self.qv_insitu_infBut_1[self.qv_insitu].setAutoRaise(False)
    self.qv_insitu_infBut_1[self.qv_insitu].setObjectName("infoButton_27")
    self.qv_insitu_horlay_1[self.qv_insitu].addWidget(self.qv_insitu_infBut_1[self.qv_insitu])
    self.qv_insitu_horlay_1[self.qv_insitu].addItem(QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, 
                                                                          QtWidgets.QSizePolicy.Minimum))
    self.qv_insitu_gridlay_1.append(QtWidgets.QGridLayout())
    self.qv_insitu_gridlay_1[self.qv_insitu].setObjectName("qv_insitu_gridlay_1_" + str(self.qv_insitu))
    self.qv_insitu_verlay_1[self.qv_insitu].addLayout(self.qv_insitu_gridlay_1[self.qv_insitu])
    self.qv_insitu_lab_2.append(QtWidgets.QLabel())
    self.qv_insitu_lab_2[self.qv_insitu].setMinimumSize(QtCore.QSize(0, 27))
    self.qv_insitu_lab_2[self.qv_insitu].setMaximumSize(QtCore.QSize(16777215, 27))
    self.qv_insitu_lab_2[self.qv_insitu].setFont(font)
    self.qv_insitu_lab_2[self.qv_insitu].setObjectName("qv_insitu_lab_2_" + str(self.qv_insitu))
    self.qv_insitu_lab_2[self.qv_insitu].setText("Link to the procedure\'s description(s):")
    self.qv_insitu_gridlay_1[self.qv_insitu].addWidget(self.qv_insitu_lab_2[self.qv_insitu], 0, 0, 1, 1)
    self.qv_insitu_line_1.append(QtWidgets.QLineEdit())
    self.qv_insitu_line_1[self.qv_insitu].setMinimumSize(QtCore.QSize(500, 27))
    self.qv_insitu_line_1[self.qv_insitu].setMaximumSize(QtCore.QSize(16777215, 27))
    self.qv_insitu_line_1[self.qv_insitu].setFont(font3)
    self.qv_insitu_line_1[self.qv_insitu].setStyleSheet("QLineEdit {\n"
    "    border-radius: 3px;\n"
    "    padding: 1px 4px 1px 4px;\n"
    "    background-color:  rgb(240, 240, 240);\n"
    "}")
    self.qv_insitu_line_1[self.qv_insitu].setObjectName("qv_insitu_line_1_" + str(self.qv_insitu))
    self.qv_insitu_gridlay_1[self.qv_insitu].addWidget(self.qv_insitu_line_1[self.qv_insitu], 0, 1, 1, 1)
    self.qv_insitu_lab_3.append(QtWidgets.QLabel())
    self.qv_insitu_lab_3[self.qv_insitu].setMinimumSize(QtCore.QSize(0, 27))
    self.qv_insitu_lab_3[self.qv_insitu].setMaximumSize(QtCore.QSize(16777215, 27))
    self.qv_insitu_lab_3[self.qv_insitu].setFont(font)
    self.qv_insitu_lab_3[self.qv_insitu].setObjectName("qv_insitu_lab_3_" + str(self.qv_insitu))
    self.qv_insitu_lab_3[self.qv_insitu].setText("Source(s) of calibration constants:")
    self.qv_insitu_gridlay_1[self.qv_insitu].addWidget(self.qv_insitu_lab_3[self.qv_insitu], 1, 0, 1, 1)
    self.qv_insitu_line_2.append(QtWidgets.QLineEdit())
    self.qv_insitu_line_2[self.qv_insitu].setMinimumSize(QtCore.QSize(500, 27))
    self.qv_insitu_line_2[self.qv_insitu].setMaximumSize(QtCore.QSize(16777215, 27))
    self.qv_insitu_line_2[self.qv_insitu].setFont(font3)
    self.qv_insitu_line_2[self.qv_insitu].setStyleSheet("QLineEdit {\n"
    "    border-radius: 3px;\n"
    "    padding: 1px 4px 1px 4px;\n"
    "    background-color:  rgb(240, 240, 240);\n"
    "}")
    self.qv_insitu_line_2[self.qv_insitu].setObjectName("qv_insitu_line_2_" + str(self.qv_insitu))
    self.qv_insitu_gridlay_1[self.qv_insitu].addWidget(self.qv_insitu_line_2[self.qv_insitu], 1, 1, 1, 1)
    self.qv_insitu_lab_4.append(QtWidgets.QLabel())
    self.qv_insitu_lab_4[self.qv_insitu].setMinimumSize(QtCore.QSize(0, 27))
    self.qv_insitu_lab_4[self.qv_insitu].setMaximumSize(QtCore.QSize(16777215, 27))
    self.qv_insitu_lab_4[self.qv_insitu].setFont(font)
    self.qv_insitu_lab_4[self.qv_insitu].setObjectName("qv_insitu_lab_4_" + str(self.qv_insitu))
    self.qv_insitu_lab_4[self.qv_insitu].setText("Source(s) of calibration materials:")
    self.qv_insitu_gridlay_1[self.qv_insitu].addWidget(self.qv_insitu_lab_4[self.qv_insitu], 2, 0, 1, 1)
    self.qv_insitu_line_3.append(QtWidgets.QLineEdit())
    self.qv_insitu_line_3[self.qv_insitu].setMinimumSize(QtCore.QSize(500, 27))
    self.qv_insitu_line_3[self.qv_insitu].setMaximumSize(QtCore.QSize(16777215, 27))
    self.qv_insitu_line_3[self.qv_insitu].setFont(font3)
    self.qv_insitu_line_3[self.qv_insitu].setStyleSheet("QLineEdit {\n"
    "    border-radius: 3px;\n"
    "    padding: 1px 4px 1px 4px;\n"
    "    background-color:  rgb(240, 240, 240);\n"
    "}")
    self.qv_insitu_line_3[self.qv_insitu].setObjectName("qv_insitu_line_3_" + str(self.qv_insitu))
    self.qv_insitu_gridlay_1[self.qv_insitu].addWidget(self.qv_insitu_line_3[self.qv_insitu], 2, 1, 1, 1)
    self.qv_insitu_verlay_1[self.qv_insitu].addItem(QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, 
                                                                          QtWidgets.QSizePolicy.Fixed))
    self.qv_insitu_horlay_5.append(QtWidgets.QHBoxLayout())
    self.qv_insitu_horlay_5[self.qv_insitu].setObjectName("qv_insitu_horlay_5_" + str(self.qv_insitu))
    self.qv_insitu_verlay_1[self.qv_insitu].addLayout(self.qv_insitu_horlay_5[self.qv_insitu])
    self.qv_insitu_lab_5.append(QtWidgets.QLabel())
    self.qv_insitu_lab_5[self.qv_insitu].setMinimumSize(QtCore.QSize(0, 27))
    self.qv_insitu_lab_5[self.qv_insitu].setMaximumSize(QtCore.QSize(16777215, 27))
    self.qv_insitu_lab_5[self.qv_insitu].setFont(font2)
    self.qv_insitu_lab_5[self.qv_insitu].setObjectName("qv_insitu_lab_5_" + str(self.qv_insitu))
    self.qv_insitu_lab_5[self.qv_insitu].setText("Conversion to geophysical units ?")
    self.qv_insitu_horlay_5[self.qv_insitu].addWidget(self.qv_insitu_lab_5[self.qv_insitu])
    self.qv_insitu_horlay_5[self.qv_insitu].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, 
                                                                          QtWidgets.QSizePolicy.Minimum))
    self.qv_insitu_round_1.append(QtWidgets.QRadioButton())
    self.qv_insitu_round_1[self.qv_insitu].setMinimumSize(QtCore.QSize(51, 27))
    self.qv_insitu_round_1[self.qv_insitu].setMaximumSize(QtCore.QSize(16777215, 27))
    self.qv_insitu_round_1[self.qv_insitu].setFont(font)
    self.qv_insitu_round_1[self.qv_insitu].setObjectName("qv_insitu_round_1_" + str(self.qv_insitu))
    self.qv_insitu_round_1[self.qv_insitu].setText("Yes")
    self.qv_insitu_horlay_5[self.qv_insitu].addWidget(self.qv_insitu_round_1[self.qv_insitu])
    self.qv_insitu_horlay_5[self.qv_insitu].addItem(QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, 
                                                                          QtWidgets.QSizePolicy.Minimum))
    self.qv_insitu_round_2.append(QtWidgets.QRadioButton())
    self.qv_insitu_round_2[self.qv_insitu].setMinimumSize(QtCore.QSize(51, 27))
    self.qv_insitu_round_2[self.qv_insitu].setMaximumSize(QtCore.QSize(16777215, 27))
    self.qv_insitu_round_2[self.qv_insitu].setFont(font)
    self.qv_insitu_round_2[self.qv_insitu].setObjectName("qv_insitu_round_2_" + str(self.qv_insitu))
    self.qv_insitu_round_2[self.qv_insitu].setText("No")
    self.qv_insitu_horlay_5[self.qv_insitu].addWidget(self.qv_insitu_round_2[self.qv_insitu])
    self.qv_insitu_horlay_5[self.qv_insitu].addItem(QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, 
                                                                          QtWidgets.QSizePolicy.Minimum))
    self.qv_insitu_group_1.append(QtWidgets.QButtonGroup())
    self.qv_insitu_group_1[self.qv_insitu].setObjectName("qv_insitu_group_1_" + str(self.qv_insitu))
    self.qv_insitu_group_1[self.qv_insitu].addButton(self.qv_insitu_round_1[self.qv_insitu])
    self.qv_insitu_group_1[self.qv_insitu].addButton(self.qv_insitu_round_2[self.qv_insitu])
    self.qv_insitu_verlay_1[self.qv_insitu].addItem(QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, 
                                                                          QtWidgets.QSizePolicy.Fixed))
    self.qv_insitu_horlay_6.append(QtWidgets.QHBoxLayout())
    self.qv_insitu_horlay_6[self.qv_insitu].setObjectName("qv_insitu_horlay_6_" + str(self.qv_insitu))
    self.qv_insitu_verlay_1[self.qv_insitu].addLayout(self.qv_insitu_horlay_6[self.qv_insitu])
    self.qv_insitu_lab_6.append(QtWidgets.QLabel())
    self.qv_insitu_lab_6[self.qv_insitu].setMinimumSize(QtCore.QSize(0, 27))
    self.qv_insitu_lab_6[self.qv_insitu].setMaximumSize(QtCore.QSize(16777215, 27))
    self.qv_insitu_lab_6[self.qv_insitu].setFont(font2)
    self.qv_insitu_lab_6[self.qv_insitu].setObjectName("qv_insitu_lab_6_" + str(self.qv_insitu))
    self.qv_insitu_lab_6[self.qv_insitu].setText("Output in standardized format")
    self.qv_insitu_horlay_6[self.qv_insitu].addWidget(self.qv_insitu_lab_6[self.qv_insitu])
    self.qv_insitu_infBut_2.append(QtWidgets.QToolButton())
    self.qv_insitu_infBut_2[self.qv_insitu].setMaximumSize(QtCore.QSize(27, 27))
    self.qv_insitu_infBut_2[self.qv_insitu].setStyleSheet("QToolButton {\n"
    "    border: 1px solid transparent;\n"
    "    background-color: transparent;\n"
    "    width: 27px;\n"
    "    height: 27px;\n"
    "}\n"
    "QToolButton:flat {\n"
    "    border: none;\n"
    "}")
    self.qv_insitu_infBut_2[self.qv_insitu].setText("")
    self.qv_insitu_infBut_2[self.qv_insitu].setIcon(icon)
    self.qv_insitu_infBut_2[self.qv_insitu].setIconSize(QtCore.QSize(23, 23))
    self.qv_insitu_infBut_2[self.qv_insitu].setAutoRaise(False)
    self.qv_insitu_infBut_2[self.qv_insitu].setObjectName("infoButton_28")
    self.qv_insitu_horlay_6[self.qv_insitu].addWidget(self.qv_insitu_infBut_2[self.qv_insitu])
    self.qv_insitu_horlay_6[self.qv_insitu].addItem(QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, 
                                                                          QtWidgets.QSizePolicy.Minimum))
    self.qv_insitu_horlay_7.append(QtWidgets.QHBoxLayout())
    self.qv_insitu_horlay_7[self.qv_insitu].setObjectName("qv_insitu_horlay_7_" + str(self.qv_insitu))
    self.qv_insitu_horlay_7[self.qv_insitu].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, 
                                                                          QtWidgets.QSizePolicy.Minimum))
    self.qv_insitu_verlay_1[self.qv_insitu].addLayout(self.qv_insitu_horlay_7[self.qv_insitu])
    self.qv_insitu_gridlay_2.append(QtWidgets.QGridLayout())
    self.qv_insitu_gridlay_2[self.qv_insitu].setHorizontalSpacing(30)
    self.qv_insitu_gridlay_2[self.qv_insitu].setVerticalSpacing(10)
    self.qv_insitu_gridlay_2[self.qv_insitu].setObjectName("qv_insitu_gridlay_2_" + str(self.qv_insitu))
    self.qv_insitu_check_1.append(QtWidgets.QCheckBox())
    self.qv_insitu_check_1[self.qv_insitu].setMinimumSize(QtCore.QSize(80, 27))
    self.qv_insitu_check_1[self.qv_insitu].setMaximumSize(QtCore.QSize(16777215, 27))
    self.qv_insitu_check_1[self.qv_insitu].setFont(font)
    self.qv_insitu_check_1[self.qv_insitu].setObjectName("qv_insitu_check_1_" + str(self.qv_insitu))
    self.qv_insitu_check_1[self.qv_insitu].setText("NetCDF")
    self.qv_insitu_gridlay_2[self.qv_insitu].addWidget(self.qv_insitu_check_1[self.qv_insitu], 0, 0, 1, 1)
    self.qv_insitu_horlay_8.append(QtWidgets.QHBoxLayout())
    self.qv_insitu_horlay_8[self.qv_insitu].setObjectName("qv_insitu_horlay_8_" + str(self.qv_insitu))
    self.qv_insitu_check_2.append(QtWidgets.QCheckBox())
    self.qv_insitu_check_2[self.qv_insitu].setMinimumSize(QtCore.QSize(110, 27))
    self.qv_insitu_check_2[self.qv_insitu].setMaximumSize(QtCore.QSize(16777215, 27))
    self.qv_insitu_check_2[self.qv_insitu].setFont(font)
    self.qv_insitu_check_2[self.qv_insitu].setObjectName("qv_insitu_check_2_" + str(self.qv_insitu))
    self.qv_insitu_check_2[self.qv_insitu].setText("NASA/Ames")
    self.qv_insitu_horlay_8[self.qv_insitu].addWidget(self.qv_insitu_check_2[self.qv_insitu])
    self.qv_insitu_horlay_8[self.qv_insitu].addItem(QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, 
                                                                          QtWidgets.QSizePolicy.Minimum))
    self.qv_insitu_gridlay_2[self.qv_insitu].addLayout(self.qv_insitu_horlay_8[self.qv_insitu], 0, 1, 1, 1)
    self.qv_insitu_check_3.append(QtWidgets.QCheckBox())
    self.qv_insitu_check_3[self.qv_insitu].setMinimumSize(QtCore.QSize(80, 27))
    self.qv_insitu_check_3[self.qv_insitu].setMaximumSize(QtCore.QSize(16777215, 27))
    self.qv_insitu_check_3[self.qv_insitu].setFont(font)
    self.qv_insitu_check_3[self.qv_insitu].setObjectName("qv_insitu_check_3_" + str(self.qv_insitu))
    self.qv_insitu_check_3[self.qv_insitu].setText("HDF")
    self.qv_insitu_gridlay_2[self.qv_insitu].addWidget(self.qv_insitu_check_3[self.qv_insitu], 1, 0, 1, 1)
    self.qv_insitu_horlay_9.append(QtWidgets.QHBoxLayout())
    self.qv_insitu_horlay_9[self.qv_insitu].setObjectName("qv_insitu_horlay_9_" + str(self.qv_insitu))
    self.qv_insitu_check_4.append(QtWidgets.QCheckBox())
    self.qv_insitu_check_4[self.qv_insitu].setMinimumSize(QtCore.QSize(80, 27))
    self.qv_insitu_check_4[self.qv_insitu].setMaximumSize(QtCore.QSize(16777215, 27))
    self.qv_insitu_check_4[self.qv_insitu].setFont(font)
    self.qv_insitu_check_4[self.qv_insitu].setObjectName("qv_insitu_check_4_" + str(self.qv_insitu))
    self.qv_insitu_check_4[self.qv_insitu].setText("Other")
    self.qv_insitu_horlay_9[self.qv_insitu].addWidget(self.qv_insitu_check_4[self.qv_insitu])
    self.qv_insitu_horlay_9[self.qv_insitu].addItem(QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Fixed, 
                                                                           QtWidgets.QSizePolicy.Minimum))
    self.qv_insitu_lab_7.append(QtWidgets.QLabel())
    self.qv_insitu_lab_7[self.qv_insitu].setMinimumSize(QtCore.QSize(15, 15))
    self.qv_insitu_lab_7[self.qv_insitu].setMaximumSize(QtCore.QSize(15, 15))
    self.qv_insitu_lab_7[self.qv_insitu].setFont(font)
    self.qv_insitu_lab_7[self.qv_insitu].setObjectName("qv_insitu_lab_7_" + str(self.qv_insitu))
    self.qv_insitu_lab_7[self.qv_insitu].setText("")
    self.qv_insitu_lab_7[self.qv_insitu].setPixmap(QtGui.QPixmap("icons/fwdarrow_icon.svg"))
    self.qv_insitu_lab_7[self.qv_insitu].setScaledContents(True)
    self.qv_insitu_lab_7[self.qv_insitu].setAlignment(QtCore.Qt.AlignCenter)
    self.qv_insitu_lab_7[self.qv_insitu].hide()
    self.qv_insitu_horlay_9[self.qv_insitu].addWidget(self.qv_insitu_lab_7[self.qv_insitu])
    self.qv_insitu_horlay_9[self.qv_insitu].addItem(QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Fixed, 
                                                                           QtWidgets.QSizePolicy.Minimum))
    self.qv_insitu_line_4.append(QtWidgets.QLineEdit())
    self.qv_insitu_line_4[self.qv_insitu].setMinimumSize(QtCore.QSize(250, 27))
    self.qv_insitu_line_4[self.qv_insitu].setMaximumSize(QtCore.QSize(250, 27))
    self.qv_insitu_line_4[self.qv_insitu].setFont(font3)
    self.qv_insitu_line_4[self.qv_insitu].setStyleSheet("QLineEdit {\n"
    "    border-radius: 3px;\n"
    "    padding: 1px 4px 1px 4px;\n"
    "    background-color:  rgb(240, 240, 240);\n"
    "}")
    self.qv_insitu_line_4[self.qv_insitu].setObjectName("qv_insitu_line_4_" + str(self.qv_insitu))
    self.qv_insitu_line_4[self.qv_insitu].hide()
    self.qv_insitu_horlay_9[self.qv_insitu].addWidget(self.qv_insitu_line_4[self.qv_insitu])
    self.qv_insitu_gridlay_2[self.qv_insitu].addLayout(self.qv_insitu_horlay_9[self.qv_insitu], 1, 1, 1, 1)
    self.qv_insitu_horlay_7[self.qv_insitu].addLayout(self.qv_insitu_gridlay_2[self.qv_insitu])
    self.qv_insitu_horlay_7[self.qv_insitu].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, 
                                                                          QtWidgets.QSizePolicy.Minimum))
    self.qv_insitu_verlay_1[self.qv_insitu].addItem(QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, 
                                                                          QtWidgets.QSizePolicy.Fixed))
    self.qv_insitu_horlay_10.append(QtWidgets.QHBoxLayout())
    self.qv_insitu_horlay_10[self.qv_insitu].setObjectName("qv_insitu_horlay_10_" + str(self.qv_insitu))
    self.qv_insitu_verlay_1[self.qv_insitu].addLayout(self.qv_insitu_horlay_10[self.qv_insitu])
    self.qv_insitu_lab_8.append(QtWidgets.QLabel())
    self.qv_insitu_lab_8[self.qv_insitu].setMinimumSize(QtCore.QSize(0, 27))
    self.qv_insitu_lab_8[self.qv_insitu].setMaximumSize(QtCore.QSize(16777215, 27))
    self.qv_insitu_lab_8[self.qv_insitu].setFont(font2)
    self.qv_insitu_lab_8[self.qv_insitu].setObjectName("qv_insitu_lab_8_" + str(self.qv_insitu))
    self.qv_insitu_lab_8[self.qv_insitu].setText("Quality-control flagging(s) applied to individual data points")
    self.qv_insitu_horlay_10[self.qv_insitu].addWidget(self.qv_insitu_lab_8[self.qv_insitu])
    self.qv_insitu_infBut_3.append(QtWidgets.QToolButton())
    self.qv_insitu_infBut_3[self.qv_insitu].setMaximumSize(QtCore.QSize(27, 27))
    self.qv_insitu_infBut_3[self.qv_insitu].setStyleSheet("QToolButton {\n"
    "    border: 1px solid transparent;\n"
    "    background-color: transparent;\n"
    "    width: 27px;\n"
    "    height: 27px;\n"
    "}\n"
    "QToolButton:flat {\n"
    "    border: none;\n"
    "}")
    self.qv_insitu_infBut_3[self.qv_insitu].setText("")
    self.qv_insitu_infBut_3[self.qv_insitu].setIcon(icon)
    self.qv_insitu_infBut_3[self.qv_insitu].setIconSize(QtCore.QSize(23, 23))
    self.qv_insitu_infBut_3[self.qv_insitu].setAutoRaise(False)
    self.qv_insitu_infBut_3[self.qv_insitu].setObjectName("infoButton_29")
    self.qv_insitu_horlay_10[self.qv_insitu].addWidget(self.qv_insitu_infBut_3[self.qv_insitu])
    self.qv_insitu_horlay_10[self.qv_insitu].addItem(QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, 
                                                                           QtWidgets.QSizePolicy.Minimum))
    self.qv_insitu_horlay_11.append(QtWidgets.QHBoxLayout())
    self.qv_insitu_horlay_11[self.qv_insitu].setObjectName("qv_insitu_horlay_11_" + str(self.qv_insitu))
    self.qv_insitu_horlay_11[self.qv_insitu].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, 
                                                                           QtWidgets.QSizePolicy.Minimum))
    self.qv_insitu_verlay_1[self.qv_insitu].addLayout(self.qv_insitu_horlay_11[self.qv_insitu])
    self.qv_insitu_area_1.append(QtWidgets.QPlainTextEdit())
    self.qv_insitu_area_1[self.qv_insitu].setMinimumSize(QtCore.QSize(600, 100))
    self.qv_insitu_area_1[self.qv_insitu].setMaximumSize(QtCore.QSize(16777215, 100))
    self.qv_insitu_area_1[self.qv_insitu].setFont(font3)
    self.qv_insitu_area_1[self.qv_insitu].setStyleSheet("QPlainTextEdit {\n"
    "    border-radius: 3px;\n"
    "    padding: 1px 4px 1px 4px;\n"
    "    background-color:  rgb(240, 240, 240);\n"
    "}")
    self.qv_insitu_area_1[self.qv_insitu].setObjectName("qv_insitu_area_1_" + str(self.qv_insitu))
    self.qv_insitu_horlay_11[self.qv_insitu].addWidget(self.qv_insitu_area_1[self.qv_insitu])
    self.qv_insitu_horlay_11[self.qv_insitu].addItem(QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, 
                                                                           QtWidgets.QSizePolicy.Minimum))
    self.qv_insitu_verlay_1[self.qv_insitu].addItem(QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, 
                                                                          QtWidgets.QSizePolicy.Fixed))
    self.qv_insitu_horlay_12.append(QtWidgets.QHBoxLayout())
    self.qv_insitu_horlay_12[self.qv_insitu].setObjectName("qv_insitu_horlay_12_" + str(self.qv_insitu))
    self.qv_insitu_verlay_1[self.qv_insitu].addLayout(self.qv_insitu_horlay_12[self.qv_insitu])
    self.qv_insitu_lab_9.append(QtWidgets.QLabel())
    self.qv_insitu_lab_9[self.qv_insitu].setMinimumSize(QtCore.QSize(0, 27))
    self.qv_insitu_lab_9[self.qv_insitu].setMaximumSize(QtCore.QSize(16777215, 27))
    self.qv_insitu_lab_9[self.qv_insitu].setFont(font2)
    self.qv_insitu_lab_9[self.qv_insitu].setObjectName("qv_insitu_lab_9_" + str(self.qv_insitu))
    self.qv_insitu_lab_9[self.qv_insitu].setText("Assumption(s)")
    self.qv_insitu_horlay_12[self.qv_insitu].addWidget(self.qv_insitu_lab_9[self.qv_insitu])
    self.qv_insitu_infBut_4.append(QtWidgets.QToolButton())
    self.qv_insitu_infBut_4[self.qv_insitu].setMaximumSize(QtCore.QSize(27, 27))
    self.qv_insitu_infBut_4[self.qv_insitu].setStyleSheet("QToolButton {\n"
    "    border: 1px solid transparent;\n"
    "    background-color: transparent;\n"
    "    width: 27px;\n"
    "    height: 27px;\n"
    "}\n"
    "QToolButton:flat {\n"
    "    border: none;\n"
    "}")
    self.qv_insitu_infBut_4[self.qv_insitu].setText("")
    self.qv_insitu_infBut_4[self.qv_insitu].setIcon(icon)
    self.qv_insitu_infBut_4[self.qv_insitu].setIconSize(QtCore.QSize(23, 23))
    self.qv_insitu_infBut_4[self.qv_insitu].setAutoRaise(False)
    self.qv_insitu_infBut_4[self.qv_insitu].setObjectName("infoButton_30")
    self.qv_insitu_horlay_12[self.qv_insitu].addWidget(self.qv_insitu_infBut_4[self.qv_insitu])
    self.qv_insitu_horlay_12[self.qv_insitu].addItem(QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, 
                                                                           QtWidgets.QSizePolicy.Minimum))
    self.qv_insitu_horlay_13.append(QtWidgets.QHBoxLayout())
    self.qv_insitu_horlay_13[self.qv_insitu].setObjectName("qv_insitu_horlay_13_" + str(self.qv_insitu))
    self.qv_insitu_horlay_13[self.qv_insitu].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, 
                                                                           QtWidgets.QSizePolicy.Minimum))
    self.qv_insitu_verlay_1[self.qv_insitu].addLayout(self.qv_insitu_horlay_13[self.qv_insitu])
    self.qv_insitu_area_2.append(QtWidgets.QPlainTextEdit())
    self.qv_insitu_area_2[self.qv_insitu].setMinimumSize(QtCore.QSize(600, 100))
    self.qv_insitu_area_2[self.qv_insitu].setMaximumSize(QtCore.QSize(16777215, 100))
    self.qv_insitu_area_2[self.qv_insitu].setFont(font3)
    self.qv_insitu_area_2[self.qv_insitu].setStyleSheet("QPlainTextEdit {\n"
    "    border-radius: 3px;\n"
    "    padding: 1px 4px 1px 4px;\n"
    "    background-color:  rgb(240, 240, 240);\n"
    "}")
    self.qv_insitu_area_2[self.qv_insitu].setObjectName("qv_insitu_area_2" + str(self.qv_insitu))
    self.qv_insitu_horlay_13[self.qv_insitu].addWidget(self.qv_insitu_area_2[self.qv_insitu])
    self.qv_insitu_horlay_13[self.qv_insitu].addItem(QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, 
                                                                           QtWidgets.QSizePolicy.Minimum))
    self.qv_insitu_verlay_1[self.qv_insitu].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, 
                                                                           QtWidgets.QSizePolicy.Expanding))
    all_info_boxes = self.qv_insitu_tab_1[self.qv_insitu].findChildren(QToolButton)
    for widget in all_info_boxes:
        widget.clicked.connect(lambda: self.button_clicked())
    all_radio_buttons = self.qv_insitu_tab_1[self.qv_insitu].findChildren(QtWidgets.QRadioButton)
    for widget in all_radio_buttons:
        widget.clicked.connect(lambda: self.set_modified())
    all_line_edits = self.qv_insitu_tab_1[self.qv_insitu].findChildren(QtWidgets.QLineEdit)
    for widget in all_line_edits:
        widget.textChanged.connect(lambda: self.set_modified())
    all_text_edits = self.qv_insitu_tab_1[self.qv_insitu].findChildren(QtWidgets.QLineEdit)
    for widget in all_text_edits:
        widget.textChanged.connect(lambda: self.set_modified())
    all_checkboxes = self.qv_insitu_tab_1[self.qv_insitu].findChildren(QtWidgets.QCheckBox)
    for widget in all_checkboxes:
        widget.clicked.connect(lambda: self.set_modified())
    self.qv_insitu_list_1[self.qv_insitu].activated.connect(lambda: self.set_modified())
    self.qv_insitu_check_4[self.qv_insitu].clicked.connect(lambda: self.output_other())
    self.qv_insitu_list_2[self.qv_insitu].activated.connect(lambda: qv_activate_tab_list(self))
    self.qv_insitu_line_list[0].append([self.qv_insitu_line_1[self.qv_insitu], self.qv_insitu_lab_2[self.qv_insitu], "text", 
                                        self.qv_tabWidget.indexOf(self.qv_insitu_tab_1[self.qv_insitu])])
    self.qv_insitu_line_list[1].append([self.qv_insitu_line_2[self.qv_insitu], self.qv_insitu_lab_3[self.qv_insitu], "text", 
                                        self.qv_tabWidget.indexOf(self.qv_insitu_tab_1[self.qv_insitu])])
    self.qv_insitu_line_list[2].append([self.qv_insitu_line_3[self.qv_insitu], self.qv_insitu_lab_4[self.qv_insitu], "text", 
                                        self.qv_tabWidget.indexOf(self.qv_insitu_tab_1[self.qv_insitu])])
    self.qv_insitu_line_list[3].append([self.qv_insitu_line_4[self.qv_insitu], self.qv_insitu_lab_7[self.qv_insitu], "text", 
                                        self.qv_tabWidget.indexOf(self.qv_insitu_tab_1[self.qv_insitu])])
    self.qv_insitu_area_list[0].append([self.qv_insitu_area_1[self.qv_insitu], self.qv_insitu_lab_8[self.qv_insitu], "text", 
                                        self.qv_tabWidget.indexOf(self.qv_insitu_tab_1[self.qv_insitu])])
    self.qv_insitu_area_list[1].append([self.qv_insitu_area_2[self.qv_insitu], self.qv_insitu_lab_9[self.qv_insitu], "text", 
                                        self.qv_tabWidget.indexOf(self.qv_insitu_tab_1[self.qv_insitu])])
    self.qv_insitu_radio_list[0].append([self.qv_insitu_group_1[self.qv_insitu], self.qv_insitu_lab_5[self.qv_insitu], 
                                        self.qv_tabWidget.indexOf(self.qv_insitu_tab_1[self.qv_insitu])])
    self.qv_insitu_combo_list[0].append([self.qv_insitu_list_1[self.qv_insitu], self.qv_insitu_lab_10[self.qv_insitu], 
                                          self.qv_tabWidget.indexOf(self.qv_insitu_tab_1[self.qv_insitu])])
    qv_update_instrument_list(self)
    qv_update_tab_list(self, "insitu")
    self.qv_insitu += 1

def close_insitu_tab(self, index, insitu_index):
    self.qv_tabWidget.removeTab(index)
    self.qv_insitu_verlay_1[insitu_index].deleteLater()
    self.qv_insitu_verlay_1.pop(insitu_index)
    self.qv_insitu_horlay_1[insitu_index].deleteLater()
    self.qv_insitu_horlay_1.pop(insitu_index)
    self.qv_insitu_horlay_5[insitu_index].deleteLater()
    self.qv_insitu_horlay_5.pop(insitu_index)
    self.qv_insitu_horlay_6[insitu_index].deleteLater()
    self.qv_insitu_horlay_6.pop(insitu_index)
    self.qv_insitu_horlay_7[insitu_index].deleteLater()
    self.qv_insitu_horlay_7.pop(insitu_index)
    self.qv_insitu_horlay_8[insitu_index].deleteLater()
    self.qv_insitu_horlay_8.pop(insitu_index)
    self.qv_insitu_horlay_9[insitu_index].deleteLater()
    self.qv_insitu_horlay_9.pop(insitu_index)
    self.qv_insitu_horlay_10[insitu_index].deleteLater()
    self.qv_insitu_horlay_10.pop(insitu_index)
    self.qv_insitu_horlay_11[insitu_index].deleteLater()
    self.qv_insitu_horlay_11.pop(insitu_index)
    self.qv_insitu_horlay_12[insitu_index].deleteLater()
    self.qv_insitu_horlay_12.pop(insitu_index)
    self.qv_insitu_horlay_13[insitu_index].deleteLater()
    self.qv_insitu_horlay_13.pop(insitu_index)
    self.qv_insitu_gridlay_1[insitu_index].deleteLater()
    self.qv_insitu_gridlay_1.pop(insitu_index)
    self.qv_insitu_gridlay_2[insitu_index].deleteLater()
    self.qv_insitu_gridlay_2.pop(insitu_index)
    self.qv_insitu_gridlay_3[insitu_index].deleteLater()
    self.qv_insitu_gridlay_3.pop(insitu_index)
    self.qv_insitu_lab_1[insitu_index].deleteLater()
    self.qv_insitu_lab_1.pop(insitu_index)
    self.qv_insitu_lab_2[insitu_index].deleteLater()
    self.qv_insitu_lab_2.pop(insitu_index)
    self.qv_insitu_lab_3[insitu_index].deleteLater()
    self.qv_insitu_lab_3.pop(insitu_index)
    self.qv_insitu_lab_4[insitu_index].deleteLater()
    self.qv_insitu_lab_4.pop(insitu_index)
    self.qv_insitu_lab_5[insitu_index].deleteLater()
    self.qv_insitu_lab_5.pop(insitu_index)
    self.qv_insitu_lab_6[insitu_index].deleteLater()
    self.qv_insitu_lab_6.pop(insitu_index)
    self.qv_insitu_lab_7[insitu_index].deleteLater()
    self.qv_insitu_lab_7.pop(insitu_index)
    self.qv_insitu_lab_8[insitu_index].deleteLater()
    self.qv_insitu_lab_8.pop(insitu_index)
    self.qv_insitu_lab_9[insitu_index].deleteLater()
    self.qv_insitu_lab_9.pop(insitu_index)
    self.qv_insitu_infBut_1[insitu_index].deleteLater()
    self.qv_insitu_infBut_1.pop(insitu_index)
    self.qv_insitu_infBut_2[insitu_index].deleteLater()
    self.qv_insitu_infBut_2.pop(insitu_index)
    self.qv_insitu_infBut_3[insitu_index].deleteLater()
    self.qv_insitu_infBut_3.pop(insitu_index)
    self.qv_insitu_infBut_4[insitu_index].deleteLater()
    self.qv_insitu_infBut_4.pop(insitu_index)
    self.qv_insitu_line_1[insitu_index].deleteLater()
    self.qv_insitu_line_1.pop(insitu_index)
    self.qv_insitu_line_2[insitu_index].deleteLater()
    self.qv_insitu_line_2.pop(insitu_index)
    self.qv_insitu_line_3[insitu_index].deleteLater()
    self.qv_insitu_line_3.pop(insitu_index)
    self.qv_insitu_line_4[insitu_index].deleteLater()
    self.qv_insitu_line_4.pop(insitu_index)
    self.qv_insitu_area_1[insitu_index].deleteLater()
    self.qv_insitu_area_1.pop(insitu_index)
    self.qv_insitu_area_2[insitu_index].deleteLater()
    self.qv_insitu_area_2.pop(insitu_index)
    self.qv_insitu_round_1[insitu_index].deleteLater()
    self.qv_insitu_round_1.pop(insitu_index)
    self.qv_insitu_round_2[insitu_index].deleteLater()
    self.qv_insitu_round_2.pop(insitu_index)
    self.qv_insitu_group_1[insitu_index].deleteLater()
    self.qv_insitu_group_1.pop(insitu_index)
    self.qv_insitu_check_1[insitu_index].deleteLater()
    self.qv_insitu_check_1.pop(insitu_index)
    self.qv_insitu_check_2[insitu_index].deleteLater()
    self.qv_insitu_check_2.pop(insitu_index)
    self.qv_insitu_check_3[insitu_index].deleteLater()
    self.qv_insitu_check_3.pop(insitu_index)
    self.qv_insitu_check_4[insitu_index].deleteLater()
    self.qv_insitu_check_4.pop(insitu_index)
    self.qv_insitu_tab_1[insitu_index].deleteLater()
    self.qv_insitu_tab_1.pop(insitu_index)
    self.qv_insitu_scroll_1[insitu_index].deleteLater()
    self.qv_insitu_scroll_1.pop(insitu_index)
    self.qv_insitu_scroll_2[insitu_index].deleteLater()
    self.qv_insitu_scroll_2.pop(insitu_index)
    self.qv_insitu_horlay_14[insitu_index].deleteLater()
    self.qv_insitu_horlay_14.pop(insitu_index)
    self.qv_insitu_lab_10[insitu_index].deleteLater()
    self.qv_insitu_lab_10.pop(insitu_index)
    self.qv_insitu_list_1[insitu_index].deleteLater()
    self.qv_insitu_list_1.pop(insitu_index)
    self.qv_insitu_infBut_5[insitu_index].deleteLater()
    self.qv_insitu_infBut_5.pop(insitu_index)
    self.qv_insitu_horlay_15[insitu_index].deleteLater()
    self.qv_insitu_horlay_15.pop(insitu_index)
    self.qv_insitu_lab_11[insitu_index].deleteLater()
    self.qv_insitu_lab_11.pop(insitu_index)
    self.qv_insitu_list_2[insitu_index].deleteLater()
    self.qv_insitu_list_2.pop(insitu_index)
    self.qv_insitu_lab_12[insitu_index].deleteLater()
    self.qv_insitu_lab_12.pop(insitu_index)
    self.qv_insitu_list_3[insitu_index].deleteLater()
    self.qv_insitu_list_3.pop(insitu_index)
    self.qv_insitu_contBut_1[insitu_index].deleteLater()
    self.qv_insitu_contBut_1.pop(insitu_index)
    self.qv_insitu_infBut_6[insitu_index].deleteLater()
    self.qv_insitu_infBut_6.pop(insitu_index)
    self.qv_insitu_line_list[0].pop(insitu_index)
    self.qv_insitu_line_list[1].pop(insitu_index)
    self.qv_insitu_line_list[2].pop(insitu_index)
    self.qv_insitu_line_list[3].pop(insitu_index)
    self.qv_insitu_area_list[0].pop(insitu_index)
    self.qv_insitu_area_list[1].pop(insitu_index)
    self.qv_insitu_radio_list[0].pop(insitu_index)
    self.qv_insitu_combo_list[0].pop(insitu_index)
    self.qv_insitu -= 1
    if self.qv_insitu == 0 and self.qv_imagery == 0:
        self.qv_tabWidget.setVisible(False)
        self.qv_tabWidget.setEnabled(False)
        self.qv_spacerItem.changeSize(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
    else:
        j = 0
        for i in range(self.qv_tabWidget.count()):
            if "Atmospheric" in self.qv_tabWidget.tabText(i):
                self.qv_tabWidget.setTabText(i, "Atmospheric/In-situ data " + str(j + 1))
                self.qv_insitu_line_list[0][j][3] = i
                self.qv_insitu_line_list[1][j][3] = i
                self.qv_insitu_line_list[2][j][3] = i
                self.qv_insitu_line_list[3][j][3] = i
                self.qv_insitu_area_list[0][j][3] = i
                self.qv_insitu_area_list[1][j][3] = i
                self.qv_insitu_radio_list[0][j][2] = i
                self.qv_insitu_combo_list[0][j][2] = i
                j += 1
        if len(self.qv_insitu_verlay_1) > 0:
            for i in range(len(self.qv_insitu_verlay_1)):
                self.qv_insitu_tab_1[i].setObjectName("qv_insitu_tab_1_" + str(i))
                self.qv_insitu_gridlay_3[i].setObjectName("qv_insitu_gridlay_3_" + str(i))
                self.qv_insitu_scroll_1[i].setObjectName("qv_insitu_scroll_1_" + str(i))
                self.qv_insitu_scroll_2[i].setObjectName("qv_insitu_scroll_2_" + str(i))
                self.qv_insitu_verlay_1[i].setObjectName("qv_insitu_verlay_1_" + str(i))
                self.qv_insitu_horlay_1[i].setObjectName("qv_insitu_horlay_1_" + str(i))
                self.qv_insitu_lab_1[i].setObjectName("qv_insitu_lab_1_" + str(i))
                self.qv_insitu_infBut_1[i].setObjectName("qv_insitu_infBut_1_" + str(i))
                self.qv_insitu_gridlay_1[i].setObjectName("qv_insitu_gridlay_1_" + str(i))
                self.qv_insitu_lab_2[i].setObjectName("qv_insitu_lab_2_" + str(i))
                self.qv_insitu_line_1[i].setObjectName("qv_insitu_line_1_" + str(i))
                self.qv_insitu_lab_3[i].setObjectName("qv_insitu_lab_3_" + str(i))
                self.qv_insitu_line_2[i].setObjectName("qv_insitu_line_2_" + str(i))
                self.qv_insitu_lab_4[i].setObjectName("qv_insitu_lab_4_" + str(i))
                self.qv_insitu_line_3[i].setObjectName("qv_insitu_line_3_" + str(i))
                self.qv_insitu_horlay_5[i].setObjectName("qv_insitu_horlay_5_" + str(i))
                self.qv_insitu_lab_5[i].setObjectName("qv_insitu_lab_5_" + str(i))
                self.qv_insitu_round_1[i].setObjectName("qv_insitu_round_1_" + str(i))
                self.qv_insitu_round_2[i].setObjectName("qv_insitu_round_2_" + str(i))
                self.qv_insitu_group_1[i].setObjectName("qv_insitu_group_1_" + str(i))
                self.qv_insitu_horlay_6[i].setObjectName("qv_insitu_horlay_6_" + str(i))
                self.qv_insitu_lab_6[i].setObjectName("qv_insitu_lab_6_" + str(i))
                self.qv_insitu_infBut_2[i].setObjectName("qv_insitu_infBut_2_" + str(i))
                self.qv_insitu_horlay_7[i].setObjectName("qv_insitu_horlay_7_" + str(i))
                self.qv_insitu_gridlay_2[i].setObjectName("qv_insitu_gridlay_2_" + str(i))
                self.qv_insitu_check_1[i].setObjectName("qv_insitu_check_1_" + str(i))
                self.qv_insitu_horlay_8[i].setObjectName("qv_insitu_horlay_8_" + str(i))
                self.qv_insitu_check_2[i].setObjectName("qv_insitu_check_2_" + str(i))
                self.qv_insitu_check_3[i].setObjectName("qv_insitu_check_3_" + str(i))
                self.qv_insitu_horlay_9[i].setObjectName("qv_insitu_horlay_9_" + str(i))
                self.qv_insitu_check_4[i].setObjectName("qv_insitu_check_4_" + str(i))
                self.qv_insitu_lab_7[i].setObjectName("qv_insitu_lab_7_" + str(i))
                self.qv_insitu_line_4[i].setObjectName("qv_insitu_line_4_" + str(i))
                self.qv_insitu_horlay_10[i].setObjectName("qv_insitu_horlay_10_" + str(i))
                self.qv_insitu_lab_8[i].setObjectName("qv_insitu_lab_8_" + str(i))
                self.qv_insitu_infBut_3[i].setObjectName("qv_insitu_infBut_3_" + str(i))
                self.qv_insitu_horlay_11[i].setObjectName("qv_insitu_horlay_11_" + str(i))
                self.qv_insitu_area_1[i].setObjectName("qv_insitu_area_1_" + str(i))
                self.qv_insitu_horlay_12[i].setObjectName("qv_insitu_horlay_12_" + str(i))
                self.qv_insitu_lab_9[i].setObjectName("qv_insitu_lab_9_" + str(i))
                self.qv_insitu_infBut_4[i].setObjectName("qv_insitu_infBut_4_" + str(i))
                self.qv_insitu_horlay_13[i].setObjectName("qv_insitu_horlay_13_" + str(i))
                self.qv_insitu_area_2[i].setObjectName("qv_insitu_area_2" + str(i))
                self.qv_insitu_horlay_14[i].setObjectName("qv_insitu_horlay_14_" + str(i))
                self.qv_insitu_lab_10[i].setObjectName("qv_insitu_lab_10_" + str(i))
                self.qv_insitu_list_1[i].setObjectName("qv_insitu_list_1_" + str(i))
                self.qv_insitu_horlay_15[i].setObjectName("qv_insitu_horlay_15_" + str(i))
                self.qv_insitu_lab_11[i].setObjectName("qv_insitu_lab_11_" + str(i))
                self.qv_insitu_list_2[i].setObjectName("qv_insitu_list_2_" + str(i))
                self.qv_insitu_lab_12[i].setObjectName("qv_insitu_lab_12_" + str(i))
                self.qv_insitu_list_3[i].setObjectName("qv_insitu_list_3_" + str(i))
                self.qv_insitu_contBut_1[i].setObjectName("qv_insitu_contBut_1_" + str(i))
    qv_update_tab_list(self, "insitu")

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
            icon.addPixmap(QtGui.QPixmap("icons/del_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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
            self.ai_delbut_2[self.ai_acft].setIconSize(QtCore.QSize(23, 23))
            self.ai_delbut_2[self.ai_acft].setStyleSheet("QToolButton {\n"
            "    border: 1px solid transparent;\n"
            "    background-color: transparent;\n"
            "    width: 27px;\n"
            "    height: 27px;\n"
            "}\n"
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
        icon.addPixmap(QtGui.QPixmap("icons/del_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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
        self.ai_delbut_2[self.ai_acft].setIconSize(QtCore.QSize(23, 23))
        self.ai_delbut_2[self.ai_acft].setStyleSheet("QToolButton {\n"
        "    border: 1px solid transparent;\n"
        "    background-color: transparent;\n"
        "    width: 27px;\n"
        "    height: 27px;\n"
        "}\n"
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
        icon.addPixmap(QtGui.QPixmap("icons/del_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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
        self.ai_delbut[self.ai_inst].setIconSize(QtCore.QSize(23, 23))
        self.ai_delbut[self.ai_inst].setStyleSheet("QToolButton {\n"
        "    border: 1px solid transparent;\n"
        "    background-color: transparent;\n"
        "    width: 27px;\n"
        "    height: 27px;\n"
        "}\n"
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
        qv_update_instrument_list(self)
        self.ai_inst += 1
        self.modified = True
        self.make_window_title()

def plusButton_8_clicked(self):
    icon2 = QtGui.QIcon()
    icon2.addPixmap(QtGui.QPixmap("icons/del_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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
    self.mm_delBut[self.mm_pofc].setIconSize(QtCore.QSize(23, 23))
    self.mm_delBut[self.mm_pofc].setStyleSheet("QToolButton {\n"
    "    border: 1px solid transparent;\n"
    "    background-color: transparent;\n"
    "    width: 27px;\n"
    "    height: 27px;\n"
    "}\n"
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
    icon2.addPixmap(QtGui.QPixmap("icons/del_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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
    self.ro_infBut_1[self.ro_roPy].setIconSize(QtCore.QSize(23, 23))
    self.ro_infBut_1[self.ro_roPy].setObjectName("ro_infBut_1" + str(self.ro_roPy))
    self.ro_infBut_1[self.ro_roPy].setEnabled(False)
    self.ro_infBut_1[self.ro_roPy].setStyleSheet("QToolButton {\n"
    "    border: 1px solid transparent;\n"
    "    background-color: transparent;\n"
    "    width: 27px;\n"
    "    height: 27px;\n"
    "}\n"
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
    self.ro_infBut_2[self.ro_roPy].setIconSize(QtCore.QSize(23, 23))
    self.ro_infBut_2[self.ro_roPy].setObjectName("ro_infBut_2" + str(self.ro_roPy))
    self.ro_infBut_2[self.ro_roPy].setEnabled(False)
    self.ro_infBut_2[self.ro_roPy].setStyleSheet("QToolButton {\n"
    "    border: 1px solid transparent;\n"
    "    background-color: transparent;\n"
    "    width: 27px;\n"
    "    height: 27px;\n"
    "}\n"
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
    self.ro_delBut[self.ro_roPy].setIconSize(QtCore.QSize(23, 23))
    self.ro_delBut[self.ro_roPy].setStyleSheet("QToolButton {\n"
    "    border: 1px solid transparent;\n"
    "    background-color: transparent;\n"
    "    width: 27px;\n"
    "    height: 27px;\n"
    "}\n"
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
    icon.addPixmap(QtGui.QPixmap("icons/del_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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
    self.au_delBut_2[self.au_wn_2].setIconSize(QtCore.QSize(23, 23))
    self.au_delBut_2[self.au_wn_2].setStyleSheet("QToolButton {\n"
    "    border: 1px solid transparent;\n"
    "    background-color: transparent;\n"
    "    width: 27px;\n"
    "    height: 27px;\n"
    "}\n"
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
    icon.addPixmap(QtGui.QPixmap("icons/del_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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
    self.au_delBut_1[self.au_wn_1].setIconSize(QtCore.QSize(23, 23))
    self.au_delBut_1[self.au_wn_1].setStyleSheet("QToolButton {\n"
    "    border: 1px solid transparent;\n"
    "    background-color: transparent;\n"
    "    width: 27px;\n"
    "    height: 27px;\n"
    "}\n"
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
        icon.addPixmap(QtGui.QPixmap("icons/del_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ai_horlay.append(QtWidgets.QHBoxLayout())
        self.ai_horlay[self.ai_inst].setObjectName("ai_horlay_" + str(self.ai_inst))
        self.ai_horlay[self.ai_inst].addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum))
        self.ai_delbut.append(QtWidgets.QToolButton())
        self.ai_delbut[self.ai_inst].setMinimumSize(QtCore.QSize(27, 27))
        self.ai_delbut[self.ai_inst].setMaximumSize(QtCore.QSize(27, 27))
        self.ai_delbut[self.ai_inst].setText("")
        self.ai_delbut[self.ai_inst].setIcon(icon)
        self.ai_delbut[self.ai_inst].setIconSize(QtCore.QSize(23, 23))
        self.ai_delbut[self.ai_inst].setStyleSheet("QToolButton {\n"
        "    border: 1px solid transparent;\n"
        "    background-color: transparent;\n"
        "    width: 27px;\n"
        "    height: 27px;\n"
        "}\n"
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
        qv_update_instrument_list(self)
        self.ai_inst += 1
        self.modified = True
        self.make_window_title()

def plusButton_3_clicked(self):
    icon2 = QtGui.QIcon()
    icon2.addPixmap(QtGui.QPixmap("icons/del_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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
    self.tr_delBut[self.tr_tpex].setIconSize(QtCore.QSize(23, 23))
    self.tr_delBut[self.tr_tpex].setStyleSheet("QToolButton {\n"
    "    border: 1px solid transparent;\n"
    "    background-color: transparent;\n"
    "    width: 27px;\n"
    "    height: 27px;\n"
    "}\n"
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
    qv_update_instrument_list(self)
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
        self.gl_unit_lb.hide()
        self.gl_unit_rl.hide()
        self.gl_unit_lb.setDisabled(True)
        self.gl_unit_rl.setDisabled(True)
    else:
        self.gl_unit_lb.show()
        self.gl_unit_rl.show()
        self.gl_unit_lb.setEnabled(True)
        self.gl_unit_rl.setEnabled(True)
        self.gl_unit_rl.setCurrentIndex(0)

def ai_aircraftRolebox_changed(self):
    if self.ai_aircraft_rl1.currentText() != "Other...":
        self.gridLayout_22.setVerticalSpacing(17)
        self.ai_label_7.show()
        self.ai_label_8.show()
        self.ai_label_9.show()
        self.ai_label_10.show()
        self.ai_label_11.show()
        self.ai_label_12.show()
        self.ai_airManufacturer_ln.hide()
        self.ai_airType_ln.hide()
        self.ai_airOperator_ln.hide()
        self.ai_country_rl.hide()
        self.ai_airNumber_ln.hide()
        self.ai_airManufacturer_ln.setEnabled(True)
        self.ai_airType_ln.setEnabled(True)
        self.ai_airOperator_ln.setEnabled(True)
        self.ai_country_rl.setEnabled(True)
        self.ai_airNumber_ln.setEnabled(True)
        query = sql_valueRead(self, "aircraftInformations", "Id", self.ai_aircraft_rl1.currentText())
        self.ai_image_bx.setPixmap(QtGui.QPixmap("eufar_aircrafts/" + query[0][6]))
        self.ai_label_7.setText(query[0][1])
        self.ai_label_8.setText(query[0][2])
        self.ai_label_9.setText(query[0][3])
        self.ai_label_10.setText(query[0][4])
        self.ai_label_11.setText(query[0][5])
        self.ai_label_12.setText(query[0][7])
        self.ai_otherAircraft = 0
    else:
        self.gridLayout_22.setVerticalSpacing(28)
        self.ai_label_7.setText("")
        self.ai_label_8.setText("")
        self.ai_label_9.setText("")
        self.ai_label_10.setText("")
        self.ai_label_11.setText("")
        self.ai_label_12.setText("EUFAR")
        self.ai_label_7.hide()
        self.ai_label_8.hide()
        self.ai_label_9.hide()
        self.ai_label_10.hide()
        self.ai_label_11.hide()
        self.ai_airManufacturer_ln.show()
        self.ai_airType_ln.show()
        self.ai_airOperator_ln.show()
        self.ai_country_rl.show()
        self.ai_airNumber_ln.show()
        self.ai_airManufacturer_ln.setEnabled(True)
        self.ai_airType_ln.setEnabled(True)
        self.ai_airOperator_ln.setEnabled(True)
        self.ai_country_rl.setEnabled(True)
        self.ai_airNumber_ln.setEnabled(True)
        self.ai_image_bx.setPixmap(QtGui.QPixmap("eufar_aircrafts/logo_eufar_emc.png"))
        query = sql_valueRead(self, "emcLocations", "Category", "Countries")
        i = 0
        self.ai_country_rl.clear()
        self.ai_country_rl.addItem("")
        self.ai_country_rl.setItemText(i, "Make a choice...")
        for item in query:
            i += 1
            self.ai_country_rl.addItem("")
            self.ai_country_rl.setItemText(i, item[1])

def ai_instrument_changed(self):
    if self.ai_instrument_rl1.currentText() == "Other...":
        self.ai_newname_lb.show()
        self.ai_insName_ln.show()
        self.ai_newmanufacturer_lb.show()
        self.ai_insManufacturer_ln.show()
        self.plusButton_9.show()
        self.ai_newname_lb.setEnabled(True)
        self.ai_insName_ln.setEnabled(True)
        self.ai_newmanufacturer_lb.setEnabled(True)
        self.ai_insManufacturer_ln.setEnabled(True)
        self.plusButton_9.setEnabled(True)
        self.plusButton_4.hide()
        self.plusButton_4.setDisabled(True)
    else:
        self.ai_newname_lb.hide()
        self.ai_insName_ln.hide()
        self.ai_newmanufacturer_lb.hide()
        self.ai_insManufacturer_ln.hide()
        self.plusButton_9.hide()
        self.ai_newname_lb.setDisabled(True)
        self.ai_insName_ln.setDisabled(True)
        self.ai_newmanufacturer_lb.setDisabled(True)
        self.ai_insManufacturer_ln.setDisabled(True)
        self.plusButton_9.setDisabled(True)
        self.plusButton_4.show()
        self.plusButton_4.setEnabled(True)

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
    
def clearLayout(layout):
    for i in reversed(range(layout.count())):   
        item = layout.itemAt(i)
        if isinstance(item, QtWidgets.QWidgetItem):
            item.widget().deleteLater()
        elif isinstance(item, QtWidgets.QLayout):
            clearLayout(item.layout())
        layout.removeItem(item)        
    
def qv_output_other(self, index = None):
    if index == None:
        index = int(self.sender().objectName()[18:])
    if self.qv_insitu_check_4[index].isChecked() == True:
        self.qv_insitu_lab_7[index].show()
        self.qv_insitu_line_4[index].show()
        self.qv_insitu_line_4[index].setEnabled(True)
    else:
        self.qv_insitu_lab_7[index].hide()
        self.qv_insitu_line_4[index].hide()
        self.qv_insitu_line_4[index].setDisabled(True)

def qv_update_instrument_list(self):
    self.instModel_list
    self.instManufacturer_list
    instrument_list = []
    for i in range(len(self.instManufacturer_list)):
        instrument_list.append(self.instManufacturer_list[i] + " - " + self.instModel_list[i])
    instrument_list.sort()
    for widget in self.qv_insitu_list_1:
        current_text = widget.currentText()
        widget.clear()
        widget.addItem("Make a choice...")
        for instrument in instrument_list:
            widget.addItem(instrument)
        if widget.findText(current_text) == -1:
            widget.setCurrentIndex(0)
        else:
            widget.setCurrentIndex(widget.findText(current_text))
    for widget in self.qv_imagery_list_2:
        current_text = widget.currentText()
        widget.clear()
        widget.addItem("Make a choice...")
        for instrument in instrument_list:
            widget.addItem(instrument)
        if widget.findText(current_text) == -1:
            widget.setCurrentIndex(0)
        else:
            widget.setCurrentIndex(widget.findText(current_text))        

def qv_activate_tab_list(self):
    if "insitu" in self.sender().objectName():
        index = int(self.sender().objectName()[17:])
        if self.sender().currentText() == "Make a choice..." or self.sender().currentText() == "Copy all form content to a new tab":
            self.qv_insitu_lab_12[index].hide()
            self.qv_insitu_list_3[index].hide()
            self.qv_insitu_lab_12[index].setDisabled(True)
            self.qv_insitu_list_3[index].setDisabled(True)
        else:
            self.qv_insitu_lab_12[index].show()
            self.qv_insitu_list_3[index].show()
            self.qv_insitu_lab_12[index].setEnabled(True)
            self.qv_insitu_list_3[index].setEnabled(True)
            qv_update_tab_list(self, "insitu")
    elif "imagery" in self.sender().objectName():
        index = int(self.sender().objectName()[18:])
        if self.sender().currentText() == "Make a choice..." or self.sender().currentText() == "Copy all form content to a new tab":
            self.qv_imagery_lab_37[index].hide()
            self.qv_imagery_list_4[index].hide()
            self.qv_imagery_lab_37[index].setDisabled(True)
            self.qv_imagery_list_4[index].setDisabled(True)
        else:
            self.qv_imagery_lab_37[index].show()
            self.qv_imagery_list_4[index].show()
            self.qv_imagery_lab_37[index].setEnabled(True)
            self.qv_imagery_list_4[index].setEnabled(True)
            qv_update_tab_list(self, "imagery")

def qv_update_tab_list(self, domain):
    if domain == "insitu":
        tab_num = self.qv_tabWidget.count()
        tab_list = []
        for i in range(tab_num):
            if "Atmospheric" in self.qv_tabWidget.tabText(i):
                tab_list.append(self.qv_tabWidget.tabText(i))
        for index, widget in enumerate(self.qv_insitu_list_3):
            current_text = widget.currentText()
            widget.clear()
            widget.addItem("Make a choice...")
            for string in tab_list:
                widget.addItem(string)
            widget.removeItem(index + 1)
            if widget.findText(current_text) == -1:
                widget.setCurrentIndex(0)
            else:
                widget.setCurrentIndex(widget.findText(current_text))
    elif domain == "imagery":
        tab_num = self.qv_tabWidget.count()
        tab_list = []
        for i in range(tab_num):
            if "Earth" in self.qv_tabWidget.tabText(i):
                tab_list.append(self.qv_tabWidget.tabText(i))
        for index, widget in enumerate(self.qv_imagery_list_4):
            current_text = widget.currentText()
            widget.clear()
            widget.addItem("Make a choice...")
            for string in tab_list:
                widget.addItem(string)
            widget.removeItem(index + 1)
            if widget.findText(current_text) == -1:
                widget.setCurrentIndex(0)
            else:
                widget.setCurrentIndex(widget.findText(current_text))

def qv_tab_cloning(self, domain, index):
    from functions.eufar_metadata_xml import save_statement_insitu
    from functions.eufar_metadata_xml import read_statement_insitu
    from functions.eufar_metadata_xml import save_statement_imagery
    from functions.eufar_metadata_xml import read_statement_imagery
    if domain == "insitu":
        if self.qv_insitu_list_2[index].currentText() == "Copy all form content to a new tab":
            statement = save_statement_insitu(self, index)
            plusButton_12_clicked(self)
            read_statement_insitu(self, statement[1:-1], self.qv_insitu - 1)
        elif self.qv_insitu_list_2[index].currentText() == "Copy all form content to an existing tab":
            if self.qv_insitu_list_3[index].currentText() != "Make a choice...":
                new_index = int(self.qv_insitu_list_3[index].currentText()[25:])
                statement = save_statement_insitu(self, index)
                read_statement_insitu(self, statement[1:-1], new_index - 1)
    elif domain == "imagery":
        if self.qv_imagery_list_3[index].currentText() == "Copy all form content to a new tab":
            statement = save_statement_imagery(self, index)
            plusButton_11_clicked(self)
            read_statement_imagery(self, statement[1:-1], self.qv_imagery - 1)
        elif self.qv_imagery_list_3[index].currentText() == "Copy all form content to an existing tab":
            if self.qv_imagery_list_4[index].currentText() != "Make a choice...":
                new_index = int(self.qv_imagery_list_4[index].currentText()[38:])
                statement = save_statement_imagery(self, index)
                read_statement_imagery(self, statement[1:-1], new_index - 1)


class MyInfo(QtWidgets.QDialog, Ui_infoWindow):
    def __init__(self, infoText):
        QWidget.__init__(self)
        self.setupUi(self)
        self.iw_label_1.setText(infoText)
        self.iw_okButton.clicked.connect(self.closeWindow)

    def closeWindow(self):
        self.close()