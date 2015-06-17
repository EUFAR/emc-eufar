# -*- coding: utf-8 -*-

import webbrowser
import os, sys
import sqlite3 as lite
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import QObject
from PyQt4.QtGui import QLabel
from PyQt4.QtGui import QWidget
from PyQt4.QtGui import QDialog
from PyQt4.QtGui import QCheckBox
from PyQt4.QtGui import QMainWindow
from PyQt4.QtGui import QLineEdit
from PyQt4.QtGui import QListWidget
from PyQt4.QtGui import QPlainTextEdit
from PyQt4.QtGui import QComboBox
from PyQt4.QtGui import QDateEdit
from PyQt4.QtCore import QDate
from ui.Ui_fillwindow import Ui_fillWindow
from functions.sql_functions import sql_valueRead


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s


def fill_all_fields(self):
    self.fillInfo = False
    self.incompleteElements = []
    self.incorrectElements = []
    incompleteElements = 0
    incorrectElements = 0
    all_checks_cl = 0
    all_checks_kw = 0
    all_texts = 1
    all_lines = 1
    all_lists = 1
    all_boundaries = 0
    all_location = 1
    labels = self.findChildren(QLabel)
    for label in labels:
	label.setStyleSheet("color: black")
    all_check_boxes = self.findChildren(QCheckBox)
    for check_box in all_check_boxes:
	if check_box.objectName()[0:3] == "cl_" and check_box.isChecked():
	    all_checks_cl = 1
	elif check_box.objectName()[0:3] == "kw_" and check_box.isChecked():
	    all_checks_kw = 1
    if all_checks_cl == 0:
	self.cl_label_1.setStyleSheet("color: rgb(200,0,0)")
	self.incompleteElements.append("cl_label_1")
    if all_checks_kw == 0:
	for label in labels:
	    if label.objectName()[0:3] == "kw_":
		label.setStyleSheet("color: rgb(200,0,0)")
	self.incompleteElements.append("kw_category_lb1")
    all_plainText_edits = self.findChildren(QPlainTextEdit)
    for widget in all_plainText_edits:
	text = widget.toPlainText()
	if not text:
            if widget.objectName()[:12] != "au_wn_con_ta" and widget.objectName()[:12] != "au_wn_lim_ta":
                all_texts = 0
                self.findChildren(QLabel, widget.objectName()[:-2] + "lb")[0].setStyleSheet("color: rgb(200,0,0)")
                self.incompleteElements.append(widget.objectName())
    all_line_edits = self.findChildren(QLineEdit)
    # exception for spatial resolution which exist for hyperspectral data but not for some in-situ data
    for widget in all_line_edits:
	if widget.objectName() == "gl_resolution_ln" or widget.objectName() == "gl_unit_ln":
	    all_line_edits.remove(widget)
    for widget in all_line_edits:
	text = widget.text()
        if not text:
            if widget.objectName()[:10] != "ro_rlPy_ln" and widget.objectName()[:10] != "ro_rlEm_ln" and widget.objectName()[:13] != "mm_conName_ln" and widget.objectName()[:14] != "mm_conEmail_ln":
                all_lines = 0
                linked_labels = self.findChildren(QLabel, widget.objectName()[:-2] + "lb")
                if linked_labels:
                    linked_labels[0].setStyleSheet("color: rgb(200,0,0)")
                self.incompleteElements.append(widget.objectName())
    if "qv_unit_ln" in self.incompleteElements:
	self.qv_label_3.setStyleSheet("color: rgb(200,0,0)")
    if self.ai_aircraft_rl1.currentText() == "Do your choice ...":
	self.ai_label_1.setStyleSheet("color: rgb(200,0,0)")
	self.incompleteElements.append("ai_label_1")
    if self.findChildren(QComboBox, "ai_instrument_rl4"):
	if self.ai_instrument_rl3.count() == 0 or self.ai_instrument_rl3.currentText() == "Do your choice ..." or not self.ai_instrument_rl3.isEnabled():
	    self.ai_label_13.setStyleSheet("color: rgb(200,0,0)")
	    self.incompleteElements.append("ai_label_13")
    all_line_edits = self.findChildren(QLineEdit)
    for widget in all_line_edits:
	if "Bound" in widget.objectName():
	    text = widget.text()
	    if not text:
		all_boundaries = 1    
    if all_boundaries == 1:
	self.gl_label_1.setStyleSheet("color: rgb(200,0,0)")
    if self.gl_category_rl1.currentText() == "Do your choice ..." or self.gl_details_rl2.currentText() == "Do your choice ...":
	all_location = 0
	self.gl_location_lb.setStyleSheet("color: rgb(200,0,0)")
	self.incompleteElements.append("gl_location_lb")
    if all_checks_cl == 0 or all_checks_kw == 0 or all_texts == 0 or all_lines == 0 or all_lists == 0 or all_location == 0:  
	fillElements = []
	cur = self.db.cursor()
	for name in self.incompleteElements:
	    query = sql_valueRead(self, "elementsInformation", "Object", unicode(name))
	    fillElements.append([query[0][0], query[0][3], query[0][2]])
	fillElements = sorted(fillElements, key=lambda element: element[0])
	writeElements = "<font color=#C80000><b><u>Incomplete fields<\u></b></font>"
	item_bf = 0
	i = 0
	for item in fillElements:
	    if item[1] == item_bf:
		writeElements = writeElements + '<li>' + item[2] + '</li>'
	    else:
		if i != 0:
		    writeElements = writeElements + "</ul></blockquote>"
		writeElements = writeElements + '<blockquote>In "' + item[1] + '", check:<ul><li>' + item[2] + '</li>'
		item_bf = item[1]
	    i += 1
	writeElements = writeElements + "</blockquote><br>"
	incompleteElements = 1

    all_lines = 1
    all_texts = 1
    all_dates = 1
    all_boundaries = 0
    all_date_edits = self.findChildren(QDateEdit)
    for widget in all_date_edits:
        if widget.objectName() == "tr_dateStart_do4" or widget.objectName() == "tr_dateEnd_do5" or widget.objectName()[:9] == "tr_dtSt_1" or widget.objectName()[:9] == "tr_dtEd_1":
            if widget.date() > QDate.currentDate():
                all_dates = 0
                self.tr_period_lb.setStyleSheet("color: rgb(0,0,200)")
                if widget.objectName() == "tr_dateStart_do4" or widget.objectName() == "tr_dateEnd_do5":
                    self.label_7.setStyleSheet("color: rgb(0,0,200)")
                    if "tr_temporal_extent" not in self.incorrectElements:
                        self.incorrectElements.append("tr_temporal_extent")
                elif widget.objectName()[:9] == "tr_dtSt_1" or widget.objectName()[:9] == "tr_dtEd_1":
                    self.tr_lab_1[int(widget.objectName()[-1:])].setStyleSheet("color: rgb(0,0,200)")
                    if ("tr_phase_" + widget.objectName()[-1:]) not in self.incorrectElements:
                        self.incorrectElements.append("tr_phase_" + widget.objectName()[-1:])
        else:
            if widget.date() > QDate.currentDate():
                all_dates = 0
                self.incorrectElements.append(widget.objectName()[:-1])
                linked_labels = self.findChildren(QLabel, widget.objectName()[:-3] + "lb")
                if linked_labels:
                    linked_labels[0].setStyleSheet("color: rgb(0,0,200)")
    all_line_edits = self.findChildren(QLineEdit)
    for widget in all_line_edits:
        if not widget.text() or widget.objectName() == "qt_spinbox_lineedit":
	    pass
	else:
	    type_test = ""
	    try:
		tmp = float(widget.text())
		type_test = "float"
	    except ValueError:
		type_test = "text"
	    try:
		tmp = int(widget.objectName()[-1:])
		query = sql_valueRead(self, "elementsInformation", "Object", unicode(widget.objectName()[:-1]))
	    except ValueError:
		query = sql_valueRead(self, "elementsInformation", "Object", unicode(widget.objectName()))
	    if query[0][4] != type_test:
		all_lines = 0
		self.incorrectElements.append(widget.objectName())
		linked_labels = self.findChildren(QLabel, widget.objectName()[:-2] + "lb")
		if linked_labels:
		    linked_labels[0].setStyleSheet("color: rgb(0,0,200)")
    for widget in all_line_edits:
	if not widget.text() or widget.objectName() == "qt_spinbox_lineedit":
	    pass
	else:
	    if "Bound" in widget.objectName():
		type_test = ""
		try:
		    tmp = float(widget.text())
		    type_test = "float"
		except ValueError:
		    type_test = "text"
		query = sql_valueRead(self, "elementsInformation", "Object", unicode(widget.objectName()))
		if query[0][4] != type_test:
		    all_boundaries = 1
    if all_boundaries == 1:
	self.gl_label_1.setStyleSheet("color: rgb(0,0,200)")
    all_plainText_edits = self.findChildren(QPlainTextEdit)
    for widget in all_plainText_edits:
	if not widget.toPlainText():
	    pass
	else:
	    type_test = ""
	    try:
		tmp = float(widget.toPlainText())
		type_test = "float"
	    except ValueError:
		type_test = "text"
	    try:
		tmp = int(widget.objectName()[-1:])
		query = sql_valueRead(self, "elementsInformation", "Object", unicode(widget.objectName()[:-1]))
	    except ValueError:
		query = sql_valueRead(self, "elementsInformation", "Object", unicode(widget.objectName()))
	    if query[0][4] != type_test:
		all_texts = 0
		self.incorrectElements.append(widget.objectName())
		linked_labels = self.findChildren(QLabel, widget.objectName()[:-2] + "lb")
		if linked_labels:
		    linked_labels[0].setStyleSheet("color: rgb(0,0,200)")
    if all_lines == 0 or all_texts == 0 or all_dates == 0:
	fillElements = []
	cur = self.db.cursor()
	for name in self.incorrectElements:
            if name[:9] == "tr_phase_":
                fillElements.append(["20." + name[-1:], "Temporal Reference", "Temporal extent - Phase " + str(int(name[-1:]) + 2)])
            else:
                try:
                    tmp = int(name[-1:])
                    query = sql_valueRead(self, "elementsInformation", "Object", unicode(name[:-1]))
                except ValueError:
                    query = sql_valueRead(self, "elementsInformation", "Object", unicode(name))
                fillElements.append([query[0][0], query[0][3], query[0][2]])
	fillElements = sorted(fillElements, key=lambda element: element[0])
	if "writeElements" in locals():
	    writeElements = writeElements + "<font color=#0000C8><b><u>Incorrect fields<\u></b></font>"
	else:
	    writeElements = "<font color=#0000C8><b><u>Incorrect fields<\u></b></font>"
	item_bf = 0
	i = 0
	for item in fillElements:
	    if item[1] == item_bf:
		writeElements = writeElements + '<li>' + item[2] + '</li>'
	    else:
		if i != 0:
		    writeElements = writeElements + "</ul></blockquote>"
		writeElements = writeElements + '<blockquote>In "' + item[1] + '", check:<ul><li>' + item[2] + '</li>'
		item_bf = item[1]
	    i += 1
	writeElements = writeElements + "</blockquote><br>"
	incorrectElements = 1
	
	
    if incompleteElements == 1 or incorrectElements == 1:
	self.fillInfo = True
	self.fillWindow = MyFill(writeElements)
	x1, y1, w1, h1 = self.geometry().getRect()
	x2, y2, w2, h2 = self.fillWindow.geometry().getRect()
	x2 = x1 + w1/2 - w2/2
	y2 = y1 + h1/2 - h2/2
	self.fillWindow.setGeometry(x2, y2, w2, h2)
	self.fillWindow.exec_()
	return self.fillWindow.cancel
    else:
        return False
	

