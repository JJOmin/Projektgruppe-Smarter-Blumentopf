#main
from Control import Control
import utime
import gc
import micropython
#from machine import Pin

#setup
gc.collect()
micropython.mem_info()
control = Control()         # Initialisierung des MVC

#Auskommentiert für Standalone Demo HIT
print('Setup Wifi')
control.setupWifi()         # Wifi setup
#print('setup Server Data')
#control.setupServerData()   # Server setup

startTime = utime.ticks_ms()            # Var fürs speichern der Startzeit vom Programm 
sensorInterval = 5000                   # Gibt an in welchem Interval Sensoren ausgelesen werden sollen 
sensorTime = startTime + sensorInterval # Timet den zeitpunkt fürs erneute auslesen der Sensoren 
serverThreshold = 5                     # Anzahl wie oft Werte gelesen werden sollen, vor Durschnittsbrechnung und Uploaud 
#serverInterval = 90000
#serverTime = startTime + serverInterval
endTime= startTime + 300000             # um das Programm zu beenden, in dem fall nach 5min
running = True                          # startet den loop
#testPin = Pin(18, Pin.IN)



#___________Loop__________#
while running:
    #sensorData = control.allSensors.readAll()
    #control.startByPress() # führt die startByPress() methode aus. Sensoren auf Knopfdruck
    
    #print(testPin.value())
    if control.btnColor.value():        # Button Prüfung Ob 0 oder 1
        control.view.printAllData()     # gieb Alle Sensor daten aus 
    #control.checkBtn()
    
    if utime.ticks_ms() > sensorTime:						# Auslesen der Sensoren
        print(control.btnWater.value())
        #if control.pump.value() == 0:
        control.pump.off()
        #else:
         #   control.pump.off()
        #control.setupWifi() # TestMemo
        print('Measuring...')
        sensorData = control.allSensors.readAll()           # Ließt die methode fürs auslesen der sensoren 
        control.model.lightLog.append(sensorData[2])        # Hinzufügen des Lichtsensorwerts zum Log
        control.model.temperatureLog.append(sensorData[1])  # Hinzufügen des Temperaturewerts zum Log
        control.model.soilLog.append(sensorData[0])         # Hinzufügen des Bodenfeuchtigkeitssensorwerts zum Log
        
        control.setCurrentValues()                          # Aktualliersierung der Log Daten! 
        control.compareData()                               # Die Methode vergleicht die aktuellen Sensorwerte mit den Grenzwerten aus der json
        
        sensorTime = utime.ticks_ms() + sensorInterval      # Aktuallisierung SensorTime für den nächsten Zeitpunkt für Auslesung 
    logSize = len(control.model.lightLog)                   # gibt logSize die Anzahl der bisher im Licht-Log gespeicherten Datenpunkte an

# HIT Demo
    if logSize == serverThreshold and control.model.isWifiConnected: # Prüft ob anzahl der werte auch serverThreshold = 6 enspricht.
    #if utime.ticks_ms() > serverTime:
        packLen = 5
        averageLightLog = control.calcAverage(control.model.lightLog, packLen)              # Brechnung Durchschnittswert für lightLog
        averageTemperatureLog = control.calcAverage(control.model.temperatureLog, packLen)  # Brechnung Durchschnittswert für temperatureLog
        averageSoilLog = control.calcAverage(control.model.soilLog, packLen)                # Brechnung Durchschnittswert für soilLog
        
        print("Server Upload steht an!")
        print("Versuche, folgende Daten hochzuladen:", [averageLightLog, averageTemperatureLog, averageSoilLog]) # ausgabe server 
        
        newPrototype = control.server.getPrototype()   # Ruft das Prototyp-Objekt vom Server ab
        if newPrototype:                               # aktualisier interne Variablen mit den erhaltenen Daten und gibt eine Liste mit diesen Daten zurück.
            control.model.prototypData = newPrototype  # Füllt aktuallisierte daten in model.prototypData
        
        print(control.model.profileData[1], control.model.prototypData[1]) # Ausgabe der Vergleichsdaten profiel und Proto 
        
        if control.model.profileData[1] != control.model.prototypData[1]:   # wenn die daten vom Profil nicht = die vom Proto sind
            #control.model.profileData = control.server.getProfile()         # Dann übernimm die werte vom Server!
            control.setupServerData() 
            print(control.model.profileData)
            print("Neues Profil:", control.model.profileData[0]["name"])    # Ausgabe neues Profiel wurde Geladen
            
        control.server.addMeasurement(averageTemperatureLog, averageLightLog, averageSoilLog) #Fügt die durchschnittlichen Messwerte dem Server hinzu
        
        control.model.lightLog = []         # Leerung des Arrays 
        control.model.temperatureLog = []   # Leerung des Arrays 
        control.model.soilLog = []          # Leerung des Arrays 
        
        #serverTime = utime.ticks_ms() + serverInterval
        
    if utime.ticks_ms() > endTime: # wenn der timer bei der entTime angekommen ist stoppe den Loop
        running = False
        
print("Saved the day")
#Sensoren Intervall (alle 5-10 sekunden)


    
    #control.startByPress()                 # führt die startByPress() methode aus. Sensoren auf Knopfdruck
    #if control.model.btnData == 0:         # Annahme: btnData ist ein Integer-Wert
        #control.sensorTemperatureTest()    # Test auslesung der Temperatur
        #control.sensorSoilTest()           # Test auslesung der Lichtstärke
        #control.sensorLightTest()          # Test auslesung der Soil