# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow_tab.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1094, 673)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(0, 400))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/emc_icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setIconSize(QtCore.QSize(27, 27))
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Triangular)
        MainWindow.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.scrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1072, 625))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.tabWidget = QtWidgets.QTabWidget(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.tabWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.tabWidget.setFont(font)
        self.tabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet("QTabWidget::pane {\n"
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
"}")
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tabWidgetPage1 = QtWidgets.QWidget()
        self.tabWidgetPage1.setObjectName("tabWidgetPage1")
        self.gridLayout_15 = QtWidgets.QGridLayout(self.tabWidgetPage1)
        self.gridLayout_15.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_15.setObjectName("gridLayout_15")
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_15.addItem(spacerItem, 0, 2, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setVerticalSpacing(20)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.id_resourceTitle_lb = QtWidgets.QLabel(self.tabWidgetPage1)
        self.id_resourceTitle_lb.setMinimumSize(QtCore.QSize(0, 0))
        self.id_resourceTitle_lb.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.id_resourceTitle_lb.setFont(font)
        self.id_resourceTitle_lb.setToolTip("")
        self.id_resourceTitle_lb.setObjectName("id_resourceTitle_lb")
        self.gridLayout_2.addWidget(self.id_resourceTitle_lb, 0, 0, 1, 1)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout_8.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout_8.setSpacing(6)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.id_resourceTitle_ln = QtWidgets.QLineEdit(self.tabWidgetPage1)
        self.id_resourceTitle_ln.setMinimumSize(QtCore.QSize(450, 27))
        self.id_resourceTitle_ln.setMaximumSize(QtCore.QSize(450, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.id_resourceTitle_ln.setFont(font)
        self.id_resourceTitle_ln.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"   padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"}")
        self.id_resourceTitle_ln.setFrame(False)
        self.id_resourceTitle_ln.setObjectName("id_resourceTitle_ln")
        self.horizontalLayout_8.addWidget(self.id_resourceTitle_ln)
        self.infoButton_1 = QtWidgets.QToolButton(self.tabWidgetPage1)
        self.infoButton_1.setMinimumSize(QtCore.QSize(27, 27))
        self.infoButton_1.setMaximumSize(QtCore.QSize(27, 27))
        self.infoButton_1.setStyleSheet("QToolButton {\n"
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
        self.infoButton_1.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/info_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.infoButton_1.setIcon(icon1)
        self.infoButton_1.setIconSize(QtCore.QSize(27, 27))
        self.infoButton_1.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.infoButton_1.setAutoRaise(False)
        self.infoButton_1.setArrowType(QtCore.Qt.NoArrow)
        self.infoButton_1.setObjectName("infoButton_1")
        self.horizontalLayout_8.addWidget(self.infoButton_1)
        spacerItem1 = QtWidgets.QSpacerItem(13, 24, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem1)
        self.gridLayout_2.addLayout(self.horizontalLayout_8, 0, 1, 1, 1)
        self.id_resourceIdent_lb = QtWidgets.QLabel(self.tabWidgetPage1)
        self.id_resourceIdent_lb.setMinimumSize(QtCore.QSize(0, 0))
        self.id_resourceIdent_lb.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.id_resourceIdent_lb.setFont(font)
        self.id_resourceIdent_lb.setToolTip("")
        self.id_resourceIdent_lb.setObjectName("id_resourceIdent_lb")
        self.gridLayout_2.addWidget(self.id_resourceIdent_lb, 1, 0, 1, 1)
        self.horizontalLayout_38 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_38.setSpacing(6)
        self.horizontalLayout_38.setObjectName("horizontalLayout_38")
        self.id_resourceIdent_ln = QtWidgets.QLineEdit(self.tabWidgetPage1)
        self.id_resourceIdent_ln.setMinimumSize(QtCore.QSize(450, 27))
        self.id_resourceIdent_ln.setMaximumSize(QtCore.QSize(450, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.id_resourceIdent_ln.setFont(font)
        self.id_resourceIdent_ln.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"   padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"}")
        self.id_resourceIdent_ln.setFrame(False)
        self.id_resourceIdent_ln.setObjectName("id_resourceIdent_ln")
        self.horizontalLayout_38.addWidget(self.id_resourceIdent_ln)
        self.infoButton_5 = QtWidgets.QToolButton(self.tabWidgetPage1)
        self.infoButton_5.setMinimumSize(QtCore.QSize(27, 27))
        self.infoButton_5.setMaximumSize(QtCore.QSize(27, 27))
        self.infoButton_5.setStyleSheet("QToolButton {\n"
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
        self.infoButton_5.setText("")
        self.infoButton_5.setIcon(icon1)
        self.infoButton_5.setIconSize(QtCore.QSize(27, 27))
        self.infoButton_5.setAutoRaise(False)
        self.infoButton_5.setObjectName("infoButton_5")
        self.horizontalLayout_38.addWidget(self.infoButton_5)
        spacerItem2 = QtWidgets.QSpacerItem(13, 24, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_38.addItem(spacerItem2)
        self.gridLayout_2.addLayout(self.horizontalLayout_38, 1, 1, 1, 1)
        self.id_resourceAbstract_lb = QtWidgets.QLabel(self.tabWidgetPage1)
        self.id_resourceAbstract_lb.setMinimumSize(QtCore.QSize(0, 0))
        self.id_resourceAbstract_lb.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.id_resourceAbstract_lb.setFont(font)
        self.id_resourceAbstract_lb.setToolTip("")
        self.id_resourceAbstract_lb.setObjectName("id_resourceAbstract_lb")
        self.gridLayout_2.addWidget(self.id_resourceAbstract_lb, 2, 0, 1, 1)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout_9.setSpacing(6)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.id_resourceAbstract_ta = QtWidgets.QPlainTextEdit(self.tabWidgetPage1)
        self.id_resourceAbstract_ta.setMinimumSize(QtCore.QSize(600, 120))
        self.id_resourceAbstract_ta.setMaximumSize(QtCore.QSize(16777215, 120))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.id_resourceAbstract_ta.setFont(font)
        self.id_resourceAbstract_ta.setStyleSheet("QPlainTextEdit {\n"
"    border-radius: 3px;\n"
"   padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"}")
        self.id_resourceAbstract_ta.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.id_resourceAbstract_ta.setObjectName("id_resourceAbstract_ta")
        self.horizontalLayout_9.addWidget(self.id_resourceAbstract_ta)
        self.infoButton_2 = QtWidgets.QToolButton(self.tabWidgetPage1)
        self.infoButton_2.setMinimumSize(QtCore.QSize(27, 27))
        self.infoButton_2.setMaximumSize(QtCore.QSize(27, 27))
        self.infoButton_2.setStyleSheet("QToolButton {\n"
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
        self.infoButton_2.setText("")
        self.infoButton_2.setIcon(icon1)
        self.infoButton_2.setIconSize(QtCore.QSize(27, 27))
        self.infoButton_2.setAutoRaise(False)
        self.infoButton_2.setObjectName("infoButton_2")
        self.horizontalLayout_9.addWidget(self.infoButton_2)
        self.gridLayout_2.addLayout(self.horizontalLayout_9, 2, 1, 1, 1)
        self.id_label_3 = QtWidgets.QLabel(self.tabWidgetPage1)
        self.id_label_3.setMinimumSize(QtCore.QSize(0, 0))
        self.id_label_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.id_label_3.setFont(font)
        self.id_label_3.setToolTip("")
        self.id_label_3.setObjectName("id_label_3")
        self.gridLayout_2.addWidget(self.id_label_3, 3, 0, 1, 1)
        self.horizontalLayout_29 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_29.setContentsMargins(2, -1, -1, -1)
        self.horizontalLayout_29.setSpacing(6)
        self.horizontalLayout_29.setObjectName("horizontalLayout_29")
        self.id_resourceType_rl1 = QtWidgets.QComboBox(self.tabWidgetPage1)
        self.id_resourceType_rl1.setMinimumSize(QtCore.QSize(120, 27))
        self.id_resourceType_rl1.setMaximumSize(QtCore.QSize(120, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.id_resourceType_rl1.setFont(font)
        self.id_resourceType_rl1.setStyleSheet("QComboBox {\n"
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
        self.id_resourceType_rl1.setFrame(False)
        self.id_resourceType_rl1.setObjectName("id_resourceType_rl1")
        self.id_resourceType_rl1.addItem("")
        self.id_resourceType_rl1.addItem("")
        self.horizontalLayout_29.addWidget(self.id_resourceType_rl1)
        self.infoButton_3 = QtWidgets.QToolButton(self.tabWidgetPage1)
        self.infoButton_3.setMinimumSize(QtCore.QSize(27, 27))
        self.infoButton_3.setMaximumSize(QtCore.QSize(27, 27))
        self.infoButton_3.setStyleSheet("QToolButton {\n"
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
        self.infoButton_3.setText("")
        self.infoButton_3.setIcon(icon1)
        self.infoButton_3.setIconSize(QtCore.QSize(27, 27))
        self.infoButton_3.setAutoRaise(False)
        self.infoButton_3.setObjectName("infoButton_3")
        self.horizontalLayout_29.addWidget(self.infoButton_3)
        spacerItem3 = QtWidgets.QSpacerItem(13, 24, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_29.addItem(spacerItem3)
        self.gridLayout_2.addLayout(self.horizontalLayout_29, 3, 1, 1, 1)
        self.id_resourceLocator_lb = QtWidgets.QLabel(self.tabWidgetPage1)
        self.id_resourceLocator_lb.setMinimumSize(QtCore.QSize(0, 0))
        self.id_resourceLocator_lb.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.id_resourceLocator_lb.setFont(font)
        self.id_resourceLocator_lb.setToolTip("")
        self.id_resourceLocator_lb.setObjectName("id_resourceLocator_lb")
        self.gridLayout_2.addWidget(self.id_resourceLocator_lb, 4, 0, 1, 1)
        self.horizontalLayout_36 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_36.setSpacing(6)
        self.horizontalLayout_36.setObjectName("horizontalLayout_36")
        self.id_resourceLocator_ln = QtWidgets.QLineEdit(self.tabWidgetPage1)
        self.id_resourceLocator_ln.setMinimumSize(QtCore.QSize(450, 27))
        self.id_resourceLocator_ln.setMaximumSize(QtCore.QSize(450, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.id_resourceLocator_ln.setFont(font)
        self.id_resourceLocator_ln.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.id_resourceLocator_ln.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"   padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"}")
        self.id_resourceLocator_ln.setFrame(False)
        self.id_resourceLocator_ln.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.id_resourceLocator_ln.setObjectName("id_resourceLocator_ln")
        self.horizontalLayout_36.addWidget(self.id_resourceLocator_ln)
        self.infoButton_4 = QtWidgets.QToolButton(self.tabWidgetPage1)
        self.infoButton_4.setMinimumSize(QtCore.QSize(27, 27))
        self.infoButton_4.setMaximumSize(QtCore.QSize(27, 27))
        self.infoButton_4.setStyleSheet("QToolButton {\n"
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
        self.infoButton_4.setText("")
        self.infoButton_4.setIcon(icon1)
        self.infoButton_4.setIconSize(QtCore.QSize(27, 27))
        self.infoButton_4.setAutoRaise(False)
        self.infoButton_4.setObjectName("infoButton_4")
        self.horizontalLayout_36.addWidget(self.infoButton_4)
        spacerItem4 = QtWidgets.QSpacerItem(13, 24, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_36.addItem(spacerItem4)
        self.gridLayout_2.addLayout(self.horizontalLayout_36, 4, 1, 1, 1)
        self.id_label_6 = QtWidgets.QLabel(self.tabWidgetPage1)
        self.id_label_6.setMinimumSize(QtCore.QSize(0, 0))
        self.id_label_6.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.id_label_6.setFont(font)
        self.id_label_6.setToolTip("")
        self.id_label_6.setObjectName("id_label_6")
        self.gridLayout_2.addWidget(self.id_label_6, 5, 0, 1, 1)
        self.horizontalLayout_42 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_42.setContentsMargins(2, -1, -1, -1)
        self.horizontalLayout_42.setSpacing(6)
        self.horizontalLayout_42.setObjectName("horizontalLayout_42")
        self.id_resourceLang_rl2 = QtWidgets.QComboBox(self.tabWidgetPage1)
        self.id_resourceLang_rl2.setMinimumSize(QtCore.QSize(120, 27))
        self.id_resourceLang_rl2.setMaximumSize(QtCore.QSize(120, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.id_resourceLang_rl2.setFont(font)
        self.id_resourceLang_rl2.setStyleSheet("QComboBox {\n"
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
        self.id_resourceLang_rl2.setFrame(False)
        self.id_resourceLang_rl2.setObjectName("id_resourceLang_rl2")
        self.id_resourceLang_rl2.addItem("")
        self.id_resourceLang_rl2.addItem("")
        self.id_resourceLang_rl2.addItem("")
        self.id_resourceLang_rl2.addItem("")
        self.id_resourceLang_rl2.addItem("")
        self.id_resourceLang_rl2.addItem("")
        self.id_resourceLang_rl2.addItem("")
        self.id_resourceLang_rl2.addItem("")
        self.id_resourceLang_rl2.addItem("")
        self.id_resourceLang_rl2.addItem("")
        self.id_resourceLang_rl2.addItem("")
        self.id_resourceLang_rl2.addItem("")
        self.id_resourceLang_rl2.addItem("")
        self.id_resourceLang_rl2.addItem("")
        self.id_resourceLang_rl2.addItem("")
        self.id_resourceLang_rl2.addItem("")
        self.id_resourceLang_rl2.addItem("")
        self.id_resourceLang_rl2.addItem("")
        self.id_resourceLang_rl2.addItem("")
        self.id_resourceLang_rl2.addItem("")
        self.id_resourceLang_rl2.addItem("")
        self.id_resourceLang_rl2.addItem("")
        self.id_resourceLang_rl2.addItem("")
        self.horizontalLayout_42.addWidget(self.id_resourceLang_rl2)
        self.infoButton_6 = QtWidgets.QToolButton(self.tabWidgetPage1)
        self.infoButton_6.setMaximumSize(QtCore.QSize(27, 27))
        self.infoButton_6.setStyleSheet("QToolButton {\n"
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
        self.infoButton_6.setText("")
        self.infoButton_6.setIcon(icon1)
        self.infoButton_6.setIconSize(QtCore.QSize(27, 27))
        self.infoButton_6.setAutoRaise(False)
        self.infoButton_6.setObjectName("infoButton_6")
        self.horizontalLayout_42.addWidget(self.infoButton_6)
        spacerItem5 = QtWidgets.QSpacerItem(13, 24, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_42.addItem(spacerItem5)
        self.gridLayout_2.addLayout(self.horizontalLayout_42, 5, 1, 1, 1)
        self.gridLayout_15.addLayout(self.gridLayout_2, 1, 1, 2, 2)
        spacerItem6 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_15.addItem(spacerItem6, 1, 3, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_15.addItem(spacerItem7, 2, 0, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 66, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_15.addItem(spacerItem8, 3, 1, 1, 1)
        self.tabWidget.addTab(self.tabWidgetPage1, "")
        self.tabWidgetPage2 = QtWidgets.QWidget()
        self.tabWidgetPage2.setObjectName("tabWidgetPage2")
        self.gridLayout_16 = QtWidgets.QGridLayout(self.tabWidgetPage2)
        self.gridLayout_16.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_16.setObjectName("gridLayout_16")
        spacerItem9 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_16.addItem(spacerItem9, 0, 1, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_16.addItem(spacerItem10, 1, 0, 1, 1)
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.gridLayout_13 = QtWidgets.QGridLayout()
        self.gridLayout_13.setHorizontalSpacing(6)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.cl_topicIntelligence_ck = QtWidgets.QCheckBox(self.tabWidgetPage2)
        self.cl_topicIntelligence_ck.setMinimumSize(QtCore.QSize(0, 27))
        self.cl_topicIntelligence_ck.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.cl_topicIntelligence_ck.setFont(font)
        self.cl_topicIntelligence_ck.setObjectName("cl_topicIntelligence_ck")
        self.gridLayout_13.addWidget(self.cl_topicIntelligence_ck, 0, 4, 1, 1)
        self.cl_topicLocation_ck = QtWidgets.QCheckBox(self.tabWidgetPage2)
        self.cl_topicLocation_ck.setMinimumSize(QtCore.QSize(0, 27))
        self.cl_topicLocation_ck.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.cl_topicLocation_ck.setFont(font)
        self.cl_topicLocation_ck.setObjectName("cl_topicLocation_ck")
        self.gridLayout_13.addWidget(self.cl_topicLocation_ck, 2, 4, 1, 1)
        self.cl_topicPlanning_ck = QtWidgets.QCheckBox(self.tabWidgetPage2)
        self.cl_topicPlanning_ck.setMinimumSize(QtCore.QSize(0, 27))
        self.cl_topicPlanning_ck.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.cl_topicPlanning_ck.setFont(font)
        self.cl_topicPlanning_ck.setObjectName("cl_topicPlanning_ck")
        self.gridLayout_13.addWidget(self.cl_topicPlanning_ck, 4, 4, 1, 1)
        self.cl_topicEconomy_ck = QtWidgets.QCheckBox(self.tabWidgetPage2)
        self.cl_topicEconomy_ck.setMinimumSize(QtCore.QSize(0, 27))
        self.cl_topicEconomy_ck.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.cl_topicEconomy_ck.setFont(font)
        self.cl_topicEconomy_ck.setObjectName("cl_topicEconomy_ck")
        self.gridLayout_13.addWidget(self.cl_topicEconomy_ck, 3, 2, 1, 1)
        self.cl_topicSociety_ck = QtWidgets.QCheckBox(self.tabWidgetPage2)
        self.cl_topicSociety_ck.setMinimumSize(QtCore.QSize(0, 27))
        self.cl_topicSociety_ck.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.cl_topicSociety_ck.setFont(font)
        self.cl_topicSociety_ck.setObjectName("cl_topicSociety_ck")
        self.gridLayout_13.addWidget(self.cl_topicSociety_ck, 5, 4, 1, 1)
        self.cl_topicStructure_ck = QtWidgets.QCheckBox(self.tabWidgetPage2)
        self.cl_topicStructure_ck.setMinimumSize(QtCore.QSize(0, 27))
        self.cl_topicStructure_ck.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.cl_topicStructure_ck.setFont(font)
        self.cl_topicStructure_ck.setObjectName("cl_topicStructure_ck")
        self.gridLayout_13.addWidget(self.cl_topicStructure_ck, 6, 4, 1, 1)
        self.cl_label_1 = QtWidgets.QLabel(self.tabWidgetPage2)
        self.cl_label_1.setMinimumSize(QtCore.QSize(0, 0))
        self.cl_label_1.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.cl_label_1.setFont(font)
        self.cl_label_1.setToolTip("")
        self.cl_label_1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.cl_label_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.cl_label_1.setScaledContents(False)
        self.cl_label_1.setObjectName("cl_label_1")
        self.gridLayout_13.addWidget(self.cl_label_1, 4, 0, 2, 1)
        self.cl_topicTransportation_ck = QtWidgets.QCheckBox(self.tabWidgetPage2)
        self.cl_topicTransportation_ck.setMinimumSize(QtCore.QSize(0, 27))
        self.cl_topicTransportation_ck.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.cl_topicTransportation_ck.setFont(font)
        self.cl_topicTransportation_ck.setObjectName("cl_topicTransportation_ck")
        self.gridLayout_13.addWidget(self.cl_topicTransportation_ck, 7, 4, 1, 1)
        self.cl_topicClimatology_ck = QtWidgets.QCheckBox(self.tabWidgetPage2)
        self.cl_topicClimatology_ck.setMinimumSize(QtCore.QSize(0, 27))
        self.cl_topicClimatology_ck.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.cl_topicClimatology_ck.setFont(font)
        self.cl_topicClimatology_ck.setObjectName("cl_topicClimatology_ck")
        self.gridLayout_13.addWidget(self.cl_topicClimatology_ck, 2, 2, 1, 1)
        self.cl_topicElevation_ck = QtWidgets.QCheckBox(self.tabWidgetPage2)
        self.cl_topicElevation_ck.setMinimumSize(QtCore.QSize(0, 27))
        self.cl_topicElevation_ck.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.cl_topicElevation_ck.setFont(font)
        self.cl_topicElevation_ck.setObjectName("cl_topicElevation_ck")
        self.gridLayout_13.addWidget(self.cl_topicElevation_ck, 4, 2, 1, 1)
        self.cl_topicOceans_ck = QtWidgets.QCheckBox(self.tabWidgetPage2)
        self.cl_topicOceans_ck.setMinimumSize(QtCore.QSize(0, 27))
        self.cl_topicOceans_ck.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.cl_topicOceans_ck.setFont(font)
        self.cl_topicOceans_ck.setObjectName("cl_topicOceans_ck")
        self.gridLayout_13.addWidget(self.cl_topicOceans_ck, 3, 4, 1, 1)
        self.cl_topicImagery_ck = QtWidgets.QCheckBox(self.tabWidgetPage2)
        self.cl_topicImagery_ck.setMinimumSize(QtCore.QSize(0, 27))
        self.cl_topicImagery_ck.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.cl_topicImagery_ck.setFont(font)
        self.cl_topicImagery_ck.setObjectName("cl_topicImagery_ck")
        self.gridLayout_13.addWidget(self.cl_topicImagery_ck, 9, 2, 1, 1)
        self.cl_topicEnvironment_ck = QtWidgets.QCheckBox(self.tabWidgetPage2)
        self.cl_topicEnvironment_ck.setMinimumSize(QtCore.QSize(0, 27))
        self.cl_topicEnvironment_ck.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.cl_topicEnvironment_ck.setFont(font)
        self.cl_topicEnvironment_ck.setObjectName("cl_topicEnvironment_ck")
        self.gridLayout_13.addWidget(self.cl_topicEnvironment_ck, 5, 2, 1, 1)
        self.cl_topicWaters_ck = QtWidgets.QCheckBox(self.tabWidgetPage2)
        self.cl_topicWaters_ck.setMinimumSize(QtCore.QSize(0, 27))
        self.cl_topicWaters_ck.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.cl_topicWaters_ck.setFont(font)
        self.cl_topicWaters_ck.setObjectName("cl_topicWaters_ck")
        self.gridLayout_13.addWidget(self.cl_topicWaters_ck, 1, 4, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_13.addItem(spacerItem11, 4, 3, 1, 1)
        self.cl_topicUtilities_ck = QtWidgets.QCheckBox(self.tabWidgetPage2)
        self.cl_topicUtilities_ck.setMinimumSize(QtCore.QSize(0, 27))
        self.cl_topicUtilities_ck.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.cl_topicUtilities_ck.setFont(font)
        self.cl_topicUtilities_ck.setObjectName("cl_topicUtilities_ck")
        self.gridLayout_13.addWidget(self.cl_topicUtilities_ck, 8, 4, 1, 1)
        self.cl_topicBiota_ck = QtWidgets.QCheckBox(self.tabWidgetPage2)
        self.cl_topicBiota_ck.setMinimumSize(QtCore.QSize(0, 0))
        self.cl_topicBiota_ck.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.cl_topicBiota_ck.setFont(font)
        self.cl_topicBiota_ck.setTristate(False)
        self.cl_topicBiota_ck.setObjectName("cl_topicBiota_ck")
        self.gridLayout_13.addWidget(self.cl_topicBiota_ck, 0, 2, 1, 1)
        self.cl_topicFarming_ck = QtWidgets.QCheckBox(self.tabWidgetPage2)
        self.cl_topicFarming_ck.setMinimumSize(QtCore.QSize(0, 27))
        self.cl_topicFarming_ck.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.cl_topicFarming_ck.setFont(font)
        self.cl_topicFarming_ck.setObjectName("cl_topicFarming_ck")
        self.gridLayout_13.addWidget(self.cl_topicFarming_ck, 6, 2, 1, 1)
        self.cl_topicBoundaries_ck = QtWidgets.QCheckBox(self.tabWidgetPage2)
        self.cl_topicBoundaries_ck.setMinimumSize(QtCore.QSize(0, 27))
        self.cl_topicBoundaries_ck.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.cl_topicBoundaries_ck.setFont(font)
        self.cl_topicBoundaries_ck.setObjectName("cl_topicBoundaries_ck")
        self.gridLayout_13.addWidget(self.cl_topicBoundaries_ck, 1, 2, 1, 1)
        self.cl_topicHealth_ck = QtWidgets.QCheckBox(self.tabWidgetPage2)
        self.cl_topicHealth_ck.setMinimumSize(QtCore.QSize(0, 27))
        self.cl_topicHealth_ck.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.cl_topicHealth_ck.setFont(font)
        self.cl_topicHealth_ck.setObjectName("cl_topicHealth_ck")
        self.gridLayout_13.addWidget(self.cl_topicHealth_ck, 8, 2, 1, 1)
        self.cl_topicInformation_ck = QtWidgets.QCheckBox(self.tabWidgetPage2)
        self.cl_topicInformation_ck.setMinimumSize(QtCore.QSize(0, 27))
        self.cl_topicInformation_ck.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.cl_topicInformation_ck.setFont(font)
        self.cl_topicInformation_ck.setObjectName("cl_topicInformation_ck")
        self.gridLayout_13.addWidget(self.cl_topicInformation_ck, 7, 2, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_13.addItem(spacerItem12, 4, 1, 1, 1)
        self.horizontalLayout_19.addLayout(self.gridLayout_13)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_19.addItem(spacerItem13)
        self.infoButton_7 = QtWidgets.QToolButton(self.tabWidgetPage2)
        self.infoButton_7.setMaximumSize(QtCore.QSize(27, 27))
        self.infoButton_7.setStyleSheet("QToolButton {\n"
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
        self.infoButton_7.setText("")
        self.infoButton_7.setIcon(icon1)
        self.infoButton_7.setIconSize(QtCore.QSize(27, 27))
        self.infoButton_7.setAutoRaise(False)
        self.infoButton_7.setObjectName("infoButton_7")
        self.horizontalLayout_19.addWidget(self.infoButton_7)
        self.gridLayout_16.addLayout(self.horizontalLayout_19, 1, 1, 2, 2)
        spacerItem14 = QtWidgets.QSpacerItem(218, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_16.addItem(spacerItem14, 2, 3, 1, 1)
        spacerItem15 = QtWidgets.QSpacerItem(20, 158, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_16.addItem(spacerItem15, 3, 2, 1, 1)
        self.tabWidget.addTab(self.tabWidgetPage2, "")
        self.tabWidgetPage3 = QtWidgets.QWidget()
        self.tabWidgetPage3.setObjectName("tabWidgetPage3")
        self.gridLayout_20 = QtWidgets.QGridLayout(self.tabWidgetPage3)
        self.gridLayout_20.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_20.setObjectName("gridLayout_20")
        spacerItem16 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_20.addItem(spacerItem16, 0, 1, 1, 1)
        spacerItem17 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_20.addItem(spacerItem17, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setVerticalSpacing(0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.kw_category_lb1 = QtWidgets.QLabel(self.tabWidgetPage3)
        self.kw_category_lb1.setMinimumSize(QtCore.QSize(0, 27))
        self.kw_category_lb1.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.kw_category_lb1.setFont(font)
        self.kw_category_lb1.setIndent(-2)
        self.kw_category_lb1.setObjectName("kw_category_lb1")
        self.gridLayout_5.addWidget(self.kw_category_lb1, 0, 0, 1, 1)
        self.kw_agriEngineering_ck = QtWidgets.QCheckBox(self.tabWidgetPage3)
        self.kw_agriEngineering_ck.setMinimumSize(QtCore.QSize(0, 0))
        self.kw_agriEngineering_ck.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.kw_agriEngineering_ck.setFont(font)
        self.kw_agriEngineering_ck.setObjectName("kw_agriEngineering_ck")
        self.gridLayout_5.addWidget(self.kw_agriEngineering_ck, 1, 0, 1, 1)
        self.kw_agriPlant_ck = QtWidgets.QCheckBox(self.tabWidgetPage3)
        self.kw_agriPlant_ck.setMinimumSize(QtCore.QSize(0, 0))
        self.kw_agriPlant_ck.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.kw_agriPlant_ck.setFont(font)
        self.kw_agriPlant_ck.setObjectName("kw_agriPlant_ck")
        self.gridLayout_5.addWidget(self.kw_agriPlant_ck, 2, 0, 1, 1)
        self.kw_foodScience_ck = QtWidgets.QCheckBox(self.tabWidgetPage3)
        self.kw_foodScience_ck.setMinimumSize(QtCore.QSize(0, 0))
        self.kw_foodScience_ck.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.kw_foodScience_ck.setFont(font)
        self.kw_foodScience_ck.setObjectName("kw_foodScience_ck")
        self.gridLayout_5.addWidget(self.kw_foodScience_ck, 3, 0, 1, 1)
        self.kw_forestScience_ck = QtWidgets.QCheckBox(self.tabWidgetPage3)
        self.kw_forestScience_ck.setMinimumSize(QtCore.QSize(0, 0))
        self.kw_forestScience_ck.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.kw_forestScience_ck.setFont(font)
        self.kw_forestScience_ck.setObjectName("kw_forestScience_ck")
        self.gridLayout_5.addWidget(self.kw_forestScience_ck, 4, 0, 1, 1)
        self.kw_soils_ck = QtWidgets.QCheckBox(self.tabWidgetPage3)
        self.kw_soils_ck.setMinimumSize(QtCore.QSize(0, 0))
        self.kw_soils_ck.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.kw_soils_ck.setFont(font)
        self.kw_soils_ck.setObjectName("kw_soils_ck")
        self.gridLayout_5.addWidget(self.kw_soils_ck, 5, 0, 1, 1)
        self.kw_category_lb2 = QtWidgets.QLabel(self.tabWidgetPage3)
        self.kw_category_lb2.setMinimumSize(QtCore.QSize(0, 27))
        self.kw_category_lb2.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.kw_category_lb2.setFont(font)
        self.kw_category_lb2.setIndent(-2)
        self.kw_category_lb2.setObjectName("kw_category_lb2")
        self.gridLayout_5.addWidget(self.kw_category_lb2, 6, 0, 1, 1)
        self.kw_aerosols_ck = QtWidgets.QCheckBox(self.tabWidgetPage3)
        self.kw_aerosols_ck.setMinimumSize(QtCore.QSize(0, 0))
        self.kw_aerosols_ck.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.kw_aerosols_ck.setFont(font)
        self.kw_aerosols_ck.setObjectName("kw_aerosols_ck")
        self.gridLayout_5.addWidget(self.kw_aerosols_ck, 7, 0, 1, 1)
        self.kw_airQuality_ck = QtWidgets.QCheckBox(self.tabWidgetPage3)
        self.kw_airQuality_ck.setMinimumSize(QtCore.QSize(0, 0))
        self.kw_airQuality_ck.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.kw_airQuality_ck.setFont(font)
        self.kw_airQuality_ck.setObjectName("kw_airQuality_ck")
        self.gridLayout_5.addWidget(self.kw_airQuality_ck, 8, 0, 1, 1)
        self.kw_altitude_ck = QtWidgets.QCheckBox(self.tabWidgetPage3)
        self.kw_altitude_ck.setMinimumSize(QtCore.QSize(0, 0))
        self.kw_altitude_ck.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.kw_altitude_ck.setFont(font)
        self.kw_altitude_ck.setObjectName("kw_altitude_ck")
        self.gridLayout_5.addWidget(self.kw_altitude_ck, 9, 0, 1, 1)
        self.kw_atmChemistry_ck = QtWidgets.QCheckBox(self.tabWidgetPage3)
        self.kw_atmChemistry_ck.setMinimumSize(QtCore.QSize(0, 0))
        self.kw_atmChemistry_ck.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.kw_atmChemistry_ck.setFont(font)
        self.kw_atmChemistry_ck.setObjectName("kw_atmChemistry_ck")
        self.gridLayout_5.addWidget(self.kw_atmChemistry_ck, 10, 0, 1, 1)
        self.kw_atmElectricity_ck = QtWidgets.QCheckBox(self.tabWidgetPage3)
        self.kw_atmElectricity_ck.setMinimumSize(QtCore.QSize(0, 0))
        self.kw_atmElectricity_ck.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.kw_atmElectricity_ck.setFont(font)
        self.kw_atmElectricity_ck.setObjectName("kw_atmElectricity_ck")
        self.gridLayout_5.addWidget(self.kw_atmElectricity_ck, 11, 0, 1, 1)
        self.kw_atmPhenomena_ck = QtWidgets.QCheckBox(self.tabWidgetPage3)
        self.kw_atmPhenomena_ck.setMinimumSize(QtCore.QSize(0, 0))
        self.kw_atmPhenomena_ck.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.kw_atmPhenomena_ck.setFont(font)
        self.kw_atmPhenomena_ck.setObjectName("kw_atmPhenomena_ck")
        self.gridLayout_5.addWidget(self.kw_atmPhenomena_ck, 12, 0, 1, 1)
        self.kw_atmPressure_ck = QtWidgets.QCheckBox(self.tabWidgetPage3)
        self.kw_atmPressure_ck.setMinimumSize(QtCore.QSize(0, 0))
        self.kw_atmPressure_ck.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.kw_atmPressure_ck.setFont(font)
        self.kw_atmPressure_ck.setObjectName("kw_atmPressure_ck")
        self.gridLayout_5.addWidget(self.kw_atmPressure_ck, 13, 0, 1, 1)
        self.kw_atmRadiation_ck = QtWidgets.QCheckBox(self.tabWidgetPage3)
        self.kw_atmRadiation_ck.setMinimumSize(QtCore.QSize(0, 0))
        self.kw_atmRadiation_ck.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.kw_atmRadiation_ck.setFont(font)
        self.kw_atmRadiation_ck.setObjectName("kw_atmRadiation_ck")
        self.gridLayout_5.addWidget(self.kw_atmRadiation_ck, 14, 0, 1, 1)
        self.kw_atmTemperature_ck = QtWidgets.QCheckBox(self.tabWidgetPage3)
        self.kw_atmTemperature_ck.setMinimumSize(QtCore.QSize(0, 0))
        self.kw_atmTemperature_ck.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.kw_atmTemperature_ck.setFont(font)
        self.kw_atmTemperature_ck.setObjectName("kw_atmTemperature_ck")
        self.gridLayout_5.addWidget(self.kw_atmTemperature_ck, 15, 0, 1, 1)
        self.kw_atmVapor_ck = QtWidgets.QCheckBox(self.tabWidgetPage3)
        self.kw_atmVapor_ck.setMinimumSize(QtCore.QSize(0, 0))
        self.kw_atmVapor_ck.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.kw_atmVapor_ck.setFont(font)
        self.kw_atmVapor_ck.setObjectName("kw_atmVapor_ck")
        self.gridLayout_5.addWidget(self.kw_atmVapor_ck, 16, 0, 1, 1)
        self.kw_atmWinds_ck = QtWidgets.QCheckBox(self.tabWidgetPage3)
        self.kw_atmWinds_ck.setMinimumSize(QtCore.QSize(0, 0))
        self.kw_atmWinds_ck.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.kw_atmWinds_ck.setFont(font)
        self.kw_atmWinds_ck.setObjectName("kw_atmWinds_ck")
        self.gridLayout_5.addWidget(self.kw_atmWinds_ck, 17, 0, 1, 1)
        self.kw_clouds_ck = QtWidgets.QCheckBox(self.tabWidgetPage3)
        self.kw_clouds_ck.setMinimumSize(QtCore.QSize(0, 0))
        self.kw_clouds_ck.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.kw_clouds_ck.setFont(font)
        self.kw_clouds_ck.setObjectName("kw_clouds_ck")
        self.gridLayout_5.addWidget(self.kw_clouds_ck, 18, 0, 1, 1)
        self.kw_precipitation_ck = QtWidgets.QCheckBox(self.tabWidgetPage3)
        self.kw_precipitation_ck.setMinimumSize(QtCore.QSize(0, 0))
        self.kw_precipitation_ck.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.kw_precipitation_ck.setFont(font)
        self.kw_precipitation_ck.setObjectName("kw_precipitation_ck")
        self.gridLayout_5.addWidget(self.kw_precipitation_ck, 19, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout_5)
        spacerItem18 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem18)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout_17 = QtWidgets.QGridLayout()
        self.gridLayout_17.setVerticalSpacing(0)
        self.gridLayout_17.setObjectName("gridLayout_17")
        self.kw_category_lb3 = QtWidgets.QLabel(self.tabWidgetPage3)
        self.kw_category_lb3.setMinimumSize(QtCore.QSize(0, 27))
        self.kw_category_lb3.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.kw_category_lb3.setFont(font)
        self.kw_category_lb3.setObjectName("kw_category_lb3")
        self.gridLayout_17.addWidget(self.kw_category_lb3, 0, 0, 1, 1)
        self.kw_ecoDynamics_ck = QtWidgets.QCheckBox(self.tabWidgetPage3)
        self.kw_ecoDynamics_ck.setMinimumSize(QtCore.QSize(0, 0))
        self.kw_ecoDynamics_ck.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.kw_ecoDynamics_ck.setFont(font)
        self.kw_ecoDynamics_ck.setObjectName("kw_ecoDynamics_ck")
        self.gridLayout_17.addWidget(self.kw_ecoDynamics_ck, 1, 0, 1, 1)
        self.kw_terEcosystems_ck = QtWidgets.QCheckBox(self.tabWidgetPage3)
        self.kw_terEcosystems_ck.setMinimumSize(QtCore.QSize(0, 0))
        self.kw_terEcosystems_ck.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.kw_terEcosystems_ck.setFont(font)
        self.kw_terEcosystems_ck.setObjectName("kw_terEcosystems_ck")
        self.gridLayout_17.addWidget(self.kw_terEcosystems_ck, 2, 0, 1, 1)
        self.kw_vegetation_ck = QtWidgets.QCheckBox(self.tabWidgetPage3)
        self.kw_vegetation_ck.setMinimumSize(QtCore.QSize(0, 0))
        self.kw_vegetation_ck.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.kw_vegetation_ck.setFont(font)
        self.kw_vegetation_ck.setObjectName("kw_vegetation_ck")
        self.gridLayout_17.addWidget(self.kw_vegetation_ck, 3, 0, 1, 1)
        self.kw_category_lb4 = QtWidgets.QLabel(self.tabWidgetPage3)
        self.kw_category_lb4.setMinimumSize(QtCore.QSize(0, 27))
        self.kw_category_lb4.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.kw_category_lb4.setFont(font)
        self.kw_category_lb4.setIndent(0)
        self.kw_category_lb4.setObjectName("kw_category_lb4")
        self.gridLayout_17.addWidget(self.kw_category_lb4, 4, 0, 1, 1)
        self.kw_frozenGround_ck = QtWidgets.QCheckBox(self.tabWidgetPage3)
        self.kw_frozenGround_ck.setMinimumSize(QtCore.QSize(0, 0))
        self.kw_frozenGround_ck.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.kw_frozenGround_ck.setFont(font)
        self.kw_frozenGround_ck.setObjectName("kw_frozenGround_ck")
        self.gridLayout_17.addWidget(self.kw_frozenGround_ck, 5, 0, 1, 1)
        self.kw_glaciersIcesheet_ck = QtWidgets.QCheckBox(self.tabWidgetPage3)
        self.kw_glaciersIcesheet_ck.setMinimumSize(QtCore.QSize(0, 0))
        self.kw_glaciersIcesheet_ck.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.kw_glaciersIcesheet_ck.setFont(font)
        self.kw_glaciersIcesheet_ck.setObjectName("kw_glaciersIcesheet_ck")
        self.gridLayout_17.addWidget(self.kw_glaciersIcesheet_ck, 6, 0, 1, 1)
        self.kw_seaIce_ck = QtWidgets.QCheckBox(self.tabWidgetPage3)
        self.kw_seaIce_ck.setMinimumSize(QtCore.QSize(0, 0))
        self.kw_seaIce_ck.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.kw_seaIce_ck.setFont(font)
        self.kw_seaIce_ck.setObjectName("kw_seaIce_ck")
        self.gridLayout_17.addWidget(self.kw_seaIce_ck, 7, 0, 1, 1)
        self.kw_snowIce_ck = QtWidgets.QCheckBox(self.tabWidgetPage3)
        self.kw_snowIce_ck.setMinimumSize(QtCore.QSize(0, 0))
        self.kw_snowIce_ck.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.kw_snowIce_ck.setFont(font)
        self.kw_snowIce_ck.setObjectName("kw_snowIce_ck")
        self.gridLayout_17.addWidget(self.kw_snowIce_ck, 8, 0, 1, 1)
        self.kw_category_lb5 = QtWidgets.QLabel(self.tabWidgetPage3)
        self.kw_category_lb5.setMinimumSize(QtCore.QSize(0, 27))
        self.kw_category_lb5.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.kw_category_lb5.setFont(font)
        self.kw_category_lb5.setObjectName("kw_category_lb5")
        self.gridLayout_17.addWidget(self.kw_category_lb5, 9, 0, 1, 1)
        self.kw_erosionSedimentation_ck = QtWidgets.QCheckBox(self.tabWidgetPage3)
        self.kw_erosionSedimentation_ck.setMinimumSize(QtCore.QSize(0, 0))
        self.kw_erosionSedimentation_ck.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.kw_erosionSedimentation_ck.setFont(font)
        self.kw_erosionSedimentation_ck.setObjectName("kw_erosionSedimentation_ck")
        self.gridLayout_17.addWidget(self.kw_erosionSedimentation_ck, 10, 0, 1, 1)
        self.kw_geomorphology_ck = QtWidgets.QCheckBox(self.tabWidgetPage3)
        self.kw_geomorphology_ck.setMinimumSize(QtCore.QSize(0, 0))
        self.kw_geomorphology_ck.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.kw_geomorphology_ck.setFont(font)
        self.kw_geomorphology_ck.setObjectName("kw_geomorphology_ck")
        self.gridLayout_17.addWidget(self.kw_geomorphology_ck, 11, 0, 1, 1)
        self.kw_landTemperature_ck = QtWidgets.QCheckBox(self.tabWidgetPage3)
        self.kw_landTemperature_ck.setMinimumSize(QtCore.QSize(0, 0))
        self.kw_landTemperature_ck.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.kw_landTemperature_ck.setFont(font)
        self.kw_landTemperature_ck.setObjectName("kw_landTemperature_ck")
        self.gridLayout_17.addWidget(self.kw_landTemperature_ck, 12, 0, 1, 1)
        self.kw_landCover_ck = QtWidgets.QCheckBox(self.tabWidgetPage3)
        self.kw_landCover_ck.setMinimumSize(QtCore.QSize(0, 0))
        self.kw_landCover_ck.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.kw_landCover_ck.setFont(font)
        self.kw_landCover_ck.setObjectName("kw_landCover_ck")
        self.gridLayout_17.addWidget(self.kw_landCover_ck, 13, 0, 1, 1)
        self.kw_landscape_ck = QtWidgets.QCheckBox(self.tabWidgetPage3)
        self.kw_landscape_ck.setMinimumSize(QtCore.QSize(0, 0))
        self.kw_landscape_ck.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.kw_landscape_ck.setFont(font)
        self.kw_landscape_ck.setObjectName("kw_landscape_ck")
        self.gridLayout_17.addWidget(self.kw_landscape_ck, 14, 0, 1, 1)
        self.kw_surfaceProperties_ck = QtWidgets.QCheckBox(self.tabWidgetPage3)
        self.kw_surfaceProperties_ck.setMinimumSize(QtCore.QSize(0, 0))
        self.kw_surfaceProperties_ck.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.kw_surfaceProperties_ck.setFont(font)
        self.kw_surfaceProperties_ck.setObjectName("kw_surfaceProperties_ck")
        self.gridLayout_17.addWidget(self.kw_surfaceProperties_ck, 15, 0, 1, 1)
        self.kw_topography_ck = QtWidgets.QCheckBox(self.tabWidgetPage3)
        self.kw_topography_ck.setMinimumSize(QtCore.QSize(0, 0))
        self.kw_topography_ck.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.kw_topography_ck.setFont(font)
        self.kw_topography_ck.setObjectName("kw_topography_ck")
        self.gridLayout_17.addWidget(self.kw_topography_ck, 16, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_17)
        spacerItem19 = QtWidgets.QSpacerItem(20, 17, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem19)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        spacerItem20 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem20)
        self.gridLayout_18 = QtWidgets.QGridLayout()
        self.gridLayout_18.setVerticalSpacing(0)
        self.gridLayout_18.setObjectName("gridLayout_18")
        self.kw_category_lb6 = QtWidgets.QLabel(self.tabWidgetPage3)
        self.kw_category_lb6.setMinimumSize(QtCore.QSize(0, 27))
        self.kw_category_lb6.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.kw_category_lb6.setFont(font)
        self.kw_category_lb6.setObjectName("kw_category_lb6")
        self.gridLayout_18.addWidget(self.kw_category_lb6, 0, 0, 1, 1)
        self.kw_bathymetry_ck = QtWidgets.QCheckBox(self.tabWidgetPage3)
        self.kw_bathymetry_ck.setMinimumSize(QtCore.QSize(0, 0))
        self.kw_bathymetry_ck.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.kw_bathymetry_ck.setFont(font)
        self.kw_bathymetry_ck.setObjectName("kw_bathymetry_ck")
        self.gridLayout_18.addWidget(self.kw_bathymetry_ck, 1, 0, 1, 1)
        self.kw_coastalProcesses_ck = QtWidgets.QCheckBox(self.tabWidgetPage3)
        self.kw_coastalProcesses_ck.setMinimumSize(QtCore.QSize(0, 0))
        self.kw_coastalProcesses_ck.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.kw_coastalProcesses_ck.setFont(font)
        self.kw_coastalProcesses_ck.setObjectName("kw_coastalProcesses_ck")
        self.gridLayout_18.addWidget(self.kw_coastalProcesses_ck, 2, 0, 1, 1)
        self.kw_marineEnvironment_ck = QtWidgets.QCheckBox(self.tabWidgetPage3)
        self.kw_marineEnvironment_ck.setMinimumSize(QtCore.QSize(0, 0))
        self.kw_marineEnvironment_ck.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.kw_marineEnvironment_ck.setFont(font)
        self.kw_marineEnvironment_ck.setObjectName("kw_marineEnvironment_ck")
        self.gridLayout_18.addWidget(self.kw_marineEnvironment_ck, 3, 0, 1, 1)
        self.kw_marineGeophysics_ck = QtWidgets.QCheckBox(self.tabWidgetPage3)
        self.kw_marineGeophysics_ck.setMinimumSize(QtCore.QSize(0, 0))
        self.kw_marineGeophysics_ck.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.kw_marineGeophysics_ck.setFont(font)
        self.kw_marineGeophysics_ck.setObjectName("kw_marineGeophysics_ck")
        self.gridLayout_18.addWidget(self.kw_marineGeophysics_ck, 4, 0, 1, 1)
        self.kw_oceanWaves_ck = QtWidgets.QCheckBox(self.tabWidgetPage3)
        self.kw_oceanWaves_ck.setMinimumSize(QtCore.QSize(0, 0))
        self.kw_oceanWaves_ck.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.kw_oceanWaves_ck.setFont(font)
        self.kw_oceanWaves_ck.setObjectName("kw_oceanWaves_ck")
        self.gridLayout_18.addWidget(self.kw_oceanWaves_ck, 5, 0, 1, 1)
        self.kw_oceanWinds_ck = QtWidgets.QCheckBox(self.tabWidgetPage3)
        self.kw_oceanWinds_ck.setMinimumSize(QtCore.QSize(0, 0))
        self.kw_oceanWinds_ck.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.kw_oceanWinds_ck.setFont(font)
        self.kw_oceanWinds_ck.setObjectName("kw_oceanWinds_ck")
        self.gridLayout_18.addWidget(self.kw_oceanWinds_ck, 6, 0, 1, 1)
        self.kw_seaTopography_ck = QtWidgets.QCheckBox(self.tabWidgetPage3)
        self.kw_seaTopography_ck.setMinimumSize(QtCore.QSize(0, 0))
        self.kw_seaTopography_ck.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.kw_seaTopography_ck.setFont(font)
        self.kw_seaTopography_ck.setObjectName("kw_seaTopography_ck")
        self.gridLayout_18.addWidget(self.kw_seaTopography_ck, 7, 0, 1, 1)
        self.kw_seaTides_ck = QtWidgets.QCheckBox(self.tabWidgetPage3)
        self.kw_seaTides_ck.setMinimumSize(QtCore.QSize(0, 0))
        self.kw_seaTides_ck.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.kw_seaTides_ck.setFont(font)
        self.kw_seaTides_ck.setObjectName("kw_seaTides_ck")
        self.gridLayout_18.addWidget(self.kw_seaTides_ck, 8, 0, 1, 1)
        self.kw_waterQuality_ck_2 = QtWidgets.QCheckBox(self.tabWidgetPage3)
        self.kw_waterQuality_ck_2.setMinimumSize(QtCore.QSize(0, 0))
        self.kw_waterQuality_ck_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.kw_waterQuality_ck_2.setFont(font)
        self.kw_waterQuality_ck_2.setObjectName("kw_waterQuality_ck_2")
        self.gridLayout_18.addWidget(self.kw_waterQuality_ck_2, 9, 0, 1, 1)
        self.kw_category_lb7 = QtWidgets.QLabel(self.tabWidgetPage3)
        self.kw_category_lb7.setMinimumSize(QtCore.QSize(0, 27))
        self.kw_category_lb7.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.kw_category_lb7.setFont(font)
        self.kw_category_lb7.setObjectName("kw_category_lb7")
        self.gridLayout_18.addWidget(self.kw_category_lb7, 10, 0, 1, 1)
        self.kw_geodetics_ck = QtWidgets.QCheckBox(self.tabWidgetPage3)
        self.kw_geodetics_ck.setMinimumSize(QtCore.QSize(0, 0))
        self.kw_geodetics_ck.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.kw_geodetics_ck.setFont(font)
        self.kw_geodetics_ck.setObjectName("kw_geodetics_ck")
        self.gridLayout_18.addWidget(self.kw_geodetics_ck, 11, 0, 1, 1)
        self.kw_geomagnetism_ck = QtWidgets.QCheckBox(self.tabWidgetPage3)
        self.kw_geomagnetism_ck.setMinimumSize(QtCore.QSize(0, 0))
        self.kw_geomagnetism_ck.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.kw_geomagnetism_ck.setFont(font)
        self.kw_geomagnetism_ck.setObjectName("kw_geomagnetism_ck")
        self.gridLayout_18.addWidget(self.kw_geomagnetism_ck, 12, 0, 1, 1)
        self.kw_geomorphicLandforms_ck = QtWidgets.QCheckBox(self.tabWidgetPage3)
        self.kw_geomorphicLandforms_ck.setMinimumSize(QtCore.QSize(0, 0))
        self.kw_geomorphicLandforms_ck.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.kw_geomorphicLandforms_ck.setFont(font)
        self.kw_geomorphicLandforms_ck.setObjectName("kw_geomorphicLandforms_ck")
        self.gridLayout_18.addWidget(self.kw_geomorphicLandforms_ck, 13, 0, 1, 1)
        self.kw_gravity_ck = QtWidgets.QCheckBox(self.tabWidgetPage3)
        self.kw_gravity_ck.setMinimumSize(QtCore.QSize(0, 0))
        self.kw_gravity_ck.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.kw_gravity_ck.setFont(font)
        self.kw_gravity_ck.setObjectName("kw_gravity_ck")
        self.gridLayout_18.addWidget(self.kw_gravity_ck, 14, 0, 1, 1)
        self.kw_category_lb10 = QtWidgets.QLabel(self.tabWidgetPage3)
        self.kw_category_lb10.setMinimumSize(QtCore.QSize(0, 27))
        self.kw_category_lb10.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.kw_category_lb10.setFont(font)
        self.kw_category_lb10.setObjectName("kw_category_lb10")
        self.gridLayout_18.addWidget(self.kw_category_lb10, 15, 0, 1, 1)
        self.kw_groundWater_ck = QtWidgets.QCheckBox(self.tabWidgetPage3)
        self.kw_groundWater_ck.setMinimumSize(QtCore.QSize(0, 0))
        self.kw_groundWater_ck.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.kw_groundWater_ck.setFont(font)
        self.kw_groundWater_ck.setObjectName("kw_groundWater_ck")
        self.gridLayout_18.addWidget(self.kw_groundWater_ck, 16, 0, 1, 1)
        self.kw_surfaceWater_ck = QtWidgets.QCheckBox(self.tabWidgetPage3)
        self.kw_surfaceWater_ck.setMinimumSize(QtCore.QSize(0, 0))
        self.kw_surfaceWater_ck.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.kw_surfaceWater_ck.setFont(font)
        self.kw_surfaceWater_ck.setObjectName("kw_surfaceWater_ck")
        self.gridLayout_18.addWidget(self.kw_surfaceWater_ck, 17, 0, 1, 1)
        self.kw_waterQuality_ck = QtWidgets.QCheckBox(self.tabWidgetPage3)
        self.kw_waterQuality_ck.setMinimumSize(QtCore.QSize(0, 0))
        self.kw_waterQuality_ck.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.kw_waterQuality_ck.setFont(font)
        self.kw_waterQuality_ck.setObjectName("kw_waterQuality_ck")
        self.gridLayout_18.addWidget(self.kw_waterQuality_ck, 18, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout_18)
        spacerItem21 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem21)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.gridLayout_19 = QtWidgets.QGridLayout()
        self.gridLayout_19.setVerticalSpacing(0)
        self.gridLayout_19.setObjectName("gridLayout_19")
        self.kw_solarFlux_ck = QtWidgets.QCheckBox(self.tabWidgetPage3)
        self.kw_solarFlux_ck.setMinimumSize(QtCore.QSize(0, 0))
        self.kw_solarFlux_ck.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.kw_solarFlux_ck.setFont(font)
        self.kw_solarFlux_ck.setObjectName("kw_solarFlux_ck")
        self.gridLayout_19.addWidget(self.kw_solarFlux_ck, 13, 0, 1, 1)
        self.kw_ionosMagnetos_ck = QtWidgets.QCheckBox(self.tabWidgetPage3)
        self.kw_ionosMagnetos_ck.setMinimumSize(QtCore.QSize(0, 0))
        self.kw_ionosMagnetos_ck.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.kw_ionosMagnetos_ck.setFont(font)
        self.kw_ionosMagnetos_ck.setObjectName("kw_ionosMagnetos_ck")
        self.gridLayout_19.addWidget(self.kw_ionosMagnetos_ck, 11, 0, 1, 1)
        self.kw_xRay_ck = QtWidgets.QCheckBox(self.tabWidgetPage3)
        self.kw_xRay_ck.setMinimumSize(QtCore.QSize(0, 0))
        self.kw_xRay_ck.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.kw_xRay_ck.setFont(font)
        self.kw_xRay_ck.setObjectName("kw_xRay_ck")
        self.gridLayout_19.addWidget(self.kw_xRay_ck, 9, 0, 1, 1)
        self.kw_category_lb9 = QtWidgets.QLabel(self.tabWidgetPage3)
        self.kw_category_lb9.setMinimumSize(QtCore.QSize(0, 27))
        self.kw_category_lb9.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.kw_category_lb9.setFont(font)
        self.kw_category_lb9.setObjectName("kw_category_lb9")
        self.gridLayout_19.addWidget(self.kw_category_lb9, 10, 0, 1, 1)
        self.kw_solarActivity_ck = QtWidgets.QCheckBox(self.tabWidgetPage3)
        self.kw_solarActivity_ck.setMinimumSize(QtCore.QSize(0, 0))
        self.kw_solarActivity_ck.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.kw_solarActivity_ck.setFont(font)
        self.kw_solarActivity_ck.setObjectName("kw_solarActivity_ck")
        self.gridLayout_19.addWidget(self.kw_solarActivity_ck, 12, 0, 1, 1)
        self.kw_lidar_ck = QtWidgets.QCheckBox(self.tabWidgetPage3)
        self.kw_lidar_ck.setMinimumSize(QtCore.QSize(0, 0))
        self.kw_lidar_ck.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.kw_lidar_ck.setFont(font)
        self.kw_lidar_ck.setObjectName("kw_lidar_ck")
        self.gridLayout_19.addWidget(self.kw_lidar_ck, 3, 0, 1, 1)
        self.kw_radioWave_ck = QtWidgets.QCheckBox(self.tabWidgetPage3)
        self.kw_radioWave_ck.setMinimumSize(QtCore.QSize(0, 0))
        self.kw_radioWave_ck.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.kw_radioWave_ck.setFont(font)
        self.kw_radioWave_ck.setObjectName("kw_radioWave_ck")
        self.gridLayout_19.addWidget(self.kw_radioWave_ck, 6, 0, 1, 1)
        self.kw_radar_ck = QtWidgets.QCheckBox(self.tabWidgetPage3)
        self.kw_radar_ck.setMinimumSize(QtCore.QSize(0, 0))
        self.kw_radar_ck.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.kw_radar_ck.setFont(font)
        self.kw_radar_ck.setObjectName("kw_radar_ck")
        self.gridLayout_19.addWidget(self.kw_radar_ck, 5, 0, 1, 1)
        self.kw_visWavelentghs_ck = QtWidgets.QCheckBox(self.tabWidgetPage3)
        self.kw_visWavelentghs_ck.setMinimumSize(QtCore.QSize(0, 0))
        self.kw_visWavelentghs_ck.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.kw_visWavelentghs_ck.setFont(font)
        self.kw_visWavelentghs_ck.setObjectName("kw_visWavelentghs_ck")
        self.gridLayout_19.addWidget(self.kw_visWavelentghs_ck, 8, 0, 1, 1)
        self.kw_uvWavelentghs_ck = QtWidgets.QCheckBox(self.tabWidgetPage3)
        self.kw_uvWavelentghs_ck.setMinimumSize(QtCore.QSize(0, 0))
        self.kw_uvWavelentghs_ck.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.kw_uvWavelentghs_ck.setFont(font)
        self.kw_uvWavelentghs_ck.setObjectName("kw_uvWavelentghs_ck")
        self.gridLayout_19.addWidget(self.kw_uvWavelentghs_ck, 7, 0, 1, 1)
        self.kw_irWavelengths_ck = QtWidgets.QCheckBox(self.tabWidgetPage3)
        self.kw_irWavelengths_ck.setMinimumSize(QtCore.QSize(0, 0))
        self.kw_irWavelengths_ck.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.kw_irWavelengths_ck.setFont(font)
        self.kw_irWavelengths_ck.setObjectName("kw_irWavelengths_ck")
        self.gridLayout_19.addWidget(self.kw_irWavelengths_ck, 2, 0, 1, 1)
        self.kw_microwave_ck = QtWidgets.QCheckBox(self.tabWidgetPage3)
        self.kw_microwave_ck.setMinimumSize(QtCore.QSize(0, 0))
        self.kw_microwave_ck.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.kw_microwave_ck.setFont(font)
        self.kw_microwave_ck.setObjectName("kw_microwave_ck")
        self.gridLayout_19.addWidget(self.kw_microwave_ck, 4, 0, 1, 1)
        self.kw_gammaRay_ck = QtWidgets.QCheckBox(self.tabWidgetPage3)
        self.kw_gammaRay_ck.setMinimumSize(QtCore.QSize(0, 0))
        self.kw_gammaRay_ck.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.kw_gammaRay_ck.setFont(font)
        self.kw_gammaRay_ck.setObjectName("kw_gammaRay_ck")
        self.gridLayout_19.addWidget(self.kw_gammaRay_ck, 1, 0, 1, 1)
        self.kw_category_lb8 = QtWidgets.QLabel(self.tabWidgetPage3)
        self.kw_category_lb8.setMinimumSize(QtCore.QSize(0, 27))
        self.kw_category_lb8.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.kw_category_lb8.setFont(font)
        self.kw_category_lb8.setObjectName("kw_category_lb8")
        self.gridLayout_19.addWidget(self.kw_category_lb8, 0, 0, 1, 1)
        self.verticalLayout_8.addLayout(self.gridLayout_19)
        spacerItem22 = QtWidgets.QSpacerItem(20, 17, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem22)
        self.horizontalLayout.addLayout(self.verticalLayout_8)
        spacerItem23 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem23)
        self.infoButton_8 = QtWidgets.QToolButton(self.tabWidgetPage3)
        self.infoButton_8.setMaximumSize(QtCore.QSize(27, 27))
        self.infoButton_8.setStyleSheet("QToolButton {\n"
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
        self.infoButton_8.setText("")
        self.infoButton_8.setIcon(icon1)
        self.infoButton_8.setIconSize(QtCore.QSize(27, 27))
        self.infoButton_8.setAutoRaise(False)
        self.infoButton_8.setObjectName("infoButton_8")
        self.horizontalLayout.addWidget(self.infoButton_8)
        self.gridLayout_20.addLayout(self.horizontalLayout, 1, 1, 2, 1)
        spacerItem24 = QtWidgets.QSpacerItem(24, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_20.addItem(spacerItem24, 2, 2, 1, 1)
        spacerItem25 = QtWidgets.QSpacerItem(20, 86, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_20.addItem(spacerItem25, 3, 1, 1, 1)
        self.tabWidget.addTab(self.tabWidgetPage3, "")
        self.tabWidgetPage4 = QtWidgets.QWidget()
        self.tabWidgetPage4.setObjectName("tabWidgetPage4")
        self.gridLayout_22 = QtWidgets.QGridLayout(self.tabWidgetPage4)
        self.gridLayout_22.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_22.setObjectName("gridLayout_22")
        spacerItem26 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_22.addItem(spacerItem26, 0, 1, 1, 1)
        spacerItem27 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_22.addItem(spacerItem27, 1, 0, 1, 1)
        self.verticalLayout_22 = QtWidgets.QVBoxLayout()
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout()
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.horizontalLayout_45 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_45.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_45.setObjectName("horizontalLayout_45")
        self.ai_label_1 = QtWidgets.QLabel(self.tabWidgetPage4)
        self.ai_label_1.setMinimumSize(QtCore.QSize(0, 27))
        self.ai_label_1.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ai_label_1.setFont(font)
        self.ai_label_1.setObjectName("ai_label_1")
        self.horizontalLayout_45.addWidget(self.ai_label_1)
        self.ai_aircraft_rl1 = QtWidgets.QComboBox(self.tabWidgetPage4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ai_aircraft_rl1.sizePolicy().hasHeightForWidth())
        self.ai_aircraft_rl1.setSizePolicy(sizePolicy)
        self.ai_aircraft_rl1.setMinimumSize(QtCore.QSize(220, 27))
        self.ai_aircraft_rl1.setMaximumSize(QtCore.QSize(220, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ai_aircraft_rl1.setFont(font)
        self.ai_aircraft_rl1.setStyleSheet("QComboBox {\n"
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
        self.ai_aircraft_rl1.setObjectName("ai_aircraft_rl1")
        self.ai_aircraft_rl1.addItem("")
        self.ai_aircraft_rl1.addItem("")
        self.ai_aircraft_rl1.addItem("")
        self.ai_aircraft_rl1.addItem("")
        self.ai_aircraft_rl1.addItem("")
        self.ai_aircraft_rl1.addItem("")
        self.ai_aircraft_rl1.addItem("")
        self.ai_aircraft_rl1.addItem("")
        self.ai_aircraft_rl1.addItem("")
        self.ai_aircraft_rl1.addItem("")
        self.ai_aircraft_rl1.addItem("")
        self.ai_aircraft_rl1.addItem("")
        self.ai_aircraft_rl1.addItem("")
        self.ai_aircraft_rl1.addItem("")
        self.ai_aircraft_rl1.addItem("")
        self.ai_aircraft_rl1.addItem("")
        self.ai_aircraft_rl1.addItem("")
        self.ai_aircraft_rl1.addItem("")
        self.ai_aircraft_rl1.addItem("")
        self.ai_aircraft_rl1.addItem("")
        self.ai_aircraft_rl1.addItem("")
        self.ai_aircraft_rl1.addItem("")
        self.horizontalLayout_45.addWidget(self.ai_aircraft_rl1)
        self.plusButton_10 = QtWidgets.QToolButton(self.tabWidgetPage4)
        self.plusButton_10.setMinimumSize(QtCore.QSize(27, 27))
        self.plusButton_10.setMaximumSize(QtCore.QSize(27, 27))
        self.plusButton_10.setStyleSheet("QToolButton {\n"
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
        self.plusButton_10.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/plus_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.plusButton_10.setIcon(icon2)
        self.plusButton_10.setIconSize(QtCore.QSize(27, 27))
        self.plusButton_10.setAutoRaise(False)
        self.plusButton_10.setObjectName("plusButton_10")
        self.horizontalLayout_45.addWidget(self.plusButton_10)
        spacerItem28 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_45.addItem(spacerItem28)
        self.infoButton_9 = QtWidgets.QToolButton(self.tabWidgetPage4)
        self.infoButton_9.setMinimumSize(QtCore.QSize(27, 27))
        self.infoButton_9.setMaximumSize(QtCore.QSize(27, 27))
        self.infoButton_9.setStyleSheet("QToolButton {\n"
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
        self.infoButton_9.setText("")
        self.infoButton_9.setIcon(icon1)
        self.infoButton_9.setIconSize(QtCore.QSize(27, 27))
        self.infoButton_9.setAutoRaise(False)
        self.infoButton_9.setObjectName("infoButton_9")
        self.horizontalLayout_45.addWidget(self.infoButton_9)
        spacerItem29 = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_45.addItem(spacerItem29)
        self.verticalLayout_17.addLayout(self.horizontalLayout_45)
        self.gridLayout_10 = QtWidgets.QGridLayout()
        self.gridLayout_10.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.gridLayout_10.setVerticalSpacing(17)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.ai_manufacturer_lb = QtWidgets.QLabel(self.tabWidgetPage4)
        self.ai_manufacturer_lb.setMinimumSize(QtCore.QSize(0, 0))
        self.ai_manufacturer_lb.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ai_manufacturer_lb.setFont(font)
        self.ai_manufacturer_lb.setIndent(5)
        self.ai_manufacturer_lb.setObjectName("ai_manufacturer_lb")
        self.gridLayout_10.addWidget(self.ai_manufacturer_lb, 0, 0, 1, 1)
        self.ai_label_7 = QtWidgets.QLabel(self.tabWidgetPage4)
        self.ai_label_7.setMinimumSize(QtCore.QSize(270, 35))
        self.ai_label_7.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ai_label_7.setFont(font)
        self.ai_label_7.setText("")
        self.ai_label_7.setWordWrap(True)
        self.ai_label_7.setIndent(10)
        self.ai_label_7.setObjectName("ai_label_7")
        self.gridLayout_10.addWidget(self.ai_label_7, 0, 1, 1, 1)
        self.ai_type_lb = QtWidgets.QLabel(self.tabWidgetPage4)
        self.ai_type_lb.setMinimumSize(QtCore.QSize(0, 0))
        self.ai_type_lb.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ai_type_lb.setFont(font)
        self.ai_type_lb.setIndent(5)
        self.ai_type_lb.setObjectName("ai_type_lb")
        self.gridLayout_10.addWidget(self.ai_type_lb, 1, 0, 1, 1)
        self.ai_label_8 = QtWidgets.QLabel(self.tabWidgetPage4)
        self.ai_label_8.setMinimumSize(QtCore.QSize(270, 35))
        self.ai_label_8.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ai_label_8.setFont(font)
        self.ai_label_8.setText("")
        self.ai_label_8.setWordWrap(True)
        self.ai_label_8.setIndent(10)
        self.ai_label_8.setObjectName("ai_label_8")
        self.gridLayout_10.addWidget(self.ai_label_8, 1, 1, 1, 1)
        self.ai_operator_lb = QtWidgets.QLabel(self.tabWidgetPage4)
        self.ai_operator_lb.setMinimumSize(QtCore.QSize(0, 0))
        self.ai_operator_lb.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ai_operator_lb.setFont(font)
        self.ai_operator_lb.setIndent(5)
        self.ai_operator_lb.setObjectName("ai_operator_lb")
        self.gridLayout_10.addWidget(self.ai_operator_lb, 2, 0, 1, 1)
        self.ai_label_9 = QtWidgets.QLabel(self.tabWidgetPage4)
        self.ai_label_9.setMinimumSize(QtCore.QSize(270, 45))
        self.ai_label_9.setMaximumSize(QtCore.QSize(16777215, 45))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ai_label_9.setFont(font)
        self.ai_label_9.setText("")
        self.ai_label_9.setWordWrap(True)
        self.ai_label_9.setIndent(10)
        self.ai_label_9.setObjectName("ai_label_9")
        self.gridLayout_10.addWidget(self.ai_label_9, 2, 1, 1, 1)
        self.ai_country_lb = QtWidgets.QLabel(self.tabWidgetPage4)
        self.ai_country_lb.setMinimumSize(QtCore.QSize(0, 0))
        self.ai_country_lb.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ai_country_lb.setFont(font)
        self.ai_country_lb.setIndent(5)
        self.ai_country_lb.setObjectName("ai_country_lb")
        self.gridLayout_10.addWidget(self.ai_country_lb, 3, 0, 1, 1)
        self.ai_label_10 = QtWidgets.QLabel(self.tabWidgetPage4)
        self.ai_label_10.setMinimumSize(QtCore.QSize(270, 35))
        self.ai_label_10.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ai_label_10.setFont(font)
        self.ai_label_10.setText("")
        self.ai_label_10.setWordWrap(True)
        self.ai_label_10.setIndent(10)
        self.ai_label_10.setObjectName("ai_label_10")
        self.gridLayout_10.addWidget(self.ai_label_10, 3, 1, 1, 1)
        self.ai_number_lb = QtWidgets.QLabel(self.tabWidgetPage4)
        self.ai_number_lb.setMinimumSize(QtCore.QSize(0, 0))
        self.ai_number_lb.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ai_number_lb.setFont(font)
        self.ai_number_lb.setWordWrap(True)
        self.ai_number_lb.setIndent(5)
        self.ai_number_lb.setObjectName("ai_number_lb")
        self.gridLayout_10.addWidget(self.ai_number_lb, 4, 0, 1, 1)
        self.ai_label_11 = QtWidgets.QLabel(self.tabWidgetPage4)
        self.ai_label_11.setMinimumSize(QtCore.QSize(270, 35))
        self.ai_label_11.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ai_label_11.setFont(font)
        self.ai_label_11.setText("")
        self.ai_label_11.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.ai_label_11.setWordWrap(True)
        self.ai_label_11.setIndent(10)
        self.ai_label_11.setObjectName("ai_label_11")
        self.gridLayout_10.addWidget(self.ai_label_11, 4, 1, 1, 1)
        self.verticalLayout_17.addLayout(self.gridLayout_10)
        self.horizontalLayout_6.addLayout(self.verticalLayout_17)
        self.verticalLayout_27 = QtWidgets.QVBoxLayout()
        self.verticalLayout_27.setObjectName("verticalLayout_27")
        self.ai_image_bx = QtWidgets.QLabel(self.tabWidgetPage4)
        self.ai_image_bx.setMinimumSize(QtCore.QSize(500, 271))
        self.ai_image_bx.setMaximumSize(QtCore.QSize(500, 271))
        self.ai_image_bx.setText("")
        self.ai_image_bx.setPixmap(QtGui.QPixmap("eufar_aircrafts/logo_eufar_emc.png"))
        self.ai_image_bx.setScaledContents(True)
        self.ai_image_bx.setAlignment(QtCore.Qt.AlignCenter)
        self.ai_image_bx.setObjectName("ai_image_bx")
        self.verticalLayout_27.addWidget(self.ai_image_bx)
        self.horizontalLayout_44 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_44.setObjectName("horizontalLayout_44")
        spacerItem30 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_44.addItem(spacerItem30)
        self.ai_label_21 = QtWidgets.QLabel(self.tabWidgetPage4)
        self.ai_label_21.setMinimumSize(QtCore.QSize(17, 17))
        self.ai_label_21.setMaximumSize(QtCore.QSize(17, 17))
        self.ai_label_21.setText("")
        self.ai_label_21.setPixmap(QtGui.QPixmap("icons/none_icon.png"))
        self.ai_label_21.setScaledContents(True)
        self.ai_label_21.setObjectName("ai_label_21")
        self.horizontalLayout_44.addWidget(self.ai_label_21)
        self.ai_label_12 = QtWidgets.QLabel(self.tabWidgetPage4)
        self.ai_label_12.setMinimumSize(QtCore.QSize(370, 15))
        self.ai_label_12.setMaximumSize(QtCore.QSize(370, 15))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ai_label_12.setFont(font)
        self.ai_label_12.setText("")
        self.ai_label_12.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.ai_label_12.setObjectName("ai_label_12")
        self.horizontalLayout_44.addWidget(self.ai_label_12)
        self.verticalLayout_27.addLayout(self.horizontalLayout_44)
        self.horizontalLayout_6.addLayout(self.verticalLayout_27)
        self.verticalLayout_22.addLayout(self.horizontalLayout_6)
        self.verticalLayout_21 = QtWidgets.QVBoxLayout()
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.verticalLayout_22.addLayout(self.verticalLayout_21)
        self.ai_line_1 = QtWidgets.QFrame(self.tabWidgetPage4)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(157, 157, 157))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(236, 236, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(196, 196, 196))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(78, 78, 78))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(105, 105, 105))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(157, 157, 157))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(206, 206, 206))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(157, 157, 157))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(236, 236, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(196, 196, 196))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(78, 78, 78))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(105, 105, 105))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(157, 157, 157))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(206, 206, 206))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(78, 78, 78))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(157, 157, 157))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(236, 236, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(196, 196, 196))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(78, 78, 78))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(105, 105, 105))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(78, 78, 78))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(78, 78, 78))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(157, 157, 157))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(157, 157, 157))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(157, 157, 157))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.ai_line_1.setPalette(palette)
        self.ai_line_1.setFrameShape(QtWidgets.QFrame.HLine)
        self.ai_line_1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.ai_line_1.setObjectName("ai_line_1")
        self.verticalLayout_22.addWidget(self.ai_line_1)
        self.verticalLayout_36 = QtWidgets.QVBoxLayout()
        self.verticalLayout_36.setObjectName("verticalLayout_36")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.ai_label_13 = QtWidgets.QLabel(self.tabWidgetPage4)
        self.ai_label_13.setMinimumSize(QtCore.QSize(0, 27))
        self.ai_label_13.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ai_label_13.setFont(font)
        self.ai_label_13.setObjectName("ai_label_13")
        self.horizontalLayout_3.addWidget(self.ai_label_13)
        self.ai_instrument_rl1 = QtWidgets.QComboBox(self.tabWidgetPage4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ai_instrument_rl1.sizePolicy().hasHeightForWidth())
        self.ai_instrument_rl1.setSizePolicy(sizePolicy)
        self.ai_instrument_rl1.setMinimumSize(QtCore.QSize(320, 27))
        self.ai_instrument_rl1.setMaximumSize(QtCore.QSize(320, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ai_instrument_rl1.setFont(font)
        self.ai_instrument_rl1.setStyleSheet("QComboBox {\n"
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
        self.ai_instrument_rl1.setFrame(False)
        self.ai_instrument_rl1.setObjectName("ai_instrument_rl1")
        self.horizontalLayout_3.addWidget(self.ai_instrument_rl1)
        self.plusButton_4 = QtWidgets.QToolButton(self.tabWidgetPage4)
        self.plusButton_4.setMinimumSize(QtCore.QSize(27, 27))
        self.plusButton_4.setMaximumSize(QtCore.QSize(27, 27))
        self.plusButton_4.setStyleSheet("QToolButton {\n"
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
        self.plusButton_4.setText("")
        self.plusButton_4.setIcon(icon2)
        self.plusButton_4.setIconSize(QtCore.QSize(27, 27))
        self.plusButton_4.setAutoRaise(False)
        self.plusButton_4.setObjectName("plusButton_4")
        self.horizontalLayout_3.addWidget(self.plusButton_4)
        spacerItem31 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem31)
        self.infoButton_10 = QtWidgets.QToolButton(self.tabWidgetPage4)
        self.infoButton_10.setMinimumSize(QtCore.QSize(27, 27))
        self.infoButton_10.setMaximumSize(QtCore.QSize(27, 27))
        self.infoButton_10.setStyleSheet("QToolButton {\n"
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
        self.infoButton_10.setText("")
        self.infoButton_10.setIcon(icon1)
        self.infoButton_10.setIconSize(QtCore.QSize(27, 27))
        self.infoButton_10.setAutoRaise(False)
        self.infoButton_10.setObjectName("infoButton_10")
        self.horizontalLayout_3.addWidget(self.infoButton_10)
        spacerItem32 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem32)
        self.verticalLayout_36.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_58 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_58.setObjectName("horizontalLayout_58")
        self.verticalLayout_36.addLayout(self.horizontalLayout_58)
        self.verticalLayout_31 = QtWidgets.QVBoxLayout()
        self.verticalLayout_31.setObjectName("verticalLayout_31")
        self.verticalLayout_36.addLayout(self.verticalLayout_31)
        self.verticalLayout_22.addLayout(self.verticalLayout_36)
        self.gridLayout_22.addLayout(self.verticalLayout_22, 1, 1, 2, 2)
        spacerItem33 = QtWidgets.QSpacerItem(121, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_22.addItem(spacerItem33, 2, 3, 1, 1)
        spacerItem34 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_22.addItem(spacerItem34, 3, 2, 1, 1)
        self.delButton_9 = QtWidgets.QToolButton(self.tabWidgetPage4)
        self.delButton_9.setEnabled(False)
        self.delButton_9.setGeometry(QtCore.QRect(925, 397, 27, 27))
        self.delButton_9.setMinimumSize(QtCore.QSize(27, 27))
        self.delButton_9.setMaximumSize(QtCore.QSize(27, 27))
        self.delButton_9.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/none_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.delButton_9.setIcon(icon3)
        self.delButton_9.setIconSize(QtCore.QSize(27, 27))
        self.delButton_9.setAutoRaise(True)
        self.delButton_9.setObjectName("delButton_9")
        self.tabWidget.addTab(self.tabWidgetPage4, "")
        self.tabWidgetPage5 = QtWidgets.QWidget()
        self.tabWidgetPage5.setObjectName("tabWidgetPage5")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.tabWidgetPage5)
        self.gridLayout_11.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_11.setObjectName("gridLayout_11")
        spacerItem35 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_11.addItem(spacerItem35, 0, 1, 1, 1)
        self.verticalLayout_24 = QtWidgets.QVBoxLayout()
        self.verticalLayout_24.setObjectName("verticalLayout_24")
        self.horizontalLayout_40 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_40.setObjectName("horizontalLayout_40")
        self.gl_location_lb = QtWidgets.QLabel(self.tabWidgetPage5)
        self.gl_location_lb.setMinimumSize(QtCore.QSize(0, 27))
        self.gl_location_lb.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.gl_location_lb.setFont(font)
        self.gl_location_lb.setWordWrap(True)
        self.gl_location_lb.setObjectName("gl_location_lb")
        self.horizontalLayout_40.addWidget(self.gl_location_lb)
        spacerItem36 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_40.addItem(spacerItem36)
        self.gl_category_rl1 = QtWidgets.QComboBox(self.tabWidgetPage5)
        self.gl_category_rl1.setMinimumSize(QtCore.QSize(160, 27))
        self.gl_category_rl1.setMaximumSize(QtCore.QSize(160, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.gl_category_rl1.setFont(font)
        self.gl_category_rl1.setStyleSheet("QComboBox {\n"
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
        self.gl_category_rl1.setObjectName("gl_category_rl1")
        self.gl_category_rl1.addItem("")
        self.gl_category_rl1.addItem("")
        self.gl_category_rl1.addItem("")
        self.gl_category_rl1.addItem("")
        self.gl_category_rl1.addItem("")
        self.horizontalLayout_40.addWidget(self.gl_category_rl1)
        self.kw_label_5 = QtWidgets.QLabel(self.tabWidgetPage5)
        self.kw_label_5.setMinimumSize(QtCore.QSize(15, 8))
        self.kw_label_5.setMaximumSize(QtCore.QSize(15, 8))
        self.kw_label_5.setLineWidth(0)
        self.kw_label_5.setText("")
        self.kw_label_5.setPixmap(QtGui.QPixmap("icons/fwd_arrow.png"))
        self.kw_label_5.setScaledContents(True)
        self.kw_label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.kw_label_5.setObjectName("kw_label_5")
        self.horizontalLayout_40.addWidget(self.kw_label_5)
        self.horizontalLayout_60 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_60.setObjectName("horizontalLayout_60")
        self.gl_details_rl2 = QtWidgets.QComboBox(self.tabWidgetPage5)
        self.gl_details_rl2.setEnabled(False)
        self.gl_details_rl2.setMinimumSize(QtCore.QSize(140, 27))
        self.gl_details_rl2.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.gl_details_rl2.setFont(font)
        self.gl_details_rl2.setStyleSheet("QComboBox {\n"
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
        self.gl_details_rl2.setMaxVisibleItems(20)
        self.gl_details_rl2.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToMinimumContentsLength)
        self.gl_details_rl2.setMinimumContentsLength(20)
        self.gl_details_rl2.setFrame(False)
        self.gl_details_rl2.setModelColumn(0)
        self.gl_details_rl2.setObjectName("gl_details_rl2")
        self.horizontalLayout_60.addWidget(self.gl_details_rl2)
        self.horizontalLayout_40.addLayout(self.horizontalLayout_60)
        self.infoButton_11 = QtWidgets.QToolButton(self.tabWidgetPage5)
        self.infoButton_11.setMaximumSize(QtCore.QSize(27, 27))
        self.infoButton_11.setStyleSheet("QToolButton {\n"
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
        self.infoButton_11.setText("")
        self.infoButton_11.setIcon(icon1)
        self.infoButton_11.setIconSize(QtCore.QSize(27, 27))
        self.infoButton_11.setAutoRaise(False)
        self.infoButton_11.setObjectName("infoButton_11")
        self.horizontalLayout_40.addWidget(self.infoButton_11)
        spacerItem37 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_40.addItem(spacerItem37)
        self.verticalLayout_24.addLayout(self.horizontalLayout_40)
        spacerItem38 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_24.addItem(spacerItem38)
        self.horizontalLayout_24 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        self.gl_label_1 = QtWidgets.QLabel(self.tabWidgetPage5)
        self.gl_label_1.setMinimumSize(QtCore.QSize(210, 27))
        self.gl_label_1.setMaximumSize(QtCore.QSize(16777215, 54))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.gl_label_1.setFont(font)
        self.gl_label_1.setWordWrap(True)
        self.gl_label_1.setObjectName("gl_label_1")
        self.horizontalLayout_24.addWidget(self.gl_label_1)
        self.gridLayout_8 = QtWidgets.QGridLayout()
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem39 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem39)
        self.gl_northBound_ln = QtWidgets.QLineEdit(self.tabWidgetPage5)
        self.gl_northBound_ln.setMinimumSize(QtCore.QSize(60, 27))
        self.gl_northBound_ln.setMaximumSize(QtCore.QSize(60, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.gl_northBound_ln.setFont(font)
        self.gl_northBound_ln.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.gl_northBound_ln.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"   padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"}")
        self.gl_northBound_ln.setFrame(False)
        self.gl_northBound_ln.setAlignment(QtCore.Qt.AlignCenter)
        self.gl_northBound_ln.setObjectName("gl_northBound_ln")
        self.horizontalLayout_2.addWidget(self.gl_northBound_ln)
        spacerItem40 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem40)
        self.gridLayout_8.addLayout(self.horizontalLayout_2, 0, 1, 1, 1)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        spacerItem41 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem41)
        self.gl_westBound_ln = QtWidgets.QLineEdit(self.tabWidgetPage5)
        self.gl_westBound_ln.setMinimumSize(QtCore.QSize(60, 27))
        self.gl_westBound_ln.setMaximumSize(QtCore.QSize(60, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.gl_westBound_ln.setFont(font)
        self.gl_westBound_ln.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"   padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"}")
        self.gl_westBound_ln.setFrame(False)
        self.gl_westBound_ln.setAlignment(QtCore.Qt.AlignCenter)
        self.gl_westBound_ln.setObjectName("gl_westBound_ln")
        self.verticalLayout_7.addWidget(self.gl_westBound_ln)
        spacerItem42 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem42)
        self.gridLayout_8.addLayout(self.verticalLayout_7, 1, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.tabWidgetPage5)
        self.label_6.setMinimumSize(QtCore.QSize(250, 250))
        self.label_6.setMaximumSize(QtCore.QSize(250, 250))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("icons/EMC_globe_terrestre.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout_8.addWidget(self.label_6, 1, 1, 1, 1)
        self.verticalLayout_28 = QtWidgets.QVBoxLayout()
        self.verticalLayout_28.setObjectName("verticalLayout_28")
        spacerItem43 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_28.addItem(spacerItem43)
        self.gl_eastBound_ln = QtWidgets.QLineEdit(self.tabWidgetPage5)
        self.gl_eastBound_ln.setMinimumSize(QtCore.QSize(60, 27))
        self.gl_eastBound_ln.setMaximumSize(QtCore.QSize(60, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.gl_eastBound_ln.setFont(font)
        self.gl_eastBound_ln.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"   padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"}")
        self.gl_eastBound_ln.setFrame(False)
        self.gl_eastBound_ln.setAlignment(QtCore.Qt.AlignCenter)
        self.gl_eastBound_ln.setObjectName("gl_eastBound_ln")
        self.verticalLayout_28.addWidget(self.gl_eastBound_ln)
        spacerItem44 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_28.addItem(spacerItem44)
        self.gridLayout_8.addLayout(self.verticalLayout_28, 1, 2, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem45 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem45)
        self.gl_southBound_ln = QtWidgets.QLineEdit(self.tabWidgetPage5)
        self.gl_southBound_ln.setMinimumSize(QtCore.QSize(60, 27))
        self.gl_southBound_ln.setMaximumSize(QtCore.QSize(60, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.gl_southBound_ln.setFont(font)
        self.gl_southBound_ln.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"   padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"}")
        self.gl_southBound_ln.setFrame(False)
        self.gl_southBound_ln.setAlignment(QtCore.Qt.AlignCenter)
        self.gl_southBound_ln.setObjectName("gl_southBound_ln")
        self.horizontalLayout_5.addWidget(self.gl_southBound_ln)
        spacerItem46 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem46)
        self.gridLayout_8.addLayout(self.horizontalLayout_5, 2, 1, 1, 1)
        self.horizontalLayout_24.addLayout(self.gridLayout_8)
        self.infoButton_12 = QtWidgets.QToolButton(self.tabWidgetPage5)
        self.infoButton_12.setMaximumSize(QtCore.QSize(27, 27))
        self.infoButton_12.setStyleSheet("QToolButton {\n"
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
        self.infoButton_12.setText("")
        self.infoButton_12.setIcon(icon1)
        self.infoButton_12.setIconSize(QtCore.QSize(27, 27))
        self.infoButton_12.setAutoRaise(False)
        self.infoButton_12.setObjectName("infoButton_12")
        self.horizontalLayout_24.addWidget(self.infoButton_12)
        spacerItem47 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_24.addItem(spacerItem47)
        self.verticalLayout_24.addLayout(self.horizontalLayout_24)
        spacerItem48 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_24.addItem(spacerItem48)
        self.horizontalLayout_41 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_41.setObjectName("horizontalLayout_41")
        self.gl_resolution_lb = QtWidgets.QLabel(self.tabWidgetPage5)
        self.gl_resolution_lb.setMinimumSize(QtCore.QSize(140, 27))
        self.gl_resolution_lb.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.gl_resolution_lb.setFont(font)
        self.gl_resolution_lb.setObjectName("gl_resolution_lb")
        self.horizontalLayout_41.addWidget(self.gl_resolution_lb)
        spacerItem49 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_41.addItem(spacerItem49)
        self.gl_resolution_rl1 = QtWidgets.QComboBox(self.tabWidgetPage5)
        self.gl_resolution_rl1.setMinimumSize(QtCore.QSize(110, 27))
        self.gl_resolution_rl1.setMaximumSize(QtCore.QSize(110, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.gl_resolution_rl1.setFont(font)
        self.gl_resolution_rl1.setStyleSheet("QComboBox {\n"
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
        self.gl_resolution_rl1.setFrame(False)
        self.gl_resolution_rl1.setObjectName("gl_resolution_rl1")
        self.gl_resolution_rl1.addItem("")
        self.gl_resolution_rl1.addItem("")
        self.horizontalLayout_41.addWidget(self.gl_resolution_rl1)
        spacerItem50 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_41.addItem(spacerItem50)
        self.horizontalLayout_27 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_27.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_27.setObjectName("horizontalLayout_27")
        self.gl_resolution_ln = QtWidgets.QLineEdit(self.tabWidgetPage5)
        self.gl_resolution_ln.setMinimumSize(QtCore.QSize(200, 27))
        self.gl_resolution_ln.setMaximumSize(QtCore.QSize(27, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.gl_resolution_ln.setFont(font)
        self.gl_resolution_ln.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"   padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"}")
        self.gl_resolution_ln.setFrame(False)
        self.gl_resolution_ln.setObjectName("gl_resolution_ln")
        self.horizontalLayout_27.addWidget(self.gl_resolution_ln)
        self.horizontalLayout_41.addLayout(self.horizontalLayout_27)
        self.infoButton_13 = QtWidgets.QToolButton(self.tabWidgetPage5)
        self.infoButton_13.setMaximumSize(QtCore.QSize(27, 27))
        self.infoButton_13.setStyleSheet("QToolButton {\n"
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
        self.infoButton_13.setText("")
        self.infoButton_13.setIcon(icon1)
        self.infoButton_13.setIconSize(QtCore.QSize(27, 27))
        self.infoButton_13.setPopupMode(QtWidgets.QToolButton.InstantPopup)
        self.infoButton_13.setAutoRaise(False)
        self.infoButton_13.setObjectName("infoButton_13")
        self.horizontalLayout_41.addWidget(self.infoButton_13)
        spacerItem51 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_41.addItem(spacerItem51)
        self.verticalLayout_24.addLayout(self.horizontalLayout_41)
        self.gridLayout_11.addLayout(self.verticalLayout_24, 1, 1, 2, 1)
        spacerItem52 = QtWidgets.QSpacerItem(179, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_11.addItem(spacerItem52, 1, 2, 1, 1)
        spacerItem53 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_11.addItem(spacerItem53, 2, 0, 1, 1)
        spacerItem54 = QtWidgets.QSpacerItem(20, 32, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_11.addItem(spacerItem54, 3, 1, 1, 1)
        self.tabWidget.addTab(self.tabWidgetPage5, "")
        self.tabWidgetPage6 = QtWidgets.QWidget()
        self.tabWidgetPage6.setObjectName("tabWidgetPage6")
        self.gridLayout_21 = QtWidgets.QGridLayout(self.tabWidgetPage6)
        self.gridLayout_21.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_21.setObjectName("gridLayout_21")
        spacerItem55 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_21.addItem(spacerItem55, 0, 1, 1, 1)
        spacerItem56 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_21.addItem(spacerItem56, 1, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setVerticalSpacing(29)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tr_dateRevision_do2 = QtWidgets.QDateEdit(self.tabWidgetPage6)
        self.tr_dateRevision_do2.setMinimumSize(QtCore.QSize(130, 27))
        self.tr_dateRevision_do2.setMaximumSize(QtCore.QSize(130, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.tr_dateRevision_do2.setFont(font)
        self.tr_dateRevision_do2.setStyleSheet("QDateEdit {\n"
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
        self.tr_dateRevision_do2.setFrame(False)
        self.tr_dateRevision_do2.setAlignment(QtCore.Qt.AlignCenter)
        self.tr_dateRevision_do2.setAccelerated(True)
        self.tr_dateRevision_do2.setCurrentSection(QtWidgets.QDateTimeEdit.YearSection)
        self.tr_dateRevision_do2.setCalendarPopup(True)
        self.tr_dateRevision_do2.setTimeSpec(QtCore.Qt.UTC)
        self.tr_dateRevision_do2.setDate(QtCore.QDate(2014, 10, 7))
        self.tr_dateRevision_do2.setObjectName("tr_dateRevision_do2")
        self.gridLayout_3.addWidget(self.tr_dateRevision_do2, 0, 1, 1, 1)
        self.infoButton_15 = QtWidgets.QToolButton(self.tabWidgetPage6)
        self.infoButton_15.setMaximumSize(QtCore.QSize(27, 27))
        self.infoButton_15.setStyleSheet("QToolButton {\n"
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
        self.infoButton_15.setText("")
        self.infoButton_15.setIcon(icon1)
        self.infoButton_15.setIconSize(QtCore.QSize(27, 27))
        self.infoButton_15.setAutoRaise(False)
        self.infoButton_15.setObjectName("infoButton_15")
        self.gridLayout_3.addWidget(self.infoButton_15, 0, 2, 1, 1)
        self.tr_dateRevision_lb = QtWidgets.QLabel(self.tabWidgetPage6)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.tr_dateRevision_lb.setFont(font)
        self.tr_dateRevision_lb.setObjectName("tr_dateRevision_lb")
        self.gridLayout_3.addWidget(self.tr_dateRevision_lb, 0, 0, 1, 1)
        self.infoButton_16 = QtWidgets.QToolButton(self.tabWidgetPage6)
        self.infoButton_16.setMaximumSize(QtCore.QSize(27, 27))
        self.infoButton_16.setStyleSheet("QToolButton {\n"
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
        self.infoButton_16.setText("")
        self.infoButton_16.setIcon(icon1)
        self.infoButton_16.setIconSize(QtCore.QSize(27, 27))
        self.infoButton_16.setAutoRaise(False)
        self.infoButton_16.setObjectName("infoButton_16")
        self.gridLayout_3.addWidget(self.infoButton_16, 1, 2, 1, 1)
        self.tr_dateCreation_do3 = QtWidgets.QDateEdit(self.tabWidgetPage6)
        self.tr_dateCreation_do3.setMinimumSize(QtCore.QSize(130, 27))
        self.tr_dateCreation_do3.setMaximumSize(QtCore.QSize(130, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.tr_dateCreation_do3.setFont(font)
        self.tr_dateCreation_do3.setStyleSheet("QDateEdit {\n"
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
        self.tr_dateCreation_do3.setFrame(False)
        self.tr_dateCreation_do3.setAlignment(QtCore.Qt.AlignCenter)
        self.tr_dateCreation_do3.setAccelerated(True)
        self.tr_dateCreation_do3.setCurrentSection(QtWidgets.QDateTimeEdit.YearSection)
        self.tr_dateCreation_do3.setCalendarPopup(True)
        self.tr_dateCreation_do3.setDate(QtCore.QDate(2014, 10, 28))
        self.tr_dateCreation_do3.setObjectName("tr_dateCreation_do3")
        self.gridLayout_3.addWidget(self.tr_dateCreation_do3, 1, 1, 1, 1)
        self.tr_dateCreation_lb = QtWidgets.QLabel(self.tabWidgetPage6)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.tr_dateCreation_lb.setFont(font)
        self.tr_dateCreation_lb.setObjectName("tr_dateCreation_lb")
        self.gridLayout_3.addWidget(self.tr_dateCreation_lb, 1, 0, 1, 1)
        self.horizontalLayout_4.addLayout(self.gridLayout_3)
        spacerItem57 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem57)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        spacerItem58 = QtWidgets.QSpacerItem(17, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem58)
        self.line_2 = QtWidgets.QFrame(self.tabWidgetPage6)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(157, 157, 157))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(236, 236, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(196, 196, 196))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(78, 78, 78))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(105, 105, 105))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(157, 157, 157))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(206, 206, 206))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(157, 157, 157))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(236, 236, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(196, 196, 196))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(78, 78, 78))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(105, 105, 105))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(157, 157, 157))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(206, 206, 206))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(78, 78, 78))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(157, 157, 157))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(236, 236, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(196, 196, 196))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(78, 78, 78))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(105, 105, 105))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(78, 78, 78))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(78, 78, 78))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(157, 157, 157))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(157, 157, 157))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(157, 157, 157))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.line_2.setPalette(palette)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        spacerItem59 = QtWidgets.QSpacerItem(17, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem59)
        self.horizontalLayout_67 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_67.setObjectName("horizontalLayout_67")
        self.verticalLayout_29 = QtWidgets.QVBoxLayout()
        self.verticalLayout_29.setObjectName("verticalLayout_29")
        spacerItem60 = QtWidgets.QSpacerItem(20, 1, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_29.addItem(spacerItem60)
        self.horizontalLayout_55 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_55.setObjectName("horizontalLayout_55")
        self.tr_period_lb = QtWidgets.QLabel(self.tabWidgetPage6)
        self.tr_period_lb.setMinimumSize(QtCore.QSize(130, 27))
        self.tr_period_lb.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.tr_period_lb.setFont(font)
        self.tr_period_lb.setObjectName("tr_period_lb")
        self.horizontalLayout_55.addWidget(self.tr_period_lb)
        spacerItem61 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_55.addItem(spacerItem61)
        self.verticalLayout_29.addLayout(self.horizontalLayout_55)
        spacerItem62 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_29.addItem(spacerItem62)
        self.horizontalLayout_67.addLayout(self.verticalLayout_29)
        self.verticalLayout_16 = QtWidgets.QVBoxLayout()
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.horizontalLayout_32 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_32.setObjectName("horizontalLayout_32")
        self.label_7 = QtWidgets.QLabel(self.tabWidgetPage6)
        self.label_7.setMinimumSize(QtCore.QSize(60, 30))
        self.label_7.setMaximumSize(QtCore.QSize(60, 30))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_32.addWidget(self.label_7)
        spacerItem63 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_32.addItem(spacerItem63)
        self.tr_dateStart_do4 = QtWidgets.QDateEdit(self.tabWidgetPage6)
        self.tr_dateStart_do4.setMinimumSize(QtCore.QSize(130, 27))
        self.tr_dateStart_do4.setMaximumSize(QtCore.QSize(130, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.tr_dateStart_do4.setFont(font)
        self.tr_dateStart_do4.setStyleSheet("QDateEdit {\n"
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
        self.tr_dateStart_do4.setFrame(False)
        self.tr_dateStart_do4.setAlignment(QtCore.Qt.AlignCenter)
        self.tr_dateStart_do4.setAccelerated(True)
        self.tr_dateStart_do4.setCurrentSection(QtWidgets.QDateTimeEdit.YearSection)
        self.tr_dateStart_do4.setCalendarPopup(True)
        self.tr_dateStart_do4.setDate(QtCore.QDate(2014, 10, 28))
        self.tr_dateStart_do4.setObjectName("tr_dateStart_do4")
        self.horizontalLayout_32.addWidget(self.tr_dateStart_do4)
        spacerItem64 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_32.addItem(spacerItem64)
        self.tr_dateEnd_do5 = QtWidgets.QDateEdit(self.tabWidgetPage6)
        self.tr_dateEnd_do5.setMinimumSize(QtCore.QSize(130, 27))
        self.tr_dateEnd_do5.setMaximumSize(QtCore.QSize(130, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.tr_dateEnd_do5.setFont(font)
        self.tr_dateEnd_do5.setStyleSheet("QDateEdit {\n"
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
        self.tr_dateEnd_do5.setFrame(False)
        self.tr_dateEnd_do5.setAlignment(QtCore.Qt.AlignCenter)
        self.tr_dateEnd_do5.setAccelerated(True)
        self.tr_dateEnd_do5.setCalendarPopup(True)
        self.tr_dateEnd_do5.setDate(QtCore.QDate(2014, 10, 28))
        self.tr_dateEnd_do5.setObjectName("tr_dateEnd_do5")
        self.horizontalLayout_32.addWidget(self.tr_dateEnd_do5)
        spacerItem65 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_32.addItem(spacerItem65)
        self.delButton_10 = QtWidgets.QToolButton(self.tabWidgetPage6)
        self.delButton_10.setEnabled(False)
        self.delButton_10.setMinimumSize(QtCore.QSize(27, 27))
        self.delButton_10.setMaximumSize(QtCore.QSize(27, 27))
        self.delButton_10.setStyleSheet("QToolButton {\n"
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
        self.delButton_10.setText("")
        self.delButton_10.setIcon(icon3)
        self.delButton_10.setIconSize(QtCore.QSize(27, 27))
        self.delButton_10.setAutoRaise(False)
        self.delButton_10.setObjectName("delButton_10")
        self.horizontalLayout_32.addWidget(self.delButton_10)
        self.verticalLayout_16.addLayout(self.horizontalLayout_32)
        self.verticalLayout_15 = QtWidgets.QVBoxLayout()
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.verticalLayout_16.addLayout(self.verticalLayout_15)
        spacerItem66 = QtWidgets.QSpacerItem(20, 17, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_16.addItem(spacerItem66)
        self.horizontalLayout_67.addLayout(self.verticalLayout_16)
        self.verticalLayout_40 = QtWidgets.QVBoxLayout()
        self.verticalLayout_40.setObjectName("verticalLayout_40")
        spacerItem67 = QtWidgets.QSpacerItem(20, 1, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_40.addItem(spacerItem67)
        self.horizontalLayout_66 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_66.setObjectName("horizontalLayout_66")
        spacerItem68 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_66.addItem(spacerItem68)
        self.plusButton_3 = QtWidgets.QToolButton(self.tabWidgetPage6)
        self.plusButton_3.setMinimumSize(QtCore.QSize(27, 27))
        self.plusButton_3.setMaximumSize(QtCore.QSize(27, 27))
        self.plusButton_3.setStyleSheet("QToolButton {\n"
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
        self.plusButton_3.setText("")
        self.plusButton_3.setIcon(icon2)
        self.plusButton_3.setIconSize(QtCore.QSize(27, 27))
        self.plusButton_3.setAutoRaise(False)
        self.plusButton_3.setObjectName("plusButton_3")
        self.horizontalLayout_66.addWidget(self.plusButton_3)
        spacerItem69 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_66.addItem(spacerItem69)
        self.infoButton_17 = QtWidgets.QToolButton(self.tabWidgetPage6)
        self.infoButton_17.setMaximumSize(QtCore.QSize(27, 27))
        self.infoButton_17.setStyleSheet("QToolButton {\n"
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
        self.infoButton_17.setText("")
        self.infoButton_17.setIcon(icon1)
        self.infoButton_17.setIconSize(QtCore.QSize(27, 27))
        self.infoButton_17.setAutoRaise(False)
        self.infoButton_17.setObjectName("infoButton_17")
        self.horizontalLayout_66.addWidget(self.infoButton_17)
        self.verticalLayout_40.addLayout(self.horizontalLayout_66)
        spacerItem70 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_40.addItem(spacerItem70)
        self.horizontalLayout_67.addLayout(self.verticalLayout_40)
        self.verticalLayout.addLayout(self.horizontalLayout_67)
        self.gridLayout_21.addLayout(self.verticalLayout, 1, 1, 1, 2)
        spacerItem71 = QtWidgets.QSpacerItem(102, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_21.addItem(spacerItem71, 1, 3, 1, 1)
        spacerItem72 = QtWidgets.QSpacerItem(20, 238, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_21.addItem(spacerItem72, 2, 2, 1, 1)
        self.tabWidget.addTab(self.tabWidgetPage6, "")
        self.tabWidgetPage7 = QtWidgets.QWidget()
        self.tabWidgetPage7.setObjectName("tabWidgetPage7")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.tabWidgetPage7)
        self.gridLayout_12.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_12.setObjectName("gridLayout_12")
        spacerItem73 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_12.addItem(spacerItem73, 1, 0, 1, 1)
        spacerItem74 = QtWidgets.QSpacerItem(236, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_12.addItem(spacerItem74, 1, 2, 1, 1)
        spacerItem75 = QtWidgets.QSpacerItem(20, 447, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_12.addItem(spacerItem75, 2, 1, 1, 1)
        self.verticalLayout_35 = QtWidgets.QVBoxLayout()
        self.verticalLayout_35.setObjectName("verticalLayout_35")
        self.horizontalLayout_56 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_56.setObjectName("horizontalLayout_56")
        spacerItem76 = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_56.addItem(spacerItem76)
        self.qv_obsRadio = QtWidgets.QRadioButton(self.tabWidgetPage7)
        self.qv_obsRadio.setMinimumSize(QtCore.QSize(20, 27))
        self.qv_obsRadio.setMaximumSize(QtCore.QSize(20, 27))
        font = QtGui.QFont()
        font.setFamily("Droid Sans Fallback")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.qv_obsRadio.setFont(font)
        self.qv_obsRadio.setStyleSheet("")
        self.qv_obsRadio.setText("")
        self.qv_obsRadio.setObjectName("qv_obsRadio")
        self.buttonGroup = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.qv_obsRadio)
        self.horizontalLayout_56.addWidget(self.qv_obsRadio)
        self.qv_obsLab = QtWidgets.QLabel(self.tabWidgetPage7)
        self.qv_obsLab.setMinimumSize(QtCore.QSize(350, 27))
        self.qv_obsLab.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.qv_obsLab.setFont(font)
        self.qv_obsLab.setObjectName("qv_obsLab")
        self.horizontalLayout_56.addWidget(self.qv_obsLab)
        spacerItem77 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_56.addItem(spacerItem77)
        self.qv_insituRadio = QtWidgets.QRadioButton(self.tabWidgetPage7)
        self.qv_insituRadio.setMinimumSize(QtCore.QSize(20, 27))
        self.qv_insituRadio.setMaximumSize(QtCore.QSize(20, 27))
        font = QtGui.QFont()
        font.setFamily("Droid Sans Fallback")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.qv_insituRadio.setFont(font)
        self.qv_insituRadio.setStyleSheet("")
        self.qv_insituRadio.setText("")
        self.qv_insituRadio.setObjectName("qv_insituRadio")
        self.buttonGroup.addButton(self.qv_insituRadio)
        self.horizontalLayout_56.addWidget(self.qv_insituRadio)
        self.qv_insituLab = QtWidgets.QLabel(self.tabWidgetPage7)
        self.qv_insituLab.setMinimumSize(QtCore.QSize(250, 27))
        self.qv_insituLab.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.qv_insituLab.setFont(font)
        self.qv_insituLab.setObjectName("qv_insituLab")
        self.horizontalLayout_56.addWidget(self.qv_insituLab)
        spacerItem78 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_56.addItem(spacerItem78)
        self.infoButton_26 = QtWidgets.QToolButton(self.tabWidgetPage7)
        self.infoButton_26.setMaximumSize(QtCore.QSize(27, 27))
        self.infoButton_26.setStyleSheet("QToolButton {\n"
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
        self.infoButton_26.setText("")
        self.infoButton_26.setIcon(icon1)
        self.infoButton_26.setIconSize(QtCore.QSize(27, 27))
        self.infoButton_26.setAutoRaise(False)
        self.infoButton_26.setObjectName("infoButton_26")
        self.horizontalLayout_56.addWidget(self.infoButton_26)
        spacerItem79 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_56.addItem(spacerItem79)
        self.verticalLayout_35.addLayout(self.horizontalLayout_56)
        self.verticalLayout_25 = QtWidgets.QVBoxLayout()
        self.verticalLayout_25.setObjectName("verticalLayout_25")
        self.verticalLayout_35.addLayout(self.verticalLayout_25)
        self.gridLayout_12.addLayout(self.verticalLayout_35, 1, 1, 1, 1)
        spacerItem80 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_12.addItem(spacerItem80, 0, 1, 1, 1)
        self.tabWidget.addTab(self.tabWidgetPage7, "")
        self.tabWidgetPage8 = QtWidgets.QWidget()
        self.tabWidgetPage8.setObjectName("tabWidgetPage8")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.tabWidgetPage8)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        spacerItem81 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_6.addItem(spacerItem81, 0, 2, 1, 1)
        spacerItem82 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem82, 1, 0, 1, 1)
        self.verticalLayout_52 = QtWidgets.QVBoxLayout()
        self.verticalLayout_52.setObjectName("verticalLayout_52")
        self.horizontalLayout_82 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_82.setObjectName("horizontalLayout_82")
        self.verticalLayout_50 = QtWidgets.QVBoxLayout()
        self.verticalLayout_50.setObjectName("verticalLayout_50")
        spacerItem83 = QtWidgets.QSpacerItem(20, 25, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_50.addItem(spacerItem83)
        self.horizontalLayout_80 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_80.setObjectName("horizontalLayout_80")
        self.au_conditions_lb = QtWidgets.QLabel(self.tabWidgetPage8)
        self.au_conditions_lb.setMinimumSize(QtCore.QSize(160, 40))
        self.au_conditions_lb.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.au_conditions_lb.setFont(font)
        self.au_conditions_lb.setWordWrap(True)
        self.au_conditions_lb.setObjectName("au_conditions_lb")
        self.horizontalLayout_80.addWidget(self.au_conditions_lb)
        self.verticalLayout_50.addLayout(self.horizontalLayout_80)
        spacerItem84 = QtWidgets.QSpacerItem(20, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_50.addItem(spacerItem84)
        self.horizontalLayout_82.addLayout(self.verticalLayout_50)
        self.verticalLayout_51 = QtWidgets.QVBoxLayout()
        self.verticalLayout_51.setObjectName("verticalLayout_51")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.au_conditions_ta = QtWidgets.QPlainTextEdit(self.tabWidgetPage8)
        self.au_conditions_ta.setMinimumSize(QtCore.QSize(600, 100))
        self.au_conditions_ta.setMaximumSize(QtCore.QSize(600, 100))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.au_conditions_ta.setFont(font)
        self.au_conditions_ta.setStyleSheet("QPlainTextEdit {\n"
"    border-radius: 3px;\n"
"   padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"}")
        self.au_conditions_ta.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.au_conditions_ta.setObjectName("au_conditions_ta")
        self.horizontalLayout_18.addWidget(self.au_conditions_ta)
        self.delButton_5 = QtWidgets.QToolButton(self.tabWidgetPage8)
        self.delButton_5.setEnabled(False)
        self.delButton_5.setMinimumSize(QtCore.QSize(27, 27))
        self.delButton_5.setMaximumSize(QtCore.QSize(27, 27))
        self.delButton_5.setStyleSheet("QToolButton {\n"
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
        self.delButton_5.setText("")
        self.delButton_5.setIcon(icon3)
        self.delButton_5.setIconSize(QtCore.QSize(27, 27))
        self.delButton_5.setAutoRaise(False)
        self.delButton_5.setObjectName("delButton_5")
        self.horizontalLayout_18.addWidget(self.delButton_5)
        self.verticalLayout_51.addLayout(self.horizontalLayout_18)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_51.addLayout(self.verticalLayout_4)
        self.horizontalLayout_82.addLayout(self.verticalLayout_51)
        self.verticalLayout_43 = QtWidgets.QVBoxLayout()
        self.verticalLayout_43.setObjectName("verticalLayout_43")
        spacerItem85 = QtWidgets.QSpacerItem(20, 36, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_43.addItem(spacerItem85)
        self.horizontalLayout_81 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_81.setObjectName("horizontalLayout_81")
        spacerItem86 = QtWidgets.QSpacerItem(17, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_81.addItem(spacerItem86)
        self.plusButton_5 = QtWidgets.QToolButton(self.tabWidgetPage8)
        self.plusButton_5.setMinimumSize(QtCore.QSize(27, 27))
        self.plusButton_5.setMaximumSize(QtCore.QSize(27, 27))
        self.plusButton_5.setStyleSheet("QToolButton {\n"
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
        self.plusButton_5.setText("")
        self.plusButton_5.setIcon(icon2)
        self.plusButton_5.setIconSize(QtCore.QSize(27, 27))
        self.plusButton_5.setAutoRaise(False)
        self.plusButton_5.setObjectName("plusButton_5")
        self.horizontalLayout_81.addWidget(self.plusButton_5)
        spacerItem87 = QtWidgets.QSpacerItem(17, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_81.addItem(spacerItem87)
        self.infoButton_18 = QtWidgets.QToolButton(self.tabWidgetPage8)
        self.infoButton_18.setMaximumSize(QtCore.QSize(27, 27))
        self.infoButton_18.setStyleSheet("QToolButton {\n"
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
        self.infoButton_18.setText("")
        self.infoButton_18.setIcon(icon1)
        self.infoButton_18.setIconSize(QtCore.QSize(27, 27))
        self.infoButton_18.setAutoRaise(False)
        self.infoButton_18.setObjectName("infoButton_18")
        self.horizontalLayout_81.addWidget(self.infoButton_18)
        self.verticalLayout_43.addLayout(self.horizontalLayout_81)
        spacerItem88 = QtWidgets.QSpacerItem(20, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_43.addItem(spacerItem88)
        self.horizontalLayout_82.addLayout(self.verticalLayout_43)
        self.verticalLayout_52.addLayout(self.horizontalLayout_82)
        spacerItem89 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_52.addItem(spacerItem89)
        self.line = QtWidgets.QFrame(self.tabWidgetPage8)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(157, 157, 157))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(236, 236, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(196, 196, 196))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(78, 78, 78))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(105, 105, 105))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(157, 157, 157))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(206, 206, 206))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(157, 157, 157))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(236, 236, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(196, 196, 196))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(78, 78, 78))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(105, 105, 105))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(157, 157, 157))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(206, 206, 206))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(78, 78, 78))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(157, 157, 157))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(236, 236, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(196, 196, 196))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(78, 78, 78))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(105, 105, 105))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(78, 78, 78))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(78, 78, 78))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(157, 157, 157))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(157, 157, 157))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(157, 157, 157))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.line.setPalette(palette)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_52.addWidget(self.line)
        spacerItem90 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_52.addItem(spacerItem90)
        self.horizontalLayout_79 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_79.setObjectName("horizontalLayout_79")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        spacerItem91 = QtWidgets.QSpacerItem(20, 25, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_11.addItem(spacerItem91)
        self.horizontalLayout_33 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_33.setObjectName("horizontalLayout_33")
        self.au_limitations_lb = QtWidgets.QLabel(self.tabWidgetPage8)
        self.au_limitations_lb.setMinimumSize(QtCore.QSize(160, 40))
        self.au_limitations_lb.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.au_limitations_lb.setFont(font)
        self.au_limitations_lb.setWordWrap(True)
        self.au_limitations_lb.setObjectName("au_limitations_lb")
        self.horizontalLayout_33.addWidget(self.au_limitations_lb)
        self.verticalLayout_11.addLayout(self.horizontalLayout_33)
        spacerItem92 = QtWidgets.QSpacerItem(20, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_11.addItem(spacerItem92)
        self.horizontalLayout_79.addLayout(self.verticalLayout_11)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.au_limitations_ta = QtWidgets.QPlainTextEdit(self.tabWidgetPage8)
        self.au_limitations_ta.setMinimumSize(QtCore.QSize(600, 100))
        self.au_limitations_ta.setMaximumSize(QtCore.QSize(600, 100))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.au_limitations_ta.setFont(font)
        self.au_limitations_ta.setStyleSheet("QPlainTextEdit {\n"
"    border-radius: 3px;\n"
"   padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"}")
        self.au_limitations_ta.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.au_limitations_ta.setObjectName("au_limitations_ta")
        self.horizontalLayout_17.addWidget(self.au_limitations_ta)
        self.delButton_6 = QtWidgets.QToolButton(self.tabWidgetPage8)
        self.delButton_6.setEnabled(False)
        self.delButton_6.setMinimumSize(QtCore.QSize(27, 27))
        self.delButton_6.setMaximumSize(QtCore.QSize(27, 27))
        self.delButton_6.setStyleSheet("QToolButton {\n"
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
        self.delButton_6.setText("")
        self.delButton_6.setIcon(icon3)
        self.delButton_6.setIconSize(QtCore.QSize(27, 27))
        self.delButton_6.setAutoRaise(False)
        self.delButton_6.setObjectName("delButton_6")
        self.horizontalLayout_17.addWidget(self.delButton_6)
        self.verticalLayout_9.addLayout(self.horizontalLayout_17)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.verticalLayout_9.addLayout(self.verticalLayout_10)
        spacerItem93 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem93)
        self.horizontalLayout_79.addLayout(self.verticalLayout_9)
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        spacerItem94 = QtWidgets.QSpacerItem(20, 36, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_12.addItem(spacerItem94)
        self.horizontalLayout_52 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_52.setObjectName("horizontalLayout_52")
        spacerItem95 = QtWidgets.QSpacerItem(17, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_52.addItem(spacerItem95)
        self.plusButton_6 = QtWidgets.QToolButton(self.tabWidgetPage8)
        self.plusButton_6.setMinimumSize(QtCore.QSize(27, 27))
        self.plusButton_6.setMaximumSize(QtCore.QSize(27, 27))
        self.plusButton_6.setStyleSheet("QToolButton {\n"
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
        self.plusButton_6.setText("")
        self.plusButton_6.setIcon(icon2)
        self.plusButton_6.setIconSize(QtCore.QSize(27, 27))
        self.plusButton_6.setAutoRaise(False)
        self.plusButton_6.setObjectName("plusButton_6")
        self.horizontalLayout_52.addWidget(self.plusButton_6)
        spacerItem96 = QtWidgets.QSpacerItem(17, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_52.addItem(spacerItem96)
        self.infoButton_19 = QtWidgets.QToolButton(self.tabWidgetPage8)
        self.infoButton_19.setMaximumSize(QtCore.QSize(27, 27))
        self.infoButton_19.setStyleSheet("QToolButton {\n"
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
        self.infoButton_19.setText("")
        self.infoButton_19.setIcon(icon1)
        self.infoButton_19.setIconSize(QtCore.QSize(27, 27))
        self.infoButton_19.setAutoRaise(False)
        self.infoButton_19.setObjectName("infoButton_19")
        self.horizontalLayout_52.addWidget(self.infoButton_19)
        self.verticalLayout_12.addLayout(self.horizontalLayout_52)
        spacerItem97 = QtWidgets.QSpacerItem(20, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_12.addItem(spacerItem97)
        self.horizontalLayout_79.addLayout(self.verticalLayout_12)
        self.verticalLayout_52.addLayout(self.horizontalLayout_79)
        self.gridLayout_6.addLayout(self.verticalLayout_52, 1, 1, 1, 2)
        spacerItem98 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem98, 1, 3, 1, 1)
        spacerItem99 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_6.addItem(spacerItem99, 2, 1, 1, 1)
        self.tabWidget.addTab(self.tabWidgetPage8, "")
        self.tabWidgetPage9 = QtWidgets.QWidget()
        self.tabWidgetPage9.setObjectName("tabWidgetPage9")
        self.gridLayout_14 = QtWidgets.QGridLayout(self.tabWidgetPage9)
        self.gridLayout_14.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_14.setObjectName("gridLayout_14")
        spacerItem100 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_14.addItem(spacerItem100, 0, 1, 1, 1)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.gridLayout_9 = QtWidgets.QGridLayout()
        self.gridLayout_9.setVerticalSpacing(30)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.ro_responsibleParty_lb = QtWidgets.QLabel(self.tabWidgetPage9)
        self.ro_responsibleParty_lb.setMinimumSize(QtCore.QSize(0, 0))
        self.ro_responsibleParty_lb.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ro_responsibleParty_lb.setFont(font)
        self.ro_responsibleParty_lb.setObjectName("ro_responsibleParty_lb")
        self.gridLayout_9.addWidget(self.ro_responsibleParty_lb, 0, 0, 1, 1)
        self.ro_responsibleParty_ln = QtWidgets.QLineEdit(self.tabWidgetPage9)
        self.ro_responsibleParty_ln.setMinimumSize(QtCore.QSize(250, 27))
        self.ro_responsibleParty_ln.setMaximumSize(QtCore.QSize(250, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ro_responsibleParty_ln.setFont(font)
        self.ro_responsibleParty_ln.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"   padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"}")
        self.ro_responsibleParty_ln.setFrame(False)
        self.ro_responsibleParty_ln.setObjectName("ro_responsibleParty_ln")
        self.gridLayout_9.addWidget(self.ro_responsibleParty_ln, 0, 1, 1, 1)
        self.infoButton_20 = QtWidgets.QToolButton(self.tabWidgetPage9)
        self.infoButton_20.setMaximumSize(QtCore.QSize(27, 27))
        self.infoButton_20.setStyleSheet("QToolButton {\n"
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
        self.infoButton_20.setText("")
        self.infoButton_20.setIcon(icon1)
        self.infoButton_20.setIconSize(QtCore.QSize(27, 27))
        self.infoButton_20.setAutoRaise(False)
        self.infoButton_20.setObjectName("infoButton_20")
        self.gridLayout_9.addWidget(self.infoButton_20, 0, 2, 1, 1)
        self.ro_responsibleEmail_lb = QtWidgets.QLabel(self.tabWidgetPage9)
        self.ro_responsibleEmail_lb.setMinimumSize(QtCore.QSize(0, 0))
        self.ro_responsibleEmail_lb.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ro_responsibleEmail_lb.setFont(font)
        self.ro_responsibleEmail_lb.setObjectName("ro_responsibleEmail_lb")
        self.gridLayout_9.addWidget(self.ro_responsibleEmail_lb, 1, 0, 1, 1)
        self.ro_responsibleEmail_ln = QtWidgets.QLineEdit(self.tabWidgetPage9)
        self.ro_responsibleEmail_ln.setMinimumSize(QtCore.QSize(250, 27))
        self.ro_responsibleEmail_ln.setMaximumSize(QtCore.QSize(250, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ro_responsibleEmail_ln.setFont(font)
        self.ro_responsibleEmail_ln.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"   padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"}")
        self.ro_responsibleEmail_ln.setFrame(False)
        self.ro_responsibleEmail_ln.setObjectName("ro_responsibleEmail_ln")
        self.gridLayout_9.addWidget(self.ro_responsibleEmail_ln, 1, 1, 1, 1)
        self.infoButton_21 = QtWidgets.QToolButton(self.tabWidgetPage9)
        self.infoButton_21.setMaximumSize(QtCore.QSize(27, 27))
        self.infoButton_21.setStyleSheet("QToolButton {\n"
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
        self.infoButton_21.setText("")
        self.infoButton_21.setIcon(icon1)
        self.infoButton_21.setIconSize(QtCore.QSize(27, 27))
        self.infoButton_21.setAutoRaise(False)
        self.infoButton_21.setObjectName("infoButton_21")
        self.gridLayout_9.addWidget(self.infoButton_21, 1, 2, 1, 1)
        spacerItem101 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_9.addItem(spacerItem101, 1, 3, 1, 1)
        self.delButton_8 = QtWidgets.QToolButton(self.tabWidgetPage9)
        self.delButton_8.setEnabled(False)
        self.delButton_8.setMinimumSize(QtCore.QSize(27, 27))
        self.delButton_8.setMaximumSize(QtCore.QSize(27, 27))
        self.delButton_8.setStyleSheet("QToolButton {\n"
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
        self.delButton_8.setText("")
        self.delButton_8.setIcon(icon3)
        self.delButton_8.setIconSize(QtCore.QSize(27, 27))
        self.delButton_8.setAutoRaise(True)
        self.delButton_8.setObjectName("delButton_8")
        self.gridLayout_9.addWidget(self.delButton_8, 1, 4, 1, 1)
        spacerItem102 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_9.addItem(spacerItem102, 1, 5, 1, 1)
        self.plusButton_7 = QtWidgets.QToolButton(self.tabWidgetPage9)
        self.plusButton_7.setMinimumSize(QtCore.QSize(27, 27))
        self.plusButton_7.setMaximumSize(QtCore.QSize(27, 27))
        self.plusButton_7.setStyleSheet("QToolButton {\n"
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
        self.plusButton_7.setText("")
        self.plusButton_7.setIcon(icon2)
        self.plusButton_7.setIconSize(QtCore.QSize(27, 27))
        self.plusButton_7.setAutoRaise(False)
        self.plusButton_7.setObjectName("plusButton_7")
        self.gridLayout_9.addWidget(self.plusButton_7, 1, 6, 1, 1)
        self.ro_label_3 = QtWidgets.QLabel(self.tabWidgetPage9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ro_label_3.sizePolicy().hasHeightForWidth())
        self.ro_label_3.setSizePolicy(sizePolicy)
        self.ro_label_3.setMinimumSize(QtCore.QSize(0, 0))
        self.ro_label_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ro_label_3.setFont(font)
        self.ro_label_3.setObjectName("ro_label_3")
        self.gridLayout_9.addWidget(self.ro_label_3, 2, 0, 1, 1)
        self.ro_responsibleRole_rl1 = QtWidgets.QComboBox(self.tabWidgetPage9)
        self.ro_responsibleRole_rl1.setMinimumSize(QtCore.QSize(200, 27))
        self.ro_responsibleRole_rl1.setMaximumSize(QtCore.QSize(200, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ro_responsibleRole_rl1.setFont(font)
        self.ro_responsibleRole_rl1.setStyleSheet("QComboBox {\n"
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
        self.ro_responsibleRole_rl1.setObjectName("ro_responsibleRole_rl1")
        self.ro_responsibleRole_rl1.addItem("")
        self.ro_responsibleRole_rl1.addItem("")
        self.ro_responsibleRole_rl1.addItem("")
        self.ro_responsibleRole_rl1.addItem("")
        self.ro_responsibleRole_rl1.addItem("")
        self.ro_responsibleRole_rl1.addItem("")
        self.ro_responsibleRole_rl1.addItem("")
        self.ro_responsibleRole_rl1.addItem("")
        self.ro_responsibleRole_rl1.addItem("")
        self.ro_responsibleRole_rl1.addItem("")
        self.ro_responsibleRole_rl1.addItem("")
        self.gridLayout_9.addWidget(self.ro_responsibleRole_rl1, 2, 1, 1, 1)
        self.infoButton_22 = QtWidgets.QToolButton(self.tabWidgetPage9)
        self.infoButton_22.setMaximumSize(QtCore.QSize(27, 27))
        self.infoButton_22.setStyleSheet("QToolButton {\n"
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
        self.infoButton_22.setText("")
        self.infoButton_22.setIcon(icon1)
        self.infoButton_22.setIconSize(QtCore.QSize(27, 27))
        self.infoButton_22.setAutoRaise(False)
        self.infoButton_22.setObjectName("infoButton_22")
        self.gridLayout_9.addWidget(self.infoButton_22, 2, 2, 1, 1)
        self.verticalLayout_5.addLayout(self.gridLayout_9)
        self.verticalLayout_18 = QtWidgets.QVBoxLayout()
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.verticalLayout_5.addLayout(self.verticalLayout_18)
        spacerItem103 = QtWidgets.QSpacerItem(20, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem103)
        self.gridLayout_14.addLayout(self.verticalLayout_5, 1, 1, 2, 1)
        spacerItem104 = QtWidgets.QSpacerItem(302, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_14.addItem(spacerItem104, 1, 2, 1, 1)
        spacerItem105 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_14.addItem(spacerItem105, 2, 0, 1, 1)
        spacerItem106 = QtWidgets.QSpacerItem(20, 191, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_14.addItem(spacerItem106, 3, 1, 1, 1)
        self.tabWidget.addTab(self.tabWidgetPage9, "")
        self.tabWidgetPage10 = QtWidgets.QWidget()
        self.tabWidgetPage10.setObjectName("tabWidgetPage10")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.tabWidgetPage10)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        spacerItem107 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_7.addItem(spacerItem107, 0, 1, 1, 1)
        self.verticalLayout_39 = QtWidgets.QVBoxLayout()
        self.verticalLayout_39.setObjectName("verticalLayout_39")
        self.horizontalLayout_37 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_37.setObjectName("horizontalLayout_37")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.mm_date_lb = QtWidgets.QLabel(self.tabWidgetPage10)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.mm_date_lb.setFont(font)
        self.mm_date_lb.setObjectName("mm_date_lb")
        self.horizontalLayout_7.addWidget(self.mm_date_lb)
        self.mm_date_do1 = QtWidgets.QDateEdit(self.tabWidgetPage10)
        self.mm_date_do1.setMinimumSize(QtCore.QSize(120, 27))
        self.mm_date_do1.setMaximumSize(QtCore.QSize(120, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.mm_date_do1.setFont(font)
        self.mm_date_do1.setStyleSheet("QDateEdit {\n"
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
        self.mm_date_do1.setWrapping(False)
        self.mm_date_do1.setFrame(False)
        self.mm_date_do1.setAlignment(QtCore.Qt.AlignCenter)
        self.mm_date_do1.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.mm_date_do1.setAccelerated(True)
        self.mm_date_do1.setCalendarPopup(True)
        self.mm_date_do1.setTimeSpec(QtCore.Qt.UTC)
        self.mm_date_do1.setDate(QtCore.QDate(2014, 10, 7))
        self.mm_date_do1.setObjectName("mm_date_do1")
        self.horizontalLayout_7.addWidget(self.mm_date_do1)
        self.infoButton_23 = QtWidgets.QToolButton(self.tabWidgetPage10)
        self.infoButton_23.setMaximumSize(QtCore.QSize(27, 27))
        self.infoButton_23.setStyleSheet("QToolButton {\n"
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
        self.infoButton_23.setText("")
        self.infoButton_23.setIcon(icon1)
        self.infoButton_23.setIconSize(QtCore.QSize(27, 27))
        self.infoButton_23.setAutoRaise(False)
        self.infoButton_23.setObjectName("infoButton_23")
        self.horizontalLayout_7.addWidget(self.infoButton_23)
        self.verticalLayout_6.addLayout(self.horizontalLayout_7)
        spacerItem108 = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_6.addItem(spacerItem108)
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.mm_label_2 = QtWidgets.QLabel(self.tabWidgetPage10)
        self.mm_label_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.mm_label_2.setFont(font)
        self.mm_label_2.setObjectName("mm_label_2")
        self.horizontalLayout_22.addWidget(self.mm_label_2)
        self.mm_language_rl1 = QtWidgets.QComboBox(self.tabWidgetPage10)
        self.mm_language_rl1.setMinimumSize(QtCore.QSize(120, 27))
        self.mm_language_rl1.setMaximumSize(QtCore.QSize(120, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.mm_language_rl1.setFont(font)
        self.mm_language_rl1.setStyleSheet("QComboBox {\n"
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
        self.mm_language_rl1.setObjectName("mm_language_rl1")
        self.mm_language_rl1.addItem("")
        self.mm_language_rl1.addItem("")
        self.mm_language_rl1.addItem("")
        self.mm_language_rl1.addItem("")
        self.mm_language_rl1.addItem("")
        self.mm_language_rl1.addItem("")
        self.mm_language_rl1.addItem("")
        self.mm_language_rl1.addItem("")
        self.mm_language_rl1.addItem("")
        self.mm_language_rl1.addItem("")
        self.mm_language_rl1.addItem("")
        self.mm_language_rl1.addItem("")
        self.mm_language_rl1.addItem("")
        self.mm_language_rl1.addItem("")
        self.mm_language_rl1.addItem("")
        self.mm_language_rl1.addItem("")
        self.mm_language_rl1.addItem("")
        self.mm_language_rl1.addItem("")
        self.mm_language_rl1.addItem("")
        self.mm_language_rl1.addItem("")
        self.mm_language_rl1.addItem("")
        self.mm_language_rl1.addItem("")
        self.mm_language_rl1.addItem("")
        self.horizontalLayout_22.addWidget(self.mm_language_rl1)
        self.infoButton_24 = QtWidgets.QToolButton(self.tabWidgetPage10)
        self.infoButton_24.setMaximumSize(QtCore.QSize(27, 27))
        self.infoButton_24.setStyleSheet("QToolButton {\n"
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
        self.infoButton_24.setText("")
        self.infoButton_24.setIcon(icon1)
        self.infoButton_24.setIconSize(QtCore.QSize(27, 27))
        self.infoButton_24.setAutoRaise(False)
        self.infoButton_24.setObjectName("infoButton_24")
        self.horizontalLayout_22.addWidget(self.infoButton_24)
        self.verticalLayout_6.addLayout(self.horizontalLayout_22)
        self.horizontalLayout_37.addLayout(self.verticalLayout_6)
        spacerItem109 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_37.addItem(spacerItem109)
        self.verticalLayout_39.addLayout(self.horizontalLayout_37)
        spacerItem110 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_39.addItem(spacerItem110)
        self.horizontalLayout_65 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_65.setObjectName("horizontalLayout_65")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout()
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        spacerItem111 = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_19.addItem(spacerItem111)
        self.horizontalLayout_54 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_54.setObjectName("horizontalLayout_54")
        self.mm_label_3 = QtWidgets.QLabel(self.tabWidgetPage10)
        self.mm_label_3.setMinimumSize(QtCore.QSize(0, 27))
        self.mm_label_3.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.mm_label_3.setFont(font)
        self.mm_label_3.setObjectName("mm_label_3")
        self.horizontalLayout_54.addWidget(self.mm_label_3)
        spacerItem112 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_54.addItem(spacerItem112)
        self.verticalLayout_19.addLayout(self.horizontalLayout_54)
        spacerItem113 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        self.verticalLayout_19.addItem(spacerItem113)
        self.horizontalLayout_65.addLayout(self.verticalLayout_19)
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.horizontalLayout_26 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_26.setObjectName("horizontalLayout_26")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.mm_contactName_lb = QtWidgets.QLabel(self.tabWidgetPage10)
        self.mm_contactName_lb.setMinimumSize(QtCore.QSize(0, 0))
        self.mm_contactName_lb.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.mm_contactName_lb.setFont(font)
        self.mm_contactName_lb.setObjectName("mm_contactName_lb")
        self.horizontalLayout_23.addWidget(self.mm_contactName_lb)
        self.mm_contactName_ln = QtWidgets.QLineEdit(self.tabWidgetPage10)
        self.mm_contactName_ln.setMinimumSize(QtCore.QSize(250, 27))
        self.mm_contactName_ln.setMaximumSize(QtCore.QSize(250, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.mm_contactName_ln.setFont(font)
        self.mm_contactName_ln.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"   padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"}")
        self.mm_contactName_ln.setFrame(False)
        self.mm_contactName_ln.setObjectName("mm_contactName_ln")
        self.horizontalLayout_23.addWidget(self.mm_contactName_ln)
        self.verticalLayout_3.addLayout(self.horizontalLayout_23)
        self.horizontalLayout_25 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        self.mm_contactEmail_lb = QtWidgets.QLabel(self.tabWidgetPage10)
        self.mm_contactEmail_lb.setMinimumSize(QtCore.QSize(0, 0))
        self.mm_contactEmail_lb.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.mm_contactEmail_lb.setFont(font)
        self.mm_contactEmail_lb.setObjectName("mm_contactEmail_lb")
        self.horizontalLayout_25.addWidget(self.mm_contactEmail_lb)
        self.mm_contactEmail_ln = QtWidgets.QLineEdit(self.tabWidgetPage10)
        self.mm_contactEmail_ln.setMinimumSize(QtCore.QSize(250, 27))
        self.mm_contactEmail_ln.setMaximumSize(QtCore.QSize(250, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.mm_contactEmail_ln.setFont(font)
        self.mm_contactEmail_ln.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"   padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"}")
        self.mm_contactEmail_ln.setFrame(False)
        self.mm_contactEmail_ln.setObjectName("mm_contactEmail_ln")
        self.horizontalLayout_25.addWidget(self.mm_contactEmail_ln)
        self.verticalLayout_3.addLayout(self.horizontalLayout_25)
        self.horizontalLayout_26.addLayout(self.verticalLayout_3)
        spacerItem114 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_26.addItem(spacerItem114)
        self.delButton_7 = QtWidgets.QToolButton(self.tabWidgetPage10)
        self.delButton_7.setEnabled(False)
        self.delButton_7.setMinimumSize(QtCore.QSize(27, 27))
        self.delButton_7.setMaximumSize(QtCore.QSize(27, 27))
        self.delButton_7.setStyleSheet("QToolButton {\n"
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
        self.delButton_7.setText("")
        self.delButton_7.setIcon(icon3)
        self.delButton_7.setIconSize(QtCore.QSize(27, 27))
        self.delButton_7.setAutoRaise(False)
        self.delButton_7.setObjectName("delButton_7")
        self.horizontalLayout_26.addWidget(self.delButton_7)
        self.verticalLayout_13.addLayout(self.horizontalLayout_26)
        self.verticalLayout_14 = QtWidgets.QVBoxLayout()
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.verticalLayout_13.addLayout(self.verticalLayout_14)
        spacerItem115 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_13.addItem(spacerItem115)
        self.horizontalLayout_65.addLayout(self.verticalLayout_13)
        self.verticalLayout_38 = QtWidgets.QVBoxLayout()
        self.verticalLayout_38.setObjectName("verticalLayout_38")
        spacerItem116 = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_38.addItem(spacerItem116)
        self.horizontalLayout_59 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_59.setObjectName("horizontalLayout_59")
        spacerItem117 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_59.addItem(spacerItem117)
        self.plusButton_8 = QtWidgets.QToolButton(self.tabWidgetPage10)
        self.plusButton_8.setMinimumSize(QtCore.QSize(27, 27))
        self.plusButton_8.setMaximumSize(QtCore.QSize(27, 27))
        self.plusButton_8.setStyleSheet("QToolButton {\n"
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
        self.plusButton_8.setText("")
        self.plusButton_8.setIcon(icon2)
        self.plusButton_8.setIconSize(QtCore.QSize(27, 27))
        self.plusButton_8.setAutoRaise(False)
        self.plusButton_8.setObjectName("plusButton_8")
        self.horizontalLayout_59.addWidget(self.plusButton_8)
        spacerItem118 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_59.addItem(spacerItem118)
        self.infoButton_25 = QtWidgets.QToolButton(self.tabWidgetPage10)
        self.infoButton_25.setMaximumSize(QtCore.QSize(27, 27))
        self.infoButton_25.setStyleSheet("QToolButton {\n"
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
        self.infoButton_25.setText("")
        self.infoButton_25.setIcon(icon1)
        self.infoButton_25.setIconSize(QtCore.QSize(27, 27))
        self.infoButton_25.setAutoRaise(False)
        self.infoButton_25.setObjectName("infoButton_25")
        self.horizontalLayout_59.addWidget(self.infoButton_25)
        self.verticalLayout_38.addLayout(self.horizontalLayout_59)
        spacerItem119 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        self.verticalLayout_38.addItem(spacerItem119)
        self.horizontalLayout_65.addLayout(self.verticalLayout_38)
        self.verticalLayout_39.addLayout(self.horizontalLayout_65)
        self.gridLayout_7.addLayout(self.verticalLayout_39, 1, 1, 2, 1)
        spacerItem120 = QtWidgets.QSpacerItem(172, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem120, 1, 2, 1, 1)
        spacerItem121 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem121, 2, 0, 1, 1)
        spacerItem122 = QtWidgets.QSpacerItem(20, 154, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_7.addItem(spacerItem122, 3, 1, 1, 1)
        self.tabWidget.addTab(self.tabWidgetPage10, "")
        self.gridLayout_4.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1094, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icons/new_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNew.setIcon(icon4)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.actionNew.setFont(font)
        self.actionNew.setIconVisibleInMenu(True)
        self.actionNew.setObjectName("actionNew")
        self.actionSave = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icons/save_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave.setIcon(icon5)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.actionSave.setFont(font)
        self.actionSave.setIconVisibleInMenu(True)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_As = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("icons/save_as_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave_As.setIcon(icon6)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.actionSave_As.setFont(font)
        self.actionSave_As.setIconVisibleInMenu(True)
        self.actionSave_As.setObjectName("actionSave_As")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("icons/open_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen.setIcon(icon7)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.actionOpen.setFont(font)
        self.actionOpen.setIconVisibleInMenu(True)
        self.actionOpen.setObjectName("actionOpen")
        self.actionExit = QtWidgets.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("icons/exit_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExit.setIcon(icon8)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.actionExit.setFont(font)
        self.actionExit.setIconVisibleInMenu(True)
        self.actionExit.setObjectName("actionExit")
        self.actionEUFAR_CreatorAbout = QtWidgets.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("icons/about_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionEUFAR_CreatorAbout.setIcon(icon9)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.actionEUFAR_CreatorAbout.setFont(font)
        self.actionEUFAR_CreatorAbout.setIconVisibleInMenu(True)
        self.actionEUFAR_CreatorAbout.setObjectName("actionEUFAR_CreatorAbout")
        self.actionINSPIRE_Standard = QtWidgets.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("icons/inspire_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionINSPIRE_Standard.setIcon(icon10)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.actionINSPIRE_Standard.setFont(font)
        self.actionINSPIRE_Standard.setIconVisibleInMenu(True)
        self.actionINSPIRE_Standard.setObjectName("actionINSPIRE_Standard")
        self.actionEUFAR_N7SP = QtWidgets.QAction(MainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("icons/eufar_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionEUFAR_N7SP.setIcon(icon11)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.actionEUFAR_N7SP.setFont(font)
        self.actionEUFAR_N7SP.setIconVisibleInMenu(True)
        self.actionEUFAR_N7SP.setObjectName("actionEUFAR_N7SP")
        self.actionPreferences = QtWidgets.QAction(MainWindow)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/icons/preferences_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPreferences.setIcon(icon12)
        self.actionPreferences.setObjectName("actionPreferences")
        self.actionChangelog = QtWidgets.QAction(MainWindow)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap("icons/changelog_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionChangelog.setIcon(icon13)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.actionChangelog.setFont(font)
        self.actionChangelog.setIconVisibleInMenu(True)
        self.actionChangelog.setObjectName("actionChangelog")
        self.actionMemory = QtWidgets.QAction(MainWindow)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap("icons/memory_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionMemory.setIcon(icon14)
        font = QtGui.QFont()
        font.setFamily("Droid Sans Fallback")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.actionMemory.setFont(font)
        self.actionMemory.setObjectName("actionMemory")
        self.actionCPU = QtWidgets.QAction(MainWindow)
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap("icons/cpu_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCPU.setIcon(icon15)
        font = QtGui.QFont()
        font.setFamily("Droid Sans Fallback")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.actionCPU.setFont(font)
        self.actionCPU.setObjectName("actionCPU")
        self.actionObject = QtWidgets.QAction(MainWindow)
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap("icons/python_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionObject.setIcon(icon16)
        font = QtGui.QFont()
        font.setFamily("Droid Sans Fallback")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.actionObject.setFont(font)
        self.actionObject.setObjectName("actionObject")
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setIcon(icon11)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.actionHelp.setFont(font)
        self.actionHelp.setObjectName("actionHelp")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_As)
        self.menuFile.addAction(self.actionExit)
        self.menuAbout.addAction(self.actionEUFAR_CreatorAbout)
        self.menuAbout.addAction(self.actionINSPIRE_Standard)
        self.menuAbout.addAction(self.actionEUFAR_N7SP)
        self.menuAbout.addAction(self.actionHelp)
        self.menuAbout.addSeparator()
        self.menuAbout.addAction(self.actionChangelog)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.id_resourceType_rl1.setCurrentIndex(0)
        self.id_resourceLang_rl2.setCurrentIndex(4)
        self.ai_aircraft_rl1.setCurrentIndex(0)
        self.ai_instrument_rl1.setCurrentIndex(-1)
        self.ro_responsibleRole_rl1.setCurrentIndex(5)
        self.mm_language_rl1.setCurrentIndex(4)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "EUFAR Metadata Creator"))
        self.id_resourceTitle_lb.setText(_translate("MainWindow", "Project title:"))
        self.id_resourceIdent_lb.setText(_translate("MainWindow", "Project acronym:"))
        self.id_resourceAbstract_lb.setText(_translate("MainWindow", "Project abstract:"))
        self.id_label_3.setText(_translate("MainWindow", "Resource type:"))
        self.id_resourceType_rl1.setItemText(0, _translate("MainWindow", "Dataset"))
        self.id_resourceType_rl1.setItemText(1, _translate("MainWindow", "Series"))
        self.id_resourceLocator_lb.setText(_translate("MainWindow", "Resource locator:"))
        self.id_resourceLocator_ln.setText(_translate("MainWindow", "http://browse.ceda.ac.uk/browse/badc/eufar/docs/00eufararchivecontents.html"))
        self.id_label_6.setText(_translate("MainWindow", "Resource language:"))
        self.id_resourceLang_rl2.setItemText(0, _translate("MainWindow", "Bulgarian"))
        self.id_resourceLang_rl2.setItemText(1, _translate("MainWindow", "Czech"))
        self.id_resourceLang_rl2.setItemText(2, _translate("MainWindow", "Danish"))
        self.id_resourceLang_rl2.setItemText(3, _translate("MainWindow", "Dutch"))
        self.id_resourceLang_rl2.setItemText(4, _translate("MainWindow", "English"))
        self.id_resourceLang_rl2.setItemText(5, _translate("MainWindow", "Estonian"))
        self.id_resourceLang_rl2.setItemText(6, _translate("MainWindow", "Finnish"))
        self.id_resourceLang_rl2.setItemText(7, _translate("MainWindow", "French"))
        self.id_resourceLang_rl2.setItemText(8, _translate("MainWindow", "German"))
        self.id_resourceLang_rl2.setItemText(9, _translate("MainWindow", "Greek"))
        self.id_resourceLang_rl2.setItemText(10, _translate("MainWindow", "Hungarian"))
        self.id_resourceLang_rl2.setItemText(11, _translate("MainWindow", "Irish"))
        self.id_resourceLang_rl2.setItemText(12, _translate("MainWindow", "Italian"))
        self.id_resourceLang_rl2.setItemText(13, _translate("MainWindow", "Latvian"))
        self.id_resourceLang_rl2.setItemText(14, _translate("MainWindow", "Lithuanian"))
        self.id_resourceLang_rl2.setItemText(15, _translate("MainWindow", "Maltese"))
        self.id_resourceLang_rl2.setItemText(16, _translate("MainWindow", "Polish"))
        self.id_resourceLang_rl2.setItemText(17, _translate("MainWindow", "Portuguese"))
        self.id_resourceLang_rl2.setItemText(18, _translate("MainWindow", "Romanian"))
        self.id_resourceLang_rl2.setItemText(19, _translate("MainWindow", "Slovak"))
        self.id_resourceLang_rl2.setItemText(20, _translate("MainWindow", "Slovenian"))
        self.id_resourceLang_rl2.setItemText(21, _translate("MainWindow", "Spanish"))
        self.id_resourceLang_rl2.setItemText(22, _translate("MainWindow", "Swedish"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage1), _translate("MainWindow", "Identification"))
        self.cl_topicIntelligence_ck.setToolTip(_translate("MainWindow", "<html><head/><body><p>Military bases, structures, activities</p></body></html>"))
        self.cl_topicIntelligence_ck.setText(_translate("MainWindow", "Intelligence / Military"))
        self.cl_topicLocation_ck.setToolTip(_translate("MainWindow", "<html><head/><body><p>Positional information and services</p></body></html>"))
        self.cl_topicLocation_ck.setText(_translate("MainWindow", "Location"))
        self.cl_topicPlanning_ck.setToolTip(_translate("MainWindow", "<html><head/><body><p>Information used for appropriate actions for future use of the land</p></body></html>"))
        self.cl_topicPlanning_ck.setText(_translate("MainWindow", "Planning / Cadastre"))
        self.cl_topicEconomy_ck.setToolTip(_translate("MainWindow", "<html><head/><body><p>Economic activities, conditions and employment</p></body></html>"))
        self.cl_topicEconomy_ck.setText(_translate("MainWindow", "Economy"))
        self.cl_topicSociety_ck.setToolTip(_translate("MainWindow", "<html><head/><body><p>Characteristics of society and cultures</p></body></html>"))
        self.cl_topicSociety_ck.setText(_translate("MainWindow", "Society"))
        self.cl_topicStructure_ck.setToolTip(_translate("MainWindow", "<html><head/><body><p>Man-made construction</p></body></html>"))
        self.cl_topicStructure_ck.setText(_translate("MainWindow", "Structure"))
        self.cl_label_1.setText(_translate("MainWindow", "Topic Categories:"))
        self.cl_topicTransportation_ck.setToolTip(_translate("MainWindow", "<html><head/><body><p>Means and aids for conveying persons and/or goods</p></body></html>"))
        self.cl_topicTransportation_ck.setText(_translate("MainWindow", "Transportation"))
        self.cl_topicClimatology_ck.setToolTip(_translate("MainWindow", "<html><head/><body><p>Processes and phenomena of the atmosphere</p></body></html>"))
        self.cl_topicClimatology_ck.setText(_translate("MainWindow", "Climatology / Meteorology / Atmosphere"))
        self.cl_topicElevation_ck.setToolTip(_translate("MainWindow", "<html><head/><body><p>Height above or below sea level</p></body></html>"))
        self.cl_topicElevation_ck.setText(_translate("MainWindow", "Elevation"))
        self.cl_topicOceans_ck.setToolTip(_translate("MainWindow", "<html><head/><body><p>Features and characteristics of salt water bodies (excluding inland waters)</p></body></html>"))
        self.cl_topicOceans_ck.setText(_translate("MainWindow", "Oceans"))
        self.cl_topicImagery_ck.setToolTip(_translate("MainWindow", "<html><head/><body><p>Base maps</p></body></html>"))
        self.cl_topicImagery_ck.setText(_translate("MainWindow", "Imagery / Base Maps / Earth Cover"))
        self.cl_topicEnvironment_ck.setToolTip(_translate("MainWindow", "<html><head/><body><p>Environmental resources, protection and conservation</p></body></html>"))
        self.cl_topicEnvironment_ck.setText(_translate("MainWindow", "Environment"))
        self.cl_topicWaters_ck.setToolTip(_translate("MainWindow", "<html><head/><body><p>Inland water features, drainage systems and their characteristics</p></body></html>"))
        self.cl_topicWaters_ck.setText(_translate("MainWindow", "Inland Waters"))
        self.cl_topicUtilities_ck.setToolTip(_translate("MainWindow", "<html><head/><body><p>Energy, water and waste systems and communications infrastructure and services</p></body></html>"))
        self.cl_topicUtilities_ck.setText(_translate("MainWindow", "Utilities / Communication"))
        self.cl_topicBiota_ck.setToolTip(_translate("MainWindow", "<html><head/><body><p>Flora and/or fauna in natural environment</p></body></html>"))
        self.cl_topicBiota_ck.setText(_translate("MainWindow", "Biota"))
        self.cl_topicFarming_ck.setToolTip(_translate("MainWindow", "<html><head/><body><p>Rearing of animals and/or cultivation of plants</p></body></html>"))
        self.cl_topicFarming_ck.setText(_translate("MainWindow", "Farming"))
        self.cl_topicBoundaries_ck.setToolTip(_translate("MainWindow", "<html><head/><body><p>Legal land descriptions</p></body></html>"))
        self.cl_topicBoundaries_ck.setText(_translate("MainWindow", "Boundaries"))
        self.cl_topicHealth_ck.setToolTip(_translate("MainWindow", "<html><head/><body><p>Health, health services, human ecology and safety</p></body></html>"))
        self.cl_topicHealth_ck.setText(_translate("MainWindow", "Health"))
        self.cl_topicInformation_ck.setToolTip(_translate("MainWindow", "<html><head/><body><p>Information pertaining to earth sciences</p></body></html>"))
        self.cl_topicInformation_ck.setText(_translate("MainWindow", "Geoscientific Information"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage2), _translate("MainWindow", "Classification"))
        self.kw_category_lb1.setText(_translate("MainWindow", "Agriculture:"))
        self.kw_agriEngineering_ck.setText(_translate("MainWindow", "Agricultural engineering"))
        self.kw_agriPlant_ck.setText(_translate("MainWindow", "Agricultural plant science"))
        self.kw_foodScience_ck.setText(_translate("MainWindow", "Food science"))
        self.kw_forestScience_ck.setText(_translate("MainWindow", "Forest science"))
        self.kw_soils_ck.setText(_translate("MainWindow", "Soils"))
        self.kw_category_lb2.setText(_translate("MainWindow", "Atmosphere:"))
        self.kw_aerosols_ck.setText(_translate("MainWindow", "Aerosols"))
        self.kw_airQuality_ck.setText(_translate("MainWindow", "Air quality"))
        self.kw_altitude_ck.setText(_translate("MainWindow", "Altitude"))
        self.kw_atmChemistry_ck.setText(_translate("MainWindow", "Atmospheric chemistry"))
        self.kw_atmElectricity_ck.setText(_translate("MainWindow", "Atmospheric electricity"))
        self.kw_atmPhenomena_ck.setText(_translate("MainWindow", "Atmospheric phenomena"))
        self.kw_atmPressure_ck.setText(_translate("MainWindow", "Atmospheric pressure"))
        self.kw_atmRadiation_ck.setText(_translate("MainWindow", "Atmospheric radiation"))
        self.kw_atmTemperature_ck.setText(_translate("MainWindow", "Atmospheric temperature"))
        self.kw_atmVapor_ck.setText(_translate("MainWindow", "Atmospheric water vapor"))
        self.kw_atmWinds_ck.setText(_translate("MainWindow", "Atmospheric winds"))
        self.kw_clouds_ck.setText(_translate("MainWindow", "Clouds"))
        self.kw_precipitation_ck.setText(_translate("MainWindow", "Precipitation"))
        self.kw_category_lb3.setText(_translate("MainWindow", "Biosphere:"))
        self.kw_ecoDynamics_ck.setText(_translate("MainWindow", "Ecological dynamics"))
        self.kw_terEcosystems_ck.setText(_translate("MainWindow", "Terrestrial ecosystems"))
        self.kw_vegetation_ck.setText(_translate("MainWindow", "Vegetation"))
        self.kw_category_lb4.setText(_translate("MainWindow", "Cryosphere:"))
        self.kw_frozenGround_ck.setText(_translate("MainWindow", "Frozen ground"))
        self.kw_glaciersIcesheet_ck.setText(_translate("MainWindow", "Glaciers / Ice sheet"))
        self.kw_seaIce_ck.setText(_translate("MainWindow", "Sea ice"))
        self.kw_snowIce_ck.setText(_translate("MainWindow", "Snow / Ice"))
        self.kw_category_lb5.setText(_translate("MainWindow", "Land Surface:"))
        self.kw_erosionSedimentation_ck.setText(_translate("MainWindow", "Erosion / Sedimentation"))
        self.kw_geomorphology_ck.setText(_translate("MainWindow", "Geomorphology"))
        self.kw_landTemperature_ck.setText(_translate("MainWindow", "Land temperature"))
        self.kw_landCover_ck.setText(_translate("MainWindow", "Land use / Land cover"))
        self.kw_landscape_ck.setText(_translate("MainWindow", "Landscape"))
        self.kw_surfaceProperties_ck.setText(_translate("MainWindow", "Surface radiative properties"))
        self.kw_topography_ck.setText(_translate("MainWindow", "Topography"))
        self.kw_category_lb6.setText(_translate("MainWindow", "Ocean:"))
        self.kw_bathymetry_ck.setText(_translate("MainWindow", "Bathymetry"))
        self.kw_coastalProcesses_ck.setText(_translate("MainWindow", "Coastal processes"))
        self.kw_marineEnvironment_ck.setText(_translate("MainWindow", "Marine environment"))
        self.kw_marineGeophysics_ck.setText(_translate("MainWindow", "Marine geophysics"))
        self.kw_oceanWaves_ck.setText(_translate("MainWindow", "Ocean waves"))
        self.kw_oceanWinds_ck.setText(_translate("MainWindow", "Ocean winds"))
        self.kw_seaTopography_ck.setText(_translate("MainWindow", "Sea surface topography"))
        self.kw_seaTides_ck.setText(_translate("MainWindow", "Tides"))
        self.kw_waterQuality_ck_2.setText(_translate("MainWindow", "Water quality"))
        self.kw_category_lb7.setText(_translate("MainWindow", "Solid Earth:"))
        self.kw_geodetics_ck.setText(_translate("MainWindow", "Geodetics"))
        self.kw_geomagnetism_ck.setText(_translate("MainWindow", "Geomagnetism"))
        self.kw_geomorphicLandforms_ck.setText(_translate("MainWindow", "Geomorphic landforms"))
        self.kw_gravity_ck.setText(_translate("MainWindow", "Gravity"))
        self.kw_category_lb10.setText(_translate("MainWindow", "Terrestrial Hydrosphere:"))
        self.kw_groundWater_ck.setText(_translate("MainWindow", "Ground water"))
        self.kw_surfaceWater_ck.setText(_translate("MainWindow", "Surface water"))
        self.kw_waterQuality_ck.setText(_translate("MainWindow", "Water quality / chemistry"))
        self.kw_solarFlux_ck.setText(_translate("MainWindow", "Solar energetic particle flux"))
        self.kw_ionosMagnetos_ck.setText(_translate("MainWindow", "Ionosphere / Magnetosphere"))
        self.kw_xRay_ck.setText(_translate("MainWindow", "X-ray"))
        self.kw_category_lb9.setText(_translate("MainWindow", "Sun-Earth Interactions:"))
        self.kw_solarActivity_ck.setText(_translate("MainWindow", "Solar activity"))
        self.kw_lidar_ck.setText(_translate("MainWindow", "LIDAR"))
        self.kw_radioWave_ck.setText(_translate("MainWindow", "Radio wave"))
        self.kw_radar_ck.setText(_translate("MainWindow", "RADAR"))
        self.kw_visWavelentghs_ck.setText(_translate("MainWindow", "Visible wavelengths"))
        self.kw_uvWavelentghs_ck.setText(_translate("MainWindow", "Ultraviolet wavelengths"))
        self.kw_irWavelengths_ck.setText(_translate("MainWindow", "Infrared wavelengths"))
        self.kw_microwave_ck.setText(_translate("MainWindow", "Microwave"))
        self.kw_gammaRay_ck.setText(_translate("MainWindow", "Gamma ray"))
        self.kw_category_lb8.setText(_translate("MainWindow", "Spectral / Engineering:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage3), _translate("MainWindow", "Keywords"))
        self.ai_label_1.setText(_translate("MainWindow", "Aircraft:"))
        self.ai_aircraft_rl1.setItemText(0, _translate("MainWindow", "Make a choice..."))
        self.ai_aircraft_rl1.setItemText(1, _translate("MainWindow", "Other..."))
        self.ai_aircraft_rl1.setItemText(2, _translate("MainWindow", "AWI - POLAR 5"))
        self.ai_aircraft_rl1.setItemText(3, _translate("MainWindow", "CNR - ERA Skyarrow"))
        self.ai_aircraft_rl1.setItemText(4, _translate("MainWindow", "CNR - Partenavia"))
        self.ai_aircraft_rl1.setItemText(5, _translate("MainWindow", "DLR - C 208"))
        self.ai_aircraft_rl1.setItemText(6, _translate("MainWindow", "DLR - DO 228 D-CFFU"))
        self.ai_aircraft_rl1.setItemText(7, _translate("MainWindow", "DLR - DO 228 D-CODE"))
        self.ai_aircraft_rl1.setItemText(8, _translate("MainWindow", "DLR - Falcon 20"))
        self.ai_aircraft_rl1.setItemText(9, _translate("MainWindow", "ENVISCOPE - Learjet 35"))
        self.ai_aircraft_rl1.setItemText(10, _translate("MainWindow", "ENVISCOPE - Partenavia"))
        self.ai_aircraft_rl1.setItemText(11, _translate("MainWindow", "FAAM - BAe 146"))
        self.ai_aircraft_rl1.setItemText(12, _translate("MainWindow", "FUB - C 207"))
        self.ai_aircraft_rl1.setItemText(13, _translate("MainWindow", "INTA - CASA 212 AR"))
        self.ai_aircraft_rl1.setItemText(14, _translate("MainWindow", "INTA - CASA 212 RS"))
        self.ai_aircraft_rl1.setItemText(15, _translate("MainWindow", "KIT - Enduro"))
        self.ai_aircraft_rl1.setItemText(16, _translate("MainWindow", "NERC - DO 228"))
        self.ai_aircraft_rl1.setItemText(17, _translate("MainWindow", "NERC - Twin Otter"))
        self.ai_aircraft_rl1.setItemText(18, _translate("MainWindow", "SAFIRE - ATR 42"))
        self.ai_aircraft_rl1.setItemText(19, _translate("MainWindow", "SAFIRE - Falcon 20"))
        self.ai_aircraft_rl1.setItemText(20, _translate("MainWindow", "SAFIRE - PIPER Aztec"))
        self.ai_aircraft_rl1.setItemText(21, _translate("MainWindow", "UEDIN - ECO Dimona"))
        self.ai_manufacturer_lb.setText(_translate("MainWindow", "Manufacturer:"))
        self.ai_type_lb.setText(_translate("MainWindow", "Aircraft type:"))
        self.ai_operator_lb.setText(_translate("MainWindow", "Operator:"))
        self.ai_country_lb.setText(_translate("MainWindow", "Country:"))
        self.ai_number_lb.setText(_translate("MainWindow", "Registration number:"))
        self.ai_label_13.setText(_translate("MainWindow", "Instrument:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage4), _translate("MainWindow", "Aircraft and Instruments"))
        self.gl_location_lb.setText(_translate("MainWindow", "Location:"))
        self.gl_category_rl1.setItemText(0, _translate("MainWindow", "Make a choice..."))
        self.gl_category_rl1.setItemText(1, _translate("MainWindow", "Continents"))
        self.gl_category_rl1.setItemText(2, _translate("MainWindow", "Countries"))
        self.gl_category_rl1.setItemText(3, _translate("MainWindow", "Oceans"))
        self.gl_category_rl1.setItemText(4, _translate("MainWindow", "Regions"))
        self.gl_label_1.setText(_translate("MainWindow", "Geographic bounding box:"))
        self.gl_resolution_lb.setText(_translate("MainWindow", "Spatial Resolution:"))
        self.gl_resolution_rl1.setItemText(0, _translate("MainWindow", "Scale"))
        self.gl_resolution_rl1.setItemText(1, _translate("MainWindow", "Distance"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage5), _translate("MainWindow", "Geographic Information"))
        self.tr_dateRevision_do2.setDisplayFormat(_translate("MainWindow", "yyyy-MM-dd"))
        self.tr_dateRevision_lb.setText(_translate("MainWindow", "Date of last revision:"))
        self.tr_dateCreation_do3.setDisplayFormat(_translate("MainWindow", "yyyy-MM-dd"))
        self.tr_dateCreation_lb.setText(_translate("MainWindow", "Date of creation:"))
        self.tr_period_lb.setText(_translate("MainWindow", "Temporal extent:"))
        self.label_7.setText(_translate("MainWindow", "Phase 1:"))
        self.tr_dateStart_do4.setDisplayFormat(_translate("MainWindow", "yyyy-MM-dd"))
        self.tr_dateEnd_do5.setDisplayFormat(_translate("MainWindow", "yyyy-MM-dd"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage6), _translate("MainWindow", "Temporal Reference"))
        self.qv_obsLab.setText(_translate("MainWindow", "Earth observation/Remote sensing data"))
        self.qv_insituLab.setText(_translate("MainWindow", "Atmospheric/In-situ data"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage7), _translate("MainWindow", "Quality and Validity"))
        self.au_conditions_lb.setText(_translate("MainWindow", "Conditions applying to access and use:"))
        self.au_conditions_ta.setPlainText(_translate("MainWindow", "As EUFAR is an EU-funded project, data in the EUFAR archive are available to everyone. All users are required to aknowledge the data providers in any publication based on EUFAR data."))
        self.au_limitations_lb.setText(_translate("MainWindow", "Limitations on public access:"))
        self.au_limitations_ta.setPlainText(_translate("MainWindow", "No limitations."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage8), _translate("MainWindow", "Access and Use Constraints"))
        self.ro_responsibleParty_lb.setText(_translate("MainWindow", "Responsible party:"))
        self.ro_responsibleEmail_lb.setText(_translate("MainWindow", "Responsible party e-mail:"))
        self.ro_label_3.setText(_translate("MainWindow", "Responsible party role:"))
        self.ro_responsibleRole_rl1.setItemText(0, _translate("MainWindow", "Author"))
        self.ro_responsibleRole_rl1.setItemText(1, _translate("MainWindow", "Custodian"))
        self.ro_responsibleRole_rl1.setItemText(2, _translate("MainWindow", "Distributor"))
        self.ro_responsibleRole_rl1.setItemText(3, _translate("MainWindow", "Originator"))
        self.ro_responsibleRole_rl1.setItemText(4, _translate("MainWindow", "Owner"))
        self.ro_responsibleRole_rl1.setItemText(5, _translate("MainWindow", "Point of Contact"))
        self.ro_responsibleRole_rl1.setItemText(6, _translate("MainWindow", "Principal Investigator"))
        self.ro_responsibleRole_rl1.setItemText(7, _translate("MainWindow", "Processor"))
        self.ro_responsibleRole_rl1.setItemText(8, _translate("MainWindow", "Publisher"))
        self.ro_responsibleRole_rl1.setItemText(9, _translate("MainWindow", "Resource Provider"))
        self.ro_responsibleRole_rl1.setItemText(10, _translate("MainWindow", "User"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage9), _translate("MainWindow", "Responsible Organisations"))
        self.mm_date_lb.setText(_translate("MainWindow", "Metadata date:"))
        self.mm_date_do1.setDisplayFormat(_translate("MainWindow", "yyyy-MM-dd"))
        self.mm_label_2.setText(_translate("MainWindow", "Metadata language:"))
        self.mm_language_rl1.setItemText(0, _translate("MainWindow", "Bulgarian"))
        self.mm_language_rl1.setItemText(1, _translate("MainWindow", "Czech"))
        self.mm_language_rl1.setItemText(2, _translate("MainWindow", "Danish"))
        self.mm_language_rl1.setItemText(3, _translate("MainWindow", "Dutch"))
        self.mm_language_rl1.setItemText(4, _translate("MainWindow", "English"))
        self.mm_language_rl1.setItemText(5, _translate("MainWindow", "Estonian"))
        self.mm_language_rl1.setItemText(6, _translate("MainWindow", "Finnish"))
        self.mm_language_rl1.setItemText(7, _translate("MainWindow", "French"))
        self.mm_language_rl1.setItemText(8, _translate("MainWindow", "German"))
        self.mm_language_rl1.setItemText(9, _translate("MainWindow", "Greek"))
        self.mm_language_rl1.setItemText(10, _translate("MainWindow", "Hungarian"))
        self.mm_language_rl1.setItemText(11, _translate("MainWindow", "Irish"))
        self.mm_language_rl1.setItemText(12, _translate("MainWindow", "Italian"))
        self.mm_language_rl1.setItemText(13, _translate("MainWindow", "Latvian"))
        self.mm_language_rl1.setItemText(14, _translate("MainWindow", "Lithuanian"))
        self.mm_language_rl1.setItemText(15, _translate("MainWindow", "Maltese"))
        self.mm_language_rl1.setItemText(16, _translate("MainWindow", "Polish"))
        self.mm_language_rl1.setItemText(17, _translate("MainWindow", "Portuguese"))
        self.mm_language_rl1.setItemText(18, _translate("MainWindow", "Romanian"))
        self.mm_language_rl1.setItemText(19, _translate("MainWindow", "Slovak"))
        self.mm_language_rl1.setItemText(20, _translate("MainWindow", "Slovenian"))
        self.mm_language_rl1.setItemText(21, _translate("MainWindow", "Spanish"))
        self.mm_language_rl1.setItemText(22, _translate("MainWindow", "Swedish"))
        self.mm_label_3.setText(_translate("MainWindow", "EMC XML file has been created by"))
        self.mm_contactName_lb.setText(_translate("MainWindow", "Name:"))
        self.mm_contactEmail_lb.setText(_translate("MainWindow", "E-mail:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage10), _translate("MainWindow", "Metadata on Metadata"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.actionNew.setText(_translate("MainWindow", "New..."))
        self.actionSave.setText(_translate("MainWindow", "Save..."))
        self.actionSave_As.setText(_translate("MainWindow", "Save As..."))
        self.actionOpen.setText(_translate("MainWindow", "Open..."))
        self.actionExit.setText(_translate("MainWindow", "Exit..."))
        self.actionExit.setIconText(_translate("MainWindow", "Exit"))
        self.actionEUFAR_CreatorAbout.setText(_translate("MainWindow", "EUFAR Metadata Creator..."))
        self.actionINSPIRE_Standard.setText(_translate("MainWindow", "INSPIRE XML Standard..."))
        self.actionEUFAR_N7SP.setText(_translate("MainWindow", "EUFAR N7SP..."))
        self.actionPreferences.setText(_translate("MainWindow", "Preferences"))
        self.actionChangelog.setText(_translate("MainWindow", "Changelog..."))
        self.actionMemory.setText(_translate("MainWindow", "Memory"))
        self.actionCPU.setText(_translate("MainWindow", "CPU"))
        self.actionObject.setText(_translate("MainWindow", "Object"))
        self.actionHelp.setText(_translate("MainWindow", "Help..."))

