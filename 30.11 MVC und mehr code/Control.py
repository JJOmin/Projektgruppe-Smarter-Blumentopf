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
        self.view = View(self.model)
        self.server = Server(self.model.ssid, self.model.wifiPw, self.model.profileUrl, self.model.prototypUrl, self.model.uploadUrl, self.model.webUser, self.model.webPw)
        self.running = False # brauchen wir nur für deu methode startByPress()
        self.btnColor = machine.Pin(self.model.btnData["dpin"], machine.Pin.IN)
        self.btnStat = False
        
         
    def setupWifi(self): #method to send Test Data to server and pulls data from the server
        self.server.connectWifi()
        #print(self.server.getRemote())
        #print(self.server.setTestDataToServer())
        #print(self.server.getRemote())     
        
        
    def setupServerData(self):
        self.model.prototypData = self.server.getPrototype()
        print(self.model.prototypData)
        
        self.model.profileData = self.server.getProfile()
        print(self.model.profileData)
        self.server.addMeasurement(20, 5, 35)
         
        
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
    
    def setCurrentValues(self):
        self.model.currentValues['light'] = self.model.lightLog[-1]
        self.model.currentValues['moisture'] = self.model.soilLog[-1]
        self.model.currentValues['temperature'] = self.model.temperatureLog[-1]
        print('Current Values:', self.model.currentValues)
        
    def startByPress(self): # die schleife wird ausgeführt wenn der taster gedrückt wird
            if self.btnColor.value() == 1: #Wenn sich der Wert vom knopf ändert
                 self.allSensors.readTemperatureSensor()
                 self.sensorSoilTest() # rufe die Mehtode oben zum lesen auf (zwischenlösung)
                 self.allSensors.readLightSensor()# Starte die methode read_temperatur() Also ließ
                 self.view.printAllData()
                 #break
                 
    def checkBtn(self):
        print(self.btnColor.value()) #1
        if self.btnColor.value() == 1 and self.btnStat == False: # 
            self.btnStat = True
        if self.btnColor.value() == 0 and self.btnStat == True:
            print("gedrückt")
      #      self.view.printAllData()
            self.btnStat = False
            
    def compareData(self):
        profile = self.model.profileData # alle profile
        
        if profile is not None: #conrol if profile is matched 
            boundaries = self.model.profileData["boundaries"] #boundaries ausgeben
            status = self.model.status
            
            logData = self.model.currentValues #currentValues ist dictionary mit aktuellen daten
            newStatus = {}
            for key, value in logData.items(): #vergleich und ausgabe
                #print(value)
                #print(data)
                min = boundaries[key]['min']
                max = boundaries[key]['max']
                
                
                if value < min:
                    print("Wert für " + key + " zu niedrig")
                    newStatus[key] = "Warning"
                    
                elif value > max:
                    print("Wert für " + key + " zu hoch")
                    newStatus[key] = "Warning"
                else:
                    newStatus[key] = "Okay"
                    print("Wert für " + key + " in Ordnung")
                    
            if newStatus != status:
                self.model.status = newStatus
                self.statusChange()
        
        
    def statusChange(self):
        print("status Change!")
        
