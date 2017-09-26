from PyQt5 import Qt, QtCore, QtWidgets, QtGui
from ui.Ui_fillwindow import Ui_fillWindow
import copy
import re
import logging


def fill_all_fields(self):
    logging.debug('check_functions.py - fill_all_fields')
    all_checks_cl = 0
    all_checks_kw = 0
    all_checks_qv = 1
    all_texts = 1
    all_lists = 1
    all_dates = 1
    all_aircraft = 1
    all_instrument = 1
    all_quality = 1
    
    # preparing all lists
    mandatory_line_edit_list = copy.copy(self.mandatory_line_edit_list)
    for sublist in self.qv_insitu_line_list:
        mandatory_line_edit_list += sublist
    for sublist in self.qv_imagery_line_list:
        mandatory_line_edit_list += sublist
    mandatory_area_edit_list = copy.copy(self.mandatory_area_edit_list)
    for sublist in self.qv_insitu_area_list:
        mandatory_area_edit_list += sublist
    mandatory_combobox_list = copy.copy(self.mandatory_combobox_list)
    for sublist in self.qv_imagery_combo_list:    
        mandatory_combobox_list += sublist
    for sublist in self.qv_insitu_combo_list:    
        mandatory_combobox_list += sublist
    mandatory_datebox_list = copy.copy(self.mandatory_datebox_list)
    for sublist in self.qv_imagery_date_list:
        mandatory_datebox_list += sublist
    mandatory_radio_list = []
    for sublist in self.qv_insitu_radio_list:
        mandatory_radio_list += sublist
    for sublist in self.qv_imagery_radio_list:
        mandatory_radio_list += sublist
        
    # preparing labels -> all black
    labels = self.findChildren(QtWidgets.QLabel)
    for label in labels:
        label.setStyleSheet("color: black")
        
    # preparing tab labels -> all black
    for i in range(self.tabWidget.count()):
        self.tabWidget.tabBar().setTabTextColor(i, QtGui.QColor(0,0,0))
    if self.qv_tabWidget.count() > 0:
        for i in range(self.qv_tabWidget.count()):
            self.qv_tabWidget.tabBar().setTabTextColor(i, QtGui.QColor(0,0,0))
        
    # check: Classification and Keywords checkboxes
    all_check_boxes = self.findChildren(QtWidgets.QCheckBox)
    for check_box in all_check_boxes:
        if check_box.objectName()[0:3] == "cl_" and check_box.isChecked():
            all_checks_cl = 1
        elif check_box.objectName()[0:3] == "kw_" and check_box.isChecked():
            all_checks_kw = 1
    if all_checks_cl == 0:
        self.tabWidget.tabBar().setTabTextColor(1, QtGui.QColor(200,0,0))
    if all_checks_kw == 0:
        self.tabWidget.tabBar().setTabTextColor(2, QtGui.QColor(200,0,0))
    
    # check : checkboxes in QV section:
    j = 0
    for i in range(self.qv_tabWidget.count()):
        if "Atmospheric" in self.qv_tabWidget.tabText(i):
            all_check_boxes = self.qv_tabWidget.widget(i).findChildren(QtWidgets.QCheckBox)
            checks_qv = 0
            for check_box in all_check_boxes:
                if check_box.isChecked():
                    checks_qv = 1
            if checks_qv == 0:
                self.qv_insitu_lab_6[j].setStyleSheet("color: rgb(200,0,0)")
                self.tabWidget.tabBar().setTabTextColor(6, QtGui.QColor(200,0,0))
                self.qv_tabWidget.tabBar().setTabTextColor(i, QtGui.QColor(200,0,0))
                all_checks_qv = 1
            j += 1
    
    # check : radiobuttons in QV section:
    for sublist in mandatory_radio_list:
        widget = sublist[0].checkedButton()
        if not widget:
            sublist[1].setStyleSheet("color: rgb(200,0,0)")
            self.tabWidget.tabBar().setTabTextColor(6, QtGui.QColor(200,0,0))
            self.qv_tabWidget.tabBar().setTabTextColor(sublist[2], QtGui.QColor(200,0,0))
    
    # check : all Text Areas
    for sublist in mandatory_area_edit_list:
        if not sublist[0].isHidden():
            if sublist[0].toPlainText() == "":
                if "qv_" in sublist[0].objectName():
                    all_texts = 0
                    sublist[1].setStyleSheet("color: rgb(200,0,0)")
                    self.tabWidget.tabBar().setTabTextColor(6, QtGui.QColor(200,0,0))
                    self.qv_tabWidget.tabBar().setTabTextColor(sublist[3], QtGui.QColor(200,0,0))
                else:
                    all_texts = 0
                    sublist[1].setStyleSheet("color: rgb(200,0,0)")
                    self.tabWidget.tabBar().setTabTextColor(sublist[3], QtGui.QColor(200,0,0))
            else:
                if "qv_" in sublist[0].objectName():
                    if not check_field_correct_area(sublist[0], sublist[2]):
                        all_texts = 0
                        sublist[1].setStyleSheet("color: rgb(0,0,200)")
                        if self.tabWidget.tabBar().tabTextColor(6).red() != 200:
                            self.tabWidget.tabBar().setTabTextColor(6, QtGui.QColor(0,0,200))
                        if self.qv_tabWidget.tabBar().tabTextColor(sublist[3]).red() != 200:
                            self.qv_tabWidget.tabBar().setTabTextColor(sublist[3], QtGui.QColor(0,0,200))
                else:
                    if not check_field_correct_area(sublist[0], sublist[2]):
                        all_texts = 0
                        sublist[1].setStyleSheet("color: rgb(0,0,200)")
                        if self.tabWidget.tabBar().tabTextColor(sublist[3]).red() != 200:
                            self.tabWidget.tabBar().setTabTextColor(sublist[3], QtGui.QColor(0,0,200))
    
    # check: all Line Edits
    for sublist in mandatory_line_edit_list:
        if not sublist[0].isHidden():
            if sublist[0].text() == "":
                if "ai_air" in sublist[0].objectName():
                    if not self.aircraft_list:
                        all_texts = 0
                        sublist[1].setStyleSheet("color: rgb(200,0,0)")
                        self.tabWidget.tabBar().setTabTextColor(sublist[3], QtGui.QColor(200,0,0))
                elif "ai_ins" in sublist[0].objectName():
                    if not self.instModel_list:
                        all_texts = 0
                        sublist[1].setStyleSheet("color: rgb(200,0,0)")
                        self.tabWidget.tabBar().setTabTextColor(sublist[3], QtGui.QColor(200,0,0))
                elif "qv_" in sublist[0].objectName():
                    all_texts = 0
                    sublist[1].setStyleSheet("color: rgb(200,0,0)")
                    self.tabWidget.tabBar().setTabTextColor(6, QtGui.QColor(200,0,0))
                    self.qv_tabWidget.tabBar().setTabTextColor(sublist[3], QtGui.QColor(200,0,0))
                    
                else:
                    all_texts = 0
                    sublist[1].setStyleSheet("color: rgb(200,0,0)")
                    self.tabWidget.tabBar().setTabTextColor(sublist[3], QtGui.QColor(200,0,0))
            else:
                if "ai_air" in sublist[0].objectName():
                    if not self.aircraft_list:
                        if not check_field_correct_line(sublist[0], sublist[2]):
                            all_texts = 0
                            sublist[1].setStyleSheet("color: rgb(0,0,200)")
                            if self.tabWidget.tabBar().tabTextColor(sublist[3]).red() != 200:
                                self.tabWidget.tabBar().setTabTextColor(sublist[3], QtGui.QColor(0,0,200))
                elif "ai_ins" in sublist[0].objectName():
                    if not self.instModel_list:
                        if not check_field_correct_line(sublist[0], sublist[2]):
                            all_texts = 0
                            sublist[1].setStyleSheet("color: rgb(0,0,200)")
                            if self.tabWidget.tabBar().tabTextColor(sublist[3]).red() != 200:
                                self.tabWidget.tabBar().setTabTextColor(sublist[3], QtGui.QColor(0,0,200))
                elif "qv_" in sublist[0].objectName():
                    if not check_field_correct_line(sublist[0], sublist[2]):
                        all_texts = 0
                        sublist[1].setStyleSheet("color: rgb(0,0,200)")
                        if self.tabWidget.tabBar().tabTextColor(6).red() != 200:
                            self.tabWidget.tabBar().setTabTextColor(6, QtGui.QColor(0,0,200))
                        if self.qv_tabWidget.tabBar().tabTextColor(sublist[3]).red() != 200:
                            self.qv_tabWidget.tabBar().setTabTextColor(sublist[3], QtGui.QColor(0,0,200))   
                else:
                    if not check_field_correct_line(sublist[0], sublist[2]):
                        all_texts = 0
                        sublist[1].setStyleSheet("color: rgb(0,0,200)")
                        if self.tabWidget.tabBar().tabTextColor(sublist[3]).red() != 200:
                            self.tabWidget.tabBar().setTabTextColor(sublist[3], QtGui.QColor(0,0,200))                    
    
    # check: all Comboboxes
    for sublist in mandatory_combobox_list:
        if not sublist[0].isHidden():
            if sublist[0].currentText() == "Make a choice...":
                if "ai_aircraft" in sublist[0].objectName():
                    if not self.aircraft_list:
                        all_lists = 1
                        sublist[1].setStyleSheet("color: rgb(200,0,0)")
                        self.tabWidget.tabBar().setTabTextColor(sublist[2], QtGui.QColor(200,0,0))
                elif "ai_instrument" in sublist[0].objectName():
                    if not self.instModel_list:
                        all_lists = 1
                        sublist[1].setStyleSheet("color: rgb(200,0,0)")
                        self.tabWidget.tabBar().setTabTextColor(sublist[2], QtGui.QColor(200,0,0))
                elif "ai_country" in sublist[0].objectName():
                    if not self.aircraft_list:
                        all_lists = 1
                        sublist[1].setStyleSheet("color: rgb(200,0,0)")
                        self.tabWidget.tabBar().setTabTextColor(sublist[2], QtGui.QColor(200,0,0))
                elif "qv_" in sublist[0].objectName():
                        all_lists = 1
                        sublist[1].setStyleSheet("color: rgb(200,0,0)")
                        self.tabWidget.tabBar().setTabTextColor(6, QtGui.QColor(200,0,0))
                        self.qv_tabWidget.tabBar().setTabTextColor(sublist[2], QtGui.QColor(200,0,0))   
                else :
                    all_lists = 1
                    sublist[1].setStyleSheet("color: rgb(200,0,0)")
                    self.tabWidget.tabBar().setTabTextColor(sublist[2], QtGui.QColor(200,0,0))
    
    # check: aircraft & instrument list
    if not self.aircraft_list :
        self.ai_aircraft_lb.setStyleSheet("color: rgb(200,0,0)")
        self.tabWidget.tabBar().setTabTextColor(3, QtGui.QColor(200,0,0))
        all_aircraft = 0
    if not self.instModel_list:
        self.ai_instrument_lb.setStyleSheet("color: rgb(200,0,0)")
        self.tabWidget.tabBar().setTabTextColor(3, QtGui.QColor(200,0,0))
        all_instrument = 0
    
    # check : all dateboxes
    current_date = QtCore.QDate.currentDate().toString(Qt.Qt.ISODate)
    for sublist in mandatory_datebox_list:
        if not sublist[0].isHidden():
            date = sublist[0].date().toString(Qt.Qt.ISODate)
            if date > current_date:
                if "qv_" in sublist[0].objectName():
                    all_dates = 0
                    if self.tabWidget.tabBar().tabTextColor(6).red() != 200:
                            self.tabWidget.tabBar().setTabTextColor(6, QtGui.QColor(0,0,200))
                    if self.qv_tabWidget.tabBar().tabTextColor(sublist[2]).red() != 200:
                        self.qv_tabWidget.tabBar().setTabTextColor(sublist[2], QtGui.QColor(0,0,200))   
                else :
                    all_dates = 0
                    sublist[1].setStyleSheet("color: rgb(0,0,200)")
                    if self.tabWidget.tabBar().tabTextColor(sublist[2]).red() != 200:
                        self.tabWidget.tabBar().setTabTextColor(sublist[2], QtGui.QColor(0,0,200))  
    
    # check QV section : no tab
    if self.qv_insitu == 0 and self.qv_imagery == 0:
        all_quality = 0
        self.tabWidget.tabBar().setTabTextColor(6, QtGui.QColor(200,0,0))
        
    # if a field is wrong -> message
    if (all_checks_cl == 0 or all_checks_kw == 0 or all_checks_qv == 0 or all_texts == 0 or all_lists == 0
        or all_quality == 0 or all_aircraft == 0 or all_instrument == 0 or all_dates == 0):  
        self.fillWindow = MyFill()
        x1, y1, w1, h1 = self.geometry().getRect()
        _, _, w2, h2 = self.fillWindow.geometry().getRect()
        self.fillWindow.setGeometry(x1 + w1/2 - w2/2, y1 + h1/2 - h2/2, w2, h2)
        self.fillWindow.setMinimumSize(QtCore.QSize(450, self.fillWindow.sizeHint().height()))
        self.fillWindow.setMaximumSize(QtCore.QSize(450, self.fillWindow.sizeHint().height()))
        self.fillWindow.exec_()
        return self.fillWindow.cancel
    else:
        return False

