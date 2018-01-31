import webbrowser
import logging
import platform
import os
import configparser
import requests
from operator import itemgetter
from PyQt5 import Qt, QtCore, QtWidgets, QtGui
from .Ui_mainwindow import Ui_MainWindow
from .Ui_logwindow import Ui_Changelog
from .Ui_aboutwindow import Ui_aboutWindow
from .Ui_inspirewindow import Ui_inspireWindow
from .Ui_presavewindow import Ui_presaveWindow
from ui.Ui_apiwindow import Ui_apiWindow
from ._version import _version, _py_version, _qt_version, _inspire_version
from functions import eufar_metadata_xml
from functions import button_functions
from functions import utility_functions
from functions.sql_functions import objectsInit
from functions.check_functions import fill_all_fields


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, path, parent=None):
        logging.info('mainwindow.py - UI initialization ...')
        QtWidgets.QMainWindow.__init__(self, parent)
        self.tabLayout = 0
        self.setupUi(self)
        objectsInit(self)
        self.aircraft_db = {}
        self.operator_db = {}
        self.instrument_db = {}
        self.operator_db = {}
        all_date_edits = self.findChildren(QtWidgets.QDateEdit)
        for widget in all_date_edits:
            widget.setDate(QtCore.QDate.currentDate())
        all_check_boxes = self.findChildren(QtWidgets.QCheckBox)
        for check_box in all_check_boxes:
            check_box.stateChanged.connect(lambda: utility_functions.set_modified(self))
        all_text_edits = self.findChildren(QtWidgets.QPlainTextEdit)
        for widget in all_text_edits:
            widget.textChanged.connect(lambda: utility_functions.set_modified(self))
        all_line_edits = self.findChildren(QtWidgets.QLineEdit)
        for widget in all_line_edits:
            widget.textChanged.connect(lambda: utility_functions.set_modified(self))
        all_rolbox_edits = self.findChildren(QtWidgets.QComboBox)
        for widget in all_rolbox_edits:
            widget.activated.connect(lambda: utility_functions.set_modified(self))
        all_date_edits = self.findChildren(QtWidgets.QDateEdit)
        for widget in all_date_edits:
            widget.dateChanged.connect(lambda: utility_functions.set_modified(self))
        all_info_boxes = self.findChildren(QtWidgets.QToolButton)
        for widget in all_info_boxes:
            widget.clicked.connect(lambda: self.button_clicked())
        self.ai_aircraft_rl1.activated.connect(lambda: self.image_changed())
        self.gl_category_rl1.activated.connect(lambda: self.category_changed())
        self.gl_resolution_rl1.activated.connect(lambda: self.rolebox_changed())
        self.ai_instrument_rl1.activated.connect(lambda: self.instrument_changed())
        self.qv_tabWidget.tabCloseRequested.connect(self.close_tab)
        self.id_resourceLocator_ln.setCursorPosition(0)
        self.qv_tabWidget.setVisible(False)
        utility_functions.fill_aircraft_combobox(self)
        utility_functions.fill_instrument_combobox(self)
        utility_functions.make_window_title(self)
        self.qv_spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_20.addItem(self.qv_spacerItem)
        self.ai_airManufacturer_ln.hide()
        self.ai_airType_ln.hide()
        self.ai_airOperator_ln.hide()
        self.ai_country_rl.hide()
        self.ai_airNumber_ln.hide()
        self.ai_newname_lb.hide()
        self.ai_insName_ln.hide()
        self.ai_newmanufacturer_lb.hide()
        self.ai_insManufacturer_ln.hide()
        self.plusButton_9.hide()
        self.gl_unit_lb.hide()
        self.gl_unit_rl.hide()
        self.menubar.setStyleSheet("QMenuBar {\n"
            "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
            "                      stop: 0 #f0f0f0, stop: 1 #e5e5e5);\n"
            "}\n"
            "\n"
            "QMenuBar::item {\n"
            "    spacing: 3px;\n"
            "    padding: 5px 5px 5px 5px;\n"
            "    background: transparent;\n"
            "}\n"
            "\n"
            "QMenuBar::item:selected {\n"
            "    border: 0px solid #7eb4ea;\n"
            "    border-radius: 1px;\n"
            "    background-color: rgb(200,200,200);\n"
            "}\n"
            "\n"
            "QMenu {\n"
            "    background-color: #f0f0f0;\n"
            "    border: 0px solid #f0f0f0;\n"
            "}\n"
            "\n"
            "QMenu::item:selected {\n"
            "    background-color: rgb(200,200,200);\n"
            "    color: black;\n"
            "}\n"
            "\n"
            "QMenu::icon {\n"
            "    margin-left: 20px;\n"
            "    background-color: red;\n"
            "    border: none;\n"
            "}")
        "patch for combobox stylesheet"
        itemDelegate = QtWidgets.QStyledItemDelegate()
        self.id_resourceType_rl1.setItemDelegate(itemDelegate)
        self.id_resourceLang_rl2.setItemDelegate(itemDelegate)
        self.ai_aircraft_rl1.setItemDelegate(itemDelegate)
        self.ai_instrument_rl1.setItemDelegate(itemDelegate)
        self.ai_country_rl.setItemDelegate(itemDelegate)
        self.gl_category_rl1.setItemDelegate(itemDelegate)
        self.gl_details_rl2.setItemDelegate(itemDelegate)
        self.gl_resolution_rl1.setItemDelegate(itemDelegate)
        self.gl_unit_rl.setItemDelegate(itemDelegate)
        self.ro_responsibleRole_rl1.setItemDelegate(itemDelegate)
        self.mm_language_rl1.setItemDelegate(itemDelegate)
        shadow = QtWidgets.QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(10)
        shadow.setColor(QtGui.QColor(63,63,63,180))
        shadow.setOffset(6, 6)
        self.ai_image_bx.setGraphicsEffect(shadow)
        self.api_eufar_acronym_completer()
        self.api_eufar_database_parsing()
        config_dict = configparser.ConfigParser()
        config_dict.read(os.path.join(path, 'emc_creator.ini'))
        show_api_info = config_dict.get('OPTIONS', 'api_info')
        result = False
        if show_api_info == 'True':
            result = self.api_eufar_information()
            if show_api_info != str(result):
                config_dict.set('OPTIONS', 'api_info', str(result))
                with open(os.path.join(path, 'emc_creator.ini'), 'w') as configfile:
                    config_dict.write(configfile)
        logging.info('mainwindow.py - UI initialized !')
        logging.info('**************************************************')


    @QtCore.pyqtSlot()
    def on_actionNew_triggered(self):
        logging.debug('mainwindow.py - on_actionNew_triggered - self.modified ' + str(self.modified))
        if self.modified:
            result = self.make_onsave_msg_box("Clear")
            if result == "iw_saveButton":
                self.save_document()
                self.reset_all_fields()
                labels = self.findChildren(QtWidgets.QLabel)
                for label in labels:
                    label.setStyleSheet("color: black")
            elif result == "iw_nosaveButton":
                self.reset_all_fields()
        else:
            self.reset_all_fields()
    
    @QtCore.pyqtSlot()
    def on_actionSave_triggered(self):
        logging.debug('mainwindow.py - on_actionSave_triggered')
        self.save_document()

    @QtCore.pyqtSlot()
    def on_actionSave_As_triggered(self):
        logging.debug('mainwindow.py - on_actionSave_As_triggered')
        self.save_document(save_as=True)

    @QtCore.pyqtSlot()
    def on_actionOpen_triggered(self):
        logging.debug('mainwindow.py - on_actionOpen_triggered - self.modified ' + str(self.modified))
        if self.modified:
            result = self.make_onsave_msg_box("Open")
            if result == "iw_saveButton":
                self.save_document()
            elif result == "iw_nosaveButton":
                self.open_file()
        else:
            self.open_file()

    @QtCore.pyqtSlot()
    def on_actionExit_triggered(self):
        logging.debug('mainwindow.py - on_actionExit_triggered')
        self.close()

    @QtCore.pyqtSlot()
    def on_actionEUFAR_CreatorAbout_triggered(self):
        logging.debug('mainwindow.py - on_actionEUFAR_CreatorAbout_triggered')
        aboutText = ("<html><head/><body><p align=justify>This is the EUFAR Metadata Creator V%s. I"
                     + "t was developed by EUFAR using Python %s and PyQT %s. The goal of the EUFAR Metad"
                     + "ata Creator is to produce metadata to facilitate data storage and searches "
                     + "for Airborne Scientific Campaigns. XML files generated by this version conf"
                     + "orm to V%s of the INSPIRE metadata and XML Standard.</p><p>For any question"
                     + "s, more information, or to submit a bug report, please contact <a href=\"ma"
                     + "ilto:bureau.at.eufar.net\"><span style=\" text-decoration: underline;"
                     + " color:#0000ff;\">bureau.at.eufar.net</span></a>.</p><p>The latest ve"
                     + "rsion and source code of the EUFAR Metadata Creator can be found at <a href"
                     + "=https://github.com/EUFAR/emc-eufar><span style=\" text-decoration"
                     + ": underline; color:#0000ff;\">https://github.com/EUFAR/emc-eufar</"
                     + "a></p></body></html>") % (_version, _py_version, _qt_version, _inspire_version)
        self.aboutWindow = MyAbout(aboutText)
        x1, y1, w1, h1 = self.geometry().getRect()
        _, _, w2, h2 = self.aboutWindow.geometry().getRect()
        self.aboutWindow.setGeometry(x1 + w1/2 - w2/2, y1 + h1/2 - h2/2, w2, h2)
        self.aboutWindow.setMinimumSize(QtCore.QSize(450, self.aboutWindow.sizeHint().height()))
        self.aboutWindow.setMaximumSize(QtCore.QSize(450, self.aboutWindow.sizeHint().height()))
        self.aboutWindow.exec_()

    @QtCore.pyqtSlot()
    def on_actionINSPIRE_Standard_triggered(self):
        logging.debug('mainwindow.py - on_actionINSPIRE_Standard_triggered')
        self.inspireWindow = MyInspire()
        x1, y1, w1, h1 = self.geometry().getRect()
        _, _, w2, h2 = self.inspireWindow.geometry().getRect()
        self.inspireWindow.setGeometry(x1 + w1/2 - w2/2, y1 + h1/2 - h2/2, w2, h2)
        self.inspireWindow.setMinimumSize(QtCore.QSize(800, self.inspireWindow.sizeHint().height()))
        self.inspireWindow.setMaximumSize(QtCore.QSize(800, self.inspireWindow.sizeHint().height()))
        self.inspireWindow.exec_()

    @QtCore.pyqtSlot()
    def on_actionEUFAR_N7SP_triggered(self):
        logging.debug('mainwindow.py - on_actionEUFAR_N7SP_triggered')
        webbrowser.open('http://www.eufar.net/')

    @QtCore.pyqtSlot()
    def on_actionHelp_triggered(self):
        logging.debug('mainwindow.py - on_actionHelp_triggered')
        webbrowser.open('http://www.eufar.net/cms/eufar-metadata-creator-help/')

    @QtCore.pyqtSlot()
    def on_actionChangelog_triggered(self):
        logging.debug('mainwindow.py - on_actionChangelog_triggered')
        self.logWindow = MyLog()
        x1, y1, w1, h1 = self.geometry().getRect()
        _, _, w2, h2 = self.logWindow.geometry().getRect()
        self.logWindow.setGeometry(x1 + w1/2 - w2/2, y1 + h1/2 - h2/2, w2, h2)
        self.logWindow.exec_()

    def closeEvent(self, event):
        logging.debug('mainwindow.py - closeEvent - self.modified ' + str(self.modified))
        if self.modified:
            result = self.make_onsave_msg_box("Close")
            if result == "iw_saveButton":
                self.save_document()
                logging.info('EMC ' + _version + ' is closing ...')
                event.accept()
            elif result == "iw_nosaveButton":
                logging.info('EMC ' + _version + ' is closing ...')
                event.accept()
            else:
                event.ignore()
        else:
            logging.info('EMC ' + _version + ' is closing ...')
            self.close()

    def save_document(self, save_as=False):
        logging.debug('mainwindow.py - save_document - save_as ' + str(save_as))
        cancel = fill_all_fields(self)
        if cancel == True:
            return
        if not self.out_file_name or save_as or self.fillInfo:
            self.out_file_name = utility_functions.get_file_name(self)
            if not self.out_file_name:
                return
            if '.xml' not in self.out_file_name:
                self.out_file_name = self.out_file_name + '.xml'
        eufar_metadata_xml.create_eufar_xml(self, self.out_file_name)
        utility_functions.make_window_title(self)

    def reset_all_fields(self):
        logging.debug('mainwindow.py - reset_all_fields starting ...')
        labels = self.findChildren(QtWidgets.QLabel)
        for label in labels:
            label.setStyleSheet("color: black")
        for i in range(self.tabWidget.count()):
            self.tabWidget.tabBar().setTabTextColor(i, QtGui.QColor(0,0,0))
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
        if self.aircraft_list:
            for i in reversed(list(range(0, len(self.aircraft_list)))):
                button_functions.delButton_9_clicked(self, i)
        if self.ai_lab_1:
            for i in reversed(list(range(0, len(self.ai_lab_1)))):
                button_functions.delButton_4_clicked(self, i)
        all_date_edits = self.findChildren(QtWidgets.QDateEdit)
        for widget in all_date_edits:
            widget.setDate(QtCore.QDate.currentDate())
        all_check_boxes = self.findChildren(QtWidgets.QCheckBox)
        for check_box in all_check_boxes:
            check_box.setCheckState(False)
        all_plainText_edits = self.findChildren(QtWidgets.QPlainTextEdit)
        for widget in all_plainText_edits:
            widget.clear()
        all_line_edits = self.findChildren(QtWidgets.QLineEdit)
        for widget in all_line_edits:
            widget.clear()
        all_rolbox_edits = self.findChildren(QtWidgets.QComboBox)
        for widget in all_rolbox_edits:
            widget.setCurrentIndex(0)
        button_functions.gl_rolebox_changed(self)
        button_functions.gl_categoryRolebox_changed(self)
        button_functions.ai_aircraftRolebox_changed(self)
        all_list_edits = self.findChildren(QtWidgets.QListWidget)
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
        self.id_resourceLocator_ln.setText("http://browse.ceda.ac.uk/browse/badc/eufar/docs/00eufar"
                                           + "archivecontents.html")
        self.id_resourceLocator_ln.setCursorPosition(0)
        self.au_conditions_ta.setPlainText("As EUFAR is an EU-funded project, data in the EUFAR arc"
                                           + "hive are available to everyone. All users are require"
                                           + "d to aknowledge the data providers in any publication"
                                           + " based on EUFAR data.")
        self.au_limitations_ta.setPlainText("No limitations.")
        for i in reversed(list(range(self.qv_tabWidget.count()))):
            self.close_tab(i)
        self.gl_roleBox = 0
        self.out_file_name = None
        self.modified = False
        self.saved = False
        utility_functions.make_window_title(self)
        logging.debug('mainwindow.py - reset_all_fields finished.')

    def make_onsave_msg_box(self, string):
        logging.debug('mainwindow.py - make_onsave_msg_box - string ' + string)
        self.presaveWindow = MyWarning(string)
        x1, y1, w1, h1 = self.geometry().getRect()
        _, _, w2, h2 = self.presaveWindow.geometry().getRect()
        self.presaveWindow.setGeometry(x1 + w1/2 - w2/2, y1 + h1/2 - h2/2, w2, h2)
        self.presaveWindow.setMinimumSize(QtCore.QSize(470, self.presaveWindow.sizeHint().height()))
        self.presaveWindow.setMaximumSize(QtCore.QSize(470, self.presaveWindow.sizeHint().height()))
        self.presaveWindow.exec_()
        try:
            return self.presaveWindow.buttonName
        except AttributeError:
            return

    def open_file(self):
        logging.debug('mainwindow.py - open_file')
        out_file_name, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Open XML File", filter="XML Files (*.xml)")
        out_file_name = str(out_file_name)
        if out_file_name:
            self.reset_all_fields()
            eufar_metadata_xml.read_eufar_xml(self, out_file_name)
            self.saved = True
            self.modified = False
            self.out_file_name = out_file_name
            utility_functions.make_window_title(self)

    def button_clicked(self):
        logging.debug('mainwindow.py - button_clicked - self.sender().objectName() ' + self.sender().objectName())
        if "infoButton" in self.sender().objectName():
            if len(self.sender().objectName()) == 12:
                count_end=-2
            else:
                count_end=-3
            getattr(button_functions, str(self.sender().objectName()[:count_end] + "_clicked"))(self,
                 self.sender().objectName())
        elif "ai_delButton_2_" in self.sender().objectName():
            getattr(button_functions, "delButton_9_clicked")(self)
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
            self.tr_dateStart_do4.setDate(QtCore.QDate.fromString(self.tr_dtSt_1[0].date().
                                                           toString(Qt.Qt.ISODate), Qt.Qt.ISODate))
            self.tr_dateEnd_do5.setDate(QtCore.QDate.fromString(self.tr_dtEd_1[0].date().
                                                         toString(Qt.Qt.ISODate), Qt.Qt.ISODate))
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
        elif "qv_insitu_contBut" in self.sender().objectName():
            getattr(button_functions, "qv_tab_cloning")(self, "insitu", int(self.sender().objectName()[20:]))
        elif "qv_imagery_contBut" in self.sender().objectName():
            getattr(button_functions, "qv_tab_cloning")(self, "imagery", int(self.sender().objectName()[21:]))
        elif self.sender().objectName() == "":
            return
        else:
            getattr(button_functions, str(self.sender().objectName() + "_clicked"))(self)

    def rolebox_changed(self):
        logging.debug('mainwindow.py - rolebox_changed')
        button_functions.gl_rolebox_changed(self)

    def image_changed(self):
        logging.debug('mainwindow.py - image_changed')
        button_functions.ai_aircraftRolebox_changed(self)

    def category_changed(self):
        logging.debug('mainwindow.py - category_changed')
        button_functions.gl_categoryRolebox_changed(self)

    def instrument_changed(self):
        logging.debug('mainwindow.py - instrument_changed')
        button_functions.ai_instrument_changed(self)
        
    def output_other(self):
        logging.debug('mainwindow.py - output_other')
        button_functions.qv_output_other(self)
        
    def close_tab(self, index):
        logging.debug('mainwindow.py - close_tab - self.qv_tabWidget.tabText(index) ' + self.qv_tabWidget.tabText(index))
        string = self.qv_tabWidget.tabText(index)
        if "Earth" in string:
            button_functions.close_imagery_tab(self, index, int(string[38:]) - 1)
        elif "Atmospheric" in string:
            button_functions.close_insitu_tab(self, index, int(string[25:]) - 1)

    def api_eufar_information(self):
        logging.debug('mainwindow.py - api_eufar_information')
        self.apiWindow = MyApi()
        x1, y1, w1, h1 = self.geometry().getRect()
        _, _, w2, h2 = self.apiWindow.geometry().getRect()
        x2 = x1 + w1/2 - w2/2
        y2 = y1 + h1/2 - h2/2
        self.apiWindow.setGeometry(x2, y2, w2, h2)
        if platform.system() == 'Linux':
            x = 500
            y = self.apiWindow.sizeHint().height()
        elif platform.system() == 'Windows':
            x = 700
            y = 400
        else:
            x = 500
            y = self.apiWindow.sizeHint().height()
        self.apiWindow.setMinimumSize(QtCore.QSize(x, y))
        self.apiWindow.setMaximumSize(QtCore.QSize(x, y))
        self.apiWindow.exec_()
        return self.apiWindow.checkboxStatus

    def api_eufar_database_parsing(self):
        logging.debug('mainwindow.py - api_eufar_database_parsing')
        self.download_and_parse_objects = DownloadAndParseJSON()
        self.download_and_parse_objects.start()
        self.download_and_parse_objects.finished.connect(self.api_eufar_asmm_db_updating)
    
    def api_eufar_asmm_db_updating(self, val):
        logging.debug('mainwindow.py - api_eufar_asmm_db_updating')
        self.aircraft_db = val[0]
        self.project_db = val[1]
        self.operator_db = val[2]
        self.instrument_db = val[3]
        self.new_operators_aircraft = []
        for _, value in self.aircraft_db.items():
            self.new_operators_aircraft.append([value['operator'],
                                                value['manufacturer_and_aircraft_type'], 
                                                value['registration_number'],
                                                value['country'],
                                                value['large_image']])
        self.new_operators_aircraft = sorted(self.new_operators_aircraft, key=itemgetter(0,1))
        self.instrument_list = []
        for _, value in self.instrument_db.items():
            self.instrument_list.append([value['name'],
                                         value['manufacturer']])
        self.instrument_list = sorted(self.instrument_list, key=itemgetter(0,1))
        current_aircraft = self.ai_aircraft_rl1.currentText()
        current_registration = self.ai_label_11.text() 
        utility_functions.fill_aircraft_combobox(self)
        button_functions.ai_aircraftRolebox_changed(self)
        if current_aircraft != 'Make a choice...' and current_aircraft != 'Other...':
            for item in self.new_operators_aircraft:
                if item[2] == current_registration:
                    aircraft = item[0] + ' - ' + item[1][item[1].find(', ') + 2:]
                    index = self.ai_aircraft_rl1.findText(aircraft)
                    if index == -1:
                        aircraft += ' - ' + current_registration
                        index = self.ai_aircraft_rl1.findText(aircraft)
                        if index != -1:
                            self.ai_aircraft_rl1.setCurrentIndex(index)
                            button_functions.ai_aircraftRolebox_changed(self)
                    else:
                        self.ai_aircraft_rl1.setCurrentIndex(index)
                        button_functions.ai_aircraftRolebox_changed(self)
                    break
        current_instrument = self.ai_instrument_rl1.currentText()
        utility_functions.fill_instrument_combobox(self)
        button_functions.ai_instrument_changed(self)
        if current_instrument != 'Make a choice...' and current_instrument != 'Other...':
            for item in self.instrument_list:
                if item[1] + ' - ' + item[0] == current_instrument:
                    index = self.ai_instrument_rl1.findText(current_instrument)
                    if index != -1:
                        self.ai_instrument_rl1.setCurrentIndex(index)
                    break
        completer_list = []
        for key, value in self.project_db.items():
            completer_list.append(key)
        self.completer_model.setStringList(completer_list)
        
    def api_eufar_acronym_completer(self):
        logging.debug('mainwindow.py - api_eufar_acronym_completer')
        self.completer = QtWidgets.QCompleter()
        self.completer.popup().setStyleSheet("QListView {\n"
        "    selection-background-color: rgb(200,200,200);\n"
        "    selection-color: black;\n"
        "    background-color: #f0f0f0;\n"
        "    border: 0px solid #f0f0f0;\n"
        "}\n"
        "\n"
        "QScrollBar:vertical {\n"
        "    border: 1px solid white;\n"
        "    background-color: rgb(240, 240, 240);\n"
        "    width: 20px;\n"
        "    margin: 21px 0px 21px 0px;\n"
        "}\n"
        "\n"
        "QScrollBar::handle:vertical {\n"
        "    background-color: rgb(205, 205, 205);\n"
        "    min-height: 25px;\n"
        "}\n"
        "\n"
        "QScrollBar:handle:vertical:hover {\n"
        "    background-color: rgb(167, 167, 167);\n"
        "}\n"
        "\n"
        "QScrollBar::add-line:vertical {\n"
        "    border-top: 1px solid rgb(240,240,240);\n"
        "    border-left: 1px solid white;\n"
        "    border-right: 1px solid white;\n"
        "    border-bottom: 1px solid white;\n"
        "    background-color: rgb(240, 240, 240);\n"
        "    height: 20px;\n"
        "    subcontrol-position: bottom;\n"
        "    subcontrol-origin: margin;\n"
        "}\n"
        "\n"
        "QScrollBar::add-line:vertical:hover {\n"
        "    background-color: rgb(219, 219, 219);\n"
        "}\n"
        "\n"
        "QScrollBar::sub-line:vertical {\n"
        "    border-top: 1px solid white;\n"
        "    border-left: 1px solid white;\n"
        "    border-right: 1px solid white;\n"
        "    border-bottom: 1px solid rgb(240,240,240);\n"
        "    background-color: rgb(240, 240, 240);\n"
        "    height: 20px;\n"
        "    subcontrol-position: top;\n"
        "    subcontrol-origin: margin;\n"
        "}\n"
        "\n"
        "QScrollBar::sub-line:vertical:hover {\n"
        "    background-color: rgb(219, 219, 219);\n"
        "}\n"
        "\n"
        "QScrollBar::up-arrow:vertical {\n"
        "    image: url(icons/up_arrow_icon.svg); \n"
        "    width: 16px;\n"
        "    height: 16px;\n"
        "}\n"
        "\n"
        "QScrollBar::up-arrow:vertical:pressed {\n"
        "    right: -1px;\n"
        "    bottom: -1px;\n"
        "}\n"
        "\n"
        "QScrollBar::down-arrow:vertical {\n"
        "    image: url(icons/down_arrow_icon.svg); \n"
        "    width: 16px;\n"
        "    height: 16px;\n"
        "}\n"
        "\n"
        "QScrollBar::down-arrow:vertical:pressed {\n"
        "    right: -1px;\n"
        "    bottom: -1px;\n"
        "}\n")
        self.id_resourceIdent_ln.setCompleter(self.completer)
        self.completer_model = QtCore.QStringListModel()
        self.completer.setModel(self.completer_model)
        self.completer.activated.connect(self.api_eufar_completer_function)
    
    def api_eufar_completer_function(self,val):
        logging.debug('mainwindow.py - api_eufar_completer_function - val ' + str(val))
        project = self.project_db[val]
        try:
            self.id_resourceTitle_ln.setText(project['title'])
        except KeyError:
            pass
        try:
            self.id_resourceAbstract_ta.setPlainText(project['abstract'])
        except KeyError:
            pass
        try:
            self.tr_dateStart_do4.setDate(QtCore.QDate.fromString(project['campaign_start'], QtCore.Qt.ISODate))
        except KeyError:
            pass
        try:
            self.tr_dateEnd_do5.setDate(QtCore.QDate.fromString(project['campaign_end'], QtCore.Qt.ISODate))
        except KeyError:
            pass
        try:
            platform = self.aircraft_db[project['aircraft']]
        except KeyError:
            platform = {}
        try:
            operator = platform['operator']
        except KeyError:
            operator = ''
        try:    
            aircraft = platform['manufacturer_and_aircraft_type']
            index = aircraft.find(', ')
            manufacturer = aircraft[: index]
            aircraft = aircraft[index + 2:]
        except KeyError:
            aircraft = ''
            manufacturer = ''
        try:
            registration = platform['registration_number']
        except KeyError:
            registration = ''
        try:
            country = platform['country']
            country = eufar_metadata_xml.reverseDictionary(country, self.new_country_code)
        except KeyError:
            country = ''
        aircraft_found = False
        if registration:
            for item in self.new_operators_aircraft:
                if item[2] == registration:
                    operator = item[0]
                    aircraft = item[1][item[1].find(', ') + 2:]
                    index = self.ai_aircraft_rl1.findText(operator + ' - ' + aircraft)
                    if index == -1:
                        index = self.ai_aircraft_rl1.findText(operator + ' - ' + aircraft + ' - ' + registration)
                        if index == -1:
                            self.ai_aircraft_rl1.setCurrentIndex(1)
                            self.ai_airManufacturer_ln.setText(manufacturer)
                            self.ai_airType_ln.setText(aircraft)
                            self.ai_airOperator_ln.setText(operator)
                            self.ai_country_rl.setCurrentIndex(self.ai_country_rl.findText(country))
                            self.ai_airNumber_ln.setText(registration)
                        else:
                            self.ai_aircraft_rl1.setCurrentIndex(index)
                    else:
                        self.ai_aircraft_rl1.setCurrentIndex(index)
                    button_functions.ai_aircraftRolebox_changed(self)
                    button_functions.plusButton_10_clicked(self, aircraft, operator, manufacturer, registration, country)
                    aircraft_found = True
                    break
            if not aircraft_found:
                self.ai_aircraft_rl1.setCurrentIndex(1)
                button_functions.ai_aircraftRolebox_changed(self)
                self.ai_airManufacturer_ln.setText(manufacturer)
                self.ai_airType_ln.setText(aircraft)
                self.ai_airOperator_ln.setText(operator)
                self.ai_country_rl.setCurrentIndex(self.ai_country_rl.findText(country))
                self.ai_airNumber_ln.setText(registration)
                button_functions.plusButton_10_clicked(self, aircraft, operator, manufacturer, registration, country)
        else:
            self.ai_aircraft_rl1.setCurrentIndex(1)
            button_functions.ai_aircraftRolebox_changed(self)
            self.ai_airManufacturer_ln.setText(manufacturer)
            self.ai_airType_ln.setText(aircraft)
            self.ai_airOperator_ln.setText(operator)
            self.ai_country_rl.setCurrentIndex(self.ai_country_rl.findText(country))
            self.ai_airNumber_ln.setText(registration)
            button_functions.plusButton_10_clicked(self, aircraft, operator, manufacturer, registration, country)


