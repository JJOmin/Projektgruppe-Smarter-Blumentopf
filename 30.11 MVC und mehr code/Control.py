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
        #self.btnpress = 
         
    def setupWifi(self): #method to send Test Data to server and pulls data from the server
        self.server.connectWifi()
        #print(self.server.getRemote())
        #print(self.server.setTestDataToServer())
        #print(self.server.getRemote())     
        
        
    def setupServerData(self):
        self.model.prototypData = self.server.getRemote(self.model.prototypUrl)
        print(self.model.prototypData)
        
        self.model.profileData = self.server.getRemote(self.model.profileUrl)
        print(self.model.profileData)
         
        
    def sensorTemperatureTest(self): #method to test the readings of TemperatureSensor
        print("Angeschlossen an: ",self.model.tempData)
        #self.allSensors = AllSensors(self.model.soilData, self.model.tempData, self.model.lightData)
        print(self.allSensors.lightSensorValue)
        self.allSensors.readTemperatureSensor() #fuehrt die auslesung über die vererbung aus 
        print(self.allSensors.lightSensorValue)
        
    def sensorLightTest(self): #method to test the readings of LightSensor
        print("Angeschlossen an: ",self.model.lightData)
        #self.allSensors = AllSensors(self.model.soilData, self.model.tempData, self.model.lightData)
        print(self.allSensors.lightSensorValue)
        self.allSensors.readLightSensor()
        print(self.allSensors.lightSensorValue)
        
    def sensorSoilTest(self): #method to test the readings of SoilSensor
        self.allSensors.readSoilSensor() #setzt neuen wert in var der Classe AllSensors alle measureDuration im abstand
        if self.allSensors.soilSensorValue != None:#wenn nicht None returnt wird (passiert wenn die letzte Messung nicht mindestens measureDuration (z.b. 5000 ms) her ist)
            #print("Auslesen des Sensores alle", self.model.soilData['measureDuration'], "ms")
            print("Bodenfeuchtigkeit: ",self.allSensors.soilSensorValue)
            
        
    def improvementPump(self): #Die Methode dürfete von der Logik her funktionieren aber muss noch an die werte vom soil sensor angeglichen werden!
        if self.allSensors.SoilSensorsValue == 0: # wenn der wert 0 ist ist kein wasser in dem Topf drin
            self.activatePump() # Starte die Pumpe
            print("Pumpe läuft")
        if self.allSensors.SoilSensorsValue >= 1: # Wenn genug wasser im Topf ist soll die pumpe aufhören. 
            self.deactivatePump() # Stopp Pumpe
            
    def ledCheck(self):
        pass
        
        
    def startByPress(self): # die schleife wird ausgeführt wenn der taster gedrückt wird
        #self.running = True # Start variable die abgefragt wird um start_by_press zu beenden.
            if self.btnColor.value() == 1: #Wenn sich der Wert vom knopf ändert
                 self.allSensors.readTemperatureSensor()
                 self.sensorSoilTest() # rufe die Mehtode oben zum lesen auf (zwischenlösung)
                 self.allSensors.readLightSensor()# Starte die methode read_temperatur() Also ließ
                 self.view.printAllData()
                 #self.running = False #Setze die Prüf variable auf false damit die funktion start_by_press nicht mehr ausgeführt wird
                 #break