def check_field_correct_line(widget, field_format):
    logging.debug('check_functions.py - check_field_correct_line')
    result = True
    if field_format == "text":
        try:
            float(widget.text())
            result = False
        except ValueError:
            result = True
    elif field_format == "float":
        try:
            float(widget.text())
            result = True
        except ValueError:
            result = False
    elif field_format == "email":
        if not re.match(r'^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$', widget.text()):
            result = False
    return result

def check_field_correct_area(widget, field_format):
    logging.debug('check_functions.py - check_field_correct_area')
    result = True
    if field_format == "text":
        try:
            float(widget.toPlainText())
            result = False
        except ValueError:
            result = True
    elif field_format == "float":
        try:
            float(widget.toPlainText())
            result = True
        except ValueError:
            result = False
    elif field_format == "email":
        if not re.match(r'^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$', widget.toPlainText()):
            result = False
    return result


class MyFill(QtWidgets.QDialog, Ui_fillWindow):
    def __init__(self):
        logging.debug('check_functions.py - MyFill - __init__')
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.fw_okButton.clicked.connect(self.closeWindow)
        self.fw_cancelButton.clicked.connect(self.cancelWindow)
        self.cancel = False
        self.fw_cancelButton.setFocus(True)

    def cancelWindow(self):
        logging.debug('check_functions.py - MyFill - cancelWindow')
        self.cancel = True
        self.close()

    def closeWindow(self):
        logging.debug('check_functions.py - MyFill - closeWindow')
        self.close()
