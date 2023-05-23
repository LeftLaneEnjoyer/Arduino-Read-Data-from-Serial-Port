import serial.tools.list_ports
import re
import datetime
import time
from my_sql_connection import mymysqlconnector


ports = serial.tools.list_ports.comports()
serialInst = serial.Serial()

portsList = []

for onePort in ports:
    portsList.append(str(onePort))
    print(str(onePort))

val = input("Select Port: COM")

for x in range(0,len(portsList)):
    if portsList[x].startswith("COM" + str(val)):
        portVar = "COM" + str(val)
        print(portVar)

serialInst.baudrate = 9600
serialInst.port = portVar
serialInst.open()

while True:
    if serialInst.in_waiting:
        packet = serialInst.readline()
        #print(packet.decode('utf').rstrip('\n'))
        temperature_pattern = r"Temperature:\s*([0-9.]+°C)"
        humidity_pattern = r"Humidity:\s*([0-9.]+%)"
        temperature_match = re.search(temperature_pattern, packet.decode('utf').rstrip('\n'))
        humidity_match = re.search(humidity_pattern, packet.decode('utf').rstrip('\n'))
        if temperature_match:
            temperature_data = temperature_match.group(1) # filtert temp
            print(temperature_data)
            tempobject = mymysqlconnector(temperature_data)
            tempobject.inserttemp()

        if humidity_match:
            humidity_data = humidity_match.group(1) # filtert humidity
            humidityobject = mymysqlconnector(humidity_data)
            humidityobject.insertluft()
            
        
            
            print( humidity_data)
        time.sleep(100)
        


  

