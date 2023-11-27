from Server import Server
from Model import Model
from AllSensors import AllSensors

class Control:
    def __init__(self):
        self.model = Model()
        self.allSensors = AllSensors(self.model.soilData, self.model.tempData, self.model.lightData)
        
    def serverTest(self): #method to send Test Data to server and pulls data from the server
        self.server = Server(self.model.ssid, self.model.wifiPw, self.model.remoteUrl, self.model.uploadUrl, self.model.webUser, self.model.webPw)
        self.server.connectWifi()
        print(self.server.getRemote())
        print(self.server.setTestDataToServer())
        print(self.server.getRemote())
        
    def sensorTemperatureTest(self): #method to test the readings of TemperatureSensor
        print("Angeschlossen an: ",self.model.tempData)
        self.allSensors = AllSensors(self.model.soilData, self.model.tempData, self.model.lightData)
        print(self.allSensors.lightSensorValue)
        self.allSensors.readTemperatureSensor()
        print(self.allSensors.lightSensorValue)
        
    def sensorLightTest(self): #method to test the readings of LightSensor
        print("Angeschlossen an: ",self.model.lightData)
        self.allSensors = AllSensors(self.model.soilData, self.model.tempData, self.model.lightData)
        print(self.allSensors.lightSensorValue)
        self.allSensors.readLightSensor()
        print(self.allSensors.lightSensorValue)
        
    def sensorSoilTest(self): #method to test the readings of SoilSensor
        self.allSensors.readSoilSensor() #setzt neuen wert in var der Classe AllSensors alle measureDuration im abstand
        
        if self.allSensors.soilSensorValue != None: #wenn nicht None returnt wird (passiert wenn die letzte Messung nicht mindestens measureDuration (z.b. 5000 ms) her ist)
            #print("Auslesen des Sensores alle", self.model.soilData['measureDuration'], "ms")
            print(self.allSensors.soilSensorValue)
        
