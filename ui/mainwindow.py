# -*- coding: utf-8 -*-

import webbrowser
import sqlite3 as lite
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import QDate
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QCheckBox, QLabel
from PyQt5.QtWidgets import QToolButton
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QListWidget
from PyQt5.QtWidgets import QPlainTextEdit
from PyQt5.QtWidgets import QComboBox
from PyQt5.QtWidgets import QDateEdit
from PyQt5.QtWidgets import QWidget
from .Ui_mainwindow import Ui_MainWindow
from .Ui_logwindow import Ui_Changelog
from .Ui_aboutwindow import Ui_aboutWindow
from .Ui_inspirewindow import Ui_inspireWindow
from .Ui_presavewindow import Ui_presaveWindow
from ._version import _version, _py_version, _qt_version, _inspire_version
from functions.eufar_metadata_xml import create_eufar_xml
from functions.eufar_metadata_xml import read_eufar_xml
from functions.eufar_metadata_xml import save_statement_observation
from functions.eufar_metadata_xml import save_statement_insitu
from functions.eufar_metadata_xml import read_statement_observation
from functions.eufar_metadata_xml import read_statement_insitu
from functions import button_functions
from functions.button_functions import gl_rolebox_changed
from functions.button_functions import ai_aircraftRolebox_changed
from functions.button_functions import gl_categoryRolebox_changed
from functions.button_functions import ai_instrument_changed
from functions.button_functions import qv_domain_changed
from functions.button_functions import qv_output_other
from functions.sql_functions import objectsInit
from functions.check_functions import fill_all_fields
from PyQt5.Qt import Qt


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        self.db = lite.connect('sqlite/emc_database.db')  # @UndefinedVariable
        QMainWindow.__init__(self, parent)
        self.tabLayout = 0
        self.setupUi(self)
        objectsInit(self)
        all_date_edits = self.findChildren(QDateEdit)
        for widget in all_date_edits:
            widget.setDate(QDate.currentDate())
        all_check_boxes = self.findChildren(QCheckBox)
        for check_box in all_check_boxes:
            check_box.stateChanged.connect(lambda: self.set_modified())
        all_text_edits = self.findChildren(QPlainTextEdit)
        for widget in all_text_edits:
            widget.textChanged.connect(lambda: self.set_modified())
        all_line_edits = self.findChildren(QLineEdit)
        for widget in all_line_edits:
            widget.textChanged.connect(lambda: self.set_modified())
        all_rolbox_edits = self.findChildren(QComboBox)
        for widget in all_rolbox_edits:
            widget.activated.connect(lambda: self.set_modified())
        all_date_edits = self.findChildren(QDateEdit)
        for widget in all_date_edits:
            widget.dateChanged.connect(lambda: self.set_modified())
        all_info_boxes = self.findChildren(QToolButton)
        for widget in all_info_boxes:
            widget.clicked.connect(lambda: self.button_clicked())
        self.ai_aircraft_rl1.activated.connect(lambda: self.image_changed())
        self.gl_category_rl1.activated.connect(lambda: self.category_changed())
        self.gl_resolution_rl1.activated.connect(lambda: self.rolebox_changed())
        self.ai_instrument_rl1.activated.connect(lambda: self.instrument_changed())
        self.qv_obsRadio.clicked.connect(lambda: self.quality_domain())
        self.qv_insituRadio.clicked.connect(lambda: self.quality_domain())
        self.make_window_title()
        

    @pyqtSlot()
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
    
    @pyqtSlot()
    def on_actionSave_triggered(self):
        self.save_document()

    @pyqtSlot()
    def on_actionSave_As_triggered(self):
        self.save_document(save_as=True)

    @pyqtSlot()
    def on_actionOpen_triggered(self):
        if self.modified:
            result = self.make_onsave_msg_box("Open","open_icon.png")
            if result == "iw_saveButton":
                self.save_document()
            elif result == "iw_nosaveButton":
                self.open_file()
        else:
            self.open_file()

    @pyqtSlot()
    def on_actionExit_triggered(self):
        self.close()

    @pyqtSlot()
    def on_actionEUFAR_CreatorAbout_triggered(self):
        aboutText = ("<html><head/><body><p align=justify>This is the EUFAR Metadata Creator V%s. I"
                     + "t was developed by EUFAR using Python %s and PyQT %s. The goal of the EUFAR Metad"
                     + "ata Creator is to produce metadata to facilitate data storage and searches "
                     + "for Airborne Scientific Campaigns. XML files generated by this version conf"
                     + "orm to V%s of the INSPIRE metadata and XML Standard.</p><p>For any question"
                     + "s, more information, or to submit a bug report, please contact <a href=\"ma"
                     + "ilto:olivier.henry.at.meteo.fr\"><span style=\" text-decoration: underline;"
                     + " color:#0000ff;\">olivier.henry.at.meteo.fr</span></a>.</p><p>The latest ve"
                     + "rsion and source code of the EUFAR Metadata Creator can be found at <a href"
                     + "=https://github.com/eufarn7sp/emc-eufar><span style=\" text-decoration"
                     + ": underline; color:#0000ff;\">https://github.com/eufarn7sp/emc-eufar</"
                     + "a></p></body></html>") % (_version, _py_version, _qt_version, _inspire_version)
        self.aboutWindow = MyAbout(aboutText)
        x1, y1, w1, h1 = self.geometry().getRect()
        x2, y2, w2, h2 = self.aboutWindow.geometry().getRect()  # @UnusedVariable
        self.aboutWindow.setGeometry(x1 + w1/2 - w2/2, y1 + h1/2 - h2/2, w2, h2)
        self.aboutWindow.setMinimumSize(QtCore.QSize(450, self.aboutWindow.sizeHint().height()))
        self.aboutWindow.setMaximumSize(QtCore.QSize(450, self.aboutWindow.sizeHint().height()))
        self.aboutWindow.exec_()

    @pyqtSlot()
    def on_actionINSPIRE_Standard_triggered(self):
        aboutText = ("<html><head/><body><p align=justify>INSPIRE is 'an European Union initiative "
                     + "to establish an infrastructure fo"
                     + "r spatial information in Europe that is geared to help to make spatial or g"
                     + "eographical information more accessible and interoperable for a wide range "
                     + "of purposes supporting sustainable development.'</p><p align=justify>The INSPIRE directiv"
                     + "e lays down a general framework for a Spatial Data Infrastructure (SDI) for"
                     + " the purposes of European Community environmental policies and policies or "
                     + "activities which may have an impact on the environment. The INSPIRE Directi"
                     + "ve entered into force on 15 May 2007.</p><p align=justify>INSPIRE is based on the infrast"
                     + "ructures for spatial information established and operated by the member sta"
                     + "tes of the European Union. The directive addresses 34 spatial data themes n"
                     + "eeded for environmental applications. To ensure that the spatial data infra"
                     + "structures of the member states are compatible and usable in a community an"
                     + "d transboundary context, the INSPIRE Directive requires that additional leg"
                     + "islation or common Implementing Rules (IR) are adopted for a number of spec"
                     + "ific areas (metadata, interoperability of spatial data sets and services, n"
                     + "etwork services, data and service sharing, monitoring and reporting). These"
                     + " are published either as Commission Regulations or as Decisions.</p><p align=justify>The "
                     + "Commission is assisted in the process of adopting such rules by a regulator"
                     + "y committee, INSPIRE Committee, composed of representatives of the member s"
                     + "tates and chaired by a representative of the Commission (this is known as t"
                     + "he Comitology procedure).</p><p align=justify>Wikipedia - Infrastructure for Spatial Info"
                     + "rmation in the European Community (<a href=https://en.wikipedia.org/wiki/In"
                     + "frastructure_for_Spatial_Information_in_the_European_Community target='_bla"
                     + "nk'><span style=\" text-decoration: underline; color:#0000ff;\">https://en."
                     + "wikipedia.org/wiki/Infrastructure_for_Spatial_Information_in_the_Eu ropean_"
                     + "Community</a>)</p><p>Link to the INSPIRE regulation: <a href=http://eur-lex"
                     + ".europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:32008R1205&from=EN target='_"
                     + "blank'><span style=\" text-decoration: underline; color:#0000ff;\">http://e"
                     + "ur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:32008R1205&from=EN</a>"
                     + "</p><p align=justify>Link to the INSPIRE website: <a href=http://inspire.ec.europa.eu/ind"
                     + "ex.cfm target='_blank'><span style=\" text-decoration: underline; color:#00"
                     + "00ff;\">http://inspire.ec.europa.eu/index.cfm</a></p></body></html>")
        self.inspireWindow = MyInspire(aboutText)
        x1, y1, w1, h1 = self.geometry().getRect()
        x2, y2, w2, h2 = self.inspireWindow.geometry().getRect()  # @UnusedVariable
        self.inspireWindow.setGeometry(x1 + w1/2 - w2/2, y1 + h1/2 - h2/2, w2, h2)
        self.inspireWindow.setMinimumSize(QtCore.QSize(600, self.inspireWindow.sizeHint().height()))
        self.inspireWindow.setMaximumSize(QtCore.QSize(600, self.inspireWindow.sizeHint().height()))
        self.inspireWindow.exec_()

    @pyqtSlot()
    def on_actionEUFAR_N7SP_triggered(self):
        webbrowser.open('http://www.eufar.net/')

    @pyqtSlot()
    def on_actionChangelog_triggered(self):
        self.logWindow = MyLog()
        x1, y1, w1, h1 = self.geometry().getRect()
        x2, y2, w2, h2 = self.logWindow.geometry().getRect()  # @UnusedVariable
        self.logWindow.setGeometry(x1 + w1/2 - w2/2, y1 + h1/2 - h2/2, w2, h2)
        self.logWindow.exec_()

    def closeEvent(self, event):
        if self.modified:
            result = self.make_onsave_msg_box("Close", "exit_icon.png")
            if result == "iw_saveButton":
                self.save_document()
                self.db.close()
                event.accept()
            elif result == "iw_nosaveButton":
                self.db.close()
                event.accept()
            else:
                event.ignore()
        else:
            self.db.close()
            self.close()

    def make_window_title(self):
        if self.saved:
            if len(self.out_file_name) > 40:
                out_file_name = "..." + self.out_file_name[30:]
            else:
                out_file_name = self.out_file_name
            title_string = "EUFAR Metadata Creator v{0} - ".format(_version) + out_file_name
        else:
            title_string = "EUFAR Metadata Creator v{0} - unsaved".format(_version)
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
        out_file_name, out_file_ext = file_dialog.getSaveFileName(self, "Save XML File",  # @UnusedVariable
                           "flight-info_!!!Unique resource identifier!!!.xml",
                           filter="XML Files (*.xml)");
        
        return str(out_file_name)

    def reset_all_fields(self):
        if self.au_wn_con_ta:
            for i in reversed(list(range(0, len(self.au_wn_con_ta)))):
                button_functions.delButton_5_clicked(self, i)
        if self.au_wn_lim_ta:
            for i in reversed(list(range(0, len(self.au_wn_lim_ta)))):
                button_functions.delButton_6_clicked(self, i)
        if self.mm_lab_1:
            for i in reversed(list(range(0, len(self.mm_lab_1)))):
                button_functions.delButton_7_clicked(self, i)	
        if self.tr_lab_1:
            for i in reversed(list(range(0, len(self.tr_lab_1)))):
                button_functions.delButton_3_clicked(self, i)
        if self.ro_lab_1:
            for i in reversed(list(range(0, len(self.ro_lab_1)))):
                button_functions.delButton_8_clicked(self, i)
        if self.ai_lab_1:
            for i in reversed(list(range(0, len(self.ai_lab_1)))):
                button_functions.delButton_4_clicked(self, i)
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
        self.ro_responsibleRole_rl1.setCurrentIndex(5)
        self.ai_label_7.clear()
        self.ai_label_8.clear()
        self.ai_label_9.clear()
        self.ai_label_10.clear()
        self.ai_label_11.clear()
        self.ai_label_12.clear()
        self.id_resourceLocator_ln.setText("http://browse.ceda.ac.uk/browse/badc/eufar/docs/00eufar"
                                           + "archivecontents.html")
        self.au_conditions_ta.setPlainText("As EUFAR is an EU-funded project, data in the EUFAR arc"
                                           + "hive are available to everyone. All users are require"
                                           + "d to aknowledge the data providers in any publication"
                                           + " based on EUFAR data.")
        self.au_limitations_ta.setPlainText("No limitations.")
        self.buttonGroup.setExclusive(False)        
        self.qv_obsRadio.setChecked(False)
        self.qv_insituRadio.setChecked(False)
        self.buttonGroup.setExclusive(True)
        qv_domain_changed(self)
        self.gl_roleBox = 0
        self.out_file_name = None
        self.modified = False
        self.saved = False
        self.make_window_title()

    def make_onsave_msg_box(self, string, iconName):
        self.presaveWindow = MyWarning(string, iconName)
        x1, y1, w1, h1 = self.geometry().getRect()
        x2, y2, w2, h2 = self.presaveWindow.geometry().getRect()  # @UnusedVariable
        self.presaveWindow.setGeometry(x1 + w1/2 - w2/2, y1 + h1/2 - h2/2, w2, h2)
        self.presaveWindow.setMinimumSize(QtCore.QSize(450, self.presaveWindow.sizeHint().height()))
        self.presaveWindow.setMaximumSize(QtCore.QSize(452, self.presaveWindow.sizeHint().height()))
        self.presaveWindow.exec_()
        return self.presaveWindow.buttonName

    def open_file(self):
        (out_file_name, filter) = QFileDialog.getOpenFileName(self, "Open XML File",  # @ReservedAssignment
                                                                       filter="XML Files (*.xml)")
        out_file_name = str(out_file_name)
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
            getattr(button_functions, str(self.sender().objectName()[:count_end] + "_clicked"))(self,
                 self.sender().objectName())
        elif "ai_delButton" in self.sender().objectName():
            getattr(button_functions, "delButton_4_clicked")(self)
        elif "tr_delBut" in self.sender().objectName():
            getattr(button_functions, "delButton_3_clicked")(self)
        elif "au_delBut_1" in self.sender().objectName():
            getattr(button_functions, "delButton_5_clicked")(self)
        elif "au_delBut_2" in self.sender().objectName():
            getattr(button_functions, "delButton_6_clicked")(self)
        elif "ro_delBut" in self.sender().objectName():
            getattr(button_functions, "delButton_8_clicked")(self)
        elif "mm_delBut" in self.sender().objectName():
            getattr(button_functions, "delButton_7_clicked")(self)
        elif "delButton_5" in self.sender().objectName():
            self.au_conditions_ta.setPlainText(self.au_wn_con_ta[0].toPlainText())
            getattr(button_functions, "delButton_5_clicked")(self, 0)
        elif "delButton_6" in self.sender().objectName():
            self.au_limitations_ta.setPlainText(self.au_wn_lim_ta[0].toPlainText())
            getattr(button_functions, "delButton_6_clicked")(self, 0)
        elif "delButton_10" in self.sender().objectName():
            self.tr_dateStart_do4.setDate(QDate.fromString(self.tr_dtSt_1[0].date().
                                                           toString(Qt.ISODate), Qt.ISODate))
            self.tr_dateEnd_do5.setDate(QDate.fromString(self.tr_dtEd_1[0].date().
                                                         toString(Qt.ISODate), Qt.ISODate))
            getattr(button_functions, "delButton_3_clicked")(self, 0)
        elif "delButton_8" in self.sender().objectName():
            self.ro_responsibleParty_ln.setText(self.ro_rlPy_ln[0].text())
            self.ro_responsibleEmail_ln.setText(self.ro_rlEm_ln[0].text())
            self.ro_responsibleRole_rl1.setCurrentIndex(self.ro_responsibleRole_rl1.
                                                        findText(self.ro_rlRl_ln[0].currentText()))
            getattr(button_functions, "delButton_8_clicked")(self, 0)
        elif "delButton_7" in self.sender().objectName():
            self.mm_conName_ln[0]
            self.mm_conEmail_ln[0]
            self.mm_contactName_ln.setText(self.mm_conName_ln[0].text())
            self.mm_contactEmail_ln.setText(self.mm_conEmail_ln[0].text())
            getattr(button_functions, "delButton_7_clicked")(self, 0)
        elif self.sender().objectName() == "":
            return
        else:
            getattr(button_functions, str(self.sender().objectName() + "_clicked"))(self)

    def rolebox_changed(self):
        gl_rolebox_changed(self)

    def image_changed(self):
        ai_aircraftRolebox_changed(self)

    def category_changed(self):
        gl_categoryRolebox_changed(self)

    def instrument_changed(self):
        ai_instrument_changed(self)
        
    def quality_domain(self):
        qv_domain_changed(self)
      
    def output_other(self):
        qv_output_other(self)
        
    def save_statement(self):
        statement = ""
        if self.qv_obsRadio.isChecked() == True:
            statement = save_statement_observation(self)
        elif self.qv_insituRadio.isChecked() == True:
            statement = save_statement_insitu(self)
        return statement
        
    def read_statement(self, statement):
        if statement.find("Earth observation/Remote sensing data") != -1:
            self.qv_obsRadio.setChecked(True)
            qv_domain_changed(self)
            read_statement_observation(self, statement)
        else:
            self.qv_insituRadio.setChecked(True)
            qv_domain_changed(self)
            read_statement_insitu(self, statement)


