#main
from Control import Control
import utime

#setup
control = Control() #Initialisierung des MVC
#control.setupWifi() #wifi setup
#control.setupServerData() #server setup
#startTime = utime.ticks_ms()
running = True
control.sensorSoilTest()

#loop
# while running:
#     #print(utime.ticks_ms())
#     #sensorData = control.allSensors.readAll()
#     #print(sensorData)
#     
#     if utime.ticks_ms() > startTime+60: #Auslesen der Sensoren
#         sensorData = control.allSensors.readAll()
#         sensorData = control.allSensors.readAll()
#         print(sensorData)
#         control.model.lightLog.append(sensorData)
#         print(control.model.lightLog)
#         #control.model.temperatureLog.append(sensorData[1])
#         #control.model.soilLog.append(sensorData[2])
#         #print(control.model.lightLog, control.model.temperatureLog,  control.model.soilLog)
#         
#         
#         startTime = utime.ticks_ms()
#         running = False
#         
# print("Saved the day")
# #Sensoren Intervall (alle 5-10 sekunden)




    
    
    
    
    
    
    
    
    #control.startByPress()
    #print(control.btnColor.value())
    #control.serverTest()
    #control.sensorSoilTest()
    #control.serverTest()#Tests the server Connection (on the Hotspot of Leos Phone)

    
    #if control.model.btnData == 0:  # Annahme: btnData ist ein Integer-Wert
        #control.sensorTemperatureTest() # funktioniert
        #control.sensorSoilTest()
        #control.sensorLightTest()
         

    