#main
from Control import Control
import utime

#setup
control = Control() #Initialisierung des MVC
control.setupWifi() #wifi setup
#control.setupServerData() #server setup
startTime = utime.ticks_ms()
sensorInterval = 5000
sensorTime = startTime + sensorInterval
serverInterval = 90000
serverTime = startTime + serverInterval
endTime= startTime + 300000
running = True

test = [3, 7, 5, 2, 8, 4, 6, 6, 4, 5]
print(control.calcAverage(test, 5))

#loop
while running:
    #print(utime.ticks_ms())
    #sensorData = control.allSensors.readAll()
    #print(sensorData)
    
    if utime.ticks_ms() > sensorTime: #Auslesen der Sensoren
        #sensorData = control.allSensors.readAll()
        sensorData = control.allSensors.readAll() #Ließt die methode fürs auslesen der sensoren 
        #print(sensorData)
        control.model.lightLog.append(sensorData[2])
        control.model.temperatureLog.append(sensorData[1])
        control.model.soilLog.append(sensorData[0])
        print(len(control.model.lightLog))
        print(control.model.lightLog, control.model.temperatureLog,  control.model.soilLog)
        
        
        sensorTime = utime.ticks_ms() + sensorInterval
        
    if utime.ticks_ms() > serverTime:
        
        print("Server Upload!")
        
        control.model.lightLog = []
        control.model.temperatureLog = []
        control.model.soilLog = []
        
        print(control.model.lightLog, control.model.temperatureLog,  control.model.soilLog)
        
        serverTime = utime.ticks_ms() + serverInterval
        
    if utime.ticks_ms() > endTime:
        running = False
        
print("Saved the day")
#Sensoren Intervall (alle 5-10 sekunden)




    
    
    
    
    #control.startByPress() # führt die startByPress() methode aus. Sensoren auf Knopfdruck
    #control.serverTest() # Tests the server Connection (on the Hotspot of Leos Phone)

    #if control.model.btnData == 0:  # Annahme: btnData ist ein Integer-Wert
        #control.sensorTemperatureTest() # Test auslesung der Temperatur
        #control.sensorSoilTest() #Test auslesung der Lichtstärke
        #control.sensorLightTest() #Test auslesung der Soil