class MyLog(QtWidgets.QDialog, Ui_Changelog):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        self.log_txBrower.setPlainText(open("Documentation/changelog.txt").
                                       read())
        self.lg_okButton.clicked.connect(self.closeWindow)
        self.lg_okButton.setFocus(True)

    def closeWindow(self):
        self.close()


class MyAbout(QtWidgets.QDialog, Ui_aboutWindow):
    def __init__(self, aboutText):
        QWidget.__init__(self)
        self.setupUi(self)
        self.aw_label_1.setText(aboutText)
        self.aw_okButton.clicked.connect(self.closeWindow)
        self.aw_okButton.setFocus(True)

    def closeWindow(self):
        self.close()
        
        
class MyInspire(QtWidgets.QDialog, Ui_inspireWindow):
    def __init__(self, aboutText):
        QWidget.__init__(self)
        self.setupUi(self)
        self.aw_label_1.setText(aboutText)
        self.aw_okButton.clicked.connect(self.closeWindow)
        self.aw_okButton.setFocus(True)

    def closeWindow(self):
        self.close()


class MyWarning(QtWidgets.QDialog, Ui_presaveWindow):
    def __init__(self, string, iconName):
        QWidget.__init__(self)
        self.setupUi(self)
        self.iw_cancelButton.setFocus(True)
        all_buttons = self.findChildren(QPushButton)
        for widget in all_buttons:
            widget.clicked.connect(lambda: self.closeWindow())
        self.iw_nosaveButton.setText(string + " without saving")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/" + iconName), QtGui.QIcon.
                       Normal, QtGui.QIcon.Off)
        self.iw_nosaveButton.setIcon(icon)

    def closeWindow(self):
        self.buttonName = self.sender().objectName()
        self.close()
