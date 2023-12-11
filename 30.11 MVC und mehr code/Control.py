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
        self.server = Server(self.model.ssid, self.model.wifiPw, self.model.uploadUrl, self.model.webUser, self.model.webPw)
        self.running = False # brauchen wir nur für deu methode startByPress()
        self.btnColor = machine.Pin(self.model.btnData["dpin"], machine.Pin.IN) 
         
    def setupWifi(self): #method to send Test Data to server and pulls data from the server
        self.server.connectWifi() #stellt wifi verbindung her
        self.server.getPrototype() #download der prototype.json vom Server
        self.server.getProfile() #download der db.json vom server für Grenzwerte der Pflanze
        #Das hier ist die Methode zum hinzufügen neuer Messdaten
        self.server.addMeasurement(1,2,3) #temperature, light, moisture to add to the server
        
        
    def setupServerData(self):
        self.model.prototypData = self.server.getRemote(self.model.prototypUrl)
        print(self.model.prototypData)
        
        self.model.profileData = self.server.getRemote(self.model.profileUrl)
        print(self.model.profileData)
         
        
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
