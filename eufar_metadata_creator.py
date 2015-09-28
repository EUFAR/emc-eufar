# -*- coding: utf-8 -*-

from PyQt4 import QtGui
from ui.mainwindow import MainWindow


def launch_eufar_creator():
    import sys
    app = QtGui.QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    launch_eufar_creator()