# Embedded-Interface-Design---Project-1
Developer Name: Shekhar Satyanarayana

Installation Instructions: 
1. go to terminal ; type git clone https://github.com/adafruit/Adafruit_Python_DHT.git (follow the instructions given in Readme)
2. go to terminal ; git clone https://github.com/shsa5563/Embedded-Interface-Design---Project-1.git 
3. copy the "temp_humid.py" into "/examples" folder (the first step would have the folder name as "Adafruit_Python_DHT"; the "examples" folder is found inside "Adafruit_Python_DHT" folder)
4. go to the folder "examples/" and paste the "temp_humid.py" file 
5. double click on the file !! Wola!!! here you go !!! its your own temp-humidity-Embedded-Interface product 
   (if you did not get any output; try this command in terminal:-
     python temp_humid.py       or   chmod 777 temp_humid.py & step5 again.)

Project Work:
1. Built the entire project with the following references : 
 https://wiki.qt.io/Raspberry_Pi_Beginners_Guide
 http://docs.python-guide.org/en/latest/writing/style/
 http://www.rspilab.com/gui-application-development-using-qt4-designer-and-pyqt-in-raspbian-for-raspberry-pi/
 http://pythonforengineers.com/your-first-gui-app-with-python-and-pyqt/
 https://learn.adafruit.com/dht-humidity-sensing-on-raspberry-pi-with-gdocs-logging/overview
 https://github.com/adafruit/DHT-sensor-library.git
 
Project Add-ons:
1. The values of temperature and humidity is logged/stored in a text file called "DHT22_Values.txt" : if the file doesnot exist, its created. 
2. A graph which sub-plots both the humidity and temeperature in single figure (The graph is a '--bo' design i.e the values are marked with a "o" and the dots are connected through "--" line design)
3. The Average of humidity and temperature values over time are calculated and displayed; the value is taken from a text file- which stores/logs the temp&humidity values with time
4. A dynamic Alert message system to alert the user once the temperature or humidity goes out of range. The user can set the high and low thresholds in a text box; I have also sanitised and validated the inputs - so, the user can only enter 2 numbers. 

Temperature &amp; Humidity sensing independent embedded system with touch-pad interface
