# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
from ui.mainwindow import MainWindow
from ui._version import _version
import os.path


def launch_eufar_creator():
    import sys
    app = QtGui.QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    print 'launching EUFAR Metadata Creator V{0} ...'.format(_version)
    launch_eufar_creator()