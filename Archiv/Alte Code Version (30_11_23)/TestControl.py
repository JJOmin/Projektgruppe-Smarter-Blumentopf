from Server import Server
from Model import Model
from View import View
from AllSensors import AllSensors
from Pump import Pump 
import machine 

class Control:
    def __init__(self):
        
        self.model = Model()
        self.allSensors = AllSensors(self.model.soilData, self.model.tempData, self.model.lightData) # Instanzierung der Atribute von den jeweili
        self.view = View(self.allSensors)
        self.server = Server(self.model.ssid, self.model.wifiPw, self.model.profileUrl, self.model.prototypUrl, self.model.uploadUrl, self.model.webUser, self.model.webPw)
        self.running = False # brauchen wir nur für deu methode startByPress()
        self.btnColor = machine.Pin(self.model.btnData["dpin"], machine.Pin.IN) 
         
    def setupWifi(self): #method to send Test Data to server and pulls data from the server
        self.server.connectWifi()
        #print(self.server.getRemote())
        #print(self.server.setTestDataToServer())
        #print(self.server.getRemote())     
        
        
    def setupServerData(self):
        self.model.prototypData = self.server.getPrototype() 
        print(self.model.prototypData) #print prototyp daten
        
        self.model.profileData = self.server.getProfile() #print profildaten
        print(self.model.profileData)
        
         
    def compareData(self):
        profile = self.model.profileData # alle profile
        
        if profile is not None: #conrol if profile is matched 
            boundaries = self.model.profileData["boundaries"] #boundaries ausgeben
            # subBoundaries = boundaries['temperature', 'light', 'soil']
        
            for sensor in boundaries:
                logData = self.model.currentValues #currentValues ist dictionary mit aktuellen daten
             
                if logData: 
                    minValueTemp = boundaries['temperature']['min'] #min und max von json kriegen
                    maxValueTemp = boundaries['temperature']['max']

                    minValueMoisture = boundaries['moisture']['min']
                    maxValueMoisture = boundaries['moisture']['max']

                    minValueLight = boundaries['light']['min']
                    maxValueLight = boundaries['light']['max']
                    
                for data in logData: #vergleich und ausgabe
                    if (minValueTemp & maxValueTemp & minValueMoisture & maxValueMoisture & minValueLight & maxValueLight) is not None : #schauen ob es min/max gibt
                        if data{'temperature'} < minValueTemp or data{'temperature'} > maxValueTemp:
                            print("1. Werte liegen außerhalb der range")
                        
                        if data{'light'} < minValueMoisture or data{'light'} > maxValueMoisture:
                            print("2. Werte liegen außerhalb der range")
                        
                        if data{'moisture'} < minValueLight or data{'moisture'} > maxValueLight:
                            print("3. Werte liegen außerhalb der range")
                        
                        else:
                            print("Werte liegen innerhalb der range") 
                            
                    else:
                        print("Werte nicht definiert") #wenn es keine min/max werte gibt -> fehlermeldung

        
        
    def sensorTemperatureTest(self): #method to test the readings of TemperatureSensor
        print("Angeschlossen an: ",self.model.tempData)
        self.allSensors.readTemperatureSensor() #fuehrt die auslesung über die vererbung aus 
        print("Temperature", self.allSensors.temperaturSensorValue)
        
    def sensorLightTest(self): #method to test the readings of LightSensor
        print("Angeschlossen an: ",self.model.lightData)
        self.allSensors.readLightSensor()
        print("Light:", self.allSensors.lightSensorValue)
        
    def sensorSoilTest(self): #method to test the readings of SoilSensor
        self.allSensors.readSoilSensor() #setzt neuen wert in var der Classe AllSensors alle measureDuration im abstand
        if self.allSensors.soilSensorValue != None:#wenn nicht None returnt wird (passiert wenn die letzte Messung nicht mindestens measureDuration (z.b. 5000 ms) her ist)
            print("Bodenfeuchtigkeit: ",self.allSensors.soilSensorValue)
            
        
    def improvementPump(self): #Die Methode dürfete von der Logik her funktionieren aber muss noch an die werte vom soil sensor angeglichen werden!
        if self.allSensors.SoilSensorsValue == 0: # wenn der wert 0 ist ist kein wasser in dem Topf drin
            self.activatePump() # Starte die Pumpe
            print("Pumpe läuft")
        if self.allSensors.SoilSensorsValue >= 1: # Wenn genug wasser im Topf ist soll die pumpe aufhören. 
            self.deactivatePump() # Stopp Pumpe
            
    def ledCheck(self):
        pass
        
    def calcAverage(self, values, newLength):
        result = []
        total = 0
        i = 0
        for value in values:
            total += value
            i += 1
            if i % newLength == 0:
                result.append(total / newLength)
                total = 0
        return result
        
    def startByPress(self): # die schleife wird ausgeführt wenn der taster gedrückt wird
            if self.btnColor.value() == 1: #Wenn sich der Wert vom knopf ändert
                 self.allSensors.readTemperatureSensor()
                 self.sensorSoilTest() # rufe die Mehtode oben zum lesen auf (zwischenlösung)
                 self.allSensors.readLightSensor()# Starte die methode read_temperatur() Also ließ
                 self.view.printAllData()
                 #break
