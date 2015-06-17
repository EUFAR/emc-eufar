# -*- coding: utf-8 -*-

import webbrowser
import datetime
import os, sys
import sqlite3 as lite
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import Qt
from PyQt4.QtCore import QDate
from PyQt4.QtCore import QObject
from PyQt4.QtCore import SIGNAL
from PyQt4.QtCore import QString
from PyQt4.QtCore import pyqtSignature
from PyQt4.QtGui import QCheckBox
from PyQt4.QtGui import QToolButton
from PyQt4.QtGui import QPushButton
from PyQt4.QtGui import QRadioButton
from PyQt4.QtGui import QMainWindow
from PyQt4.QtGui import QFileDialog
from PyQt4.QtGui import QInputDialog
from PyQt4.QtGui import QLabel
from PyQt4.QtGui import QLineEdit
from PyQt4.QtGui import QListWidget
from PyQt4.QtGui import QTextEdit, QPlainTextEdit
from PyQt4.QtGui import QComboBox
from PyQt4.QtGui import QDateEdit
from PyQt4.QtGui import QCompleter
from PyQt4.QtGui import QMessageBox
from PyQt4.QtGui import QWidget
from PyQt4.QtGui import QCursor
from Ui_mainwindow import Ui_MainWindow
from Ui_logwindow import Ui_Changelog
from Ui_fillwindow import Ui_fillWindow
from Ui_aboutwindow import Ui_aboutWindow
from Ui_presavewindow import Ui_presaveWindow
from Ui_infowindow import Ui_infoWindow
from _version import _version
from _version import _xml_version
from _version import _inspire_version
from eufar_metadata_xml import create_eufar_xml
from eufar_metadata_xml import read_eufar_xml
from functions import button_functions
from functions.button_functions import gl_rolebox_changed
from functions.button_functions import ai_aircraftRolebox_changed
from functions.button_functions import ai_instrumentRolebox_changed
from functions.button_functions import ai_instrumentDomain_changed
#from functions.button_functions import gl_referenceRolebox_changed
from functions.button_functions import gl_categoryRolebox_changed
from functions.sql_functions import objectsInit
from functions.sql_functions import sql_valueRead
from functions.check_functions import fill_all_fields

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
	if getattr(sys, 'frozen', False):
	    self.progPath = sys._MEIPASS
	else:
	    self.progPath = os.path.abspath(".")
	self.db = lite.connect(self.progPath + '/sqlite/emc_database.db')
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        objectsInit(self)
        all_date_edits = self.findChildren(QDateEdit)
	for widget in all_date_edits:
	    widget.setDate(QDate.currentDate())
        all_check_boxes = self.findChildren(QCheckBox)
        for check_box in all_check_boxes:
            QObject.connect(check_box, SIGNAL("stateChanged(int)"), self.set_modified)
        all_text_edits = self.findChildren(QPlainTextEdit)
        for widget in all_text_edits:
            QObject.connect(widget, SIGNAL("textChanged()"), self.set_modified)
        all_line_edits = self.findChildren(QLineEdit)
        for widget in all_line_edits:
            QObject.connect(widget, SIGNAL("textChanged(QString)"), self.set_modified)
	all_rolbox_edits = self.findChildren(QComboBox)
	for widget in all_rolbox_edits:
	    QObject.connect(widget, SIGNAL("activated(QString)"), self.set_modified)
        all_date_edits = self.findChildren(QDateEdit)
        for widget in all_date_edits:
	    QObject.connect(widget, SIGNAL("dateChanged(QDate)"), self.set_modified)
	all_info_boxes = self.findChildren(QToolButton)
	for widget in all_info_boxes:
	    QObject.connect(widget, SIGNAL("clicked()"), self.button_clicked) 
	QObject.connect(self.gl_resolution_rl1, SIGNAL("activated(QString)"), self.rolebox_changed)
	QObject.connect(self.ai_aircraft_rl1, SIGNAL("activated(QString)"), self.image_changed)	
	all_radio_buttons = self.findChildren(QRadioButton)
	for widget in all_radio_buttons:
	    QObject.connect(widget, SIGNAL("clicked()"), self.domain_clicked)
	#QObject.connect(self.ai_instrument_rl1, SIGNAL("activated(QString)"), self.instrument_changed)
	#QObject.connect(self.ai_instrument_rl2, SIGNAL("activated(QString)"), self.instrument_changed)
	#if self.findChildren(QComboBox, "ai_instrument_rl4"):
	    #QObject.connect(self.ai_instrument_rl4, SIGNAL("activated(QString)"), self.instrument_changed)
	#QObject.connect(self.gl_system_rl1, SIGNAL("activated(QString)"), self.reference_changed)
	QObject.connect(self.gl_category_rl1, SIGNAL("activated(QString)"), self.category_changed)
        self.make_window_title()
        self.setWindowIcon(QtGui.QIcon(self.progPath + "/icons/emc_icon.png"))


    @pyqtSignature("")
    def on_generateXMLButton_clicked(self):
        self.save_document()


    @pyqtSignature("")
    def on_exitButton_clicked(self):
        self.close()


    @pyqtSignature("")
    def on_actionNew_triggered(self):
        if self.modified:
            result = self.make_onsave_msg_box("Clear","new_icon.png")
            if result == "iw_saveButton":
                self.save_document()
		self.reset_all_fields()
		labels = self.findChildren(QLabel)
                for label in labels:
                    label.setStyleSheet("color: black")
            elif result == "iw_nosaveButton":
                self.reset_all_fields()
        else:
            self.reset_all_fields()


    @pyqtSignature("")
    def on_actionSave_triggered(self):
        self.save_document()


    #@pyqtSignature("")
    #def on_actionMemory_triggered(self):
        #import psutil
	#process = psutil.Process(os.getpid())
	#mem = process.get_memory_info()[0] / float(2 ** 20)
	#memBox = QMessageBox()
        #memBox.about(self, "Memory use","The programme is currently using " + str(mem) + "MB of memory.")


    #@pyqtSignature("")
    #def on_actionCPU_triggered(self):
        #import psutil
	#process = psutil.Process(os.getpid())
	#mem = process.get_cpu_percent(interval=1)
	#memBox = QMessageBox()
        #memBox.about(self, "CPU use","The programme is currently using " + str(mem) + "% of all CPUs.")

    
    #@pyqtSignature("")
    #def on_actionObject_triggered(self):
	#(new_item, response) = QInputDialog.getText(self, "Debug",  "Enter the object's name", text=QString(),)
	#if new_item and response:
	    #print " "
	    #print new_item, ":"
	    #currentObject = getattr(self, str(new_item))
	    #print dir(currentObject)
	    #print type(currentObject)
	    #try:
		#print len(currentObject)
	    #except TypeError:
		#print "this object does not have a len() attribute"
	    #print currentObject
    

    @pyqtSignature("")
    def on_actionSave_As_triggered(self):
        self.save_document(save_as=True)


    @pyqtSignature("")
    def on_actionOpen_triggered(self):
        if self.modified:
            result = self.make_onsave_msg_box("Open","open_icon.png")
            if result == "iw_saveButton":
                self.save_document()
	    elif result == "iw_nosaveButton":
                self.open_file()
        else:
            self.open_file()


    @pyqtSignature("")
    def on_actionExit_triggered(self):
	self.close()


    @pyqtSignature("")
    def on_actionEUFAR_CreatorAbout_triggered(self):
	aboutText = "<html><head/><body><p align=justify>This is the EUFAR Metadata Creator V%s. It was developed by EUFAR using Python and PyQT. The goal of the EUFAR Metadata Creator is to produce metadata to facilitate data storage and searches for Airborne Scientific Campaigns. XML files generated by this version conform to V%s of the INSPIRE metadata and XML Standard.</p><p>For any questions, more information, or to submit a bug report, please contact <a href=\"mailto:xxxxxxxxxxxx@xxxxxxx\"><span style=\" text-decoration: underline; color:#0000ff;\">xxxxxxxxxxxxxxxxxxxxx</span></a>.</p><p>The latest version and source code of the EUFAR Metadata Creator can be found at <a href=https://github.com/eufarn7sp/emc-eufar-java><span style=\" text-decoration: underline; color:#0000ff;\">https://github.com/eufarn7sp/emc-eufar-java</a></p></body></html>" % (_version, _inspire_version)
	self.aboutWindow = MyAbout(aboutText)
	x1, y1, w1, h1 = self.geometry().getRect()
	x2, y2, w2, h2 = self.aboutWindow.geometry().getRect()
	x2 = x1 + w1/2 - w2/2
	y2 = y1 + h1/2 - h2/2
	self.aboutWindow.setGeometry(x2, y2, w2, h2)
	resolution = QtGui.QDesktopWidget().screenGeometry()
	var = 1050 / resolution.height()
        self.aboutWindow.setMinimumSize(QtCore.QSize(450, self.aboutWindow.sizeHint().height()))
        self.aboutWindow.setMaximumSize(QtCore.QSize(452, self.aboutWindow.sizeHint().height()))
        self.aboutWindow.exec_()


    @pyqtSignature("")
    def on_actionINSPIRE_Standard_triggered(self):
	webbrowser.open('http://inspire.ec.europa.eu/')
	
	
    @pyqtSignature("")
    def on_actionEUFAR_N7SP_triggered(self):
	webbrowser.open('http://www.eufar.net/')
	

    @pyqtSignature("")
    def on_actionChangelog_triggered(self):
        self.logWindow = MyLog()
        x1, y1, w1, h1 = self.geometry().getRect()
        x2, y2, w2, h2 = self.logWindow.geometry().getRect()
        x2 = x1 + w1/2 - w2/2
        y2 = y1 + h1/2 - h2/2
        self.logWindow.setGeometry(x2, y2, w2, h2)
        self.logWindow.exec_()
  

    def closeEvent(self, event):
        if self.modified:
            result = self.make_onsave_msg_box("Close", "exit_icon.png")
            if result == "iw_saveButton":
                self.save_document()
                print 'closing EUFAR Metadata Creator V{0} ...'.format(_version)
                self.db.close()
                event.accept()
            elif result == "iw_nosaveButton":
		print 'closing EUFAR Metadata Creator V{0} ...'.format(_version)
		self.db.close()
		event.accept()
            else:
                event.ignore()
        else:
	    print 'closing EUFAR Metadata Creator V{0} ...'.format(_version)
	    self.db.close()
            self.close()


    def make_window_title(self):
        if self.saved:
            if len(self.out_file_name) > 40:
                out_file_name = "..." + self.out_file_name[30:]
            title_string = "EUFAR Metadata Creator V{0} - ".format(_version) + out_file_name
        else:
            title_string = "EUFAR Metadata Creator V{0} - unsaved".format(_version)
        if self.modified:
            title_string += ' - modified'
        self.setWindowTitle(title_string)


    def set_modified(self):
        if not self.modified:
            self.modified = True
            self.make_window_title()


    def save_document(self, save_as=False):
	cancel = fill_all_fields(self)
	if cancel == True:
            return
	if not self.out_file_name or save_as or self.fillInfo:
	    self.out_file_name = self.get_file_name()
	    if not self.out_file_name:
		return
	    if '.xml' not in self.out_file_name:
		self.out_file_name = self.out_file_name + '.xml'
	create_eufar_xml(self, self.out_file_name)
	self.make_window_title()
	
	
    def get_file_name(self):
        file_dialog = QFileDialog()
        file_dialog.setDefaultSuffix('xml')
        out_file_name = unicode(file_dialog.getSaveFileName(self, "Save XML File", filter='XML Files (*.xml)'))
        return out_file_name


    def reset_all_fields(self):
	if self.au_wn_con_ta:
	    length = len(self.au_wn_con_ta)
	    for item in range(0, length):
		button_functions.delButton_5_clicked(self)
        if self.au_wn_lim_ta:
	    length = len(self.au_wn_lim_ta)
	    for item in range(0, length):
		button_functions.delButton_6_clicked(self)	
        if self.mm_lab_1:
	    length = len(self.mm_lab_1)
	    for item in range(0, length):
		button_functions.delButton_7_clicked(self)	
        if self.tr_lab_1:
	    length = len(self.tr_lab_1)
	    for item in range(0, length):
		button_functions.delButton_3_clicked(self)	
	if self.ro_lab_1:
	    length = len(self.ro_lab_1)
	    for item in range(0, length):
		button_functions.delButton_8_clicked(self)
	all_date_edits = self.findChildren(QDateEdit)
	for widget in all_date_edits:
	    widget.setDate(QDate.currentDate())
        all_check_boxes = self.findChildren(QCheckBox)
        for check_box in all_check_boxes:
            check_box.setCheckState(False)
        all_plainText_edits = self.findChildren(QPlainTextEdit)
        for widget in all_plainText_edits:
	    widget.clear()
        all_line_edits = self.findChildren(QLineEdit)
        for widget in all_line_edits:
            widget.clear()
	all_rolbox_edits = self.findChildren(QComboBox)
	for widget in all_rolbox_edits:
	    widget.setCurrentIndex(0)
	gl_rolebox_changed(self)
	gl_categoryRolebox_changed(self)
	ai_aircraftRolebox_changed(self)
	all_list_edits = self.findChildren(QListWidget)
	for widget in all_list_edits:
	    widget.clear()
	self.id_resourceLang_rl2.setCurrentIndex(4)
	self.mm_language_rl1.setCurrentIndex(4)
	self.ro_responsibleRole_rl1.setCurrentIndex(4)
	self.ai_label_7.clear()
	self.ai_label_8.clear()
	self.ai_label_9.clear()
	self.ai_label_10.clear()
	self.ai_label_11.clear()
	self.ai_label_12.clear()
	self.gl_roleBox = 0
        self.out_file_name = None
        self.modified = False
        self.saved = False
        self.make_window_title()


    def make_onsave_msg_box(self, string, iconName):
	self.presaveWindow = MyWarning(string, iconName)
	x1, y1, w1, h1 = self.geometry().getRect()
	x2, y2, w2, h2 = self.presaveWindow.geometry().getRect()
	x2 = x1 + w1/2 - w2/2
	y2 = y1 + h1/2 - h2/2
	self.presaveWindow.setGeometry(x2, y2, w2, h2)
	resolution = QtGui.QDesktopWidget().screenGeometry()
	var = 1050 / resolution.height()
	self.presaveWindow.setMinimumSize(QtCore.QSize(450, self.presaveWindow.sizeHint().height()))
        self.presaveWindow.setMaximumSize(QtCore.QSize(452, self.presaveWindow.sizeHint().height()))
        self.presaveWindow.exec_()
	return self.presaveWindow.buttonName


    def open_file(self):
        (out_file_name, filter) = QFileDialog.getOpenFileNameAndFilter(self, "Open XML File", filter="XML Files (*.xml)")
        out_file_name = unicode(out_file_name)
        if out_file_name:
	    self.reset_all_fields()
            read_eufar_xml(self, out_file_name)
            self.saved = True
            self.modified = False
            self.out_file_name = out_file_name
            self.make_window_title()

	
    def button_clicked(self):
	if "infoButton" in self.sender().objectName():
	    if len(self.sender().objectName()) == 12:
		count_end=-2
	    else:
		count_end=-3
	    getattr(button_functions, str(self.sender().objectName()[:count_end] + "_clicked"))(self, self.sender().objectName())
	else:
	    if "kw_plsBut" in self.sender().objectName():
		getattr(button_functions, str(self.sender().objectName()[0:11] + "_clicked"))(self)
		
	    elif "kw_delBut" in self.sender().objectName():
		getattr(button_functions, str(self.sender().objectName()[0:11] + "_clicked"))(self)

	    else:
		getattr(button_functions, str(self.sender().objectName() + "_clicked"))(self)


    def rolebox_changed(self):
	gl_rolebox_changed(self)
	
	
    def image_changed(self):
	ai_aircraftRolebox_changed(self)


    def instrument_changed(self):
	ai_instrumentRolebox_changed(self)


    #def reference_changed(self):
	#gl_referenceRolebox_changed(self)


    def category_changed(self):
	gl_categoryRolebox_changed(self)


    def domain_clicked(self):
	ai_instrumentDomain_changed(self)
	

