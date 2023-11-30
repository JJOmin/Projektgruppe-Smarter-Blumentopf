from Server import Server
from Model import Model
from AllSensors import AllSensors
import machine 

class Control:
    def __init__(self):
        self.model = Model()
        self.allSensors = AllSensors(self.model.soilData, self.model.tempData, self.model.lightData) # Instanzierung der Atribute von den jeweili
        self.server = Server(self.model.ssid, self.model.wifiPw, self.model.remoteUrl, self.model.uploadUrl, self.model.webUser, self.model.webPw)
        self.running = False # brauchen wir nur für deu methode startByPress()
        self.btnColor = machine.Pin(self.model.btnData["dpin"], machine.Pin.IN)
        #self.btnpress = 
        
        
    def serverTest(self): #method to send Test Data to server and pulls data from the server
        self.server.connectWifi()
        print(self.server.getRemote())
        print(self.server.setTestDataToServer())
        print(self.server.getRemote())
        
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
        
        if self.allSensors.soilSensorValue != None: #wenn nicht None returnt wird (passiert wenn die letzte Messung nicht mindestens measureDuration (z.b. 5000 ms) her ist)
            #print("Auslesen des Sensores alle", self.model.soilData['measureDuration'], "ms")
            print(self.allSensors.soilSensorValue)
        
    def startByPress(self): # die schleife wird ausgeführt wenn der taster gedrückt wird
         self.running = True # Start variable die abgefragt wird um start_by_press zu beenden.
         while self.running: # endloschschleife solange 
             
             #self.allSensors.readLightSensor()# Starte die methode read_temperatur() Also ließ
             #self.allSensors.readSoilSensor()
             if self.btnColor.value() == 1: #Wenn sich der Wert vom knopf ändert
                 self.allSensors.readTemperatureSensor()
                 self.running = False # Setze die Prüf variable auf false damit die funktion start_by_press nicht mehr ausgeführt wird
                 #break