class MyLog(QtWidgets.QDialog, Ui_Changelog):
    def __init__(self):
        logging.debug('mainwindow.py - MyLog - __init__')
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.log_txBrower.setPlainText(open("Documentation/changelog.txt").read())
        self.lg_okButton.clicked.connect(self.closeWindow)
        self.lg_okButton.setFocus(True)

    def closeWindow(self):
        logging.debug('mainwindow.py - MyLog - closeWindow')
        self.close()


class MyAbout(QtWidgets.QDialog, Ui_aboutWindow):
    def __init__(self, aboutText):
        logging.debug('mainwindow.py - MyAbout - __init__')
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.aw_label_1.setText(aboutText)
        self.aw_okButton.clicked.connect(self.closeWindow)
        self.aw_okButton.setFocus(True)

    def closeWindow(self):
        logging.debug('mainwindow.py - MyAbout - closeWindow')
        self.close()
        
        
class MyInspire(QtWidgets.QDialog, Ui_inspireWindow):
    def __init__(self):
        logging.debug('mainwindow.py - MyInspire - __init__')
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.aw_okButton.clicked.connect(self.closeWindow)
        self.aw_okButton.setFocus(True)

    def closeWindow(self):
        logging.debug('mainwindow.py - MyInspire - closeWindow')
        self.close()