class MyLog(QtGui.QDialog, Ui_Changelog):
    def __init__(self):
        QWidget.__init__(self)
        if getattr(sys, 'frozen', False):
	    self.progPath = sys._MEIPASS
	else:
	    self.progPath = os.path.abspath(".")
        self.setupUi(self)
        self.log_txBrower.setPlainText(open(self.progPath + "/" + "Documentation/changelog.txt").read())
        self.lg_okButton.clicked.connect(self.closeWindow)
        self.lg_okButton.setFocus(True)

    def closeWindow(self):
	self.close()


class MyAbout(QtGui.QDialog, Ui_aboutWindow):
    def __init__(self, aboutText):
        QWidget.__init__(self)
        if getattr(sys, 'frozen', False):
	    self.progPath = sys._MEIPASS
	else:
	    self.progPath = os.path.abspath(".")
        self.setupUi(self)
        self.aw_label_1.setText(aboutText)
        self.aw_okButton.clicked.connect(self.closeWindow)
        self.aw_okButton.setFocus(True)

    def closeWindow(self):
	self.close()


class MyWarning(QtGui.QDialog, Ui_presaveWindow):
    def __init__(self, string, iconName):
        QWidget.__init__(self)
        if getattr(sys, 'frozen', False):
	    self.progPath = sys._MEIPASS
	else:
	    self.progPath = os.path.abspath(".")
        self.setupUi(self)
        self.iw_cancelButton.setFocus(True)
        all_buttons = self.findChildren(QPushButton)
	for widget in all_buttons:
	    QObject.connect(widget, SIGNAL("clicked()"), self.closeWindow) 
        self.iw_nosaveButton.setText(string + " without saving")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(self.progPath + "/icons/" + iconName)), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.iw_nosaveButton.setIcon(icon)

    def closeWindow(self):
	self.buttonName = self.sender().objectName()
	self.close()
