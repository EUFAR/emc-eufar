import logging
import sys
import os
import configparser
from PyQt5.QtWidgets import QApplication
from ui.mainwindow import MainWindow
from ui._version import _version


def launch_eufar_creator(path):
    app = QApplication(sys.argv)
    ui = MainWindow(path)
    ui.show()
    sys.exit(app.exec_())


def handle_exception(exc_type, exc_value, exc_traceback):
    if issubclass(exc_type, KeyboardInterrupt):
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return
    logging.critical('Uncaught exception', exc_info=(exc_type, exc_value, exc_traceback))


sys.excepthook = handle_exception


if __name__ == '__main__':
    path = os.path.abspath(os.path.dirname(__file__))
    config_dict = configparser.ConfigParser()
    config_dict.read(os.path.join(path, 'emc_creator.ini'))
    if not config_dict.get('LOG', 'path'):
        log_filename = os.path.join(path, 'emc_creator_log.out')
    else:
        log_filename = os.path.join(config_dict.get('LOG', 'path'),'emc_creator_log.out')
    logging.getLogger('').handlers = []
    logging.basicConfig(filename = log_filename,
                        level = getattr(logging, config_dict.get('LOG', 'level')),
                        filemode = 'w',
                        format = '%(asctime)s : %(levelname)s : %(message)s')
    formatter = logging.Formatter('%(levelname)s : %(message)s')
    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG)
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)
    logging.info('**************************************************')
    logging.info('EMC ' + _version + ' is starting ...')
    logging.info('**************************************************')
    launch_eufar_creator(path)
    