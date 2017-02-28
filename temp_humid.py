#!/usr/bin/python
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Sat Feb 25 21:59:23 2017
#      by: PyQt4 UI code generator 4.11.2
#
# Below is the permission notice for thr Adafruit RTH code
# -------------------------------------------------------------------------------
# Copyright (c) 2014 Adafruit Industries
# Author: Tony DiCola

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# ------------------------------------------------------------------------------

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *
from PyQt4.QtCore import * 
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style 
import datetime
import matplotlib.dates as mdates
import numpy as np
import datetime
import time
import Adafruit_DHT

# default values for the text files for alert message--Start--
default_temp_low = 15
default_temp_high = 30
default_humidity_low = 15
default_humidity_high = 30
# default values for the text files for alert message--End--

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Temperature_Humidity_Meter(object):
    def setupUi(self, Temperature_Humidity_Meter):
        Temperature_Humidity_Meter.setObjectName(_fromUtf8("Temperature_Humidity_Meter"))
        Temperature_Humidity_Meter.resize(525, 316)
        self.centralWidget = QtGui.QWidget(Temperature_Humidity_Meter)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.pushButton_cancel = QtGui.QPushButton(self.centralWidget)
        self.pushButton_cancel.setGeometry(QtCore.QRect(410, 40, 101, 31))
        self.pushButton_cancel.setObjectName(_fromUtf8("pushButton_cancel"))
        self.pushButton_refresh = QtGui.QPushButton(self.centralWidget)
        self.pushButton_refresh.setGeometry(QtCore.QRect(410, 100, 101, 31))
        self.pushButton_refresh.setObjectName(_fromUtf8("pushButton_refresh"))
        self.label_temp = QtGui.QLabel(self.centralWidget)
        self.label_temp.setGeometry(QtCore.QRect(130, 20, 101, 31))
        self.label_temp.setObjectName(_fromUtf8("label_temp"))
        self.label_Humidity = QtGui.QLabel(self.centralWidget)
        self.label_Humidity.setGeometry(QtCore.QRect(280, 20, 101, 31))
        self.label_Humidity.setObjectName(_fromUtf8("label_Humidity"))
        self.label_time = QtGui.QLabel(self.centralWidget)
        self.label_time.setGeometry(QtCore.QRect(250, 210, 101, 31))
        self.label_time.setObjectName(_fromUtf8("label_time"))
        self.label_status = QtGui.QLabel(self.centralWidget)
        self.label_status.setGeometry(QtCore.QRect(10, 210, 201, 21))
        self.label_status.setObjectName(_fromUtf8("label_status"))
        self.label_temp_Val = QtGui.QLabel(self.centralWidget)
        self.label_temp_Val.setGeometry(QtCore.QRect(130, 60, 101, 31))
        self.label_temp_Val.setObjectName(_fromUtf8("label_temp_Val"))
        self.label_humid_Val = QtGui.QLabel(self.centralWidget)
        self.label_humid_Val.setGeometry(QtCore.QRect(280, 60, 101, 31))
        self.label_humid_Val.setObjectName(_fromUtf8("label_humid_Val"))
        self.label_time_Val = QtGui.QLabel(self.centralWidget)
        self.label_time_Val.setGeometry(QtCore.QRect(320, 210, 151, 31))
        self.label_time_Val.setObjectName(_fromUtf8("label_time_Val"))
        self.label_set_alert = QtGui.QLabel(self.centralWidget)
        self.label_set_alert.setGeometry(QtCore.QRect(10, 150, 101, 31))
        self.label_set_alert.setObjectName(_fromUtf8("label_set_alert"))
        self.textEdit_temp_high = QtGui.QLineEdit(self.centralWidget)
        self.textEdit_temp_high.setGeometry(QtCore.QRect(130, 140, 104, 21))
        self.textEdit_temp_high.setObjectName(_fromUtf8("textEdit_temp_high"))
# Validating the input of the text box (Temperature & Humidity high values)--Start--
        self.textEdit_temp_high.setValidator(QtGui.QIntValidator())
        self.textEdit_temp_high.setMaxLength(2)
        
        self.textEdit_humidity_high = QtGui.QLineEdit(self.centralWidget)
        self.textEdit_humidity_high.setGeometry(QtCore.QRect(280, 140, 104, 21))
        self.textEdit_humidity_high.setObjectName(_fromUtf8("textEdit_humidity_high"))

        self.textEdit_humidity_high.setValidator(QtGui.QIntValidator())
        self.textEdit_humidity_high.setMaxLength(2)
