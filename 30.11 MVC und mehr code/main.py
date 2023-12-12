#main
from Control import Control
import utime
#from machine import Pin

#setup
control = Control() #Initialisierung des MVC
control.setupWifi() #wifi setup
control.setupServerData() #server setup

startTime = utime.ticks_ms()
sensorInterval = 5000
sensorTime = startTime + sensorInterval
serverThreshold = 6
#serverInterval = 90000
#serverTime = startTime + serverInterval
endTime= startTime + 300000 # um den if block zu beenden 
running = True # startet den loop

#testPin = Pin(18, Pin.IN)

#loop
while running:
    #print(utime.ticks_ms())
    #sensorData = control.allSensors.readAll()
    #print(sensorData)
    #control.startByPress() # führt die startByPress() methode aus. Sensoren auf Knopfdruck
    
    #print(testPin.value())
    if control.btnColor.value():
        control.view.printAllData()
    #control.checkBtn()
    
    if utime.ticks_ms() > sensorTime: #Auslesen der Sensoren
        #sensorData = control.allSensors.readAll()
        sensorData = control.allSensors.readAll() #Ließt die methode fürs auslesen der sensoren 
        #print(sensorData)
        control.model.lightLog.append(sensorData[2]) # wertrückgabe
        control.model.temperatureLog.append(sensorData[1]) # wertrückgabe
        control.model.soilLog.append(sensorData[0]) #wertrückgabe
        #print(len(control.model.lightLog))
        #print(control.model.lightLog, control.model.temperatureLog,  control.model.soilLog)
        
        control.setCurrentValues() # dictionary das für bessere auslesen ist?
        control.compareData()
        
        
        sensorTime = utime.ticks_ms() + sensorInterval #
        
    logSize = len(control.model.lightLog)
    if logSize == serverThreshold:
    #if utime.ticks_ms() > serverTime:
        
        packLen = 2
        averageLightLog = control.calcAverage(control.model.lightLog, packLen)
        averageTemperatureLog = control.calcAverage(control.model.temperatureLog, packLen)
        averageSoilLog = control.calcAverage(control.model.soilLog, packLen)
        
        print("Server Upload!")
        print("Uploaded", [averageLightLog, averageTemperatureLog, averageSoilLog], "to Server!")
        
        newPrototype = control.server.getPrototype()
        if newPrototype:
            control.model.prototypData = newPrototype
        
        print(control.model.profileData[1], control.model.prototypData[1])
        
        if control.model.profileData[1] != control.model.prototypData[1]:
            control.model.profileData = control.server.getProfile()
            print("Neues Profil:", control.model.profileData[0]["name"])
            
        control.server.addMeasurement(averageTemperatureLog, averageLightLog, averageSoilLog)
        
        control.model.lightLog = []
        control.model.temperatureLog = []
        control.model.soilLog = []
        
        #serverTime = utime.ticks_ms() + serverInterval
        
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