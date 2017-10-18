# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Gui.ui'
#
# Created: Wed Oct 18 21:29:44 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 469)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.startInput = QtGui.QLineEdit(self.centralwidget)
        self.startInput.setObjectName("startInput")
        self.gridLayout.addWidget(self.startInput, 1, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.endInput = QtGui.QLineEdit(self.centralwidget)
        self.endInput.setObjectName("endInput")
        self.gridLayout.addWidget(self.endInput, 2, 1, 1, 1)
        self.textBrowser = QtGui.QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 3, 0, 1, 2)
        self.submit = QtGui.QPushButton(self.centralwidget)
        self.submit.setObjectName("submit")
        self.gridLayout.addWidget(self.submit, 4, 0, 1, 1)
        self.reset = QtGui.QPushButton(self.centralwidget)
        self.reset.setObjectName("reset")
        self.gridLayout.addWidget(self.reset, 4, 2, 1, 1)
        self.close = QtGui.QPushButton(self.centralwidget)
        self.close.setObjectName("close")
        self.gridLayout.addWidget(self.close, 4, 3, 1, 1)
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 5, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.close, QtCore.SIGNAL("clicked()"), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Google Navigations", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Start:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "End:", None, QtGui.QApplication.UnicodeUTF8))
        self.submit.setText(QtGui.QApplication.translate("MainWindow", "Submit", None, QtGui.QApplication.UnicodeUTF8))
        self.reset.setText(QtGui.QApplication.translate("MainWindow", "Reset", None, QtGui.QApplication.UnicodeUTF8))
        self.close.setText(QtGui.QApplication.translate("MainWindow", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Status:", None, QtGui.QApplication.UnicodeUTF8))