# Validating the input of the text box (Temperature & Humidity high values)--End--
        
        self.pushButton_temp_graph = QtGui.QPushButton(self.centralWidget)
        self.pushButton_temp_graph.setGeometry(QtCore.QRect(410, 170, 101, 31))
        self.pushButton_temp_graph.setObjectName(_fromUtf8("pushButton_temp_graph"))
        self.label_avg = QtGui.QLabel(self.centralWidget)
        self.label_avg.setGeometry(QtCore.QRect(10, 100, 101, 31))
        self.label_avg.setObjectName(_fromUtf8("label_avg"))
        self.label_avg_temp = QtGui.QLabel(self.centralWidget)
        self.label_avg_temp.setGeometry(QtCore.QRect(130, 100, 101, 31))
        self.label_avg_temp.setObjectName(_fromUtf8("label_avg_temp"))
        self.label_avg_humidity = QtGui.QLabel(self.centralWidget)
        self.label_avg_humidity.setGeometry(QtCore.QRect(280, 100, 101, 31))
        self.label_avg_humidity.setObjectName(_fromUtf8("label_avg_humidity"))
        self.label_val = QtGui.QLabel(self.centralWidget)
        self.label_val.setGeometry(QtCore.QRect(10, 60, 101, 31))
        self.label_val.setObjectName(_fromUtf8("label_val"))
        self.textEdit_temp_low = QtGui.QLineEdit(self.centralWidget)
        self.textEdit_temp_low.setGeometry(QtCore.QRect(130, 180, 104, 21))
        self.textEdit_temp_low.setObjectName(_fromUtf8("textEdit_temp_low"))
# Validating the input of the text box (Temperature & Humidity low values)--Start--

        self.textEdit_temp_low.setValidator(QtGui.QIntValidator())
        self.textEdit_temp_low.setMaxLength(2)
        
        self.textEdit_humid_low = QtGui.QLineEdit(self.centralWidget)
        self.textEdit_humid_low.setGeometry(QtCore.QRect(280, 180, 104, 21))
        self.textEdit_humid_low.setObjectName(_fromUtf8("textEdit_humid_low"))

        self.textEdit_humid_low.setValidator(QtGui.QIntValidator())
        self.textEdit_humid_low.setMaxLength(2)
# Validating the input of the text box (Temperature & Humidity low values)--End--

        self.label_set_alert_2 = QtGui.QLabel(self.centralWidget)
        self.label_set_alert_2.setGeometry(QtCore.QRect(80, 140, 101, 31))
        self.label_set_alert_2.setObjectName(_fromUtf8("label_set_alert_2"))
        self.label_set_alert_3 = QtGui.QLabel(self.centralWidget)
        self.label_set_alert_3.setGeometry(QtCore.QRect(80, 170, 101, 31))
        self.label_set_alert_3.setObjectName(_fromUtf8("label_set_alert_3"))
        Temperature_Humidity_Meter.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(Temperature_Humidity_Meter)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 525, 27))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        Temperature_Humidity_Meter.setMenuBar(self.menuBar)
        self.mainToolBar = QtGui.QToolBar(Temperature_Humidity_Meter)
        self.mainToolBar.setObjectName(_fromUtf8("mainToolBar"))
        Temperature_Humidity_Meter.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtGui.QStatusBar(Temperature_Humidity_Meter)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        Temperature_Humidity_Meter.setStatusBar(self.statusBar)

        self.retranslateUi(Temperature_Humidity_Meter)
        QtCore.QMetaObject.connectSlotsByName(Temperature_Humidity_Meter)

    def retranslateUi(self, Temperature_Humidity_Meter):
        Temperature_Humidity_Meter.setWindowTitle(_translate("Temperature_Humidity_Meter", "MainWindow", None))
        self.pushButton_cancel.setText(_translate("Temperature_Humidity_Meter", "Cancel", None))
        self.pushButton_refresh.setText(_translate("Temperature_Humidity_Meter", "Refresh", None))
        self.label_temp.setText(_translate("Temperature_Humidity_Meter", "Temperature", None))
        self.label_Humidity.setText(_translate("Temperature_Humidity_Meter", "Humidity", None))
        self.label_time.setText(_translate("Temperature_Humidity_Meter", "Time:", None))
        self.label_status.setText(_translate("Temperature_Humidity_Meter", "", None))
        self.label_temp_Val.setText(_translate("Temperature_Humidity_Meter", "", None))
        self.label_humid_Val.setText(_translate("Temperature_Humidity_Meter", "", None))
        self.label_time_Val.setText(_translate("Temperature_Humidity_Meter", "", None))
        self.label_set_alert.setText(_translate("Temperature_Humidity_Meter", "Set Alert", None))
        self.pushButton_temp_graph.setText(_translate("Temperature_Humidity_Meter", "View Graph", None))
        self.label_avg.setText(_translate("Temperature_Humidity_Meter", "Average", None))
        self.label_avg_temp.setText(_translate("Temperature_Humidity_Meter", "", None))
        self.label_avg_humidity.setText(_translate("Temperature_Humidity_Meter", "", None))
        self.label_val.setText(_translate("Temperature_Humidity_Meter", "Value", None))
        self.label_set_alert_2.setText(_translate("Temperature_Humidity_Meter", "High: ", None))
        self.label_set_alert_3.setText(_translate("Temperature_Humidity_Meter", "Low:", None))
