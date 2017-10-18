import Controller, Model, View
from PySide.QtGui import *
from PySide import QtGui


import sys


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    c = Controller.Controller()
    c.show()
    sys.exit(app.exec_())