class MyFill(QtGui.QDialog, Ui_fillWindow):
    def __init__(self, fillElements):
        QWidget.__init__(self)
        if getattr(sys, 'frozen', False):
	    self.progPath = sys._MEIPASS
	else:
	    self.progPath = os.path.abspath(".")
        self.setupUi(self)
        self.fw_okButton.clicked.connect(self.closeWindow)
        self.fw_detailButton.clicked.connect(self.detailElements_show)
        self.fw_cancelButton.clicked.connect(self.cancelWindow)
        self.incompleteElements = fillElements
        self.cancel = False
        self.fw_cancelButton.setFocus(True)

    
    def detailElements_show(self):
	self.fw_detailButton.setText("Hide details")
	self.fw_detailButton.clicked.disconnect(self.detailElements_show)
	self.fw_detailButton.clicked.connect(self.detailElements_hide)
	x1, y1, self.w, self.h = self.geometry().getRect()
	self.h1 = 400
	self.h2 = self.h1 - 186
	self.setMinimumHeight(self.h1)
	self.setMaximumHeight(self.h1)
	self.textBrowser = QtGui.QTextBrowser()
        font = QtGui.QFont()
        font.setPointSize(9)
        self.textBrowser.setFont(font)
        self.textBrowser.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser.setFrameShape(QtGui.QFrame.NoFrame)
        self.textBrowser.setAcceptRichText(True)
        self.textBrowser.setMinimumHeight(self.h2)
	self.textBrowser.setMaximumHeight(self.h2)
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.verticalLayout.addWidget(self.textBrowser)
        self.textBrowser.setText(self.incompleteElements)


    def detailElements_hide(self):
	self.fw_detailButton.setText("Show details")
	self.fw_detailButton.clicked.disconnect(self.detailElements_hide)
	self.fw_detailButton.clicked.connect(self.detailElements_show)
	self.textBrowser.clear()
	self.textBrowser.deleteLater()
	self.setMinimumHeight(self.h)
	self.setMaximumHeight(self.h)
	
    def cancelWindow(self):
        self.cancel = True
        self.close()

    def closeWindow(self):
	self.close()

