from Server import Server
from Model import Model
from View import View
from AllSensors import AllSensors
from Pump import Pump 
import machine
import utime
import gc

class Control:
    def __init__(self):
        
        self.model = Model()
        
        self.allSensors = AllSensors(self.model.soilData, self.model.tempData, self.model.lightData) # Instanzierung der Atribute von den jeweili
        self.view = View(self.model)
        self.server = Server(self.model.ssid, self.model.wifiPw, self.model.profileUrl, self.model.prototypUrl, self.model.uploadUrl, self.model.webUser, self.model.webPw)
        self.running = False # brauchen wir nur für deu methode startByPress()
        self.btnColor = machine.Pin(self.model.btnData["dpin"], machine.Pin.IN)
        self.btnWater = machine.Pin(34, machine.Pin.IN)
        self.pump = machine.Pin(32, machine.Pin.OUT)
        self.btnStat = False
        self.leds = {
            "light": machine.Pin(self.model.ledPins["light"], machine.Pin.OUT),
            "temperature": machine.Pin(self.model.ledPins["temperature"], machine.Pin.OUT),
            "moisture": machine.Pin(self.model.ledPins["moisture"], machine.Pin.OUT)
            }
        self.blink_speed_ms = 500
        self.model.profileData = self.model.load_json(self.model.localFileName)
        
        
         
    def setupWifi(self): #method to send Test Data to server and pulls data from the server
        if self.model.isWifiConnected == False: #TestMemo
            self.server.connectWifi() #TestMemo
        #self.model.isWifiConnected = True #TestMemo (komplett weg)
            self.setupServerData() #TestMemo
        self.model.isWifiConnected = self.server.sta_if.isconnected()#TestMemo
            
        
        
    def setupServerData(self): # Abruf Proto daten und Speicher im Model

        if self.model.isWifiConnected:
            prototype_data = self.server.getPrototype()
            profile_data = self.server.getProfile()
            if prototype_data is not None and profile_data is not None:
                self.model.profileData = profile_data #TestMemo (komplett weg)
                self.model.prototypData = prototype_data
                self.model.status = {
                    'light': self.model.prototypData[0]['sensors']['light']['status'],
                    'moisture': self.model.prototypData[0]['sensors']['moisture']['status'],
                    'temperature': self.model.prototypData[0]['sensors']['temperature']['status']
                }
            else:
                print("Error: Failed to retrieve server data.")
        
        #Falls Verbindung fehlt
        self.model.profileData = self.server.getProfile()
        if self.model.profileData != self.model.load_json(self.model.localFileName) and self.model.profileData != False and self.model.profileData is not None :
             self.model.save_json_if_changed(self.model.localFileName, self.model.profileData)
         
        if self.model.profileData == False :
             if self.model.load_json(self.model.localFileName) is not None:
                 self.model.profileData = self.model.load_json(self.model.localFileName)
         
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
        
    def calcAverage(self, values, packLen):
        result = []
        total = 0
        i = 0
        for value in values:
            total += value
            i += 1
            if i % packLen == 0:
                result.append(total / packLen)
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
                 
    def checkBtn(self):
        print(self.btnColor.value()) #1
        if self.btnColor.value() == 1 and self.btnStat == False: # 
            self.btnStat = True
        if self.btnColor.value() == 0 and self.btnStat == True:
            print("gedrückt")
            self.btnStat = False
            
    def compareData(self):
        gc.collect()

        print(self.model.profileData)
        profile = self.model.profileData[0] # aktives profil
        
        if profile is not None: #conrol if profile is matched 
            boundaries = profile["boundaries"] #boundaries ausgeben
            status = self.model.status
            
            logData = self.model.currentValues #currentValues ist dictionary mit aktuellen daten
            newStatus = {}
            for key, value in logData.items(): #vergleich und ausgabe
                min = boundaries[key]['min']
                max = boundaries[key]['max']
                
                
                if value < min:
                    newStatus[key] = "Warning"
                    
                elif value > max:
                    newStatus[key] = "Warning"
                else:
                    newStatus[key] = "Okay"
                    
            print("Status:", newStatus)
            if newStatus != status:
                self.model.status = newStatus
                self.statusChange()
        
    def statusChange(self):
        print("status Change!")
        
        self.updateLeds(self.model.status)
        
    def updateLeds(self, stats):
        for key, value in stats.items():
            if value == "Okay":
                self.leds[key].off()
            elif value == "Warning":
                self.leds[key].on()