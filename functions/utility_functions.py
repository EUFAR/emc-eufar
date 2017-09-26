import logging
from ui._version import _version
from PyQt5 import QtWidgets


def set_modified(self):
    logging.debug('utility_functions.py - set_modified - self.modified ' + str(self.modified))
    if not self.modified:
        self.modified = True
        make_window_title(self)


def make_window_title(self):
        logging.debug('mainwindow.py - make_window_title - self.modified ' + str(self.modified) +
                      ' ; self.saved ' + str(self.saved))
        title_string = 'EMC Creator v' + _version
        file_string = ''
        saved_string = ''
        modified_string = ''
        if self.out_file_name:
            file_string = ' - ' + self.out_file_name
        if not self.saved:
            saved_string = ' - unsaved'
        if self.modified:
            modified_string = ' - modified'
        title_string = title_string + file_string + saved_string + modified_string
        self.setWindowTitle(title_string)


def get_file_name(self):
    logging.debug('utility_functions.py - get_file_name')
    file_dialog = QtWidgets.QFileDialog()
    file_dialog.setDefaultSuffix('xml')
    out_file_name, _ = file_dialog.getSaveFileName(self, "Save XML File",
                                                   "!!!Project acronym!!!_xxxxxxxxxx.xml",
                                                   filter="XML Files (*.xml)");
    return str(out_file_name)


def fill_instrument_combobox(self):
    logging.debug('utility_functions.py - fill_instrument_combobox')
    tmp = []
    for item in self.instrument_list:
        tmp.append(item[1] + ' - ' + item[0])
    self.ai_instrument_rl1.clear()
    self.ai_instrument_rl1.addItem('Make a choice...')
    self.ai_instrument_rl1.addItem('Other...')
    self.ai_instrument_rl1.addItems(sorted(tmp))
    
    
def fill_aircraft_combobox(self):
    logging.debug('utility_functions.py - fill_aircraft_combobox')
    self.ai_aircraft_rl1.clear()
    aircraft_list = []
    for i, item in enumerate(self.new_operators_aircraft):
        full_aircraft = item[1]
        try:
            if item[1] == self.new_operators_aircraft[i - 1][1] and item[0] == self.new_operators_aircraft[i - 1][0]:
                full_aircraft += ' - ' + item[2]
        except IndexError: pass
        try:
            if item[1] == self.new_operators_aircraft[i + 1][1] and item[0] == self.new_operators_aircraft[i + 1][0]:
                full_aircraft += ' - ' + item[2]
        except IndexError: pass
        aircraft_list.append(item[0] + ' - ' + full_aircraft[full_aircraft.find(', ') + 2:])
    self.ai_aircraft_rl1.addItem('Make a choice...')
    self.ai_aircraft_rl1.addItem('Other...')
    self.ai_aircraft_rl1.addItems(aircraft_list)
