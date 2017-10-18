from PySide import QtCore, QtGui
from PySide.QtGui import *
import Model
import View
import json
import requests
import sys
import html
import re


class Controller(QtGui.QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.myView = View.Ui_MainWindow()
        self.myView.setupUi(self)
        self.myModel = Model.Model()

        self.endInput = self.myView.endInput
        self.startInput = self.myView.startInput

        self.output = ""

        self.statusString = ""

        self.write = self.myView.textBrowser
        self.status = self.myView.label_4

        self.connect()




    def connect(self):
        """
        connects buttons to methods
        :return: None
        """
        self.myView.submit.clicked.connect(self.submit_clicked)
        self.myView.reset.clicked.connect(self.reset_clicked)

    def submit_clicked(self):
        """
        runs the Api with the parameters from InputSpaces
        and prints output from json to textBrowser
        :return: None
        """

        self.statusString = ''

        #sets params to Inputs
        self.myModel.setParams(self.startInput.text(),self.endInput.text())

        #reads json response and puts the into a readable format
        response = requests.get(self.myModel.url, self.myModel.params)
        dict =  response.json()
        for route in dict['routes']:
            for leg in route['legs']:
                self.output += 'Die <b>Gesamtdistanz</b> beträgt: <b>' + leg['distance']['text'] + '</b><br>'
                self.output += 'Die <b>Gesamtdauer</b> beträgt: <b>' + leg['duration']['text'] + '</b><br>'

                for step in leg['steps']:
                    self.output += (step['html_instructions'])
                    self.output += ', Entfernung: ' + step['distance']['text'] + ', Dauer: ' + step['duration']['text'] + '<br>'


        self.write.insertHtml(self.output)

        #also gets the status
        for geocode in dict['geocoded_waypoints']:
            self.statusString += 'Eintrag: ' + geocode['geocoder_status'] + ', '

        self.statusString += 'gesamtstatus: ' + dict['status']
        self.status.setText(self.statusString)


    def reset_clicked(self):
        """
        resets the Gui and input-variables
        :return: None
        """
        self.endInput.clear()
        self.startInput.clear()
        self.output = ''
        self.write.setText('')