# Attaching the events to the UI elements--Start--

        self.pushButton_refresh.clicked.connect(self.getDHTvalue)
        self.pushButton_refresh.clicked.connect(self.avrgCal)
        self.pushButton_cancel.clicked.connect(self.closeApplication)
        self.pushButton_temp_graph.clicked.connect(self.plotgraph)
# Attaching the events to the UI elements--End--

# Setting the defalut values to the limiters of temperature and humidity --Start--

        self.textEdit_temp_low.setText(str(default_temp_low))
        self.textEdit_temp_high.setText(str(default_temp_high))
        self.textEdit_humid_low.setText(str(default_humidity_low))
        self.textEdit_humidity_high.setText(str(default_humidity_high))
# Setting the defalut values to the limiters of temperature and humidity --End--

# Function to calculate the average of the temp & humidity --Start--
    def avrgCal(self):
        graph_data = open('DHT22_values.txt','r').read()
        lines = graph_data.split('\n')
        xs = []
        ys = []
        for line in lines:
                if len(line) > 1:
                        x,y,y1 = line.split(',')
                        xs.append(x)
                        ys.append(y)
        val1 =sum(map(float,xs))/ float(len(xs))
        val2 = sum(map(float,ys)) / float(len(ys))
        self.label_avg_temp.setText('{0:0.1f}*C'.format(val1))
        self.label_avg_humidity.setText('{0:0.1f}%'.format(val2))
# Function to calculate the average of the temp & humidity --End--


# Function to plot the graph for  temp & humidity --Start--
    def plotgraph(self):
        style.use('fivethirtyeight')
        fig = plt.figure()
        ax1 =fig.add_subplot(1,2,1)
        ax2 =fig.add_subplot(1,2,2)

        graph_data = open('DHT22_values.txt','r').read()
        lines = graph_data.split('\n')
        xs = []
        ys = []
        y1s =[]
        for line in lines:
                if len(line) > 1:
                        x,y,y1 = line.split(',')
                        xs.append(x)
                        ys.append(y)
                        y1s.append(y1)
        y1s = [datetime.datetime.strptime(elem,"%Y-%m-%d %H:%M") for elem in y1s]
        ax1.clear()
        ax1.plot(y1s,xs, '--bo')
        ax1.set_title ('Temperature vs Time')
        ax1.set_ylabel ('Temperature in *C')
        ax1.set_xlabel('Time')
        ax1.format_xdata = mdates.DateFormatter("%Y-%m-%d %H:%M")
        ax2.clear()
        ax2.plot(y1s,ys,'--bo')
        ax2.set_title ('Humidity vs Time')
        ax2.set_ylabel ('Humidity in %')
        ax2.set_xlabel('Time')
        ax2.set_title ('Humidity vs Time')
        ax2.format_xdata = mdates.DateFormatter("%Y-%m-%d %H:%M")
        plt.show()
# Function to plot the graph for  temp & humidity --End--

# Function get temp & humidity from the sensor; to alert the user for out of range values--Start--
    def getDHTvalue(self):
        humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, 4)
        if humidity is not None and temperature is not None:
            temp_value = '{0:0.1f}'.format(temperature)
            humidity_value = '{0:0.1f}'.format(humidity)
            Date_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
            self.label_temp_Val.setText(temp_value + '*C')
            self.label_humid_Val.setText(humidity_value + '%')
            self.label_status.setText("Sensor Data Retrieved")
            self.label_time_Val.setText(Date_time)
            
            temp_low_limit= self.textEdit_temp_low.text()
            temp_low_limit = float(str(temp_low_limit)) if str(temp_low_limit) != "" else default_temp_low

            temp_high_limit = self.textEdit_temp_high.text()
            temp_high_limit = float(str(temp_high_limit)) if str(temp_high_limit) != "" else default_temp_high

            humid_low_limit= self.textEdit_humid_low.text()
            humid_low_limit = float(str(humid_low_limit)) if str(humid_low_limit) != "" else default_humidity_low
                        
            humid_high_limit= self.textEdit_humidity_high.text()
            humid_high_limit = float(str(humid_high_limit)) if str(humid_high_limit) != "" else default_humidity_high

            if temperature < temp_low_limit or temperature > temp_high_limit:
                QtGui.QMessageBox.critical(self.label_avg_temp, "Message", "Temperature out of range")
            if humidity < humid_low_limit or humidity > humid_high_limit:
                QtGui.QMessageBox.critical(self.label_avg_humidity, "Message", "Humidity out of range")
            with open("DHT22_values.txt","a") as DHT22_values:
                DHT22_values.write(temp_value + ','+humidity_value+ ','+ Date_time+ '\n')
            
        else:
            self.label_status.setText("Sensor Data Not Retrieved")
# Function get temp & humidity from the sensor--End--

# Function to close application --Start--
    def closeApplication(self):
        sys.exit(1)
# Function to close application --End--
        

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Temperature_Humidity_Meter = QtGui.QMainWindow()
    ui = Ui_Temperature_Humidity_Meter()
    ui.setupUi(Temperature_Humidity_Meter)
    Temperature_Humidity_Meter.show()
    sys.exit(app.exec_())

