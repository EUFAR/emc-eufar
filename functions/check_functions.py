# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QCheckBox
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QPlainTextEdit
from PyQt5.QtWidgets import QDateEdit
from PyQt5.QtCore import QDate
from ui.Ui_fillwindow import Ui_fillWindow
from functions.sql_functions import sql_valueRead
import os


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
    all_quality = 1
    
    # preparing labels -> all black
    labels = self.findChildren(QLabel)
    for label in labels:
        label.setStyleSheet("color: black")
        
    # check: Classification and Keywords checkboxes
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
        
    # check : all QPlainTextEdit
    all_plainText_edits = self.findChildren(QPlainTextEdit)
    for widget in all_plainText_edits:
        text = widget.toPlainText()
        if not text:
            if widget.objectName()[:12] != "au_wn_con_ta" and widget.objectName()[:12] != "au_wn_lim_ta":
                all_texts = 0
                self.findChildren(QLabel, widget.objectName()[:-2] + "lb")[0].setStyleSheet("color:"
                    + " rgb(200,0,0)")
                self.incompleteElements.append(widget.objectName())
    
    # check: all QLine Edit
    all_line_edits = self.findChildren(QLineEdit)
    # exception for spatial resolution which exist for hyperspectral data but not for some in-situ data
    for widget in all_line_edits:
        if widget.objectName() == "gl_resolution_ln" or widget.objectName() == "gl_unit_ln":
            all_line_edits.remove(widget)
    for widget in all_line_edits:
        text = widget.text()
        if not text:
            if widget.objectName()[:10] != "ro_rlPy_ln" and widget.objectName()[:10] != "ro_rlEm_ln"and widget.objectName()[:13] != "mm_conName_ln" and widget.objectName()[:14] != "mm_conEmail_ln":
                all_lines = 0
                linked_labels = self.findChildren(QLabel, widget.objectName()[:-2] + "lb")
                if linked_labels:
                    linked_labels[0].setStyleSheet("color: rgb(200,0,0)")
                self.incompleteElements.append(widget.objectName())
    
    # check: for spatial resolution, if the distance is selected and something has been entered for 
    # the distance, the unit shouldn't be empty
    if self.gl_resolution_rl1.currentText() == 'Distance':
        if self.gl_unit_rl.currentText() == "Make a choice...":
            self.incompleteElements.append("qv_unit_ln")
            self.qv_label_3.setStyleSheet("color: rgb(200,0,0)")
    
    # check: aircraft selection
    if self.ai_aircraft_rl1.currentText() == "Make a choice...":
        self.ai_label_1.setStyleSheet("color: rgb(200,0,0)")
        self.incompleteElements.append("ai_label_1")
    elif self.ai_aircraft_rl1.currentText() == "Other...":
        if self.ai_country_rl.currentText() == "Make a choice...":
            self.ai_country_lb.setStyleSheet("color: rgb(200,0,0)")
            self.incompleteElements.append("ai_country_lb")
    
    # check: instrument selection
    if self.ai_instrument_rl1.currentText() == "Make a choice..." and len(self.instModel_list) == 0:
        self.ai_label_13.setStyleSheet("color: rgb(200,0,0)")
        self.incompleteElements.append("ai_label_13")
    
    # check: coordinates in Geographic Information
    all_line_edits = self.findChildren(QLineEdit)
    for widget in all_line_edits:
        if "Bound" in widget.objectName():
            text = widget.text()
            if not text:
                all_boundaries = 1    
    if all_boundaries == 1:
        self.gl_label_1.setStyleSheet("color: rgb(200,0,0)")
    
    # check: localisation selection
    if self.gl_category_rl1.currentText() == "Make a choice..." or self.gl_details_rl2.currentText() == "Make a choice...":
        all_location = 0
        self.gl_location_lb.setStyleSheet("color: rgb(200,0,0)")
        self.incompleteElements.append("gl_location_lb")
        
    # check: quality and validity radiobuttons, comboboxes
    if self.qv_obsRadio.isChecked() == False and self.qv_insituRadio.isChecked() == False:
        all_quality = 0
        self.qv_obsLab.setStyleSheet("color: rgb(200,0,0)")
        self.qv_insituLab.setStyleSheet("color: rgb(200,0,0)")
        self.incompleteElements.append("qv_insituLab")
    elif self.qv_obsRadio.isChecked() == False and self.qv_insituRadio.isChecked() == True:
        if self.qv_insituGeoUnit_rd1.isChecked() == False and self.qv_insituGeoUnit_rd2.isChecked() == False:
            all_quality = 0
            self.qv_insituGeoUnit.setStyleSheet("color: rgb(200,0,0)")
            self.incompleteElements.append("qv_insituGeoUni")
        if self.qv_insituOutFormat_rd1.isChecked() == False and self.qv_insituOutFormat_rd2.isChecked() == False and self.qv_insituOutFormat_rd3.isChecked() == False and self.qv_insituOutFormat_rd4.isChecked() == False:
            all_quality = 0
            self.qv_insituOutFormat.setStyleSheet("color: rgb(200,0,0)")
            self.incompleteElements.append("qv_insituOutFormat")
    elif self.qv_obsRadio.isChecked() == True and self.qv_insituRadio.isChecked() == False:
        if self.qv_obsProLvl_rl.currentText() == "Make a choice...":
            all_quality = 0
            self.qv_obsProLvl.setStyleSheet("color: rgb(200,0,0)")
            self.incompleteElements.append("qv_obsProLvl")
        if self.qv_obsDrkCur_rd1.isChecked() == False and self.qv_obsDrkCur_rd2.isChecked() == False:
            all_quality = 0
            self.qv_obsDrkCur.setStyleSheet("color: rgb(200,0,0)")
            self.incompleteElements.append("qv_obsDrkCur")
        if self.qv_obsIntMask_rd1.isChecked() == False and self.qv_obsIntMask_rd2.isChecked() == False:
            all_quality = 0
            self.qv_obsIntMask.setStyleSheet("color: rgb(200,0,0)")
            self.incompleteElements.append("qv_obsIntMask")
        if self.qv_obsBadMask_rd1.isChecked() == False and self.qv_obsBadMask_rd2.isChecked() == False:
            all_quality = 0
            self.qv_obsBadMask.setStyleSheet("color: rgb(200,0,0)")
            self.incompleteElements.append("qv_obsBadMask")
        if self.qv_obsSatPix_rd1.isChecked() == False and self.qv_obsSatPix_rd2.isChecked() == False:
            all_quality = 0
            self.qv_obsSatPix.setStyleSheet("color: rgb(200,0,0)")
            self.incompleteElements.append("qv_obsSatPix")
        if self.qv_obsSpeNeigh_rd1.isChecked() == False and self.qv_obsSpeNeigh_rd2.isChecked() == False:
            all_quality = 0
            self.qv_obsSpeNeigh.setStyleSheet("color: rgb(200,0,0)")
            self.incompleteElements.append("qv_obsSpeNeigh")
        if self.qv_obsPosInfo_rd1.isChecked() == False and self.qv_obsPosInfo_rd2.isChecked() == False:
            all_quality = 0
            self.qv_obsPosInfo.setStyleSheet("color: rgb(200,0,0)")
            self.incompleteElements.append("qv_obsPosInfo")
        if self.qv_obsAttInfo_rd1.isChecked() == False and self.qv_obsAttInfo_rd2.isChecked() == False:
            all_quality = 0
            self.qv_obsAttInfo.setStyleSheet("color: rgb(200,0,0)")
            self.incompleteElements.append("qv_obsAttInfo")
        if self.qv_obsSynProb_rd1.isChecked() == False and self.qv_obsSynProb_rd2.isChecked() == False:
            all_quality = 0
            self.qv_obsSynProb.setStyleSheet("color: rgb(200,0,0)")
            self.incompleteElements.append("qv_obsSynProb")
        if self.qv_obsIntGeo_rd1.isChecked() == False and self.qv_obsIntGeo_rd2.isChecked() == False:
            all_quality = 0
            self.qv_obsIntGeo.setStyleSheet("color: rgb(200,0,0)")
            self.incompleteElements.append("qv_obsIntGeo")
        if self.qv_obsAtmCorr_rd1.isChecked() == False and self.qv_obsAtmCorr_rd2.isChecked() == False:
            all_quality = 0
            self.qv_obsAtmCorr.setStyleSheet("color: rgb(200,0,0)")
            self.incompleteElements.append("qv_obsAtmCorr")
        if self.qv_obsCldMask_rd1.isChecked() == False and self.qv_obsCldMask_rd2.isChecked() == False:
            all_quality = 0
            self.qv_obsCldMask.setStyleSheet("color: rgb(200,0,0)")
            self.incompleteElements.append("qv_obsCldMask")
        if self.qv_obsShdMask_rd1.isChecked() == False and self.qv_obsShdMask_rd2.isChecked() == False:
            all_quality = 0
            self.qv_obsShdMask.setStyleSheet("color: rgb(200,0,0)")
            self.incompleteElements.append("qv_obsShdMask")
        if self.qv_obsHazMask_rd1.isChecked() == False and self.qv_obsHazMask_rd2.isChecked() == False:
            all_quality = 0
            self.qv_obsHazMask.setStyleSheet("color: rgb(200,0,0)")
            self.incompleteElements.append("qv_obsHazMask")
        if self.qv_obsDEMMea_rd1.isChecked() == False and self.qv_obsDEMMea_rd2.isChecked() == False:
            all_quality = 0
            self.qv_obsDEMMea.setStyleSheet("color: rgb(200,0,0)")
            self.incompleteElements.append("qv_obsDEMMea")
        if self.qv_obsIllAng_rd1.isChecked() == False and self.qv_obsIllAng_rd2.isChecked() == False:
            all_quality = 0
            self.qv_obsIllAng.setStyleSheet("color: rgb(200,0,0)")
            self.incompleteElements.append("qv_obsIllAng")
        if self.qv_obsBRDFGeo_rd1.isChecked() == False and self.qv_obsBRDFGeo_rd2.isChecked() == False:
            all_quality = 0
            self.qv_obsBRDFGeo.setStyleSheet("color: rgb(200,0,0)")
            self.incompleteElements.append("qv_obsBRDFGeo")
            
            
    # preparing report
    if all_checks_cl == 0 or all_checks_kw == 0 or all_texts == 0 or all_lines == 0 or all_lists == 0 or all_location == 0 or all_quality == 0:  
        fillElements = []
        cur = self.db.cursor()
        for name in self.incompleteElements:
            query = sql_valueRead(self, "elementsInformation", "Object", name)
            fillElements.append([query[0][0], query[0][3], query[0][2]])
        fillElements = sorted(fillElements, key=lambda element: element[0])
        writeElements = r"<font color=#C80000><b><u>Incomplete fields<\u></b></font>"
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
                query = sql_valueRead(self, "elementsInformation", "Object", widget.objectName()[:-1])
            except ValueError:
                query = sql_valueRead(self, "elementsInformation", "Object", widget.objectName())
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
                query = sql_valueRead(self, "elementsInformation", "Object", widget.objectName())
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
                query = sql_valueRead(self, "elementsInformation", "Object", widget.objectName()[:-1])
            except ValueError:
                query = sql_valueRead(self, "elementsInformation", "Object", widget.objectName())
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
                fillElements.append(["20." + name[-1:], "Temporal Reference", "Temporal extent - "
                                     + "Phase " + str(int(name[-1:]) + 2)])
            else:
                try:
                    tmp = int(name[-1:])
                    query = sql_valueRead(self, "elementsInformation", "Object", name[:-1])
                except ValueError:
                    query = sql_valueRead(self, "elementsInformation", "Object", name)
                fillElements.append([query[0][0], query[0][3], query[0][2]])
        fillElements = sorted(fillElements, key=lambda element: element[0])
        if "writeElements" in locals():
            writeElements = writeElements + r"<font color=#0000C8><b><u>Incorrect fields<\u></b></font>"
        else:
            writeElements = r"<font color=#0000C8><b><u>Incorrect fields<\u></b></font>"
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
        x2, y2, w2, h2 = self.fillWindow.geometry().getRect()  # @UnusedVariable
        self.fillWindow.setGeometry(x1 + w1/2 - w2/2, y1 + h1/2 - h2/2, w2, h2)
        self.fillWindow.exec_()
        return self.fillWindow.cancel
    else:
        return False


class MyFill(QtWidgets.QDialog, Ui_fillWindow):
    def __init__(self, fillElements):
        QWidget.__init__(self)
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
        x1, y1, self.w, self.h = self.geometry().getRect()  # @UnusedVariable
        if os.name == "nt":
            self.h1 = 450
            self.h2 = self.h1 - 236
        else:
            self.h1 = 400
            self.h2 = self.h1 - 186
        self.setMinimumHeight(self.h1+20)
        self.setMaximumHeight(self.h1+20)
        self.textBrowser = QtWidgets.QTextBrowser()
        font = QtGui.QFont()
        font.setPointSize(9)
        self.textBrowser.setFont(font)
        self.textBrowser.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser.setAcceptRichText(True)
        self.textBrowser.setMinimumHeight(self.h2)
        self.textBrowser.setMaximumHeight(self.h2)
        self.textBrowser.setObjectName("textBrowser")
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