class MyWarning(QtWidgets.QDialog, Ui_presaveWindow):
    def __init__(self, string):
        logging.debug('mainwindow.py - MyWarning - __init__ - string ' + string)
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.iw_cancelButton.setFocus(True)
        all_buttons = self.findChildren(QtWidgets.QToolButton)
        for widget in all_buttons:
            widget.clicked.connect(lambda: self.closeWindow())
        self.iw_nosaveButton.setText(string + " without saving")

    def closeWindow(self):
        logging.debug('mainwindow.py - MyWarning - closeWindow - self.sender().objectName() ' + self.sender().objectName())
        self.buttonName = self.sender().objectName()
        self.close()
        
        
class MyApi(QtWidgets.QDialog, Ui_apiWindow):
    def __init__(self):
        logging.debug('mainwindow.py - MyApi - __init__')
        QtWidgets.QWidget.__init__(self)
        logging.debug('button_functions.py - MyInfo')
        self.setupUi(self)
        self.iw_okButton.clicked.connect(self.closeWindow)
        
    def closeWindow(self):
        logging.debug('mainwindow.py - MyApi - closeWindow - self.checkBox.isChecked() ' + str(self.checkBox.isChecked()))
        self.checkboxStatus = self.checkBox.isChecked()
        self.close()
        
        
class DownloadAndParseJSON(Qt.QThread):
    finished = QtCore.pyqtSignal(list)
    def __init__(self):
        Qt.QThread.__init__(self)
        logging.debug('mainwindow.py - DownloadAndParseJSON - starting ...')
        self.url_list = ['http://eufar.net/api/json/ta/open/aircraft/', 
                         'http://eufar.net/api/sad89712hhdsa89yp1/json/projects/',
                         'http://eufar.net/api/json/ta/open/operators/',
                         'http://eufar.net/api/json/instruments/'
                         ]
        self.db_list = []

    def run(self):   
        for url in self.url_list:
            dict_tmp = {}
            try:
                logging.debug('mainwindow.py - DownloadAndParseJSON - ' + url + ' running ...')
                req = requests.get(url=url)
                json_object = req.json()
                for item in json_object:
                    dict_tmp[item['acronym']] = dict(item)
                self.db_list.append(dict_tmp)
            except Exception:
                self.db_list.append(dict_tmp)
                logging.error('mainwindow.py - DownloadAndParseJSON - ' + url + ' error in connexion or json object')
        self.finished.emit(self.db_list)
        
    def stop(self):
        self.terminate()
